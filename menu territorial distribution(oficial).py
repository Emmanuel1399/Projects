listprovince=[]
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
            menuadmin()
        else:
            print("Invalid value")
            distribucionTerritorial()
    except ValueError:
        print("Invalid value")
        distribucionTerritorial()
def agregarprovincia():
    print("__Add province___")
    province=input("write the province to add: ")#escriba la provincia a aregar
    exist = False
    i = 0
    while i < len(listprovince):
        if province == listprovince[i]["provincia"]:
            exist= True
            break
        i+=1
    if  not exist:
        y={"provincia":province,"cantones":[],"ballots":[]}
        listprovince.append(y)
        print("agregado correctamente")
        print(listprovince)
        distribucionTerritorial()
    else:
        print("The province: " + provincia + " already exists")
        agregarprovincia()
def agregarcanton():
    print("___Add canton___")
    canton = input("write the canton to add: ")# escriba el canton a agregar
    prov= input("In which province belong the canton: ")
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
                    j+=1
            i += 1
        if exist == True:
            print("canton already exist")#canton ya existe
            agregarcanton()
        elif not exist:
            x = {"canton": canton,"distritos": []}
            i = 0
            while i < len(listprovince):
                if prov == listprovince[i]["provincia"]:
                    listprovince[i]["cantones"].append(x)
                    print("___canton added___")#canton agregado
                    print(listprovince)
                    distribucionTerritorial()
                    break
                i += 1
    else:
        print("list empty,append provincia")#lista en blanco agrege una provincia
        agregarprovincia()
def agregardistrito():
    print("___Add district___")
    if len(listprovince)!=0:
        distrito= input("write the district you are going to add: ")#escriba el distrito que va agregar
        canton = input("write the canton where the district will be added: ")
        lis=detectcanton(canton)
        prov=lis[0]
        canton=lis[1]
        x={"distrito":distrito}
        if len(listprovince)!= 0:
            exist=False
            e=0
            while e < len(listprovince):
                if prov==listprovince[e]["provincia"]:
                    q=0
                    while q <len(listprovince[e]["cantones"]):
                        if canton==listprovince[e]["cantones"][q]["canton"]:
                            y=0
                            while y <len(listprovince[e]["cantones"]):
                                if len(listprovince[e]["cantones"][q]["distritos"])!=0:
                                    if distrito==listprovince[e]["cantones"][q]["distritos"][y]["distrito"]:
                                        exist = True
                                y+=1
                        q+=1
                e+= 1
            if exist==True:
                print("district already exist in canton")#distrito ya existe en el cantón
                agregardistrito()
            else:
                i=0
                while i<len(listprovince):
                    if prov==listprovince[i]["provincia"]:
                        j=0
                        while j<len(listprovince[i]["cantones"]):
                            if canton == listprovince[i]["cantones"][j]["canton"]:
                                listprovince[i]["cantones"][j]["distritos"].append(x)
                                print("district added")#distrito agregado
                                print(listprovince)
                                distribucionTerritorial()
                                break
                        j+=1
                    i+=1
    else:
        print("list cantons empty")#lista de cantones vacia
        distribucionTerritorial()
def quitarprovincia():
    print("___Remove province___")
    if listprovince != 0:
        province=input("what province will remove: ")#cual provincia va a eliminar
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
                    del listprovince[i]["provincia"]
                    print(listprovince)
                    distribucionTerritorial()
                    break

                i+=1
    else:
        print("list empty")
        distribucionTerritorial()
def quitarcanton():
    print("___Remove canton___")
    canton=input("what canton will remove?: ")#cual canton va a eliminar
    prov=input("what province will remove: ")#cual es la provincia del canton para eliminar
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
                            del listprovince[i]["cantones"][j]["canton"]
                            distribucionTerritorial()
                            break
                    j+=1
            i+=1
def quitardistrito():
    print("___Remove district___")
    distrit=input("what district remove?: ")#cual distrito eliminara#cual es el canton del distrito a eliminar
    canton = input("which canton belong the district: ")
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
                        while y < len(listprovince[e]["cantones"][q]["canton"]):
                            if len(listprovince[e]["cantones"][q]["distritos"]) != 0:
                                if distrito == listprovince[e]["cantones"][q]["distritos"][y]["distrito"]:
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
                    while j<len(listprovince[i]["cantones"]):
                        if canton==listprovince[i]["cantones"][j]["canton"]:
                            e=0
                            while e<len(listprovince):
                                if distrit==listprovince[i]["cantones"][j]["distritos"][e]["distrito"]:
                                    del listprovince[i]["cantones"][j]["distritos"][e]["distrito"]
                                    print(listprovince)
                                    distribucionTerritorial()
                                    break
                            e+=1
                    j+=1
            i+=1
    else:
        print("list empty")
        distribucionTerritorial()
def detectprov(prov):
    if len(listprovince)!=0:# escriba la provincia a aregar
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
def modifyprovince():
    if len(listprovince)!=0:
        province=input("which province you will modify?: ")
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
                    newprovince=input("which will be the new name for the province?: ")
                    listprovince[i]["provincia"]=newprovince
                    distribucionTerritorial()
                    break
                i+=1
    else:
        print("list empty")
        distribucionTerritorial()
def modifycanton():
    if len(listprovince)!=0:
        canton = input("what canton will be modify: ")  # cual canton va a eliminar
        prov = input("in which province belong the canton?: ")  # cual es la provincia del canton para eliminar
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
                            newcanton=input("which will be the new name of the canton?: ")
                            listprovince[i]["cantones"][j]["canton"]=newcanton
                            distribucionTerritorial()
                            break
                        j+=1
                i+=1
    else:
        print("list empty")
        distribucionTerritorial()
def modifydistric():
    distrit = input("what district it will be modify?: ")  # cual distrito eliminara#cual es el canton del distrito a eliminar
    canton = input("which canton belong the district: ")
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
                            if len(listprovince[e]["cantones"][q]["distritos"]) != 0:
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
                    while j < len(listprovince):
                        if canton == listprovince[i]["cantones"][j]["canton"]:
                            e = 0
                            while e < len(listprovince):
                                if distrit == listprovince[i]["cantones"][j]["distritos"][e]["distrito"]:
                                    newdistric=input("which will be the new name of the distric?: ")
                                    listprovince[i]["cantones"][j]["distritos"][e]["distrito"]=newdistric
                                    distribucionTerritorial()
                                    break
                                e+=1
                        j+=1
                i+=1
    else:
        print("list empty")
        distribucionTerritorial()
def detectcanton(canton):
    prov = input("which province belong the district?: ")
    if len(listprovince)!=0:
        exist = False
        i = 0
        while i < len(listprovince):
            if prov == listprovince[i]["provincia"]:
                j=0
                while j < len(listprovince[i]["cantones"]):
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
                distribucionTerritorial()
        else:
            print("list empty")
            distribucionTerritorial()
    else:
        print("list empty")
        distribucionTerritorial()
distribucionTerritorial()