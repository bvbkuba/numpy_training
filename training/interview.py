""" ZADANIE 3. NALEŻY WYGENEROWAĆ LISTĘ LICZB OD 2 DO 5.5 ZE SKOKIEM CO 0.5, DANE WYNIKOWE MUSZĄ BYĆ TYPU DECIMAL."""

def generate_numbers():
    """
    The function hasn't arguments. It return list of numbers between 2 and 5.5 with step 0.5. Type decimal.
    """
    from decimal import Decimal   #import Decimal
    list_of_numbers = []
    step = Decimal(0.5)   #step
    number = Decimal(2)    #start
    while number<=5.5:  #simple loop
        list_of_numbers.append(number)
        number+= step

    return list_of_numbers

print(generate_numbers())


"""ZADANIE 1. GENERATOR KODÓW POCZTOWYCH
przyjmuje 2 stringi: "79-900" i "80-155" i zwraca listę kodów pomiędzy nimi"""


def post_code_generator(code1:str,code2:str):
    """
    The func return list of postcodes between first and second postcode.
    """

    try:
        code1 = int((code1.replace('-','')))        #transform postcode to int
        code2 = int(code2.replace('-',''))
        if code1 < 10000 or code1>99999 or code2 < 10000 or code2>99999: #conditional : post code must be like NN-NNN
            raise IndentationError
        difference = abs(code1-code2)  #I could write in in line 36 - list comprahensions, but it's better to write the code.
        if code2>code1:
            return [str(code1+i)[:2]+ '-'+str(code1+i)[2:] for i in range(1,difference)]
        elif code1>code2:
            return [str(code2+i)[:2]+'-'+str(code2+i)[2:] for i in range(1,difference)]
        elif code1==code2:
            return []
        else:
            return 'Incorrect data'

    except IndentationError as ie:
        return f"Probably you didn't write good type of arguments. Please enter a postcodes like string. 'NN-NNN'. More informations: {ie} "
    except Exception as e:
        return f"Error. More information in : {ex}"

print(post_code_generator("51-500",'31-10'))

"""ZADANIE 2. PODANA JEST LISTA ZAWIERAJĄCA ELEMENTY O WARTOŚCIACH 1-n. NAPISZ FUNKCJĘ KTÓRA SPRAWDZI JAKICH ELEMENTÓW BRAKUJE
1-n = [1,2,3,4,5,...,10]
np. n=10
wejście: [2,3,7,4,9], 10
wyjście: [1,5,6,8,10]"""

def lack_numbers(list_numbers:list, n):
    """The function return list of lacking numbers. For example:
n=10
in: [2,3,7,4,9], 10
out: [1,5,6,8,10]

    """
    try:
        lack_of_list_numbers = [i for i in range(1,n+1) if i not in list_numbers]  #simple list comprahensions
        return lack_of_list_numbers
    except TypeError as e:
        return f"Please remember that first argument must be a list, second an int. More information: {e}"
    except Exception as ex:
        return f"Error. More information in : {ex}"


