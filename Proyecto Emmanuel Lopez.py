users=[]#list of registered users
def login():
    ID=input("write your identification: ")
    password=input("write your password: ")
    if len(users)!=0:
        i=0
        while i < len(users):
            if users[i]["ID"]==ID and users[i]["password"]==password:
                print("welcome")
                if users[i]["typeuser"]==True:
                    menuAdmi()
                    break
                if users[i]["typeuser"]==False:
                    if len(listprovince)!=0:
                        CONSULTSINV()
                        break
                    else:
                        print("not exists datas")
                        menu()
            i+=1
        i=0
        while i< len(users):
            if users[i]["ID"]!=ID or users[i]["password"]!=password:
                print("the password or the ID are incorrect")
                menu()
                break
            i+=1
    else:
        print("empty record")
        register()
# To enter the administrator menu or the guest menu,
# the password and the ID must be the same as those in the "user list",
# the function uses flags (True or False) to call the menu that corresponds to the user.
def register():
    print("___registering___")
    name=input("write your name: ")
    age=input("write your age: ")
    ID=input("write your identificaction: ")
    email=input("write your e-mail: ")
    password=input("write your password: ")
    admin=opcionadmin()
    x={"name":name,"age":age,"ID":ID,"email":email,"password":password,"typeuser":admin}
    users.append(x)
    print("succers user register")
    print(users)
    print("_____________________________________________________ \n")
    menu()
#The "register" function adds the data of a new user in the list of "users",
#so that later the user can use the program with its respective functions.
def menu():
    print("___Welcome, what do you want to do?___\n"
            "Option 1: login\n"
            "Option 2: register \n"
            "Option 3: exit")
    try:
        opcion=int(input("write a number to select an action: "))
        if opcion==1:
            login()
        elif opcion==2:
            register()
        elif opcion==3:
            print("good bye")
            return
        else:
            print("Invalid value, try again")
            menu()
    except ValueError:
        print("Invalid value, try again")
        menu()
#main menu
def opcionadmin():
    try:
        opcion=int(input("write 1 for Administrator\n"
                         "write 2 for Invited\n"
                         "What type of user do you want to be?: "))
        admin=False
        if opcion==1:
            admin=True
        elif opcion==2:
            admin=False
        else:
            print("invalid value")
            opcionadmin()
        return admin
    except ValueError:
        print("invalid value")
        opcionadmin()
#"opcionadmin" is a function that recognizes and saves the user type the person elected.
def menuinvitado():
    print("Invited")
#main menu of invited
def menuAdmi():
    print("___Aministrator menu___")
    print("Option 1: Territorial distribution\n"
          "Option 2: Administration of political parties\n"
          "Option 3: Administration of ballots\n"
          "Option 4: Result status\n"
          "Option 5: consultations\n"
          "Option 6: go back")
    try:
        opcion= int(input("write a number to select an action: "))
        if opcion==1:
            distribucionTerritorial()

        elif opcion==2:
            menuPartidos()

        elif opcion==3:
            menuPapeletas()

        elif opcion==4:
            results()
        elif opcion==5:
            if len(listprovince) != 0:
             CONSULTAS()
            else:
                print("not exist datas")
                menuAdmi()
        elif opcion==6:
            menu()
        else:
            print("Invalid value")
            menuAdmi()
    except ValueError:
        print("Invalid value")
        menuAdmi()
#main menu of aministrator
listprovince=[]#list, where are the provinces, the cantons, the districts.
#It is also the place where the legislative vote of each province is kept and where the votes are created.
def distribucionTerritorial():
    print("___Territorial distribution menu___")
    print("what do you want to do?\n"
          "opcion 1: Add province\n"
          "opcion 2: Add canton\n"
          "opcion 3: Add district\n"
          "opcion 4: Modify provinde\n"
          "opcion 5: Modify canton\n"
          "opcion 6: Modify district\n"
          "opcion 7: Remove province\n"
          "opcion 8: Remove canton\n"
          "opcion 9: Remove district\n"
          "opcion 10: back to the principal menu")
    try:
        opcion=int(input("to choose an opcion: "))
        if opcion==1:
            agregarprovincia()
        elif opcion==2:
            agregarcanton()
        elif opcion==3:
            agregardistrito()
        elif opcion==4:
            modifyprovince()
        elif opcion==5:
            modifycanton()
        elif opcion==6:
            modifydistric()
        elif opcion==7:
            quitarprovincia()
        elif opcion==8:
            quitarcanton()
        elif opcion==9:
            quitardistrito()
        elif opcion==10:
            menuAdmi()
        else:
            print("Invalid value")
            distribucionTerritorial()
    except ValueError:
        print("Invalid value")
        distribucionTerritorial()
#Territorial distribution" is where the provinces, cantons and districts create.
#Our code has a wide variety of conditions so that there are no equal districts in the same canton,
#so that there are no equal cantons in the same province
#and so that there are no equal provinces in the country.
#One of these conditions were the boolean.
#They were used to activate or shut down,add or removed, if any condition found some data or not.
def agregarprovincia():
    print("__Add province___")
    province=str(input("write the province to add: ")).upper()
    diputies=int(input("write the number of the diputies of the province: "))
    exist = False
    i = 0
    while i < len(listprovince):
        if province == listprovince[i]["provincia"]:
            exist= True
            break
        i+=1
    if  not exist:
        y={"provincia":province,"cantones":[],"ballots":[],"diputies":diputies}
        listprovince.append(y)
        print(province+" province added")
        print(listprovince)
        distribucionTerritorial()
    else:
        print("The province: " + province + " already exists")
        agregarprovincia()
#this function is responsible for adding a new province and
#validates that the name of the new province is different from those that already exist.
def agregarcanton():
    print("___Add canton___")
    canton = str(input("write the canton to add: ")).upper()
    prov= str(input("In which province belong the canton: ")).upper()
    detectprov(prov)
    if len(listprovince)!=0:
        exist = False
        i = 0
        while i < len(listprovince):
            j=0
            if prov==listprovince[i]["provincia"]:
                while j<len(listprovince[i]["cantones"]):
                    if len(listprovince[i]["cantones"])!=0:
                        if canton==listprovince[i]["cantones"][j]["canton"]:
                            exist = True
                            break
                    j+=1
            i += 1
        if exist == True:
            print("canton already exist")
            agregarcanton()
        elif not exist:
            x = {"canton": canton,"distritos": []}
            i = 0
            while i < len(listprovince):
                if prov == listprovince[i]["provincia"]:
                    listprovince[i]["cantones"].append(x)
                    print("___canton added___")
                    print(listprovince)
                    distribucionTerritorial()
                    break
                i += 1
    else:
        print("list empty,append provincia")
        agregarprovincia()
#this function is responsible for adding a new canton and
#validates that the name of the new canton is different from those that already exist.
def agregardistrito():
    print("___Add district___")
    if len(listprovince)!=0:
        distrito= str(input("write the district you are going to add: ")).upper()
        canton = str(input("write the canton where the district will be added: ")).upper()
        lis=detectcanton(canton)
        prov=lis[0]
        x={"distrito":distrito,"PresidentialVotes":[],"LegislativeVotes":[]}
        if len(listprovince)!= 0:
            exist=False
            e=0
            while e < len(listprovince):
                if prov==listprovince[e]["provincia"]:
                    q=0
                    while q <len(listprovince[e]["cantones"]):
                        if canton==listprovince[e]["cantones"][q]["canton"]:
                            y=0
                            while y <len(listprovince[e]["cantones"][q]["distritos"]):
                                if len(listprovince[e]["cantones"][q]["distritos"])!=0:
                                    if distrito==listprovince[e]["cantones"][q]["distritos"][y]["distrito"]:
                                        exist = True
                                        break
                                y+=1
                        q+=1
                e+= 1
            if exist==True:
                print("district already exist in canton")
                agregardistrito()
            else:
                i=0
                while i<len(listprovince):
                    if prov==listprovince[i]["provincia"]:
                        j=0
                        while j<len(listprovince[i]["cantones"]):
                            if canton == listprovince[i]["cantones"][j]["canton"]:
                                listprovince[i]["cantones"][j]["distritos"].append(x)
                                print("district added")
                                print(listprovince)
                                distribucionTerritorial()
                                break
                            j+=1
                    i+=1
    else:
        print("list cantons empty")
        distribucionTerritorial()
#this function is responsible for adding a new district and
#validates that the name of the new district is different from those that already exist
def quitarprovincia():
    print("___Remove province___")
    if listprovince != 0:
        province=str(input("what province will remove: ")).upper()
        exist = False
        i = 0
        while i < len(listprovince):
            if province == listprovince[i]["provincia"]:
                exist = True
                break
            i += 1
        if not exist:
            print("the",province,"doesn't exist or it ws deleted")
            distribucionTerritorial()
        else:
            i=0
            while i< len(listprovince):
                if province == listprovince[i]["provincia"]:
                    del listprovince[i]
                    print(listprovince)
                    distribucionTerritorial()
                    break

                i+=1
    else:
        print("list empty")
        distribucionTerritorial()
#Verify if the province already exists.
#If the province exists, it eliminates it
def quitarcanton():
    print("___Remove canton___")
    canton=str(input("what canton will remove?: ")).upper()
    prov=str(input("what province will remove: ")).upper()
    detectprov(prov)
    if len(listprovince)!=0:
        exist = False
        i = 0
        while i < len(listprovince):
            j=0
            if prov==listprovince[i]["provincia"]:
                while j<len(listprovince[i]["cantones"]):
                    if len(listprovince[i]["cantones"])!=0:
                        if canton==listprovince[i]["cantones"][j]["canton"]:
                            exist = True
                            break
                    j+=1
            i += 1
        if not exist:
            print("this", canton,"doesn't or it was deleted")
            distribucionTerritorial()
        else:
            i=0
            while i<len(listprovince):
                if prov == listprovince[i]["provincia"]:
                    j=0
                    while j<len(listprovince):
                        if canton==listprovince[i]["cantones"][j]["canton"]:
                            del listprovince[i]["cantones"][j]
                            distribucionTerritorial()
                            break
                    j+=1
                i+=1
