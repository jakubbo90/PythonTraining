# zdanie='encyklopedia'
# print(zdanie[4])
# print(zdanie[-3])
# print(zdanie[2:8])
# print(zdanie[:7])
# print(zdanie[8:])
# print(zdanie[1:7:2])
# print(zdanie[::-1])
# print(zdanie[:-1])
# print(zdanie[::2])
# print(zdanie[::-2])

# temperature = input("Podaj temperaturę:")
# temperature = int(temperature)
# HOT_TEMP = 30
# WARM_TEMP = 25
# COLD_TEMP = 20
# if temperature >= HOT_TEMP:
#     print("It's hot")
# elif (temperature) >= WARM_TEMP:
#     print("It's warm")
# else:
#     print("It's cold")
#
# slowo = input("Podaj zdanie:")
# if  slowo[0].lower() == 'a':
#     print(f"Zdanie '{slowo}' zaczyna się na pierwszą literę alfabetu")
# elif slowo[0].lower() == 'z':
#     print(f"Zdanie '{slowo}' zaczyna się na ostatnią literę alfabetu")
# else:
#     print(f"Zdanie '{slowo}' nie zaczyna się ani od pierwszej ani od ostatniej litery alfabetu")

# zdanie = input("Podaj zdanie:")
# zdanie_splitted = zdanie.split()
# slowo = input("Szukane słowo:")
#
# if slowo in zdanie_splitted:
#     print(f"Słowo {slowo} znajduje się z zdaniu '{zdanie}'")
# else:
#     print(f"Słowo {slowo} nie znajduje się z zdaniu '{zdanie}'")

# lista = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# print(lista[1:3])

# repeatHowManyTimes = int(input("Please tell me how many times to repeat..."))
# # for index in range(repeatHowManyTimes):
# #     print("Hello, it's me")

# for character in "encyklopedia":
#     print(character)

#Zadanie 0

# lista_miesiecy=['Jan','Feb','Mar','Apr','May']
# for miesiac in lista_miesiecy:
#     print(miesiac)

#Zadanie 1
# text = "Python is a fantastic snake"
# for character in text[0::4]:
#     print(character,end="")


#Zadanie 1 v.2
# text = "Python is a fantastic snake"
# how_many_characters=len(text)
# every_second_index=range(0,how_many_characters,3)
# print(every_second_index)
#
# for idx in every_second_index:
#     print(text[idx],end="")

#Zadanie 2
# text = "Python is a fantastic snake"
# text_splitted = text.split()
# for element in text_splitted:
#     print(element)

# zdanie=input("Podaj zdanie do rozbicia:")
# zdanie_splitted = zdanie.split()
# for element in zdanie_splitted:
#     print(element)


x_input = input("Podaj wartość, dla której chcesz obliczyć silnię:")
try:
    int(x_input)
    x=int(x_input)
except:
    print("Liczba nie jest liczbą całkowitą. Podaj inną liczbę.")
y = 1

if 'x' in locals():
    for element in range(1,x+1):
        y=(element*y)
    print(y)