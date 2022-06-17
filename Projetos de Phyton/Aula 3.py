a = int(input("valor 1 : "))
b = int(input("valor 2 : "))
c = int(input("valor 3 : "))
if a > b and a > c:
    print('o maior numero é {}'.format(a))
elif b > a and b > c:
    print('o maior numero é {}'.format(b))
else:
    print("o maior numero é {}".format(c))
print("Fim")