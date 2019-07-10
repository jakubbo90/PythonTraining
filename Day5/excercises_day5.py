def dodaj_imie(imie, imiona=[]):
    imiona.append(imie)
    return imiona

# napisz funkcję sumujący wszystkie elementy w liscie
def sum_list(list2sum):
    suma=sum(list2sum)
    return(suma)

list4functions = [1,2,5]
print("Suma z listy: " + str(sum_list(list4functions)))

# znajdz najwiekszy / najmniejszy element w liscie - napisz dwie funkcje
def find_largest_from_list_recznie(list4functions):
    list4functions.sort(reverse=True)
    largest_recznie = list4functions[0]
    return largest_recznie

print("Najwiekszy z listy recznie: " + str(find_largest_from_list_recznie(list4functions)))

def find_largest_from_list(list4functions):
    largest = max(list4functions)
    return largest

print("Najwiekszy z listy: " + str(find_largest_from_list(list4functions)))

def find_lowest_from_list_recznie(list4functions):
    list4functions.sort(reverse=False)
    lowest_recznie = list4functions[0]
    return lowest_recznie

print("Najmniejszy z listy recznie: " + str(find_lowest_from_list_recznie(list4functions)))

def find_lowest_from_list(list4functions):
    lowest = min(list4functions)
    return lowest

print("Najmniejszy z listy: " + str(find_lowest_from_list(list4functions)))

# funkcja ktory zmieni zdanie w liste wyrazow
zdanie = "Ala ma kota, kot ma Ale"
def words_list(zdanie):
    zdanie_splitted = zdanie.split()
    return zdanie_splitted

print("Lista wyrazow ze zdania: " + str(words_list(zdanie)))

# napisz funckję przyjmujaca liste stringow,
# a zwracakaca liczbe stringow dl. min. 2, ktore zaczynaja sie i koncza na te same znaki
# ['abc', 'xyz', 'aba', '1221'] - odp = 2

lista_stringow = ['abc', 'xyz', 'aba', '1221', '9asdadsd9', 'aa']
def search4strings_starting_ending_the_same(lista_stringow):
    selected_strings = []
    for word in lista_stringow:
        if word[0] == word[-1] and len(word) >2:
            selected_strings.append(word)
        else:
            pass
    return selected_strings

print("Lista wyrazow ze zdania zaczynajace sie na te sama litere i sa dluzsze niz 2: " + str(search4strings_starting_ending_the_same(lista_stringow)))

# program znajdujacy wartosci, ktre wystepuja tylko raz
lista_a = [10,20,30,20,10,50,60,40,80,50,40]

def find_unique_number(lista_a):
    unique_list = []
    for number in lista_a:
        occurence = lista_a.count(number)
        if occurence == 1:
            unique_list.append(number)
        else:
            pass
    return unique_list

print("Lista unikalnych liczb: " + str(find_unique_number(lista_a)))


# program usuwajacy zduplikowane wartosci w liscie (w miejscu! - tzn bez drugiej listy)
# podpowiedz - del lub pop()

lista_b = [10,10,20,10,10,20,10,20,20,20,40,50,40,10,30,50,50,30,1]
def remove_duplicates(lista_b):
    for number in lista_b:
        occurence = lista_b.count(number)
        if occurence == 1:
            pass
        else:
            lista_b.remove(number)
    return lista_b

print("!!!!Lista z usunietymi duplikatami z uzyciem remove(): " + str(remove_duplicates(lista_b)))

lista_b2 = [10,10,20,10,10,20,10,20,20,20,40,50,40,10,30,50,50,30,1]
def remove_duplicates_set(lista_b2):
    lista_b2 = list(set(lista_b2))
    return lista_b2

print("!!!!Lista z usunietymi duplikatami z uzyciem set(): " + str(remove_duplicates_set(lista_b2)))


# program sprawdza czy dwie listy maja co najmniej jeden wspolny element,
# jesli tak wypisuje True
lista_c = [10,20,20,10,50,60,40,80,50,30]
lista_d = [110,150,30,300]

def find_if_common(lista_c, lista_d):
    for number in lista_c:
        if number in lista_d:
            return True

print("Lista_c i Lista_d mają wspólną część: " + str(find_if_common(lista_c, lista_d)))

# stworz macierz (4 x 5), ktorej wszystkie komorki wypelnione sa znakiem *
matrix_sign = '*'
print("Macierz:")
for element in range(4):
    print(5*matrix_sign)

# wybierz losowo element z listy
# wskazowka - import random
import random
lista_e = [10,20,30,20,10,50,60,40,80,50,123,554,123,33455,1,12366,36,87,2]
def find_random_in_list(lista_e):
    random_element = random.choice(lista_e)
    return random_element

print("Random element z listy_e: " + str(find_random_in_list(lista_e)))

# oblicz częstość elementów w liście (ile razy)
# jedna wersja zwykla pętle, ify itd
# druga - moze jest jakis modul gotowy???
my_list = [10,10,20,10,10,20,10,20,20,20,40,50,40,10,30,50,50,30]
def count_list_elements(my_list):
    my_list.sort()
    print(f'My list: {my_list}')
    list_of_counts = []
    for element in my_list:
        element_count = my_list.count(element)
        list_of_counts.append(tuple((element, element_count)))
    list_of_counts=list(set(list_of_counts))
    list_of_counts.sort()
    print(f'List of counted elements: {list_of_counts}')

print(count_list_elements(my_list))
