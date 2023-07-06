import matplotlib.pyplot as plt
import numpy as np

#원자번호 구하는거
def num(atomic):
    for i in range(1, 21):
        if atomic in atomic_data:
            atomic_number = atomic_data[atomic]

    return atomic_number

#주기 구하는거
def periodl(num):
    if num <= 2:
        period = 1
    elif num <= 10:
        period = 2
    elif num <= 18:
        period = 3
    else:
        period = 4
    return period

#유효 핵전하 구하기
def Zeffl(num):
    if num <= 2:
        Zeff = num - ((num-1) * 0.35)
    elif num <= 10:
        Zeff = num - 2 * 0.85 - (num-3)*0.35
    elif num <= 18:
        Zeff = num - 10 * 0.85 - (num-11)*0.35
    else:
        Zeff = num - 18 * 0.85 - (num-19)*0.35

    return Zeff

def second_largest_number(num):
    second = largest = -float('inf') 
    
    for n in num:
        if n > largest:
            second = largest
            largest = n
        elif second < n < largest:
            second = n

    return second

def Zeff_graph(Z_second,atomic_t):
    x = np.arange(4)

    plt.bar(x, Z_second)
    plt.xticks(x, atomic_t)

    plt.show()

def stripel(num):
    if num <= 2:
        if num == 2:
            stripe = 8
        else:
            stripe = 1
    elif num <= 10:
        stripe = num - 2
    elif num <= 18:
        stripe = num - 10
    else:
        stripe = num - 18
    return stripe

def atomic_radius(a_num,a_period,a_stripe,b_num,b_period,b_stripe):
    #원자 반지름
    if a_period == b_period:
        if a_num < b_num:
            inequality_sign = ">"
        else:
            inequality_sign = "<"
    elif a_stripe == b_stripe:
        if a_num < b_num:
            inequality_sign = "<"
        else:
            inequality_sign = ">"
    elif a_period != b_period and a_stripe != b_stripe:
       if a_period == 1:
           inequality_sign = “<“
       elif b_period == 1:
           inequality_sign = “>”
       elif 5 <= a_num <= 10:
           inequality_sign = “<“
       elif 5 <= b_num <= 10:
           inequality_sign = “>“
       elif a_num == 4 and 15 <= b_num <= 18:
           inequality_sign = “>”
       elif b_num == 4 and 15 <= a_num <= 18:
           inequality_sign = “<“
       elif a_num == 3 and 13 <= b_num <= 14 :
           inequality_sign = “>”
       elif b_num == 3 and 13 <= a_num <= 14:
          inequality_sign = “<“
       elif a_period ==3 and b_period == 4:
          inequality_sign = “<“
       elif b_period ==3 and a_period == 4:
          inequality_sign = “>“
       elif a_period == 4:
          inequality_sign = “>“
       elif b_period == 4:
          inequality_sign = “<”
    return inequality_sign


       


atomic_data = {'H': 1, 'He': 2, 
               'Li': 3, 'Be': 4, 'B': 5, 'C': 6, 'N': 7, 'O': 8,'F': 9, 'Ne': 10,
               'Na': 11, 'Mg': 12, 'Al': 13, 'Si': 14, 'P': 15, 'S': 16, 'Cl': 17, 'Ar': 18,
               'K': 19, 'Ca': 20}

input1 = str(input("4개의 원자를 공백으로 구분하여 입력하세요ex)Li He B C: "))
a = input1.split( )[0]
b = input1.split( )[1]
c = input1.split( )[2]
d = input1.split( )[3]
#원자번호 구하는거
a_num = int(num(a))
b_num = int(num(b))
c_num = int(num(c))
d_num = int(num(d))
#주기 구하는거
a_period = periodl(a_num)
b_period = periodl(b_num)
c_period = periodl(c_num)
d_period = periodl(d_num)
#유효 핵전하 구하기
a_Zeff = Zeffl(a_num)
b_Zeff = Zeffl(b_num)
c_Zeff = Zeffl(c_num)
d_Zeff = Zeffl(d_num)

a_stripe = stripel(a_num)
b_stripe = stripel(b_num)
c_stripe = stripel(c_num)
d_stripe = stripel(d_num)

Zeff_total = [[a,a_Zeff],[b,b_Zeff],[c,c_Zeff],[d,d_Zeff]]
Zeff_total.sort(key=lambda x: x[1])
Z_range = len(Zeff_total)
atomic_t = []
Z_second = []
for i in Zeff_total:
    atomic_t.append(i[0])
for l in Zeff_total:
    Z_second.append(l[1])

Zeff_graph(Z_second,atomic_t)

#원자 반지름
a_b = atomic_radius(a_num,a_period,a_stripe,b_num,b_period,b_stripe)
a_c = atomic_radius(a_num,a_period,a_stripe,c_num,c_period,c_stripe)
a_d = atomic_radius(a_num,a_period,a_stripe,d_num,d_period,d_stripe)
b_c = atomic_radius(b_num,b_period,b_stripe,c_num,c_period,c_stripe)
b_d = atomic_radius(b_num,b_period,b_stripe,d_num,d_period,d_stripe)
c_d = atomic_radius(c_num,c_period,c_stripe,d_num,d_period,d_stripe)
