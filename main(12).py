numeros=input()
lista=[]
pares=0
impares=0
while True:
  if numeros.isdigit():
    numeros=int(numeros)
    lista.append(numeros)
    numeros=input()
  elif numeros=="*":
    break

for i in lista:
  if i%2==0:
    pares+=1
  else:
    impares+=1

print("PARES="+str(pares))
print("IMPARES="+str(impares))