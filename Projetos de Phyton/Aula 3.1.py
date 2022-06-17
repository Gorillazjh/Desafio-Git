a = int(input("numero 1: "))
b  = int(input("numero 2: "))
resto = a % 2
resto_b = b % 2
if resto == 0 or not resto_b > 0:
    print("é par")
else:
    print("não foi digitado numero par")
print("fim")
