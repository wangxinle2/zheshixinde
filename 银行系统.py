from DBUtils import update
from DBUtils import select
import random
# 银行的数据库
# 银行名称
bank_name = "中国工商银行昌平支行"


def welcome():
    print("---------------------------------------")
    print("-     中国工商银行账户管理系统V1.0      -")
    print("---------------------------------------")
    print("-  1.开户                             -")
    print("-  2.存钱                             -")
    print("-  3.取钱                             -")
    print("-  4.转账                             -")
    print("-  5.查询                             -")
    print("-  6.Bye!                             -")
    print("--------------------------------------")


# 银行的开户逻辑
def bank_addUser(account,username,password,country,province,street,door,money):

    #查询银行的表中的用户数量
    sql = "select count(*) from ban"
    param =[]
    data = select(sql,param,mode="all")

    if data[0][0] > 100:
        return 3

    #根据username查询数据库中是否存在该用户
    sql1 ="select username from ban where username=%s"
    param1 = [username]
    user = select(sql1,param1,mode="all")

    if not user:
        sql3 = "insert into user(account, username, password, country, province, street, door, money, bank_name) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        param3 = [account, username, password, country, province, street, door, money, bank_name]
        update(sql3,param3)
        return 1
    else:
        return 2

# 开户的输入数据
def addUser():

    username = input("请输入姓名：")

    password = input("请输入密码：")

    country = input("请输入国籍：")

    province = input("请输入省份：")

    street = input("请输入街道：")

    door = input("请输入您家门牌号：")

    money =int(input("请输入初始化您的银行卡余额："))

    # datetime = input("请输入开户日期：")

    account = random.randint(10000000, 99999999)

    status = bank_addUser(account,username,password,country,province,street,door,money)

    if status == 3:
        print("对不起，该银行用户已满，请携带证件到其他银行办理！")
    elif status == 2:
        print("您之前已经开过户！禁止重复开户！")
    elif status == 1:
        print("嘻嘻，开户成功！以下卡户的个人信息：")
        sql = "select * from ban where username=%s"
        param = [username]
        data = select(sql,param,mode="all")
        info = '''
            ------------个人信息查询结果-------------
            用户名：%s
            账号：%d
            密码：%s
                国籍：%s
                省份：%s
                街道：%s
                门牌号：%s
            余额：%s
            开户时间：%s
            开户行名称：%s
            ---------------------------------------
        '''
        print(info % (
        data[0][1], data[0][0], data[0][2], data[0][3], data[0][4], data[0][5], data[0][6], data[0][7], data[0][8],
        data[0][9]))


# 取钱的库


def bank_quq(account1, password1,jin):
    sql5 ="select * from ban where account = %s"
    param5=[account1]
    data5=select(sql5,param5,mode="all")
    if account1==data5[0][0]:
        if password1==data5[0][2]:
            if jin<=data5[0][7]:
                sql5 = "update ban set money=money-%s where account=%s and password=%s"
                param5 = [jin, account1, password1]
                update(sql5, param5)
                return 0
            elif jin>data5[0][7]:
                return 3
        elif password1!=data5[0][2]:
            return 2
    elif account1!=data5[0][0]:
        return 1

def quq():
    account1 = int(input("请输入账号"))
    password1 = int(input("请输入密码"))
    jin=int(input("请输入要取款的金额"))
    status = bank_quq(account1, password1,jin)
    if status == 1:
        print("用户不存在")
    elif status == 2:
        print("密码错误")
    elif status == 3:
        print("余额不足")
    elif status == 0:
        print("取款成功")

def bank_cx(account2,password2):
    sql6="select * from ban where account = %s"
    param6=[account2]
    data6=select(sql6,param6,mode="all")
    if not data6:
        return 1
    if account2==data6[0][0]:
        if password2 == data6[0][2]:
            print("以下是您查询",data6[0][1],"的账户信息")
            print("----------------")
            print("账号",data6[0][0])
            print("密码",data6[0][1])
            print("余额",data6[0][7])
            print("用户居住地址",data6[0][3],data6[0][4],data6[0][5],data6[0][6])
            print("开户行",data6[0][9])
            print("----------------")
            print(data6)
            return 2
        elif password2 !=data6[0][1]:
            return 3


def cx():
    account2=int(input("请输入您的账号"))
    password2=int(input("请输入您的密码"))
    status=bank_cx(account2,password2)
    if status==1:
        print("该用户不存在")
    elif status==3:
        print("您输入的密码错误")








while True:
    welcome()
    chose = input("请输入业务编号：")
    if chose == "1":
        addUser()
    elif chose == "2":
        pass
    elif chose == "3":
        quq()
    elif chose == "4":
        pass
    elif chose == "5":
        cx()
    elif chose == "6":
        pass
