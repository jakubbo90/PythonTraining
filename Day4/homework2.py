## https://www.geeksforgeeks.org/args-kwargs-python/

# 4. Napisz funkcję, która przyjmuje dowolną ilość parametrów - zaloz ze beda podawane liczbowe, funkcja ma wypisywac te parametry, uzywajac petli for in

def homework4(*argv):
    for arg in argv:
        print(f'Argument: {arg}')

print(homework4(1, 2, 3, 4, 5))

# 5. Zmodyfikuj funkcje z zadania wyzej tak, aby na koncu wypisala sume liczb podanych do funckji

def homework4(*argv):
    sum=0
    for arg in argv:
        sum = sum+arg
    print(f'Suma: {sum}')

print(homework4(1, 2, 3, 4, 5))

# 6. Inside - out - napisz dwie funckje - dodawanie (np o nazwie add) oraz mnozenie dwoch liczb (np o nazwie multiply), nastapnie wywolaj operację
# multiply(add(2, 6), 2)

def add(first_number,second_number):
    sum = float(first_number) + float(second_number)
    return(sum)

def multiply(arg1, arg2):
    multiply_result = float(arg1)*arg2
    print(f'Rezultat mnożenia: {multiply_result}')

print(multiply(add(2, 6), 3))

# 7. Napisz funkcję rozbijajaca zdanie na slowa (ma zwracac liste ze slowami) oraz funkcje sortujaca liste slow, nastepnie wywolaj sortowanie na slowach podanego przez uzytkownika zdania

sentence = input('Podaj zdanie:')
def split_sentence_to_words(sentence):
    word_list = sentence.split()
    return word_list

def sort_words(word_list):
    word_list.sort()
    return word_list
    print(word_list)

print(sort_words(split_sentence_to_words(sentence)))


# 8 (optional) Zaimportuj modul (plik) i uzyj funkcji z tego modulu
#  help(nazwa_pliku) - zadokumentuj troche kodu!

import split_sort_module
sentence2 = input('Podaj zdanie (modul zostanie uzyty):')
print(split_sort_module.sort_words(split_sort_module.split_sentence_to_words(sentence2)))
