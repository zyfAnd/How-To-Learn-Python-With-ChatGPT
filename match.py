#match 就像是 java或者前端里的 Switch
#

yourscore  = 'B'
match yourscore: #match 是python 3.10版本开始引入的 所以确保版本在3.10 及其以上
    case 'A':
        print('your socre is A')
    case 'B':
        print('your score is B')
    case 'C':
        print('your score is C')
    case 'D':
        print('your score is D')