#Verify if the canton already exists.
#If the canton exists, it eliminates it
def quitardistrito():
    print("___Remove district___")
    distrit=str(input("what district remove?: ")).upper()
    canton = str(input("which canton belong the district: ")).upper()
    lis = detectcanton(canton)
    prov = lis[0]
    canton = lis[1]
    exist = False
    if len(listprovince) != 0:
        e = 0
        while e < len(listprovince):
            if prov == listprovince[e]["provincia"]:
                q = 0
                while q < len(listprovince[e]["cantones"]):
                    if canton == listprovince[e]["cantones"][q]["canton"]:
                        y = 0
                        while y < len(listprovince[e]["cantones"][q]["distritos"]):
                            if len(listprovince[e]["cantones"][q]["distritos"]) != 0:
                                if distrit == listprovince[e]["cantones"][q]["distritos"][y]["distrito"]:
                                    exist=True
                                    break
                            y += 1
                    q += 1
            e += 1
        if not exist:
            print("the district doesn't exist or it was delete before")
            distribucionTerritorial()
        else:
            i=0
            while i<len(listprovince):
                if prov==listprovince[i]["provincia"]:
                    j=0
                    while j<len(listprovince):
                        if canton==listprovince[i]["cantones"][j]["canton"]:
                            e=0
                            while e<len(listprovince):
                                if distrit==listprovince[i]["cantones"][j]["distritos"][e]["distrito"]:
                                    del listprovince[i]["cantones"][j]["distritos"][e]
                                    print(listprovince)
                                    distribucionTerritorial()
                                    break
                                e+=1
                        j+=1
                i+=1
    else:
        print("list empty")
        distribucionTerritorial()
#Verify if the district already exists.
#If the district exists, it eliminates it
def detectprov(prov):
    if len(listprovince)!=0:
        exist=False
        i = 0
        while i < len(listprovince):
            if prov == listprovince[i]["provincia"]:
                exist=True
                break
            i += 1
        if exist==True:
            province=listprovince[i]["provincia"]
            return province
        else:
            print("the province doesn't exist, try again")
            distribucionTerritorial()
    else:
        print("list empty")
        distribucionTerritorial()
#this function verifies if the province exists
#to use the data in another method
def modifyprovince():
    if len(listprovince)!=0:
        province=str(input("which province you will modify?: ")).upper()
        exist = False
        i = 0
        while i < len(listprovince):
            if province == listprovince[i]["provincia"]:
                exist = True
                break
            i += 1
        if not exist:
            print("the", province, "doesn't exist or it ws deleted")
            distribucionTerritorial()
        else:
            i = 0
            while i < len(listprovince):
                if province == listprovince[i]["provincia"]:
                    newprovince=str(input("which will be the new name for the province?: ")).upper()
                    listprovince[i]["provincia"]=newprovince
                    distribucionTerritorial()
                    break
                i+=1
    else:
        print("list empty")
        distribucionTerritorial()
#This function replaces an existing province with a new one.
def modifycanton():
    if len(listprovince)!=0:
        canton = str(input("what canton will be modify: ")).upper()
        prov = str(input("in which province belong the canton?: ")).upper()
        detectprov(prov)
        exist = False
        i = 0
        while i < len(listprovince):
            j = 0
            if prov == listprovince[i]["provincia"]:
                while j < len(listprovince[i]["cantones"]):
                    if len(listprovince[i]["cantones"]) != 0:
                        if canton == listprovince[i]["cantones"][j]["canton"]:
                            exist = True
                            break
                    j += 1
            i += 1
        if not exist:
            print("this", canton, "doesn't or it was deleted")
            distribucionTerritorial()
        else:
            i = 0
            while i < len(listprovince):
                if prov == listprovince[i]["provincia"]:
                    j = 0
                    while j < len(listprovince[i]["cantones"]):
                        if canton == listprovince[i]["cantones"][j]["canton"]:
                            newcanton=str(input("which will be the new name of the canton?: ")).upper()
                            listprovince[i]["cantones"][j]["canton"]=newcanton
                            distribucionTerritorial()
                            break
                        j+=1
                i+=1
    else:
        print("list empty")
        distribucionTerritorial()
#This function replaces an existing canton with a new one.
def modifydistric():
    distrit = str(input("which district would be modify?: ")).upper()
    canton = str(input("in which canton belong the district: ")).upper()
    lis = detectcanton(canton)
    prov = lis[0]
    exist = False
    if len(listprovince) != 0:
        e = 0
        while e < len(listprovince):
            if prov == listprovince[e]["provincia"]:
                q = 0
                while q < len(listprovince[e]["cantones"]):
                    if canton == listprovince[e]["cantones"][q]["canton"]:
                        y = 0
                        while y < len(listprovince[e]["cantones"][q]["distritos"]):
                            if len(listprovince[e]["cantones"][q]["distritos"])!= 0:
                                if distrit == listprovince[e]["cantones"][q]["distritos"][y]["distrito"]:
                                    exist = True
                                    break
                            y += 1
                    q += 1
            e += 1
        if not exist:
            print("the district doesn't exist or it was delete before")
            distribucionTerritorial()
        else:
            i = 0
            while i < len(listprovince):
                if prov == listprovince[i]["provincia"]:
                    j = 0
                    while j < len(listprovince[i]["cantones"]):
                        if canton == listprovince[i]["cantones"][j]["canton"]:
                            e = 0
                            while e < len(listprovince[i]["cantones"][e]["distritos"]):
                                if distrit == listprovince[i]["cantones"][j]["distritos"][e]["distrito"]:
                                    newdistric=str(input("which will be the new name of the distric?: ")).upper()
                                    listprovince[i]["cantones"][j]["distritos"][e]["distrito"]=newdistric
                                    distribucionTerritorial()
                                    break
                                e+=1
                        j+=1
                i+=1
    else:
        print("list empty")
        distribucionTerritorial()
#This function replaces an existing district with a new one.
def detectcanton(canton):
    prov = input("which province belong the district?: ").upper()
    if len(listprovince)!=0:
        exist = False
        i = 0
        while i < len(listprovince):
            if prov == listprovince[i]["provincia"]:
                j=0
                while j < len(listprovince[i]["cantones"]):
                    if len(listprovince[i]["cantones"]) != 0:
                        if canton == listprovince[i]["cantones"][j]["canton"]:
                            exist = True
                            canton=listprovince[i]["cantones"][j]["canton"]
                            break
                        j += 1
            i += 1

        if not exist:
            print("the canton doesn't exist, try again")
            distribucionTerritorial()
        if len(listprovince)!=0:
            exist = False
            i = 0
            while i < len(listprovince):
                if prov == listprovince[i]["provincia"]:
                    exist = True
                    break
                i += 1
            if exist == True:
                prov = listprovince[i]["provincia"]
                return [prov,canton]
            else:
                print("the province doesn't exist, try again")
                menuAdmi()
        else:
            print("list empty")
            menuAdmi()
    else:
        print("list empty")
        menuAdmi()
#this function verifies if the canton exists
#to use the data in another method
partidos=[]#list where all political parties are kept.
def menuPartidos():
    print("___Menu administration of political parties___")
    print("Option 1: Create a political party\n"
          "Option 2: Modify a political party\n"
          "Option 3: Remove a political party\n"
          "Option 4: Back to the principal menu")
    try:
        opcion= int(input("write a number to select an action: "))
        if opcion==1:
            crearParti()

        elif opcion==2:
            modificarParti()

        elif opcion==3:
            eliminarParti()

        elif opcion==4:
            menuAdmi()

        else:
            print("Invalid value")
            menuPartidos()
    except ValueError:
        print("Invalid value")
        menuPartidos()
#main menu of administration of political parties
def crearParti():
    print("___Create a political party___")
    nameP= str(input("write the name of the political party: ")).upper()
    year= input("write the founding year of the political party: ")
    colors=str(input("write the colors of the political party:")).upper()
    coideologica=str(input("write the ideological current of the political party:")).upper()
    parti = {"name": nameP, "year": year, "colors": colors, "ideology": coideologica}
    if len(partidos)!=0:
        exist=False
        i=0
        while i<len(partidos):
            if nameP== partidos[i]["name"]:
                exist=True
                print(partidos)
                print("the political party "+ nameP + " already exists")
                menuPartidos()
                break
            i+=1
        if not exist:
            partidos.append(parti)
            print("create political party")
            print(partidos)
            menuPartidos()
    else:
        partidos.append(parti)
        print("create political party")
        print(partidos)
        menuPartidos()
#the function adds a new political party to a list
#and check if the new political party already exists so that it does not add it to the list.
def modificarParti():
    print("___Modify a political party___")
    print("write the name and colors of the political party")
    nombre = str(input("write the name political party: ")).upper()
    colores = str(input("write the colors of the political party: ")).upper()
    print(partidos)
    print("write the new data of the political party")
    nuevoN=str(input("write the new name of the political party: ")).upper()
    nuevoF=input("write the new foundation year of the political party: ")
    nuevoC=str(input("write the new colors of the political party: ")).upper()
    nuevoI=str(input("write the new ideological current of the political party: ")).upper()
    if len(partidos)!=0:
        i=0
        while i < len(partidos):
            if nombre==partidos[i]["name"] and colores==partidos[i]["colors"]:

                partidos[i]["name"]=nuevoN

                partidos[i]["year"]=nuevoF

                partidos[i]["colors"]=nuevoC

                partidos[i]["ideology"]=nuevoI

                print(nombre + " political party has been modified")
                print(partidos)
                menuPartidos()
                break
            i+=1
        else:
            print("Invalid value")
            menuPartidos()
    else:
        print("empty list")
        menuPartidos()
#the function modifies an existing political party so that it is comfortable for the administrator.
def eliminarParti():
    print("___Remove political party")
    nombreEliminar=str(input("write the political party to remove: ")).upper()
    if len(partidos)!=0:
        i=0
        while i < len(partidos):
            if nombreEliminar== partidos[i]["name"]:
                partidos.pop(i)
                print(partidos)
                print(nombreEliminar + " political party remove")
                menuPartidos()
                break
            i+=1
        else:
            print("Invalid value")
            menuPartidos()
    else:
        print("empty list")
        menuPartidos()
#the function eliminates an existing political party from the list where all the political parties are kept
PP=[]# list of political parties of the presidential vote(it is the presidential ballot)
def menuPapeletas():
    print("___Administration of ballots___")
    print("Option 1: Create a ballot\n"
          "Option 2: Modify a ballot\n"
          "Option 3: Remove a ballot\n"
          "Option 4: Back to the principal menu")
    try:
        opcion= int(input("write a number to select an action: "))
        if opcion==1:
            crearPapeletas()
        elif opcion==2:
            modificarPapeletas()
        elif opcion==3:
            eliminarPapeletas()
        elif opcion==4:
            menuAdmi()
        else:
            print("Invalid value")
            menuPapeletas()
    except ValueError:
        print("Invalid value")
        menuPapeletas()
