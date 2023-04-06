# stan_konta = input("Ile masz kasy?")
# stan_konta = int(stan_konta)
# stan_konta = stan_konta + 500 * 2
# print(stan_konta)


# x = 9
# y = x/2
#
# print(y)

# temperature = 15
# happy = False
#
# if temperature > 10 or happy:
#     print("git idę")
# elif temperature > -10:
#     print("ciepło ubierz się")
# else:
#     print("nie git")


# for i in range(1, 10, 2):
#     print(i)

# while temperature > 10:
#     print("elo")
#     temperature -= 1


oceny = [4, 1, 2, 6, 4, 4, 3, 1]

# for ocena in oceny:
#     print(oceny[ocena], end=" ")

# for i, ocena in enumerate(oceny):
#     if i % 2 == 0 and ocena > 3:
#         print(ocena, " Jest na pozycji na liście jako ", i)


oceny.append(5) #dodaje do listy
oceny.extend([1,1,1]) #dodaje większą liczbe rzeczy do listy
oceny.insert(1, 6) #dodaje recz do listy w konkretnym miejscu
oceny.pop() #Usuwa ostatni element
oceny.sort() #Sortuje w porządku rosnącym



print(oceny)









