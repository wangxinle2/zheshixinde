import random

# 银行的数据库
bank = {}
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
def bank_addUser(account, username, password, country, province, street, door, money):
    if len(bank) > 100:
        return 3

    if username in bank:
        return 2

    # 正常开户
    bank[username] = {
        "account": account,
        "password": password,
        "country": country,
        "province": province,
        "street": street,
        "door": door,
        "money": money,
        "bank_name": bank_name
    }
    return 1


# 开户的输入数据
def addUser():
    username = input("请输入姓名：")

    password = input("请输入密码：")

    country = input("请输入国籍：")

    province = input("请输入省份：")

    street = input("请输入街道：")
    door = input("请输入您家门牌号：")

    money = int(input("请输入初始化您的银行卡余额："))

    account = random.randint(10000000, 99999999)

    status = bank_addUser(account, username, password, country, province, street, door, money)

    if status == 3:
        print("对不起，该银行用户已满，请携带证件到其他银行办理！")
    elif status == 2:
        print("您之前已经开过户！禁止重复开户！")
    elif status == 1:
        print("嘻嘻，开户成功！以下卡户的个人信息：")
        info = '''
            ------------个人信息查询结果-------------
            用户名：%s
            账号：%s
            密码：%s
            地址：
                国籍：%s
                省份：%s
                街道：%s
                门牌号：%s
            余额：%s
            开户行名称：%s
            ---------------------------------------
        '''
        print(info % (username, account, password, country, province, street, door, money, bank_name))
        print(bank)


# 取钱的库


def bank_quq(account1, password1,jin):
    for k in bank.keys():
        if account1 != bank[k]["account"]:
            return 1
        if  account1 == bank[k]["account"] :
            if password1 != bank[k]["password"]:
                return 2
            if jin > bank[k]["money"]:
                return 3
            else:
                bank[k]["money"]= bank[k]["money"]-jin
                return 0




def quq():
    account1 = int(input("请输入账号"))

    password1 = input("请输入密码")

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
        pass
    elif chose == "6":
        pass
