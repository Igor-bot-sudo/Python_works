class Atbash():
    __atbash_dict = {'А': 'я', 'Б': 'ю', 'В': 'э', 'Г': 'ь', 'Д': 'ы',\
                    'Е': 'ъ', 'Ё': 'щ', 'Ж': 'ш', 'З': 'ч', 'И': 'ц',\
                    'Й': 'х', 'К': 'ф', 'Л': 'у', 'М': 'т', 'Н': 'с',\
                    'О': 'р', 'П': 'п', 'Р': 'о', 'С': 'н', 'Т': 'м',\
                    'У': 'л', 'Ф': 'к', 'Х': 'й', 'Ц': 'и', 'Ч': 'з',\
                    'Ш': 'ж', 'Щ': 'ё', 'Ъ': 'е', 'Ы': 'д', 'Ь': 'г',\
                    'Э': 'в', 'Ю': 'б', 'Я': 'а', 'а': 'Я', 'б': 'Ю',\
                    'в': 'Э', 'г': 'Ь', 'д': 'Ы', 'е': 'Ъ', 'ё': 'Щ',\
                    'ж': 'Ш', 'з': 'Ч', 'и': 'Ц', 'й': 'Х', 'к': 'Ф',\
                    'л': 'У', 'м': 'Т', 'н': 'С', 'о': 'Р', 'п': 'П',\
                    'р': 'О', 'с': 'Н', 'т': 'М', 'у': 'Л', 'ф': 'К',\
                    'х': 'Й', 'ц': 'И', 'ч': 'З', 'ш': 'Ж', 'щ': 'Ё',\
                    'ъ': 'Е', 'ы': 'Д', 'ь': 'Г', 'э': 'В', 'ю': 'Б',\
                    'я': 'А'}  

    def encode(self, message):
        result = ''
        for i in message:
            if i in self.__atbash_dict.keys():
                result += self.__atbash_dict[i]
            else:
                result += i
        return result

    def decode(self, message):
        result = ''
        dict_keys = list(self.__atbash_dict.keys())
        dict_values = list(self.__atbash_dict.values())
        for i in message:
            if i in dict_values:
                indx = dict_values.index(i)
                result += dict_keys[indx]
            else:
                result += i
        return result


# a = Atbash()
# print(a.encode('Чтобы переварить знания, надо поглощать их с аппетитом.'))
# print(a.decode('зМРЮД ПЪОЪЭЯОЦМГ ЧСЯСЦА, СЯЫР ПРЬУРЁЯМГ ЦЙ Н ЯППЪМЦМРТ.'))
