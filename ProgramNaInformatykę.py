nazwa = input("Podaj nazwę miejscowości bez spacji: ")
co_druga_litera = ""

for i in range(len(nazwa)):
    if i % 2 == 0:
        co_druga_litera += nazwa[i] + " "

print("Co druga litera nazwy miejscowości to:", co_druga_litera)