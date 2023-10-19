class Caesar:
    __letters_upper = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ\
АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    __letters_lower = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя\
абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def __init__(self, shift) -> None:
        self.__shift = shift

    def encode(self, message):
        result = ''
        for i in message:
            if i in Caesar.__letters_upper:
                position = Caesar.__letters_upper.find(i)
                new_position = position + self.__shift
                result += Caesar.__letters_upper[new_position]
            elif i in Caesar.__letters_lower:
                position = Caesar.__letters_lower.find(i)
                new_position = position + self.__shift
                result += Caesar.__letters_lower[new_position]
            else:
                result += i
        return result

    def decode(self, message):
        result = ''
        for i in message:
            if i in Caesar.__letters_upper:
                position = Caesar.__letters_upper.rfind(i)
                new_position = position - self.__shift
                result += Caesar.__letters_upper[new_position]
            elif i in Caesar.__letters_lower:
                position = Caesar.__letters_lower.rfind(i)
                new_position = position - self.__shift
                result += Caesar.__letters_lower[new_position]
            else:
                result += i
        return result
  