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

def Zeff_graph(Z_second,atomic_t,title):
    x = np.arange(4)

    plt.bar(x, Z_second)
    plt.xticks(x, atomic_t)

    plt.title(title)

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
           inequality_sign = "<"
       elif b_period == 1:
           inequality_sign = ">"
       elif 5 <= a_num <= 10:
           inequality_sign = "<"
       elif 5 <= b_num <= 10:
           inequality_sign = ">"
       elif a_num == 4 and 15 <= b_num <= 18:
           inequality_sign = ">"
       elif b_num == 4 and 15 <= a_num <= 18:
           inequality_sign = "<"
       elif a_num == 3 and 13 <= b_num <= 18:
           inequality_sign = ">"
       elif b_num == 3 and 13 <= a_num <= 18:
          inequality_sign = "<"
       elif a_num == 3 and 11 <= b_num <= 12:
           inequality_sign = "<"
       elif b_num == 3 and 11 <= a_num <= 12:
          inequality_sign = ">" 
       elif a_period == 2 and b_period == 3:
           inequality_sign = "<"
       elif b_period == 2 and a_period == 3:
          inequality_sign = ">" 
       elif a_period == 4:
          inequality_sign = ">"
       elif b_period == 4:
          inequality_sign = "<"
    return inequality_sign

#이온화 에너지 구하기
def ionizationl(t):
    for i in range(1, 21):
        if t in ionization_data:
            ionization_number = ionization_data[t]

    return ionization_number

ionization_data = {0:0,1: 1312,2: 2372.5,
                   3: 520.3, 4:899.5, 5: 800.6, 6: 1086.5, 7: 1402.3, 8: 1313.9, 9: 1681, 10: 2080.7,
                   11: 495.8, 12: 737.7, 13: 577.5, 14: 786.5, 15: 1011.8, 16: 999.6, 17: 1251.2, 18:1520.6,
                   19: 418.8, 20:589.8}


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

Zeff_graph(Z_second,atomic_t,"effective nuclear charge")

#원자 반지름
a_b = atomic_radius(a_num,a_period,a_stripe,b_num,b_period,b_stripe)
a_c = atomic_radius(a_num,a_period,a_stripe,c_num,c_period,c_stripe)
a_d = atomic_radius(a_num,a_period,a_stripe,d_num,d_period,d_stripe)
b_c = atomic_radius(b_num,b_period,b_stripe,c_num,c_period,c_stripe)
b_d = atomic_radius(b_num,b_period,b_stripe,d_num,d_period,d_stripe)
c_d = atomic_radius(c_num,c_period,c_stripe,d_num,d_period,d_stripe)

a_ratio = []
b_ratio = []
c_ratio = []
d_ratio = []
a_ratio.append(a_b)
a_ratio.append(a_c)
a_ratio.append(a_d)
b_ratio.append(a_b)
b_ratio.append(b_c)
b_ratio.append(b_d)
c_ratio.append(a_c)
c_ratio.append(b_c)
c_ratio.append(c_d)
d_ratio.append(a_d)
d_ratio.append(b_d)
d_ratio.append(c_d)

a_th = 0
b_th = 0
c_th = 0
d_th = 0
if a_ratio.count('>') ==3:
    a_th = 0
elif a_ratio.count('>') ==2:
    a_th = 1
elif a_ratio.count('>') ==1:
    a_th = 2
elif a_ratio.count('>') ==0:
    a_th = 3

if b_ratio[0] == '<' and b_ratio.count('>') == 2:
    b_th = 0
elif b_ratio[0] == '<' and b_ratio.count('>') == 1:
    b_th = 1
elif b_ratio[0] == '>' and b_ratio.count('>') == 3:
    b_th = 1
elif b_ratio[0] == '<' and b_ratio.count('>') == 0:
    b_th = 2
elif b_ratio[0] == '>' and b_ratio.count('>') == 2:
    b_th = 2
elif b_ratio[0] == '>' and b_ratio.count('>') == 1:
    b_th = 3

if c_ratio[2] == '>' and b_ratio.count('<') == 2:
    c_th = 0
elif c_ratio[2] == '>' and b_ratio.count('<') == 1:
    c_th = 1
elif c_ratio[2] == '<' and b_ratio.count('<') == 3:
    c_th = 1
elif c_ratio[2] == '>' and b_ratio.count('<') == 0:
    c_th = 2
elif c_ratio[2] == '<' and b_ratio.count('<') == 2:
    c_th = 2
elif c_ratio[2] == '>' and b_ratio.count('>') == 2:
    c_th = 3

if d_ratio.count('<') ==3:
    d_th = 0
elif d_ratio.count('<') ==2:
    d_th = 1
elif a_ratio.count('<') ==1:
    d_th = 2
elif a_ratio.count('<') ==0:
    d_th = 3

total_example= list(range(4))
total_example[a_th] = a
total_example[b_th] = b
total_example[c_th] = c
total_example[d_th] = d
print(total_example)
print("원자 반지름: ",total_example[0], ">", total_example[1], ">", total_example[2], ">", total_example[3])

a_ionization1 = ionizationl(a_num)
b_ionization1 = ionizationl(b_num)
c_ionization1 = ionizationl(c_num)
d_ionization1 = ionizationl(d_num)

ionization_total = [[a,a_ionization1],[b,b_ionization1],[c,c_ionization1],[d,d_ionization1]]
ionization_total.sort(key=lambda x: -x[1])
i_range = len(ionization_total)
ionization_t = []
i_second = []
for i in ionization_total:
    ionization_t.append(i[0])
for l in ionization_total:
    i_second.append(l[1])

Zeff_graph(i_second,ionization_t,"1st ionization energy")
print("1차 이온화 에너지: ",ionization_t[0],">",ionization_t[1],">",ionization_t[2],">",ionization_t[3])

a_ionization2 = ionizationl(a_num - 1)
b_ionization2 = ionizationl(b_num - 1)
c_ionization2 = ionizationl(c_num - 1)
d_ionization2 = ionizationl(d_num - 1)

ionization_total2 = [[a,a_ionization2],[b,b_ionization2],[c,c_ionization2],[d,d_ionization2]]
ionization_total2.sort(key=lambda x: -x[1])
i_range = len(ionization_total2)
ionization_t2 = []
i_second2 = []
for i in ionization_total2:
    ionization_t2.append(i[0])
for l in ionization_total2:
    i_second2.append(l[1])

Zeff_graph(i_second2,ionization_t2,"Secondary ionization energy")
print("2차 이온화 에너지: ",ionization_t2[0],">",ionization_t2[1],">",ionization_t2[2],">",ionization_t2[3])
