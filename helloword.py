print ("Hello world")
#------------------------------------------------------------------------
#calcolo dei numeri in python
#------------------------------------------------------------------------
print(10//3)
print(10**3)
print("5"+"2")
print("Hello","World")
#------------------------------------------------------------------------
#VARIABILI
#------------------------------------------------------------------------
nome = input("Come ti chiami?")
print(nome)
ciao = "ciao"
num = input("inserisci un numero: ")
num = int(num)
#------------------------------------------------------------------------
#FORMATTAZIONE
#------------------------------------------------------------------------
num = input("inserisci un numero")
string = input("inserisci una stringa")
print("questa è la stringa"+string+"questo è il numero"+ str(num)) 

num = input("inserisci un numero")
string = input("inserisci una stringa")
print("Questa è la stringa %s questo è il numero %d" % (string,num))

cat = "bob"
age = 13
peso = 56.43883547
peso = float(peso)
print(f"Il nome del gatto è {cat} la sua età è {age} il suo peso è {peso}")
print("il numero che hai inserito è", num)