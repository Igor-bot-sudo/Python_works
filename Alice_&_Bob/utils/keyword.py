class KeyWord:
    __letters_upper = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    __letters_lower = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def __init__(self, keyword) -> None:
        self.__keyword = ''.join(dict.fromkeys(keyword))
        x = self.__keyword.upper()
        t = ''.join([k for k in KeyWord.__letters_upper if k not in x])
        self.__lu = f'{x}{t}'

        x = self.__keyword.lower()
        t = ''.join([k for k in KeyWord.__letters_lower if k not in x])
        self.__ll = f'{x}{t}'     

    def encode(self, message):
        result = ''
        for i in message:
            if i in self.__letters_upper:
                position = self.__letters_upper.find(i)
                result += self.__lu[position]
            elif i in self.__letters_lower:
                position = self.__letters_lower.find(i)
                result += self.__ll[position]
            else:
                result += i
        return result

    def decode(self, message):
        result = ''
        for i in message:
            if i in self.__lu:
                position = self.__lu.find(i)
                result += self.__letters_upper[position]
            elif i in self.__ll:
                position = self.__ll.find(i)
                result += self.__letters_lower[position]
            else:
                result += i
        return result
