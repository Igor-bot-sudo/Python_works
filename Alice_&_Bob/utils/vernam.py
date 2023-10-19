from random import randint

class Vernam:
    __symbols = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ0123456789 ,.:-?!()' 

    def __init__(self) -> None:
        var_num = 65
        self.forward_dict = {}
        self.backward_dict = {}
        for i in range(len(Vernam.__symbols)):
            self.forward_dict[Vernam.__symbols[i]] = str(var_num)
            self.backward_dict[str(var_num)] = Vernam.__symbols[i]
            var_num += 1

    def encode(self, message):
        message = message.upper()
        for x in message:
            if x not in Vernam.__symbols:
                message = message.replace(x, ' ')

        code_key = ''
        l = len(Vernam.__symbols)
        for _ in message:
            i = randint(0, l-1)
            code_key += Vernam.__symbols[i]

        result = ''
        coding_string = ''
        for i in range(len(message)):
            a = int(self.forward_dict[message[i]])
            b = int(self.forward_dict[code_key[i]])
            c = a ^ b
            b = hex(b)
            if len(b) < 4:
                b = '0x0' + b[-1]
            coding_string += b
            c = hex(c)
            if len(c) < 4:
                c = '0x0' + c[-1]
            result += c
        coding_string = coding_string.replace("0x", '')
        result = result.replace("0x", '')
        result += coding_string
        return result

    def decode(self, message):
        result = ''
        message_length = len(message)//2
        code_key = message[message_length:]
        message = message[:message_length]
        for i in range(message_length//2):
            s1 =  message[i*2] + message[i*2+1]
            s2 =  code_key[i*2] + code_key[i*2+1]
            a = int(s1, 16)
            b = int(s2, 16)
            c = str(a ^ b)
            result += self.backward_dict[c]
        return result
