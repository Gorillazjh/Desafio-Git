a = int(input("Digite nota numero 1: "))
while a > 10:
    a= int(input("Nota Incorreta favor digitar novamente a nota 1: "))
b = int(input("Digite nota numero 2: "))
while b > 10:
    b= int(input("Nota Incorreta favor digitar novamente a nota 2: "))
c = int(input("Digite nota numero 2: "))
while c > 10:
    b= int(input("Nota Incorreta favor digitar novamente a nota 3: "))
media = (a+b+c)/3
print("A mediá é: {}".format(media))
if media >=6:
    print("A media {} dentro das metricas necessarias".format(media))
else:
    print("Media {} inferior ao necessario para processeguir no semestre".format(media))

