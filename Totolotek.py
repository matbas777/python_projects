'''   fdvbrtybyynyn  yj6uju6j  j6j6jjjujuyj m7m78mu6  '''
import random

my_numbers = {1, 2, 3, 4, 5, 6}

numbers = list(range(1, 50))
lalal = {1, 2, 3, 4}
# print(len(lalal))

def lottery():
    # KOMENTARZ DO RANDOM NUMBERS
    random_numbers = []
    while len(random_numbers) != 6:
        new_number = random.choice(numbers)
        if new_number not in random_numbers:
            random_numbers.append(new_number)
    return random_numbers

# print(len(set(lottery()).intersection(my_numbers)))
# print(len(z))
i =1
proba_6 = 1
proba_5 = 1
proba_4 = 1
proba_3 = 1
while not set(lottery()).issubset(my_numbers):
    proba_6 += 1
    i +=1
    print(i)
    if len(set(lottery()).intersection(my_numbers)) > 5:
        proba_5 += 1
    # else:
    #     print('masz wygrana! trafile 5')
    if len(set(lottery()).intersection(my_numbers)) > 4:
        proba_4 += 1
    # else:
    #     print('masz wygrana! trafile 4')
    if len(set(lottery()).intersection(my_numbers)) > 3:
        proba_3 += 1
    # else:
    #     print('masz wygrana! trafile 3')
else:
    print('glowna wygrana')
print(proba_6)
print(proba_5)
print(proba_4)
print(proba_3)






# print(random_numbers)
#
# alal = {1, 2, 3, 4, 5, 6}
#
# print(alal.issubset(my_numbers))