#main menu of the administration of ballot
def crearPapeletas():
    print("___Create ballot___")
    print("Option 1: Presidential ballot\n"
          "Option 2: legislative ballot\n"
          "Option 3: Go back")
    try:
        opcion=int(input("write a number to select an action: "))
        if opcion==1:
            presidencial()
        elif opcion==2:
            legislativa()
        elif opcion==3:
            menuPapeletas()
        else:
            print("Invalid value")
            crearPapeletas()
    except ValueError:
        print("Invalid value")
        crearPapeletas()
#menu of create ballots
def presidencial():
    print("___Create presidential ballot___")
    nombrePartido= str(input("write the name of the political party: ")).upper()
    if len(PP)==0:
        if len(partidos)!=0:
            exist= False
            i=0
            while i < len(partidos):
                if nombrePartido == partidos[i]["name"]:
                    exist=True
                    break
                i+=1
            if exist==True:
                x={"party":nombrePartido}
                i=0
                while i < len(partidos):
                    if nombrePartido== partidos[i]["name"]:
                        PP.append(x)
                        print(PP)
                        print(nombrePartido + " political party added and presidential ballot created")
                        menuPapeletas()
                        break
                    i+=1
                else:
                    print(nombrePartido + " political party not exist,try again")
                    crearPapeletas()
            else:
                print("Not exists politicals party")
    else:
        print("ballot already is created, try in modify ballot")
        menuPapeletas()
# the function is responsible for creating the presidential ballot.
# Create the presidential ballot and add a political party on the ballot.
# Once the ballot is created, you can not create two presidential ballots.
def legislativa():
    print("___Create legislative ballot___")
    prov=str(input("write the assigned province of the legislative ballot: ")).upper()
    if len(listprovince)!=0:
        exist=False
        i = 0
        while i < len(listprovince):
            if prov == listprovince[i]["provincia"]:
                if len(listprovince[i]["ballots"])==0:
                    exist=True
                    x = {"Papeleta Legislativa": []}
                    listprovince[i]["ballots"].append(x)
                    print("created legislative ballot")
                    print(listprovince)
                    crearPapeletas()
                    break
            i+=1
        if not exist:
            print("Invalid value")
            print(listprovince)
            crearPapeletas()
        else:
            print("Invalid value")
            crearPapeletas()
    else:
        print(listprovince)
        print("empty list")
        menuPapeletas()
# the function is responsible for creating the legislative ballot by province.
# Create the legislative ballot and add it to a key with the name "ballots" in the list of territorial distribution.
# Once the ballot is created, you can not create two legislative ballots in the same province.
def modificarPapeletas():
    print("___Modify a ballot___")
    print("Option 1: presidental ballot\n"
          "Option 2: legislative ballot\n"
          "Option 3: Go back")
    try:
        opcion= int(input("write a number to select an action: "))
        if opcion==1:
            modificarPapeletaPP()
        elif opcion == 2:
            modificarPapeletaPL()
        elif opcion == 3:
            menuPapeletas()
        else:
            print("Invalid value")
            modificarPapeletas()
    except ValueError:
        print("Invalid value")
        modificarPapeletas()
#menu of modify ballots
def modificarPapeletaPP():
    print("___Modify a presidental ballot___\n"
          "Option 1: Add political party\n"
          "Option 2: Remove political party\n"
          "Option 3: go back")
    try:
        opcion= int(input("write a number to select an action: "))
        if opcion==1:
            agregarPartidoPapeletaP()
        elif opcion==2:
            eliminarPartidoPapeletaPP()
        elif opcion==3:
            modificarPapeletas()
        else:
            print("Invalid value")
            modificarPapeletaPP()
    except ValueError:
        print("Invalid value")
        modificarPapeletaPP()
##menu of modify presidential ballot
def agregarPartidoPapeletaP():
    print("___Add political party___")
    partido= str(input("write the name of the political party: ")).upper()
    if len(partidos)!=0:
        exist=False
        i=0
        while i < len(partidos):
            if partido== partidos[i]["name"]:
                if len(PP)!=0:
                    j=0
                    while j < len(PP):
                        if partido== PP[j]["party"]:
                            exist=True
                            print(partido + " political party already exist in presidential ballot")
                            modificarPapeletaPP()
                            break
                        j+=1
            i+=1

        if not exist:
            x = {"party": partido}
            i = 0
            if len(PP)!=0:
                while i < len(partidos):
                    if partido == partidos[i]["name"]:
                        PP.append(x)
                        print(PP)
                        print(partido + " added political party")
                        modificarPapeletaPP()
                        break
                    i += 1
                else:
                    print("political party not exist")
                    modificarPapeletaPP()
    else:
        print("empty ballot")
        modificarPapeletaPP()
# Its main function is to add political parties to the presidential vote.
# also identifies if the political party already exists on the ballot.
def eliminarPartidoPapeletaPP():
    print("___Remove political party___")
    partido = str(input("write the name of the political party: ")).upper()
    if len(PP) != 0:
        i=0
        while i< len(PP):
            if partido == PP[i]["party"]:
                PP.pop(i)
                print(PP)
                print(partido + " political party remove")
                modificarPapeletaPP()
                break
            i += 1
        else:
            print("political party not exist")
            modificarPapeletaPP()
    else:
        print("empty ballot")
        modificarPapeletaPP()
# Its main function is to remove political parties to the presidential ballot.
# also identifies if the political party already exists on the ballot.
def modificarPapeletaPL():
    print("___Modify legislative ballot___\n"
          "Option 1: Add political party\n"
          "Option 2: Remove political party\n"
          "Option 3: Go back")
    try:
        opcion= int(input("write a number to select an action: "))
        if opcion==1:
            agregarPartidoPapeletaPL()
        elif opcion==2:
            eliminarpartidoPL()
        elif opcion==3:
            modificarPapeletas()
        else:
            print("Invalid value")
            modificarPapeletaPL()
    except ValueError:
        print("Invalid value")
        modificarPapeletaPL()
#menu of modify legislative ballots
def agregarPartidoPapeletaPL():
    print("___Append political party in legislative ballot___ ")
    partido=str(input("write the name of the political party: ")).upper()
    provincia=str(input("write the name of the province where the political party that be appended: ")).upper()
    if len(listprovince)!=0:
        exist=False
        i = 0
        z = {"party": partido}
        while i < len(listprovince):
            if provincia == listprovince[i]["provincia"]:
                if len(listprovince[i]["ballots"]) != 0:
                    j=0
                    while j< len(partidos):
                        if partido == partidos[j]["name"]:
                            y=0
                            while y < len(listprovince[i]["ballots"][0]["Papeleta Legislativa"]):
                                if partido== listprovince[i]["ballots"][0]["Papeleta Legislativa"][y]["party"]:
                                    exist=True
                                    print(listprovince)
                                    print(partido + " political party already exist in legislative ballot")
                                    modificarPapeletaPL()
                                    break
                                y+=1
                        j+=1
            i+=1
        if not exist:
            i=0
            while i < len(listprovince):
                if provincia==listprovince[i]["provincia"]:
                    if len(listprovince[i]["ballots"]) != 0:
                        listprovince[i]["ballots"][0]["Papeleta Legislativa"].append(z)
                        print(listprovince)
                        print(partido + " political party added in legislative ballot")
                        modificarPapeletaPL()
                        break
                i+=1
            else:
                print("Invalid value")
                modificarPapeletaPL()
    else:
        print(listprovince)
        print("empty list")
        menuPapeletas()
# Its main function is to add political parties to the legislative ballot.
# also identifies if the political party already exists on the ballot.
def eliminarpartidoPL():
    print("___Remove political party___")
    partido = str(input("write the name of the political party: ")).upper()
    provincia = str(input("write the name of the province where the political party that be removed: ")).upper()
    if len(listprovince)!=0:
        i=0
        while i< len(listprovince):
            if provincia==listprovince[i]["provincia"]:
                if len(listprovince[i]["ballots"]) != 0:
                    j=0
                    while j<len(listprovince):
                        if partido==listprovince[i]["ballots"][0]["Papeleta Legislativa"][j]["party"]:
                            del(listprovince[i]["ballots"][0]["Papeleta Legislativa"][j])
                            print(listprovince)
                            print(partido + " political party removed")
                            modificarPapeletaPL()
                            break
                        j+=1
            i+=1
        else:
            print("Invalid value")
            modificarPapeletaPL()
    else:
        print(listprovince)
        print("empty list")
        menuPapeletas()
# Its main function is to eliminate political parties in the legislative vote.
# also identifies if the political party already exists on the ballot and the ballot is empty
def eliminarPapeletas():
    print("___Remove a ballon___\n"
          "Option 1) Remove a ballot presidental\n"
          "Option 2) Remove a ballot legislative\n"
          "Opcion 3) go back")
    try:
        opcion= int(input("write a number to select an action: "))
        if opcion==1:
            eliminarPapeletaPP()
        if opcion==2:
            eliminarPapeletaPL()
        if opcion==3:
            menuPapeletas()
        else:
            print("Invalid value")
            eliminarPapeletas()
    except ValueError:
        print("Invalid value")
        eliminarPapeletas()
#menu of remove ballots
def eliminarPapeletaPP():
    print("___Remove ballot presidental___\n"
          "Option 1) Remove ballot\n"
          "Option 2) Go back")
    try:
        opcion=int(input("write a number to select an action: "))
        if opcion==1:
            if len(PP)!=0:
                    PP.clear()
                    print(PP)
                    print("removed presidental ballot")
                    eliminarPapeletaPP()
            else:
                print("Ballot empty")
                eliminarPartidoPapeletaPP()
        if opcion==2:
            eliminarPapeletas()
        else:
            print("Invalid value")
            eliminarPapeletaPP()
    except ValueError:
        print("Invalid value")
        eliminarPapeletaPP()
# Its function is to empty the presidential ballot
# is returned to the previous menu
def eliminarPapeletaPL():
    print("___Remove a ballot legislative___\n"
          "Option 1) Remove a ballot\n"
          "Option 2) Go back")
    try:
        opcion=int(input("write a number to select an action: "))
        if opcion==1:
            print("___Remove a ballot legislative___")
            provincia=str(input("write the name of the province where is the ballot: ")).upper()
            if len(listprovince)!=0:
                i=0
                while i < len(listprovince):
                    if provincia== listprovince[i]["provincia"]:
                        listprovince[i]["ballots"].clear()
                        print(listprovince)
                        print("removed ballot legislative")
                        eliminarPapeletaPL()
                        break
                    i+=1
                else:
                    print("Invalid value")
                    eliminarPapeletaPL()
            else:
                print(listprovince)
                print("empty list")
                menuPapeletas()
        if opcion==2:
            eliminarPapeletas()
        else:
            print("Invalid value")
            eliminarPapeletaPL()
    except ValueError:
        print("Invalid value")
        eliminarPapeletaPL()
