spendings = [140, 30, 999, 145, 538, 878, 901, 613, 471, 286, 147, 90]
income = [300, 40, 0, 4000, 8911, 73, 85, 0, 9000, 941, 658, 190]
coeph = []
def calc(list ,list1):
    for i in range (12):
        try:
            a = list[i] / list1[i]
            coeph.append(a)
        except ZeroDivisionError:
            a = 0
            coeph.append(a)
            continue
calc(spendings,income)
total_coeph = sum(coeph)/12
print(f'{coeph}---------коэфициент,-------{total_coeph}----------средний коэфициент')
