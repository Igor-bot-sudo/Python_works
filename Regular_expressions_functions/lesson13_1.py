# import numbers
import re

numbers = ['4451 224611', '7657018439', '24 57 193847', '48 59 226582', \
           '40 87 547 510', '47-91-923-643', '47-25-661575']
accordances = ('\d{2} \d{2} \d{6}', '\d{2} \d{2} \d{3} \d{3}', \
               '\d{2}-\d{2}-\d{3}-\d{3}', '\d{2}-\d{2}-\d{6}')

for i in numbers:
    crit = False
    for k in accordances:
        regex = r'{}'.format(k)
        if re.search(regex, i):
            crit = True
            break
    if crit:
        print(f'{i} является номером паспорта')
    else:
        print(f'{i} не является номером паспорта')
