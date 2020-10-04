#-------------------------------
#Liste
#------------------------------
lista = [5,4,3,2,1,0]
type(lista)
len(lista)

lista[5]
lista[4]
lista[0:3]
lista[::-1]#capovolta
lista[3:]#da indice tre in poi
lista[0] = 10
lista[-2:] = [33,44]#modifica gli ultimi due
lista[:4]

animali = ["cane", "gatto", "maiale", "topo", "apple"]
animali.remove("gatto")
print(animali)
animali.append("mulo")
print(animali)
"cane" in animali
"gatto" in animali
animali.pop(1)
print(animali)

animali.insert(3,"chi compra apple")
print(animali)
#Tuple non si possono modificare ma possono essere eterogenere
tupla = (0, "ciao", "ciao", 3 , 8 , False)
len(tupla)
tupla.count("ciao")
tupla.index(3)
tupla[3:]

