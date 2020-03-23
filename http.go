package utils

import (
	"bytes"
	"crypto"
	"encoding/hex"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"net/url"
	"strconv"
	"strings"
	"time"

	"github.com/gin-gonic/gin"
	"github.com/spf13/viper"

	"github.com/go-xweb/log"
)

// http post请求 Content-Type：application/json
func HTTPPostJsonRequest(requestUrl string, param map[string]interface{}) ([]byte, error) {
	now := time.Now()
	defer func() {
		log.Printf("requestUrl:%v cost:%v\n", requestUrl, time.Since(now))
	}()
	// 拼接链接参数
	requestBody := ParamToStr(param)
	// 将参数转化为json比特流
	jsonByte, err := json.Marshal(param)
	if err != nil {
		log.Errorf("jiguang: url:%v req:%v err:%v\n", requestUrl, requestBody, err.Error())
		return nil, err
	}
	// 构造post请求，json数据以body的形式传递
	req, err := http.NewRequest("POST", requestUrl, bytes.NewReader(jsonByte))
	req.Header.Set("Content-Type", "application/json;charset=UTF-8")
	// 初始化
	client := &http.Client{}
	resp, err := client.Do(req)
	req.Close = true
	if err != nil {
		log.Errorf("HTTPPostJSONRequest: url:%v param:%v err:%v", requestUrl, param, err.Error())
		return nil, err
	}
	defer resp.Body.Close()
	// 获取body数据
	body, _ := ioutil.ReadAll(resp.Body)
	return body, nil
}

// http post请求 Content-Type：application/x-www-form-urlencoded
func HTTPPostFormRequest(c *gin.Context, requestUrl string, param map[string]interface{}) ([]byte, error) {
	now := time.Now()
	defer func() {
		log.Printf("requestUrl:%v cost:%v\n", requestUrl, time.Since(now))
	}()
	// 拼接链接参数
	requestBody := ParamToStr(param)
	// 构造post请求，json数据以body的形式传递
	req, err := http.NewRequest("POST", requestUrl, strings.NewReader(requestBody))
	req.Header.Set("Content-Type", "application/x-www-form-urlencoded")
	// 验证header
	p := get_validate_param(param)
	user_agent := req.Header.Get("User-Agent") + ";BTCSO IS"
	req.Header.Set("apikey", p["apikey"].(string))
	req.Header.Set("apisecret", p["apisecret"].(string))
	req.Header.Set("sign", p["sign"].(string))
	req.Header.Set("timestamp", p["timestamp"].(string))
	req.Header.Set("user-agent", user_agent)

	//	log.Infof("内部验证数据：apikey:%s  apisecret:%s  sign:%s  timestamp:%s  user_agent:%s", p["apikey"].(string), p["apisecret"].(string), p["sign"].(string), p["timestamp"], user_agent)
	// 初始化
	client := &http.Client{}
	resp, err := client.Do(req)
	req.Close = true
	if err != nil {
		log.Errorf("HTTPPostJSONRequest: url:%v param:%v err:%v", requestUrl, param, err.Error())
		return nil, err
	}
	defer resp.Body.Close()
	// 获取body数据
	body, _ := ioutil.ReadAll(resp.Body)
	return body, nil
}

// 拼接链接参数
func ParamToStr(param map[string]interface{}) string {
	IsFirst := true
	tmp := ""
	for k, v := range param {
		if IsFirst {
			tmp = fmt.Sprintf("%v%v=%v", tmp, k, v)
			IsFirst = false
		} else {
			tmp = fmt.Sprintf("%v&%v=%v", tmp, k, v)
		}
	}
	return tmp
}

// HTTP GET Request utilities
func HttpTimeoutGet(url string, timeout time.Duration) ([]byte, error) {
	client := http.Client{Timeout: timeout}
	rsp, err := client.Get(url)
	if err != nil {
		return []byte(""), err
	}
	defer rsp.Body.Close()
	body, err := ioutil.ReadAll(rsp.Body)
	return body, err
}

// http get请求
func HTTPGetRequest(c *gin.Context, requestUrl string) ([]byte, error) {
	now := time.Now()
	defer func() {
		log.Printf("requestUrl:%v cost:%v\n", requestUrl, time.Since(now))
	}()
	responseBytes, err := HttpTimeoutGet(requestUrl, 50*time.Second)
	if err != nil {
		log.Errorf("HTTPGetRequest: url:%v  err:%v", requestUrl, err.Error())
		return nil, err
	}
	return responseBytes, nil
}

// http param get 请求
func HTTPGetParamRequest(c *gin.Context, requestUrl string, param map[string]interface{}) ([]byte, error) {
	now := time.Now()
	defer func() {
		log.Printf("requestUrl:%v cost:%v\n", requestUrl, time.Since(now))
	}()
	// 参数链接
	requestParams := ParamToStr(param)
	responseBytes, err := HttpTimeoutGet(requestUrl+requestParams, 20*time.Second)
	if err != nil {
		log.Errorf("HTTPGetRequest: url:%v  err:%v", requestUrl, err.Error())
		return nil, err
	}
	return responseBytes, nil
}

// 获取内部验证参数
func get_validate_param(p map[string]interface{}) map[string]interface{} {
	// 当前系统时间戳
	curTime := time.Now().UnixNano() / 1e6
	// 接口调用密钥
	apikey := viper.GetString("api.apikey")
	apisecret := viper.GetString("api.apisecret")
	param := map[string]interface{}{}
	param["apikey"] = apikey
	param["apisecret"] = apisecret
	param["timestamp"] = strconv.FormatInt(curTime, 10)
	param["token"] = p["token"]
	// 参数连接
	signString := fmt.Sprintf("apikey=%s&apisecret=%s&timestamp=%v&token=%s", apikey, apisecret, curTime, p["token"])
	s := urlencode("", signString)
	s = strings.ToUpper(s[1:])
	// SHA256加密
	sign := get_sha256(s + apisecret + "BTCSOEX")
	param["sign"] = strings.ToUpper(sign)
	log.Printf("====sign加密前数据：%s====sign加密后: %s", signString, param["sign"])
	return param
}

// SHA256加密
func get_sha256(s string) string {
	h := crypto.SHA256.New()
	h.Write([]byte(s))
	return hex.EncodeToString(h.Sum(nil))
}

// urlencode编码
func urlencode(k, s string) string {
	v := url.Values{}
	v.Add(k, s)
	return v.Encode()
}
