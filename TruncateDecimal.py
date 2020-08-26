def truncateDecimal(num,digits=0):
    num = str(float(num))
    nummian = num.split(".")[0]
    numsub = num.split(".")[1]
    numsub = numsub[:digits]
    num = nummian+"."+numsub
    # print(num)
    return num

if __name__ == "__main__":
    pass