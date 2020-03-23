# def fetch_dicts2(query_string, bind_name='', *query_args):
#     if not bind_name:
#         connection = db.get_engine(current_app)
#     else:
#         connection = db.get_engine(current_app, bind=bind_name)
#
#     cx = connection.execute(query_string, query_args)
#
#     cursor = cx.cursor
#
#     col_names = [desc[0] for desc in cursor.description]
#     rv = []
#     while True:
#         row = cursor.fetchone()
#         if row is None:
#             break
#         row_dict = dict(zip(col_names, row))
#         rv.append(row_dict)
#
#     cursor.close()
#     return rv

def fetch_sql(query_string, *query_args):

    result = db.engine.execute(query_string, query_args).fetchall()

    return result

# sql="""select t1.company_id,t1.company_name,sum(t1.coins) as coins,t1.bank,t1.account,t1.account_name from
#     (select company_id,company_name,sum(coins) as coins,bank,account,account_name from business_monthly_payment
#     where ym>='%s' and ym<='%s' and game_id in %s
#     group by game_name,company_name,bank,account,account_name,company_id  ) as t1
#     group by t1.company_name,t1.bank,t1.account,t1.account_name,t1.company_id"""%(start,end,game_ids)
#     result = fetch_dicts2(sql,'','')


