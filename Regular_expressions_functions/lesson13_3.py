import re


logins = ['Xia2nnБey6alogin', 'Mmyaakot', 'Ki47e0ra8hlogin', 'Tchel',\
        'n12login', 'Wol23fga7nlogin', 'Brighto', 'Olidia', 'Fabilogin',\
        '2name2login', 'name22login', 'x4login', '25login']

num = 0
for i in logins: 
    if re.search(r'^([A-Za-z]+[\d]+[A-Za-z\d]*[\d]+[A-Za-z]*|'
                 r'[A-Za-z]*[\d]+[A-Za-z\d]*[\d]+[A-Za-z]+|'
                 r'[A-Za-z]*[\d]+[A-Za-z\d]+[\d]+[A-Za-z]*)login$', i):
        print(i)
        num += 1

print(f'\nОбщее число валидных логинов: {num}')
