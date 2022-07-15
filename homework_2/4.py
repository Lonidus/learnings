educational_grant, expenses = 10000, 12000
month = 0
summ = 0
while month < 10:
    month = month + 1
    summ = summ + round(educational_grant - expenses)
    expenses = expenses * 1.03
print(summ * -1)