# its function is to eliminate the legislative ballot of a province
# identify if the written province exists
# is returned to the previous menu
def results():
    print("___Result status___\n"
          "Option 1) Create legislative results\n"
          "Option 2) Create presidential results\n"
          "Option 3) Modify legislative results\n"
          "Option 4) Modify presidential results\n"
          "Option 5) Go back")
    try:
        option=int(input("write a number to select an action: "))

        if option==1:
            createLegislativeResults()
        elif option==2:
            createPresidentiaVotes()
        elif option==3:
            ModifyLegislativeResults()
        elif option==4:
            ModifyPresidentialResults()
        elif option==5:
            menuAdmi()
        else:
            print("Invalid value")
            results()
    except ValueError:
        print("Invalid value")
        results()
#results menu
def createLegislativeResults():
    print("___Create legislative results___")
    district=str(input("write the district where belong the political party result: ")).upper()
    canton = str(input("write the canton where the district located: ")).upper()
    lis = detectcanton(canton)
    prov = lis[0]
    exist2 = False
    exist = False
    band2 = False
    if len(listprovince) != 0:
        e = 0
        while e < len(listprovince):
            if prov == listprovince[e]["provincia"]:
                q = 0
                while q < len(listprovince[e]["cantones"]):
                    if canton == listprovince[e]["cantones"][q]["canton"]:
                        y = 0
                        while y < len(listprovince[e]["cantones"][q]["distritos"]):
                            if district == listprovince[e]["cantones"][q]["distritos"][y]["distrito"]:
                                exist=True
                                break
                            y+=1
                    q+=1
            e+=1
        if exist==True:
            band=False
            partido=str(input("write el political party: ")).upper()
            votos=str(input("write the number of votes: "))
            x = {"party": partido, "votes": votos}
            if votos.isalpha():
                band=True
            if band==True:
                print("Invalid value, try again")
                createLegislativeResults()
            else:
                i=0
                while i < len(listprovince):
                    if prov== listprovince[i]["provincia"]:
                        j=0
                        while j < len(listprovince[i]["ballots"][0]["Papeleta Legislativa"]):
                            if partido==listprovince[i]["ballots"][0]["Papeleta Legislativa"][j]["party"]:
                                exist2=True
                                break
                            j+=1
                    i+=1
                if exist2==True:
                    e = 0
                    while e < len(listprovince):
                        if prov == listprovince[e]["provincia"]:
                            q = 0
                            while q < len(listprovince[e]["cantones"]):
                                if canton == listprovince[e]["cantones"][q]["canton"]:
                                    y = 0
                                    while y < len(listprovince[e]["cantones"][q]["distritos"]):
                                        if district == listprovince[e]["cantones"][q]["distritos"][y]["distrito"]:
                                            k=0
                                            while k< len(listprovince[e]["cantones"][q]["distritos"][y]["LegislativeVotes"]):
                                                if partido==listprovince[e]["cantones"][q]["distritos"][y]["LegislativeVotes"][k]["party"]:
                                                    band2=True
                                                    break
                                                k+=1
                                        y += 1
                                q += 1
                        e += 1
                    if not band2:
                        e = 0
                        while e < len(listprovince):
                            if prov == listprovince[e]["provincia"]:
                                q = 0
                                while q < len(listprovince[e]["cantones"]):
                                    if canton == listprovince[e]["cantones"][q]["canton"]:
                                        y = 0
                                        while y < len(listprovince[e]["cantones"][q]["distritos"]):
                                            if district == listprovince[e]["cantones"][q]["distritos"][y]["distrito"]:
                                                listprovince[e]["cantones"][q]["distritos"][y]["LegislativeVotes"].append(x)
                                                print("results added")
                                                print(listprovince)
                                                results()
                                                break
                                            y += 1
                                    q += 1
                            e += 1
                    else:
                        print("the political party already has results, try again")
                        results()
                else:
                    print("Invalid value, the political party not exist in ballot")
                    results()
        else:
            print("province or canton or distrit not exist")
            results()
    else:
        print("empty list")
        results()
#This function assigns a number of votes to a political party in the legislative vote.
#The political party has to exist on the legislative ballot of each province, if the party does not exist.
#The function is responsible for notifying the administrator that the party does not exist on the ballot.
def ModifyLegislativeResults():
    print("___Modify legislative results__")
    district = str(input("write the distrit: ")).upper()
    canton = str(input("write the canton where the distrit located: ")).upper()
    lis = detectcanton(canton)
    prov = lis[0]
    exist = False
    band2 = False
    if len(listprovince) != 0:
        e = 0
        while e < len(listprovince):
            if prov == listprovince[e]["provincia"]:
                q = 0
                while q < len(listprovince[e]["cantones"]):
                    if canton == listprovince[e]["cantones"][q]["canton"]:
                        y = 0
                        while y < len(listprovince[e]["cantones"][q]["distritos"]):
                            if district == listprovince[e]["cantones"][q]["distritos"][y]["distrito"]:
                                exist = True
                                break
                            y += 1
                    q += 1
            e += 1
        if exist==True:
            band = False
            partido = str(input("write the name of the political party that you want modify the results: ")).upper()
            newvotos = str(input("write the new number of votes: "))
            p = {"party": partido, "votes": newvotos}
            if newvotos.isalpha():
                band = True
            if band == True:
                print("Invalid value, write numbers in votes")
                results()
            if not band:
                e = 0
                while e < len(listprovince):
                    if prov == listprovince[e]["provincia"]:
                        q = 0
                        while q < len(listprovince[e]["cantones"]):
                            if canton == listprovince[e]["cantones"][q]["canton"]:
                                y= 0
                                while y < len(listprovince[e]["cantones"][q]["distritos"]):
                                    if district == listprovince[e]["cantones"][q]["distritos"][y]["distrito"]:
                                        k=0
                                        while k < len(listprovince[e]["cantones"][q]["distritos"][y]["LegislativeVotes"]):
                                            if partido ==listprovince[e]["cantones"][q]["distritos"][y]["LegislativeVotes"][k]["party"]:
                                                band2=True
                                                break
                                            k+=1
                                    y += 1
                            q += 1
                    e += 1
                if band2==True:
                    e = 0
                    while e < len(listprovince):
                        if prov == listprovince[e]["provincia"]:
                            q = 0
                            while q < len(listprovince[e]["cantones"]):
                                if canton == listprovince[e]["cantones"][q]["canton"]:
                                    y = 0
                                    while y < len(listprovince[e]["cantones"][q]["distritos"]):
                                        if district == listprovince[e]["cantones"][q]["distritos"][y]["distrito"]:
                                            k = 0
                                            while k < len(listprovince[e]["cantones"][q]["distritos"][y]["LegislativeVotes"]):
                                                if partido == listprovince[e]["cantones"][q]["distritos"][y]["LegislativeVotes"][k]["party"]:
                                                    listprovince[e]["cantones"][q]["distritos"][y]["LegislativeVotes"][k]=p
                                                    print("the resuts was modify successfully")
                                                    print(listprovince)
                                                    results()
                                                    break
                                                k += 1
                                        y += 1
                                q += 1
                        e += 1
                else:
                    print("the results political party not exists, try again")
                    results()
            else:
                print("Invalid value")
                results()
        else:
            print("province or canton or distrit not exist")
            results()
    else:
        print("empty list")
        results()
# This function assigns a new number of votes to a political party in the legislative vote.
# The political party must exist in the legislative vote of each province and have a number of votes already established.
# If the political party does not meet the above conditions.
#The function does not modify any political party.
# If not, the function deletes the previous result with a new one that the administrator wrote.
# thus modifying the outcome of the party in the elections.
def createPresidentiaVotes():
    print("___Create presidential results___")
    district = str(input("write the district where belong the political party result: ")).upper()
    canton = str(input("write the canton where the district located: ")).upper()
    lis = detectcanton(canton)
    prov = lis[0]
    exist2 = False
    exist = False
    band2 = False
    if len(listprovince) != 0:
        e = 0
        while e < len(listprovince):
            if prov == listprovince[e]["provincia"]:
                q = 0
                while q < len(listprovince[e]["cantones"]):
                    if canton == listprovince[e]["cantones"][q]["canton"]:
                        y = 0
                        while y < len(listprovince[e]["cantones"][q]["distritos"]):
                            if district == listprovince[e]["cantones"][q]["distritos"][y]["distrito"]:
                                exist = True
                                break
                            y += 1
                    q += 1
            e += 1
        if exist == True:
            band = False
            partido = str(input("write el political party: ")).upper()
            votos = str(input("write the number of votes: "))
            x = {"party": partido, "votes": votos}
            if votos.isalpha():
                band = True
            if band == True:
                print("Invalid value, try again")
                results()
            if not band:
                j = 0
                while j < len(listprovince):
                    if partido == PP[j]["party"]:
                        exist2 = True
                        break
                    j += 1
            if exist2 == True:
                e = 0
                while e < len(listprovince):
                    if prov == listprovince[e]["provincia"]:
                        q = 0
                        while q < len(listprovince[e]["cantones"]):
                            if canton == listprovince[e]["cantones"][q]["canton"]:
                                y = 0
                                while y < len(listprovince[e]["cantones"][q]["distritos"]):
                                    if district == listprovince[e]["cantones"][q]["distritos"][y]["distrito"]:
                                        k = 0
                                        while k < len(listprovince[e]["cantones"][q]["distritos"][y]["PresidentialVotes"]):
                                            if partido == listprovince[e]["cantones"][q]["distritos"][y]["PresidentialVotes"][k]["party"]:
                                                band2 = True
                                                break
                                            k += 1
                                    y += 1
                            q += 1
                    e += 1
                if not band2:
                    e = 0
                    while e < len(listprovince):
                        if prov == listprovince[e]["provincia"]:
                            q = 0
                            while q < len(listprovince[e]["cantones"]):
                                if canton == listprovince[e]["cantones"][q]["canton"]:
                                    y = 0
                                    while y < len(listprovince[e]["cantones"][q]["distritos"]):
                                        if district == listprovince[e]["cantones"][q]["distritos"][y]["distrito"]:
                                            listprovince[e]["cantones"][q]["distritos"][y]["PresidentialVotes"].append(x)
                                            print("results added")
                                            print(listprovince)
                                            results()
                                            break
                                        y += 1
                                q += 1
                        e += 1
                else:
                    print("the political party already has results, try again")
                    results()
            else:
                print("Invalid value, the political party not exist in ballot")
                results()
        else:
            print("province or canton or distrit not exist")
            results()
    else:
        print("empty list")
        results()
