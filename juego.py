from random import randint
carton=[[],[],[],[],[]]
def cartonBingo(carton):
    randint(0,75)
    i=0
    while len(carton[4])<5:

        while len(carton[i])<5:
            num=randint(1,76)
            e=0
            while e<len(carton):
                if num in carton[e]:
                    num=randint(1,76)
                    e=0
                e+=1
            num=num
            carton[i].append(num)
        i+=1
    print(carton)
    menu()
def validarNum(carton):
    num=int(input("ingrese un numero: "))
    i=0
    while i<len(carton):
        e=0
        while e<len(carton[i]):
            if num==carton[i][e]:
                carton[i][e]="x"
            e+=1
        i+=1
    win=False
    j=0
    while j<len(carton):
        d=0
        while d<len(carton[j]):
            r=0
            while carton[j][r]=="x":
                r+=1
                if r==5:
                    win=True
                    break

            d+=1
        j+=1
    n=0
    while n<len(carton):
        g=0
        while carton[g][n]=="x":
            g+=1
            if g==5:
                win=True
                break
        n+=1

    if win==True:
        print("gano")
        menu()
    else:
        validarNum(carton)

def menu():
    print("opcion 1) crear carton\n"
          "opcion 2) jugar\n"
          "opcion 3) salir")

    opcion=int(input("ingrese la opcion escogida: "))
    if opcion==1:
        cartonBingo(carton)
    if opcion==2:
        if carton[0]!=0:
            validarNum(carton)
        else:
            print("no se ha creado el carton")
            menu()
    if opcion==3:
        print("gracias")
menu()