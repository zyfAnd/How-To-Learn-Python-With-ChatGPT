age = input()
age = int(age)
if age >=6 and age <18:
    print('你是青少年')
elif age>=18 and age <60:
    print('你是成年人，未退休')
elif age<6 :
    print('你是儿童')
else :
    print('你是老年人')