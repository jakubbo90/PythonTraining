# jako prace domową - przejrzyj zadania - examples z folderu Trainings - przykłady nie zaczynaja sie od numeru
# oraz rozwiaz zadania z folderu Trainings (pliki zaczynajace sie od numerow)

# oraz:

# 1 stwórz słownik, którego kluczem będą słowa, natomiast wartością znaczenie tych słów
# może być słownik miejskiego slangu ;)

slang_dict = {"ziomek": "kumpel", "stara": "matka", "hajs": "pieniadze", "melanz": "impreza"}

# print(slang_dict.keys())
# print(slang_dict.values())
# print(slang_dict.get("ziomek"))
print(slang_dict.items())

print("For key in slang dict wynik:")
for key in slang_dict:
    print(key,slang_dict.get(key))

# 2 zapisz prosta zawartosc slownika miejskiego slangu do pliku, w kazdej linii klucz - wartosc
# np kasiora - Opis slowa kasiora, w nowej linii nastepna para
print("Zadanie 2:")
with open("slang.txt","w") as plik_slang:
    for key in slang_dict:
        plik_slang.writelines(f"{key}: {slang_dict.get(key)}\n")


# 3 zapisz slownik slangu miejskiego do pliku csv, gdzie klucz (slowo) i wartosc (wyjasnienie slowa)
# beda oddzielone pionową linią pipe (|) - przyklad zapisu pliku csv w Day6\exercises\cs_example

import csv
with open("slang.csv","w",newline='') as csv_plik:
    writer = csv.writer(csv_plik, delimiter="|")
    writer.writerows(slang_dict.items())


# 4 zapisz slownik slangu miejskiego jako pickle - przyklad w Day6\exercises\pickle_1.py
# odczytaj plik i sprawdz czy poprawnie zapisano dane

import pickle
with open("slang_pickle.txt","wb") as pickle_writer:
    pickle.dump(slang_dict,pickle_writer)

with open("slang_pickle.txt","rb") as pickle_reader:
    dict_reader = pickle.load(pickle_reader)
    print(dict_reader)

# 5 odczytaj plik article.txt w calosci - plik umieszczony w Day5\exercises\article.txt
# pozwol uzytkownikowi na podanie slowa i policz ile razy dane slowo wystepuje w artykule
# (powiedz uzytkownikowi ile razy wystepuje)

# PROGRAM DO OBLICZANIA WYSTEPOWANIA KAZDEGO ZE SLOW:
import re

with open("article.txt", "r") as plik:
    word_list = []
    article = plik.read()
    splitted_article = article.split()
    # print(splitted_article)
    for word in splitted_article:
        word_list.append(word)
    word_list[:] = [re.sub('[^A-Za-z0-9-]+', '', s) for s in word_list]
    word_list.sort()
    word_list = [x.lower() for x in word_list]
    unique_words = []
    unique_words = set(word_list)
    unique_words_list = list(unique_words)
    unique_words_list.sort()
    for word in unique_words_list:
        word_list_counter = []
        word_list_counter = [x for x in word_list if x == word]
        print(f"Word '{word}' occurence number is: {len(word_list_counter)}")
    # word_list = [word for line in word_list for word in line.split()]
    # print(word_list)
    # print(number_of_lines)
    # for line in lines:
    #     print(line,end='')

# PROGRAM DO OBLICZANIA WYSTEPOWANIA PODANEGO SLOWA:

with open("article.txt", "r") as plik_choose:
    chosen_word = input(f"Choose word to count in article: ")
    chosen_word.lower()
    word_list_choose = []
    article_choose = plik_choose.read()
    splitted_article_choose = article.split()
    for word_choose in splitted_article_choose:
        word_list_choose.append(word_choose)
    word_list_choose[:] = [re.sub('[^A-Za-z0-9-]+', '', s) for s in word_list_choose]
    word_list_choose = [x.lower() for x in word_list_choose]
    selected_word_list = [x for x in word_list_choose if x == chosen_word]
    print(f"Word '{chosen_word}' occurence in article is: {len(selected_word_list)}")


# 6 utwórz program, w ktorym uzytkownik bedzie mogl powiekszac baze slow slangu miejskiego
# na poczatku programu zaladuj slownik z pliku pickle
# (sprawdz czy plik istnieje, albo po wykonaniu zadania 4 uzyj istniejacego pliku)
# napisz program tak, aby uzytkownik mogl dodawac slowa i ich wyjasnienie, dopoki nie zechce wyjsc z programu
# (moze byc krotkie pytanie czy chcesz dodac slowo do slownika? TAK/NIE)
# na koncu programu zapisz slownik ponownie do pliku pickle, aby zapisac zmiany

import pickle
with open("slang_pickle.txt","rb") as pickle_reader:
    dict_reader = pickle.load(pickle_reader)
    print(f"Stary slownik: {dict_reader}")

updated_dictionary = dict_reader

print("Podaj slowo, a nastepnie jego wyjasnienie.")
next = "TAK"
choose_list = ["TAK","NIE"]
bledny_wybor = "OK"
while next != "NIE":
        if next != "NIE":
            next = input("Czy chcesz dodac kolejne slowo? (TAK/NIE): ")
        else:
            break
        if next in choose_list:
            if (bledny_wybor == "NOT OK" or next == "TAK") and next != "NIE":
                pass
            else:
                next = input("Czy chcesz dodac kolejne slowo? (TAK/NIE): ")
            if next == "TAK":
                slowo = input("Podaj slowo w slangu: ")
                wyjasnienie = input("Podaj wyjasnienie slowa: ")
                wybor = input("Czy chcesz dodac slowo do slownika? (TAK/NIE): ")
                if wybor in choose_list:
                    if wybor == "TAK":
                        updated_dictionary[slowo] = wyjasnienie
                    else:
                        break
                else:
                    print("Wybor powinien byc TAK lub NIE, sprobuj ponownie.")
                    bledny_wybor = "NOT OK"
                    next == "TAK"
                    continue
        else:
            print("Wybor powinien byc TAK lub NIE, sprobuj ponownie.")
            bledny_wybor = "NOT OK"
            continue

with open("slang_pickle.txt","wb") as pickle_writer:
    pickle.dump(updated_dictionary,pickle_writer)

with open("slang_pickle.txt", "rb") as pickle_reader:
    dict_reader = pickle.load(pickle_reader)
    print(f"Nowy slownik: {dict_reader}")