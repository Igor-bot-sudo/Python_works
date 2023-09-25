order = {}
def purchase(prod: tuple[str, int]) -> dict[str, int]:
    order[prod[0]] = prod[1]

# while True:
#     product = input('\nТовар: ')
#     cost = int(input('Цена: '))
#     purchase((product, cost))
#     answer = input('Продолжить? [Да/нет]: ')
#     if answer.lower() in ('д', 'да'):
#         continue
#     else:
#         break

# print(order)