#This function assigns a number of votes to a political party in the presidential vote.
# The political party must exist on the presidential ballot, if the party does not exist.
#The function is responsible for notifying the administrator that the party does not exist on the ballot.
def ModifyPresidentialResults():
    print("___Modify legislative results__")
    district = str(input("write the distrit: ")).upper()
    canton = str(input("write the canton where the distrit located: ")).upper()
    lis = detectcanton(canton)
    prov = lis[0]
    exist = False
    band2 = False
    if len(listprovince) != 0:
        e = 0
        while e < len(listprovince):
            if prov == listprovince[e]["provincia"]:
                q = 0
                while q < len(listprovince[e]["cantones"]):
                    if canton == listprovince[e]["cantones"][q]["canton"]:
                        y = 0
                        while y < len(listprovince[e]["cantones"][q]["distritos"]):
                            if district == listprovince[e]["cantones"][q]["distritos"][y]["distrito"]:
                                exist = True
                                break
                            y += 1
                    q += 1
            e += 1
        if exist == True:
            band = False
            partido = str(input("write the name of the political party that you want modify the results: ")).upper()
            newvotos = str(input("write the new number of votes: "))
            p = {"party": partido, "votes": newvotos}
            if newvotos.isalpha():
                band = True
            if band == True:
                print("Invalid value, write numbers in votes")
                results()
            if not band:
                e = 0
                while e < len(listprovince):
                    if prov == listprovince[e]["provincia"]:
                        q = 0
                        while q < len(listprovince[e]["cantones"]):
                            if canton == listprovince[e]["cantones"][q]["canton"]:
                                y = 0
                                while y < len(listprovince[e]["cantones"][q]["distritos"]):
                                    if district == listprovince[e]["cantones"][q]["distritos"][y]["distrito"]:
                                        k = 0
                                        while k < len(listprovince[e]["cantones"][q]["distritos"][y]["PresidentialVotes"]):
                                            if partido == listprovince[e]["cantones"][q]["distritos"][y]["PresidentialVotes"][k]["party"]:
                                                band2 = True
                                                break
                                            k += 1
                                    y += 1
                            q += 1
                    e += 1
                if band2 == True:
                    e = 0
                    while e < len(listprovince):
                        if prov == listprovince[e]["provincia"]:
                            q = 0
                            while q < len(listprovince[e]["cantones"]):
                                if canton == listprovince[e]["cantones"][q]["canton"]:
                                    y = 0
                                    while y < len(listprovince[e]["cantones"][q]["distritos"]):
                                        if district == listprovince[e]["cantones"][q]["distritos"][y]["distrito"]:
                                            k = 0
                                            while k < len(listprovince[e]["cantones"][q]["distritos"][y]["PresidentialVotes"]):
                                                if partido == listprovince[e]["cantones"][q]["distritos"][y]["PresidentialVotes"][k]["party"]:
                                                    listprovince[e]["cantones"][q]["distritos"][y]["PresidentialVotes"][k] = p
                                                    print("the resuts was modify successfully")
                                                    results()
                                                    break
                                                k += 1
                                        y += 1
                                q += 1
                        e += 1
                else:
                    print("the results political party not exists, try again")
                    results()
            else:
                print("Invalid value")
                results()
        else:
            print("province or canton or distrit not exist")
            results()
    else:
        print("empty list")
        results()
