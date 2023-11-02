import random


rand_list = []

def fill_random(rand_list):
    for i in range(20):
        rand_list.append(random.uniform(0, 20))

fill_random(rand_list)
print(rand_list)