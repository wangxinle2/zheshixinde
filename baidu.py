import xlrd
import pymysql
from DBUtils import update
from DBUtils import select
# 工作簿对象
af= xlrd.open_workbook(filename=r"C:\Users\MECHREV\Desktop\1.xls")
st = af.sheet_by_index(0)
rows = st.nrows
cols = st.ncols

telecom= 0#手机号
move = 0
link = 0
man = 0
girl = 0#男女
age = 0#年龄
wage = 0#工资
wage3 = 0
media = 0#公司
epi = 0# 疫情地区

for num  in range(1,rows):
    data = st.row_values(num)
    if data[5] .startswith('14' or '17'):
        telecom+= 1
    elif data[5].startswith('13'):
        move += 1
    elif data[5].startswith('15'):
        link += 1
    if data[8] == "男":
        man += 1
    elif data[8] =='女' :
        girl += 1
    if data[7] > 45 :
        age += 1
    if data[11] > 8000:
        wage += 1
    elif data[11] < 3000:
        wage3 += 1
    if data[13] .endswith('传媒有限公司'):
        media += 1
    if data[9] .startswith('黑龙江'or'北京'or'福建'or'四川'):
        epi += 1

print("a、表格的总人数为：%s人" %num)
print('b、使用电信：%s人 ,使用移动:%s人 ,使用联通：%s人' %(telecom,move,link))
print("c、男生人数为：%s人 ,女生人数为:%s人" %(man,girl))
print('d、45岁以上的人数为：%s人' %age)
print('e、工资8000以上的人数为：%s人 ,工资3000以下的人数为：%s人' %(wage,wage3))
print('f、去传媒有限公司的人数为:%s人'%media)
print('g、高危地区的人数为：%s人'%epi)
