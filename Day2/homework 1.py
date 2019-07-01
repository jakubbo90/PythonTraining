#Easy

# 1. Przypisz do zmiennej o nazwie float_but_int wartosc dzielenia 50 / 2. Jakiego typu jest wynik (do sprawdzenia typu type(zmienna))?
#   Sprawdz przy pomocy metody wbudowanej w otrzymany wyzej typ czy liczba jest calkowita (dokumentacja - dir(nazwa_zmiennej) lub help(typ)), dokumentacja Python
float_but_int = 50/2
print(type(float_but_int))
print(float_but_int.is_integer())

#2. (Kalkulator, albo Python) - liczba zapisana w systemie binarnym na 8 bitach - 11011010 to w systemie dziesietnym liczba:

print (int('11011010',2))

# 3. Przypisz do 3 zmiennych pojedyncze slowa "Sun", "is", "setting", polacz je w jeden ciag znaków, ale tak, aby kazde slowo bylo w nowej linii, kazda nowa linia ma miec jedno
# wiecej wciecie tabulatora, tak aby wygladalo to nastepujaco:


word1 = 'Sun'
word2 = 'is'
word3 = 'setting'

print(f'{word1}\n\t{word2}\n\t\t{word3}')


#Medium
#4. zapoznaj sie z metoda input() w Python - wyszukaj w dokumentacji i sprawdz dzialanie. Funkcja print zachec uzytkownika, aby podal liczbe, nastepnie wypisz kwadrat oraz szescian tej liczby
# Postaraj sie o odpowiedni wyglad odpowiedzi, opisujacy uzyskane wyniki, np.
# zescian liczby x wynosi x^3, natomiast kwadrat x^2

print('Podaj liczbę, dla której chcesz obliczyć kwadrat i sześcian')
liczba=input()
kwadrat=float(liczba)**2
szescian=float(liczba)**3
print(f'Kwadrat liczby {liczba} wynosi {kwadrat}\nSześcian liczby {liczba} wynosi {szescian}')

#Challenging

#5. Warunek if - przy pomocy metody input pobierz od uzytkownia wartosc temperatury. Ustaw 3 minimalne temperatury jako zmienne - zimna, ciepla, goraca (np. 10 stopni, 20 stopni, 30 stopni)
# i na podstawie temperatury podanej przez uzytkownika, wyswietl czy jest zimno, cieplo, czy goraco

print('Podaj temperaturę:')
temp = input()
temp = int(temp)
zimno=10
cieplo=20
goraco=30

if temp < zimno:
    print('Zimno')
elif temp >= zimno and temp < cieplo:
    print ('Ciepło')
else:
    print('Gorąco')

#5. Oblicz silnie z podanej przez uzytkownika (metoda input) liczby -
# wyszukaj algorytm na silnie i napisz - przydadza sie zmienne, warunek if, operator *=

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