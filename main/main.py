def show_menu():
    print('1. Citire liste')
    print('2. Afisati daca cele doua liste au acelasi numar de elemente pare')
    print('3. Afisati o lista care reprezinta intersectia celor doua liste citite de la tastatura')
    print('4. Afisati toate palindroamele obtinute prin concatenarea elementelor de pe aceleasi pozitii in cele doua liste')
    print('5.  Citiți o a treia listă și afișați listele obținute prin înlocuirea în cele două liste citite la punctul 1 a tuturor elementelor cu oglinditul lor dacă îndeplinesc următoarea regulă: elementele sunt divizibile cu toate elementele din a treia lista. Dacă nu îndeplinesc regula, păstrați elementul așa cum e')
    print('x. Exit')

def read_list():
    integers=[]
    int_as_str= input('Dati o lista de int-uti separate printr-un spatiu:  ')
    int_as_list_of_str = int_as_str.split(' ')
    for int_str in int_as_list_of_str:
        integers.append(int(int_str))
    return integers

def read_list2():

    integers_2=[]
    integers_as_str=input('Dati inca o lista de int-uri separate printr-un spatiu: ')
    integers_as_list_of_str = integers_as_str.split(' ')
    for integers_str in integers_as_list_of_str:
        integers_2.append(int(integers_str))
    return integers_2


def nr_pare_1(lst1):
    """
    Determina numarul elementelor pare din prima lista
    :param lst1: prima lista de int-uri
    :return: numarul elementelor pare din lista
    """

    result1=None
    nrp1=0
    for elem in lst1:
        if int(elem) % 2 == 0:
            nrp1=nrp1+1
        if result1 is None:
            result1=int(elem)
        else:
         result1= nrp1
    return result1



def test_nr_pare_1():
    assert nr_pare_1([2,3,4,5]) == 2
    assert nr_pare_1([2, 3, 4, 6]) == 3
    assert nr_pare_1([5,3]) is None

def nr_pare_2(lst2):
     """
    Determina numarul elementelor pare din a doua lista
    :param lst2: a doua lista de int-uri
    :return: numarul elementelor pare din lista
     """
     result2=None
     nrp2 = 0
     for elem in lst2:
          if int(elem) % 2 == 0:
                nrp2 = nrp2 + 1
          if result2 is None:
              result2=int(elem)
          else:
              result2= nrp2

     return result2

def test_nr_pare_2():
    assert nr_pare_2([2, 3, 4, 5]) == 2
    assert nr_pare_2([2, 3, 4, 6]) == 3
    assert nr_pare_2([2, 3]) == 1



def get_nr_elemente_pare(lst1,lst2):
    """
    Determina daca cele doua liste au acelasi numar de elemente pare
    :param lst1: prima lista de int-uri
    :param lst2: a doua lista de int-uri
    :return: True daca cele doua liste au acelasi numar de elemente pare,False in caz contrar
    """
    if result1(nrp1) == result2(nrp2):
        return True
    return False


def test_get_nr_elemente_pare():
    assert get_elemente_pare([2, 4, 5],[5,8,6]) == True
    assert get_elemente_pare([2, 4, 6], [5, 8, 6]) == False
    assert get_elemente_pare([1, 4, 5], [5, 8]) == True

def show_nr_elem_pare(lst1,lst2):
    result= get_nr_elemente_pare(lst1,lst2)
    print(f' Listele: {lst1} si {lst2} au acelasi nr de elemente pare: {result}')



def main():
    lst1=[]
    lst2=[]
    while True:
        show_menu()
        option=input('Alegeti optiunea: ')
        if option == '1':
            lst1=read_list()
            lst2=read_list2()

        elif option =='2':
            show_nr_elem_pare(lst1, lst2)
        elif option == '3':
            pass
        elif option == '4':
            pass
        elif option == '5':
            pass
        elif option == 'x':
            break
        else:
            print('Optiune invalida, reancearca!')


if __name__ == '__main__':
    test_nr_pare_1
    test_nr_pare_2
    test_get_nr_elemente_pare
    main()