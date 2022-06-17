a= int(input("Digite nota 1: "))
if  a >=10:
    a = int(input("Você digitou a nota 1 errada"))
b= int(input("Digite nota 2: "))
if b >=10:
    b= int(input("Você digitou a nota 2 errada"))
c= int(input("Digite nota 3: "))
if c >=10:
    c= int(input("Você digitou a nota 3 errada"))
d= int(input("Digite nota 4: "))
if d >=10:
    d= int(input("Você digitou a nota 4 errada"))
media = (a+b+c+d)/4
print("media:{}".format(media))







#    1 Forma que aprendi
# if a <=10 and b <=10 and c <=10 and d <=10:
#     print("media igual a {}".format(media))
# else:
#     print("nota invalida")