
def main():

    print("hello world !")

if __name__ == "__main__":
     main()

# ceci est un commentaire
# délaration des variables

nombre=30
print(nombre)

nombre="trente"
print(nombre)

print("hello i'm " + str(30))

# fonction

age = 30 # variable GLOBALE

def uneFonction():
    global age # permet d'appeler la variable GLOBALE "age" dans la fonction 
    age=18 # variable LOCALE
    print(age)

uneFonction()
print(age)

################## LES FONCTIONS #####################

def fonctionTest(arg1, arg2):
    print(arg1, " ", arg2)

fonctionTest(3, 6)

#########################

def fontionMultiplay(arg3, arg4 = 6): # (arg4 = 6) est une valeurs par défault qui peut etre modifier dans l'appel de la fonction
    return(arg3 * arg4)

print(fontionMultiplay(3, 2)) # on peut choisir l'orde des arguments ex: (arg4=2, arg3=3)

#########################

def add(*args): # la fonction prend un nombre inconue de paramètres 
    result = 0
    for x in args:
        result = result + x
    return result # ATTENTION a l'indentation !!!! 

print(add(4, 9, 5, 10)) 

################################ CONDITIONS ##################################

def main2():
    x, y = 20, 20

    if ( x < y ):
        rs = " X is less than Y "
    elif ( x == y ):
        rs = " X is the same than Y "
    else:
        rs = " X is greater than Y "
    print(rs)


main2()

##################

def main3():
    x, y = 20, 20

    rs = " X is less than Y " if (x < y) else " X is the same or greater than Y "
    print(rs)

main3()