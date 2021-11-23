import pymysql

host="localhost"
user="root"
password="123456"
database="bank"

# 增，删，改
def update(sql,param):
    con = pymysql.connect(host=host,user=user,password=password,database=database)
    cusor = con.cursor()

    cusor.execute(sql,param)

    con.commit()

    cusor.close()
    con.close()

# 查询
def select(sql,param,mode="many",size=0):
    con = pymysql.connect(host=host,user=user,password=password,database=database)
    cusor = con.cursor()

    cusor.execute(sql,param)

    con.commit()
    # 提取数据
    if mode == "all":
        return cusor.fetchall()
    elif mode == "one":
        return cusor.fetchone()
    elif mode == "many":
        return cusor.fetchmany(size)


    cusor.close()
    con.close()