# This function assigns a new number of votes to a political party in the presidential vote.
# The political party must exist in the presidential vote and have a number of votes already established.
# If the political party does not meet the above conditions.
#The function does not modify any political party.
# If not, the function deletes the previous result with a new one that the administrator wrote.
# thus modifying the outcome of the party in the elections.
def CONSULTSINV():
    allPartyVotes = []
    allCantonsVotes = []
    allCantonPartyVotes = []
    allProviceVotes = []
    allDistritvotes = []
    allProvincePartyVotes = []
    def consults():
        def countvotes():
            i = 0
            while i < len(listprovince):
                prov = listprovince[i]["provincia"]
                j = 0
                while j < len(listprovince[i]["cantones"]):
                    e = 0
                    while e < len(listprovince[i]["cantones"][j]["distritos"]):
                        q = 0
                        canton = listprovince[i]["cantones"][j]["canton"]
                        while q < len(listprovince[i]["cantones"][j]["distritos"]):
                            m = 0
                            distrito = listprovince[i]["cantones"][j]["distritos"][e]["distrito"]
                            while m < len(listprovince[i]["cantones"][j]["distritos"][e]["LegislativeVotes"]):
                                party = listprovince[i]["cantones"][j]["distritos"][e]["LegislativeVotes"][m]["party"]
                                CantonVotes = 0
                                if party == listprovince[i]["cantones"][j]["distritos"][e]["LegislativeVotes"][m]["party"]:
                                    votes = int(listprovince[i]["cantones"][j]["distritos"][e]["LegislativeVotes"][m]["votes"])
                                    CantonVotes += votes
                                    q += 1
                                m += 1
                                x = {"province": prov, "canton": canton, "distrito": distrito, "party": party, "votes": CantonVotes}
                                allPartyVotes.append(x)
                        e += 1
                    j += 1
                i += 1

        def countDistritvotes():
            i = 0
            while i < len(listprovince):
                j = 0
                prov = listprovince[i]["provincia"]
                while j < len(listprovince[i]["cantones"]):
                    canton = listprovince[i]["cantones"][j]["canton"]
                    e = 0
                    CantonVotes = 0
                    while e < len(listprovince[i]["cantones"][j]["distritos"]):
                        q = 0
                        while q < len(listprovince[i]["cantones"][j]["distritos"][e]["LegislativeVotes"]):
                            votes = int(listprovince[i]["cantones"][j]["distritos"][e]["LegislativeVotes"][q]["votes"])
                            CantonVotes += votes
                            q += 1
                        e += 1
                    x = {"province": prov, "canton": canton, "totalvotes": CantonVotes}
                    allCantonsVotes.append(x)
                    j += 1
                i += 1

        def countCantonsVotes():
            i = 0
            while i < len(listprovince):
                j = 0
                prov = listprovince[i]["provincia"]
                while j < len(listprovince[i]["cantones"]):
                    u = 0
                    while u < len(listprovince[i]["ballots"][0]["Papeleta Legislativa"]):
                        y = 0
                        party = listprovince[i]["ballots"][0]["Papeleta Legislativa"][u]["party"]
                        while y < len(listprovince[i]["cantones"][j]["distritos"]):
                            canton = listprovince[i]["cantones"][j]["canton"]
                            Countvotes = 0
                            m = 0
                            while m < len(allPartyVotes):
                                if canton == allPartyVotes[m]["canton"] and party == allPartyVotes[m]["party"]:
                                    vot = int(allPartyVotes[m]["votes"])
                                    Countvotes += vot
                                m += 1

                            y += 1
                        x = {"province": prov, "canton": canton, "party": party, "votes": Countvotes}
                        allCantonPartyVotes.append(x)
                        u += 1
                    j += 1
                i += 1

        def countProvincevotes():
            i = 0
            while i < len(listprovince):
                prov = listprovince[i]["provincia"]
                j = 0
                countprovinceVotes = 0
                while j < len(allCantonsVotes):
                    if prov == allCantonsVotes[j]["province"]:
                        votos = int(allCantonsVotes[j]["totalvotes"])
                        countprovinceVotes += votos
                    j += 1
                y = {"province": prov, "TotalVotes": countprovinceVotes}
                allProviceVotes.append(y)
                i += 1

        def votesDistrit():
            i = 0
            while i < len(listprovince):
                j = 0
                prov = listprovince[i]["provincia"]
                while j < len(listprovince[i]["cantones"]):
                    y = 0
                    while y < len(listprovince[i]["cantones"][j]["distritos"]):
                        distrito =listprovince[i]["cantones"][j]["distritos"][y]["distrito"]
                        votescount = 0
                        g = 0
                        while g < len(allPartyVotes):
                            if distrito == allPartyVotes[g]["distrito"] and prov == allPartyVotes[g]["province"]:
                                vote = allPartyVotes[g]["votes"]
                                votescount += vote
                            g += 1
                        x = {"distrito": distrito, "Totalvotes": votescount}
                        allDistritvotes.append(x)
                        y += 1
                    j += 1
                i += 1

        def allvotesprovince():
            i = 0
            while i < len(listprovince):
                prov = listprovince[i]["provincia"]
                e = 0
                while e < len(listprovince[i]["ballots"][0]["Papeleta Legislativa"]):
                    count = 0
                    party = listprovince[i]["ballots"][0]["Papeleta Legislativa"][e]["party"]
                    y = 0
                    while y < len(allCantonPartyVotes):
                        if party == allCantonPartyVotes[y]["party"] and prov == allCantonPartyVotes[y]["province"]:
                            vote = allCantonPartyVotes[y]["votes"]
                            count += vote
                        y += 1
                    e += 1
                    x = {"province": prov, "party": party, "totalvotes": count}
                    allProvincePartyVotes.append(x)
                i += 1

        countvotes()
        countDistritvotes()
        countCantonsVotes()
        countProvincevotes()
        votesDistrit()
        allvotesprovince()
    allPartyVotesPP = []
    allCantonsVotesPP = []
    allCantonPartyVotesPP = []
    allProviceVotesPP = []
    allDistritvotesPP = []
    allProvincePartyVotesPP = []
    def consultsPP():
        def countvotesPP():
            i = 0
            while i < len(listprovince):
                prov = listprovince[i]["provincia"]
                j = 0
                while j < len(listprovince[i]["cantones"]):
                    e = 0
                    while e < len(listprovince[i]["cantones"][j]["distritos"]):
                        q = 0
                        canton = listprovince[i]["cantones"][j]["canton"]
                        while q < len(listprovince[i]["cantones"][j]["distritos"]):
                            m = 0
                            distrito = listprovince[i]["cantones"][j]["distritos"][e]["distrito"]
                            while m < len(listprovince[i]["cantones"][j]["distritos"][e]["PresidentialVotes"]):
                                party = listprovince[i]["cantones"][j]["distritos"][e]["PresidentialVotes"][m]["party"]
                                CantonVotes = 0
                                if party == listprovince[i]["cantones"][j]["distritos"][e]["PresidentialVotes"][m]["party"]:
                                    votes = int(listprovince[i]["cantones"][j]["distritos"][e]["PresidentialVotes"][m]["votes"])
                                    CantonVotes += votes
                                    q += 1
                                m += 1
                                x = {"province": prov, "canton": canton, "distrito": distrito, "party": party, "votes": CantonVotes}
                                allPartyVotesPP.append(x)
                        e += 1
                    j += 1
                i += 1

        def countDistritvotesPP():
            i = 0
            while i < len(listprovince):
                j = 0
                prov = listprovince[i]["provincia"]
                while j < len(listprovince[i]["cantones"]):
                    canton = listprovince[i]["cantones"][j]["canton"]
                    e = 0
                    CantonVotes = 0
                    while e < len(listprovince[i]["cantones"][j]["distritos"]):
                        q = 0
                        while q < len(listprovince[i]["cantones"][j]["distritos"][e]["PresidentialVotes"]):
                            votes = int(listprovince[i]["cantones"][j]["distritos"][e]["PresidentialVotes"][q]["votes"])
                            CantonVotes += votes
                            q += 1
                        e += 1
                    x = {"province": prov, "canton": canton, "totalvotes": CantonVotes}
                    allCantonsVotesPP.append(x)
                    j += 1
                i += 1

        def countCantonsVotesPP():
            i = 0
            while i < len(listprovince):
                j = 0
                prov = listprovince[i]["provincia"]
                while j < len(listprovince[i]["cantones"]):
                    u = 0
                    while u < len(PP):
                        y = 0
                        party = PP[u]["party"]
                        while y < len(listprovince[i]["cantones"][j]["distritos"]):
                            canton = listprovince[i]["cantones"][j]["canton"]
                            Countvotes = 0
                            m = 0
                            while m < len(allPartyVotesPP):
                                if canton == allPartyVotesPP[m]["canton"] and party == allPartyVotesPP[m]["party"]:
                                    vot = int(allPartyVotesPP[m]["votes"])
                                    Countvotes += vot
                                m += 1

                            y += 1
                        x = {"province": prov, "canton": canton, "party": party, "votes": Countvotes}
                        allCantonPartyVotesPP.append(x)
                        u += 1
                    j += 1
                i += 1

        def countProvincevotesPP():
            i = 0
            while i < len(listprovince):
                prov = listprovince[i]["provincia"]
                j = 0
                countprovinceVotes = 0
                while j < len(allCantonsVotesPP):
                    if prov == allCantonsVotesPP[j]["province"]:
                        votos = int(allCantonsVotesPP[j]["totalvotes"])
                        countprovinceVotes += votos
                    j += 1
                y = {"province": prov, "TotalVotes": countprovinceVotes}
                allProviceVotesPP.append(y)
                i += 1

        def votesDistritPP():
            i = 0
            while i < len(listprovince):
                j = 0
                prov = listprovince[i]["provincia"]
                while j < len(listprovince[i]["cantones"]):
                    y = 0
                    while y < len(listprovince[i]["cantones"][j]["distritos"]):
                        distrito = listprovince[i]["cantones"][j]["distritos"][y]["distrito"]
                        votescount = 0
                        g = 0
                        while g < len(allPartyVotesPP):
                            if distrito == allPartyVotesPP[g]["distrito"] and prov == allPartyVotesPP[g]["province"]:
                                vote = allPartyVotesPP[g]["votes"]
                                votescount += vote
                            g += 1
                        x = {"distrito": distrito, "Totalvotes": votescount}
                        allDistritvotesPP.append(x)
                        y += 1
                    j += 1
                i += 1

        def allvotesprovincePP():
            i = 0
            while i < len(listprovince):
                prov = listprovince[i]["provincia"]
                e = 0
                while e < len(PP):
                    count = 0
                    party = PP[e]["party"]
                    y = 0
                    while y < len(allCantonPartyVotesPP):
                        if party == allCantonPartyVotesPP[y]["party"] and prov == allCantonPartyVotesPP[y]["province"]:
                            vote = allCantonPartyVotesPP[y]["votes"]
                            count += vote
                        y += 1
                    e += 1
                    x = {"province": prov, "party": party, "totalvotes": count}
                    allProvincePartyVotesPP.append(x)
                i += 1

        countvotesPP()
        countDistritvotesPP()
        countCantonsVotesPP()
        countProvincevotesPP()
        votesDistritPP()
        allvotesprovincePP()

    def menusCosultsAdmin():
        print("_____Consuts Menu______")
        print("option 1) National results\n"
              "option 2) Provincial results\n"
              "option 3) Cantonal results\n"
              "option 4) Distrital results\n"
              "option 5) Conformation of the legislative assembly\n"
              "option 6) Back to principal menu")
        try:
            opcion = int(input("write number chose: "))
            if opcion == 1:
                nationalResults()
            elif opcion == 2:
                provincialResults()
            elif opcion == 3:
                cantonalResults()
            elif opcion == 4:
                distritalResults()
            elif opcion == 5:
                LegislativeAssembly(allProvincePartyVotes)
            elif opcion == 6:
                menu()
            else:
                print("invalid value")
                menusCosultsAdmin()
        except ValueError:
            print("Invalid value")
            menusCosultsAdmin()
    # this is a menu of the consults
    def nationalResults():
        i = 0
        Resultsnational = []
        VotesNacional = 0
        while i < len(allProviceVotesPP):
            voto = allProviceVotesPP[i]["TotalVotes"]
            VotesNacional += voto
            i += 1
        e = 0
        while e < len(PP):
            party = PP[e]["party"]
            votes = 0
            y = 0
            while y < len(allProvincePartyVotesPP):
                if party == allProvincePartyVotesPP[y]["party"]:
                    vote = allProvincePartyVotesPP[y]["totalvotes"]
                    votes += vote
                y += 1
            x = {"party": party, "nationalvotes": votes}
            Resultsnational.append(x)
            e += 1
        j = 0
        print("----National Results----")
        print("Total Votes", "=", VotesNacional)
        while j < len(Resultsnational):
            party = Resultsnational[j]["party"]
            votes1 = Resultsnational[j]["nationalvotes"]
            porcentvotes = (votes1 * 100) // VotesNacional

            print(party, "=", porcentvotes, "%", " ", "All Votes=", votes1)

            j += 1
        menusCosultsAdmin()
    # this function will going to count any vote form any province to show the all votes
    # and show the percentage of all political party
    def provincialResults():
        i = 0
        print("----Province Results----")
        while i < len(allProviceVotesPP):
            prov = allProviceVotesPP[i]["province"]
            votoprovincial = allProviceVotesPP[i]["TotalVotes"]
            j = 0
            print("Province", "=", prov, "Totalvotes", "=", votoprovincial)
            while j < len(allProvincePartyVotesPP):

                partido = allProvincePartyVotesPP[j]["party"]
                if prov == allProvincePartyVotesPP[j]["province"]:
                    voto = allProvincePartyVotesPP[j]["totalvotes"]
                    porcentaje = (voto * 100) // votoprovincial
                    print(partido, "=", porcentaje, "%", "=", "total votes", "=", voto)
                j += 1
            i += 1
        menusCosultsAdmin()
    # this will take any count of votes from provinces ant show a percentage one by one
    def cantonalResults():
        print("----Canton Results----")
        i = 0
        while i < len(allCantonsVotesPP):
            prov = allCantonsVotesPP[i]["province"]
            canton = allCantonsVotesPP[i]["canton"]
            votosTotales = allCantonsVotesPP[i]["totalvotes"]
            print("province = ", prov, "canton = ", canton, "totavotes = ", votosTotales)
            j = 0
            while j < len(allCantonPartyVotesPP):
                if prov == allCantonPartyVotesPP[j]["province"] and canton == allCantonPartyVotesPP[j]["canton"]:
                    partido = allCantonPartyVotesPP[j]["party"]
                    votos = allCantonPartyVotesPP[j]["votes"]
                    porcentaje = (votos * 100) // votosTotales
                    print(partido, "=", porcentaje, "%", "=", "votes= ", votos)
                j += 1
            i += 1
        menusCosultsAdmin()
    # this show results of elections of any cantonal results and percentage
    def distritalResults():
        print("----District Results----")
        i = 0
        while i < len(listprovince):
            prov = listprovince[i]["provincia"]
            e = 0
            while e < len(listprovince[i]["cantones"]):
                canton = listprovince[i]["cantones"][e]["canton"]
                w = 0
                while w < len(listprovince[i]["cantones"][e]["distritos"]):
                    district = listprovince[i]["cantones"][e]["distritos"][w]["distrito"]
                    h = 0
                    while h < len(allDistritvotesPP):
                        if district == allDistritvotesPP[h]["distrito"]:
                            totalVotes = allDistritvotesPP[h]["Totalvotes"]
                            y = 0
                            while y < len(allPartyVotesPP):
                                if district == allPartyVotesPP[y]["distrito"]:
                                    votos = allPartyVotesPP[y]["votes"]
                                    party = allPartyVotesPP[y]["party"]
                                    porcentaje = (votos * 100) // totalVotes
                                    print("province: ", prov, " canton: ", canton, " district: ", district, " totalvotes: ", totalVotes, " party: ", party, " porcent: ", porcentaje)
                                y += 1
                        h += 1
                    w += 1
                e += 1

            i += 1
        menusCosultsAdmin()
    # this show any district result and show the percentage of all
    def LegislativeAssembly(list):
        x = list[:]
        y = []
        h = 0
        while h < len(listprovince):
            prov = listprovince[h]["provincia"]
            w = {"province": prov, "party": []}
            y.append(w)
            w = 0
            while w < len(allProvincePartyVotes):
                i = 0
                while i < len(x):
                    if prov == x[i]["province"]:
                        party = ""
                        votes = 0
                        e = 0
                        while i < len(x):
                            if votes < x[i]["totalvotes"]:
                                votes = x[i]["totalvotes"]
                                party = x[i]["party"]
                                e = i
                            i += 1
                        mayor = {"party": party, "totalvotes": votes}
                        y[h]["party"].append(mayor)
                        x.pop(e)
                    i += 1
                w += 1
            h += 1
        quotient(y)
    # this show the number  of deputies from provinces an take how many deputies are from political party
    def quotient(list):
        i = 0
        newlist = []
        while i < len(listprovince):
            spaces = int(listprovince[i]["diputies"])
            prov = listprovince[i]["provincia"]
            e = 0
            while e < len(allProviceVotes):
                if prov == allProviceVotes[e]["province"]:
                    totalvotes = int(allProviceVotes[e]["TotalVotes"])
                    quotient = totalvotes / spaces
                    listdeputies = []
                    if prov == list[e]["province"]:
                        j = 0
                        while j < len(list[e]["party"]):
                            if spaces > 0:
                                party = list[e]["party"][j]["party"]
                                vote = list[e]["party"][j]["totalvotes"]
                                space = 0
                                while vote > quotient:
                                    vote = vote - quotient
                                    if vote > 0:
                                        space += 1
                                    spaces -= 1
                                y = {"party": party, "deputies": space}
                                listdeputies.append(y)
                                j += 1
                        if spaces > 0:
                            if j >= len(list[e]["party"]):
                                j = 0
                            while spaces > 0:
                                quotient = quotient / 2
                                party = list[e]["party"][j]["party"]
                                vote = list[e]["party"][j]["totalvotes"]

                                while spaces > 0:
                                    space = 0
                                    while vote > quotient and spaces > 0:
                                        vote = vote - quotient
                                        space += 1
                                        spaces -= 1
                                y = {"party": party, "deputies": space}
                                listdeputies.append(y)
                                j += 1
                            if spaces > 0:
                                while spaces > 0:
                                    party = list[e]["party"][j]["party"]
                                    space = 1
                                    y = {"party": party, "deputies": space}
                                    listdeputies.append(y)
                                    spaces -= 1
                                    j += 1
                        x = {"province": prov, "desputies": listdeputies}
                        newlist.append(x)
                e += 1
            i += 1
        j = 0
        print("_____Deputies_____")
        while j < len(newlist):
            t = 0
            print("---", newlist[j]["province"], "---")
            while t < len(newlist[j]["desputies"]):
                print(newlist[j]["desputies"][t]["party"], "=", newlist[j]["desputies"][t]["deputies"])
                t += 1
            j += 1
        menusCosultsAdmin()
    consults()
    consultsPP()
    menusCosultsAdmin()

