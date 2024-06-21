students  = {'Michel': 95, "Yanfu": 90, 'Bob':98,'Yanfu':88}

#判断某个key是不是在 dict里

if 'Yanfu' in students:
    print(students.get('Yanfu'))


#移除某个key
if 'Yanfu' in students:
    students.pop('Yanfu') 