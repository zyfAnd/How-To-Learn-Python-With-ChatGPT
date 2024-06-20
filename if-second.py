age = input()
age = int(age)#转换成int类型的数字
if age>=18:
    print('你的年龄是:', age)
    print('你是成年人了')
elif age>=6:
    print('你的年龄是:', age)
    print('你是青少年')
else:
    print('你的年龄是:', age)
    print('你是儿童')