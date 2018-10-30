# coding: utf-8
# Author: Zhongyang Zhang
# Email : mirakuruyoo@gmail.com

import time
def compute(sum, sum_credit, fo):
    result = sum/sum_credit
    print("==> Your GPA is:%.3f"%result)
    fo.write("\n==> Your GPA is:%.3f"%result)
    fo.close()

print("\n==> Please input a number to continue or \n==> Input a 'q' to quit!")
sum_credit = 0
sum = 0
fo = open("GPA_Report_%s.txt"%time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()), "w+")
while True:
    while True:
        credit = input("credit:")
        if credit == 'q':
            compute(sum, sum_credit, fo)
            exit(0)
        else:
            try:
                credit = float(credit)
            except:
                pass
            else:
                break
    while True:
        grade  = input("grade:")
        if grade == 'q':
            compute(sum, sum_credit, fo)
            exit(0)
        else:
            try:
                grade  = float(grade)
            except:
                pass
            else:
                break
    if grade >= 85:
        point = 4.0
    elif grade < 60:
        point = 0.0
    else:
        point = 1.5 + (grade - 60) * 0.1
    sum += credit * point
    sum_credit += credit
    fo.write("credit: %.2f, grade: %.1f, point: %.1f\n" % (credit, grade, point))



