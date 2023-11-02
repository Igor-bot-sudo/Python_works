import re


numbers = ['E120AF', 'A618EP', 'AO308', '48 582', \
           'WE3456', 'GY469U', 'H934PB']

for i in numbers:
        if re.search(r'[A-Z]{1}[0-9]{3}[A-Z]{2}', i):
            print(f'{i} является автомобильным номером')
        else:
            print(f'{i} не является автомобильным номером')