def CONSULTAS():
    allPartyVotes=[]
    allCantonsVotes=[]
    allCantonPartyVotes=[]
    allProviceVotes=[]
    allDistritvotes=[]
    allProvincePartyVotes=[]
    def consults():
        def countvotes():
            i = 0
            while i < len(listprovince):
                prov = listprovince[i]["provincia"]
                j = 0
                while j < len(listprovince[i]["cantones"]):
                    e = 0
                    while e < len(listprovince[i]["cantones"][j]["distritos"]):
                        q = 0
                        canton = listprovince[i]["cantones"][j]["canton"]
                        while q < len(listprovince[i]["cantones"][j]["distritos"]):
                            m = 0
                            distrito = listprovince[i]["cantones"][j]["distritos"][e]["distrito"]
                            while m < len(listprovince[i]["cantones"][j]["distritos"][e]["LegislativeVotes"]):
                                party = listprovince[i]["cantones"][j]["distritos"][e]["LegislativeVotes"][m]["party"]
                                CantonVotes = 0
                                if party == listprovince[i]["cantones"][j]["distritos"][e]["LegislativeVotes"][m]["party"]:
                                    votes = int(listprovince[i]["cantones"][j]["distritos"][e]["LegislativeVotes"][m]["votes"])
                                    CantonVotes += votes
                                    q += 1
                                m += 1
                                x = {"province": prov, "canton": canton, "distrito": distrito, "party": party, "votes": CantonVotes}
                                allPartyVotes.append(x)
                        e += 1
                    j += 1
                i += 1
        def countDistritvotes():
            i=0
            while i<len(listprovince):
                j=0
                prov=listprovince[i]["provincia"]
                while j<len(listprovince[i]["cantones"]):
                    canton=listprovince[i]["cantones"][j]["canton"]
                    e=0
                    CantonVotes = 0
                    while e<len(listprovince[i]["cantones"][j]["distritos"]):
                        q=0
                        while q<len(listprovince[i]["cantones"][j]["distritos"][e]["LegislativeVotes"]):
                            votes=int(listprovince[i]["cantones"][j]["distritos"][e]["LegislativeVotes"][q]["votes"])
                            CantonVotes+=votes
                            q+=1
                        e+=1
                    x = {"province":prov,"canton": canton, "totalvotes": CantonVotes}
                    allCantonsVotes.append(x)
                    j+=1
                i+=1
        def countCantonsVotes():
            i = 0
            while i < len(listprovince):
                j = 0
                prov = listprovince[i]["provincia"]
                while j < len(listprovince[i]["cantones"]):
                    u = 0
                    while u < len(listprovince[i]["ballots"][0]["Papeleta Legislativa"]):
                        y = 0
                        party = listprovince[i]["ballots"][0]["Papeleta Legislativa"][u]["party"]
                        while y < len(listprovince[i]["cantones"][j]["distritos"]):
                            canton = listprovince[i]["cantones"][j]["canton"]
                            Countvotes = 0
                            m = 0
                            while m < len(allPartyVotes):
                                if canton == allPartyVotes[m]["canton"] and party == allPartyVotes[m]["party"]:
                                    vot = int(allPartyVotes[m]["votes"])
                                    Countvotes += vot
                                m += 1

                            y += 1
                        x = {"province": prov, "canton": canton, "party": party, "votes": Countvotes}
                        allCantonPartyVotes.append(x)
                        u += 1
                    j += 1
                i += 1
        def countProvincevotes():
            i=0
            while i<len(listprovince):
                prov=listprovince[i]["provincia"]
                j=0
                countprovinceVotes = 0
                while j<len(allCantonsVotes):
                    if prov==allCantonsVotes[j]["province"]:
                        votos=int(allCantonsVotes[j]["totalvotes"])
                        countprovinceVotes+=votos
                    j+=1
                y={"province":prov,"TotalVotes":countprovinceVotes}
                allProviceVotes.append(y)
                i+=1
        def votesDistrit():
            i = 0
            while i < len(listprovince):
                j = 0
                prov = listprovince[i]["provincia"]
                while j < len(listprovince[i]["cantones"]):
                    y = 0
                    while y < len(listprovince[i]["cantones"][j]["distritos"]):
                        distrito = listprovince[i]["cantones"][j]["distritos"][y]["distrito"]
                        votescount = 0
                        g = 0
                        while g < len(allPartyVotes):
                            if distrito == allPartyVotes[g]["distrito"] and prov == allPartyVotes[g]["province"]:
                                vote = allPartyVotes[g]["votes"]
                                votescount += vote
                            g += 1
                        x = {"distrito": distrito, "Totalvotes": votescount}
                        allDistritvotes.append(x)
                        y += 1
                    j += 1
                i += 1
        def allvotesprovince():
            i = 0
            while i < len(listprovince):
                prov = listprovince[i]["provincia"]
                e=0
                while e<len(listprovince[i]["ballots"][0]["Papeleta Legislativa"]):
                    count = 0
                    party=listprovince[i]["ballots"][0]["Papeleta Legislativa"][e]["party"]
                    y=0
                    while y<len(allCantonPartyVotes):
                        if party==allCantonPartyVotes[y]["party"]and prov==allCantonPartyVotes[y]["province"]:
                            vote=allCantonPartyVotes[y]["votes"]
                            count+=vote
                        y+=1
                    e+=1
                    x={"province":prov,"party":party,"totalvotes":count}
                    allProvincePartyVotes.append(x)
                i+=1
        countvotes()
        countDistritvotes()
        countCantonsVotes()
        countProvincevotes()
        votesDistrit()
        allvotesprovince()
    allPartyVotesPP=[]
    allCantonsVotesPP=[]
    allCantonPartyVotesPP=[]
    allProviceVotesPP=[]
    allDistritvotesPP=[]
    allProvincePartyVotesPP=[]
    def consultsPP():
        def countvotesPP():
            i = 0
            while i < len(listprovince):
                prov = listprovince[i]["provincia"]
                j = 0
                while j < len(listprovince[i]["cantones"]):
                    e = 0
                    while e < len(listprovince[i]["cantones"][j]["distritos"]):
                        q = 0
                        canton = listprovince[i]["cantones"][j]["canton"]
                        while q < len(listprovince[i]["cantones"][j]["distritos"]):
                            m = 0
                            distrito = listprovince[i]["cantones"][j]["distritos"][e]["distrito"]
                            while m < len(listprovince[i]["cantones"][j]["distritos"][e]["PresidentialVotes"]):
                                party = listprovince[i]["cantones"][j]["distritos"][e]["PresidentialVotes"][m]["party"]
                                CantonVotes = 0
                                if party == listprovince[i]["cantones"][j]["distritos"][e]["PresidentialVotes"][m]["party"]:
                                    votes = int(listprovince[i]["cantones"][j]["distritos"][e]["PresidentialVotes"][m]["votes"])
                                    CantonVotes += votes
                                    q += 1
                                m += 1
                                x = {"province": prov, "canton": canton, "distrito": distrito, "party": party, "votes": CantonVotes}
                                allPartyVotesPP.append(x)
                        e += 1
                    j += 1
                i += 1
        def countDistritvotesPP():
            i=0
            while i<len(listprovince):
                j=0
                prov=listprovince[i]["provincia"]
                while j<len(listprovince[i]["cantones"]):
                    canton=listprovince[i]["cantones"][j]["canton"]
                    e=0
                    CantonVotes = 0
                    while e<len(listprovince[i]["cantones"][j]["distritos"]):
                        q=0
                        while q<len(listprovince[i]["cantones"][j]["distritos"][e]["PresidentialVotes"]):
                            votes=int(listprovince[i]["cantones"][j]["distritos"][e]["PresidentialVotes"][q]["votes"])
                            CantonVotes+=votes
                            q+=1
                        e+=1
                    x = {"province":prov,"canton": canton, "totalvotes": CantonVotes}
                    allCantonsVotesPP.append(x)
                    j+=1
                i+=1
        def countCantonsVotesPP():
            i = 0
            while i < len(listprovince):
                j = 0
                prov = listprovince[i]["provincia"]
                while j < len(listprovince[i]["cantones"]):
                    u = 0
                    while u < len(PP):
                        y = 0
                        party =PP[u]["party"]
                        while y < len(listprovince[i]["cantones"][j]["distritos"]):
                            canton = listprovince[i]["cantones"][j]["canton"]
                            Countvotes = 0
                            m = 0
                            while m < len(allPartyVotesPP):
                                if canton == allPartyVotesPP[m]["canton"] and party == allPartyVotesPP[m]["party"]:
                                    vot = int(allPartyVotesPP[m]["votes"])
                                    Countvotes += vot
                                m += 1

                            y += 1
                        x = {"province": prov, "canton": canton, "party": party, "votes": Countvotes}
                        allCantonPartyVotesPP.append(x)
                        u += 1
                    j += 1
                i += 1
        def countProvincevotesPP():
            i=0
            while i<len(listprovince):
                prov=listprovince[i]["provincia"]
                j=0
                countprovinceVotes = 0
                while j<len(allCantonsVotesPP):
                    if prov==allCantonsVotesPP[j]["province"]:
                        votos=int(allCantonsVotesPP[j]["totalvotes"])
                        countprovinceVotes+=votos
                    j+=1
                y={"province":prov,"TotalVotes":countprovinceVotes}
                allProviceVotesPP.append(y)
                i+=1
        def votesDistritPP():
            i = 0
            while i < len(listprovince):
                j = 0
                prov = listprovince[i]["provincia"]
                while j < len(listprovince[i]["cantones"]):
                    y = 0
                    while y < len(listprovince[i]["cantones"][j]["distritos"]):
                        distrito = listprovince[i]["cantones"][j]["distritos"][y]["distrito"]
                        votescount = 0
                        g = 0
                        while g < len(allPartyVotesPP):
                            if distrito == allPartyVotesPP[g]["distrito"] and prov == allPartyVotesPP[g]["province"]:
                                vote = allPartyVotesPP[g]["votes"]
                                votescount += vote
                            g += 1
                        x = {"distrito": distrito, "Totalvotes": votescount}
                        allDistritvotesPP.append(x)
                        y += 1
                    j += 1
                i += 1
        def allvotesprovincePP():
            i = 0
            while i < len(listprovince):
                prov = listprovince[i]["provincia"]
                e=0
                while e<len(PP):
                    count = 0
                    party=PP[e]["party"]
                    y=0
                    while y<len(allCantonPartyVotesPP):
                        if party==allCantonPartyVotesPP[y]["party"]and prov==allCantonPartyVotesPP[y]["province"]:
                            vote=allCantonPartyVotesPP[y]["votes"]
                            count+=vote
                        y+=1
                    e+=1
                    x={"province":prov,"party":party,"totalvotes":count}
                    allProvincePartyVotesPP.append(x)
                i+=1
        countvotesPP()
        countDistritvotesPP()
        countCantonsVotesPP()
        countProvincevotesPP()
        votesDistritPP()
        allvotesprovincePP()

    def menusCosultsAdmin():
        print("_____Consuts Menu______")
        print("option 1) National results\n"
              "option 2) Provincial results\n"
              "option 3) Cantonal results\n"
              "option 4) Distrital results\n"
              "option 5) Conformation of the legislative assembly\n"
              "option 6) Back to admin menu")
        try:
            opcion=int(input("write number chose: "))
            if opcion==1:
                nationalResults()
            elif opcion==2:
                provincialResults()
            elif opcion==3:
                cantonalResults()
            elif opcion==4:
                distritalResults()
            elif opcion==5:
                LegislativeAssembly(allProvincePartyVotes)
            elif opcion==6:
                menuAdmi()
            else:
                print("invalid value")
                menusCosultsAdmin()
        except ValueError:
            print("Invalid value")
            menusCosultsAdmin()
        menusCosultsAdmin()
    #this is a menu of the consults
    def nationalResults():
        i=0
        Resultsnational=[]
        VotesNacional=0
        while i <len(allProviceVotesPP):
            voto=allProviceVotesPP[i]["TotalVotes"]
            VotesNacional+=voto
            i+=1
            e=0
            while e<len(PP):
                party=PP[e]["party"]
                votes=0
                y=0
                while y<len(allProvincePartyVotesPP):
                    if party==allProvincePartyVotesPP[y]["party"]:
                        vote=allProvincePartyVotesPP[y]["totalvotes"]
                        votes+=vote
                    y+=1
                x={"party":party,"nationalvotes":votes}
                Resultsnational.append(x)
                e+=1
            j=0
        print("----National Results----")
        print("Total Votes","=",VotesNacional)
        while j<len(Resultsnational):
            party=Resultsnational[j]["party"]
            votes1=Resultsnational[j]["nationalvotes"]
            porcentvotes=(votes1*100)//VotesNacional

            print(party,"=",porcentvotes,"%"," ","All Votes=",votes1)

            j+=1
        menusCosultsAdmin()
    #this function will going to count any vote form any province to show the all votes
    #and show the percentage of all political party
    def provincialResults():
        i=0
        print("----Province Results----")
        while i<len(allProviceVotesPP):
            prov=allProviceVotesPP[i]["province"]
            votoprovincial=allProviceVotesPP[i]["TotalVotes"]
            j=0
            print("Province","=",prov,"Totalvotes","=",votoprovincial)
            while j < len(allProvincePartyVotesPP):

                partido = allProvincePartyVotesPP[j]["party"]
                if prov == allProvincePartyVotesPP[j]["province"]:
                    voto=allProvincePartyVotesPP[j]["totalvotes"]
                    porcentaje=(voto*100)//votoprovincial
                    print(partido,"=",porcentaje,"%","=","total votes","=",voto)
                j+=1
            i+=1
        menusCosultsAdmin()
    #this will take any count of votes from provinces ant show a percentage one by one
    def cantonalResults():
        print("----Canton Results----")
        i=0
        while i< len(allCantonsVotesPP):
            prov=allCantonsVotesPP[i]["province"]
            canton=allCantonsVotesPP[i]["canton"]
            votosTotales=allCantonsVotesPP[i]["totalvotes"]
            print("province = ",prov,"canton = ",canton,"totavotes = ",votosTotales)
            j=0
            while j< len(allCantonPartyVotesPP):
                if prov== allCantonPartyVotesPP[j]["province"]and canton==allCantonPartyVotesPP[j]["canton"]:
                    partido=allCantonPartyVotesPP[j]["party"]
                    votos=allCantonPartyVotesPP[j]["votes"]
                    porcentaje=(votos*100)//votosTotales
                    print(partido,"=",porcentaje,"%","=","votes= ",votos)
                j+=1
            i+=1
        menusCosultsAdmin()
    #this show results of elections of any cantonal results and percentage
    def distritalResults():
        print("----District Results----")
        i=0
        while i<len(listprovince):
            prov=listprovince[i]["provincia"]
            e=0
            while e< len(listprovince[i]["cantones"]):
                canton=listprovince[i]["cantones"][e]["canton"]
                w=0
                while w<len(listprovince[i]["cantones"][e]["distritos"]):
                    district=listprovince[i]["cantones"][e]["distritos"][w]["distrito"]
                    h=0
                    while h<len(allDistritvotesPP):
                        if district==allDistritvotesPP[h]["distrito"]:
                            totalVotes=allDistritvotesPP[h]["Totalvotes"]
                            y=0
                            while y < len(allPartyVotesPP):
                                if district== allPartyVotesPP[y]["distrito"]:
                                    votos=allPartyVotesPP[y]["votes"]
                                    party=allPartyVotesPP[y]["party"]
                                    porcentaje= (votos*100)//totalVotes
                                    print("province: ",prov," canton: ",canton," district: ",district," totalvotes: ",totalVotes," party: ",party," porcent: ",porcentaje)
                                y+=1
                        h+=1
                    w+=1
                e+=1

            i+=1
        menusCosultsAdmin()
    #this show any district result and show the percentage of all
    def LegislativeAssembly(list):
        x=list[:]
        y=[]
        h=0
        while h<len(listprovince):
            prov=listprovince[h]["provincia"]
            w = {"province": prov,"party":[]}
            y.append(w)
            w=0
            while w<len(list):
                i=0
                while i<len(list):
                    if prov == x[i]["province"]:
                        party=""
                        votes=0
                        e=0
                        while i<len(x):
                            if votes<x[i]["totalvotes"]:
                                votes=x[i]["totalvotes"]
                                party=x[i]["party"]
                                e=i
                            i+=1
                        mayor={"party":party,"totalvotes":votes}
                        y[h]["party"].append(mayor)
                        x.pop(e)
                    i+=1
                w+=1
            h+=1
        print(y)
        quotient(y)
    #this show the number  of deputies from provinces an take how many deputies are from political party
    def quotient(list):
        i = 0
        newlist = []
        while i < len(listprovince):
            spaces = int(listprovince[i]["diputies"])
            prov = listprovince[i]["provincia"]
            e = 0
            while e < len(allProviceVotes):
                if prov == allProviceVotes[e]["province"]:
                    totalvotes = int(allProviceVotes[e]["TotalVotes"])
                    quotient = totalvotes / spaces
                    listdeputies=[]
                    if prov == list[e]["province"]:
                        j = 0
                        while j<len(list[e]["party"]):
                            if spaces>0:
                                party=list[e]["party"][j]["party"]
                                vote=list[e]["party"][j]["totalvotes"]
                                space=0
                                while vote>quotient:
                                    vote=vote-quotient
                                    if vote>0:
                                       space+=1
                                    spaces-=1
                                y={"party":party,"deputies":space}
                                listdeputies.append(y)
                                j+=1
                        if spaces>0:
                            if j>=len(list[e]["party"]):
                                j=0
                            while spaces>0:
                                quotient=quotient/2
                                party = list[e]["party"][j]["party"]
                                vote = list[e]["party"][j]["totalvotes"]

                                while spaces>0:
                                    space = 0
                                    while vote>quotient and spaces>0:
                                        vote = vote - quotient
                                        space += 1
                                        spaces-=1
                                y = {"party": party, "deputies": space}
                                listdeputies.append(y)
                                j+=1
                            if spaces>0:
                                while spaces>0:
                                    party = list[e]["party"][j]["party"]
                                    space=1
                                    y = {"party": party, "deputies": space}
                                    listdeputies.append(y)
                                    spaces-=1
                                    j+=1
                        x={"province":prov,"desputies":listdeputies}
                        newlist.append(x)
                e+=1
            i+=1
        j=0
        print("_____Deputies_____")
        while j < len(newlist):
            t = 0
            print("---", newlist[j]["province"], "---")
            while t < len(newlist[j]["desputies"]):
                print(newlist[j]["desputies"][t]["party"], "=", newlist[j]["desputies"][t]["deputies"])
                t += 1
            j+=1
        menusCosultsAdmin()
    consultsPP()
    consults()
    menusCosultsAdmin()
menu()
