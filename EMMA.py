lista=[1,4,5,6,2]
def count(list):
    if list==[]:
        return 0
    else:
        if list[0]%2==0:
            return 1+count(list[1:])
        else:
            return 0+count(list[1:])
print(count(lista))
