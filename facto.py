def facto(n):
    if (n<0) :
        raise ValueError("entier negatif")
    if (n==0):
        return 1
    else:
        return n*facto(n-1)

n = input("Donner un entier n : ")
try:
    print(facto(n))
except ValueError:
    print("Boom! Erreur ")
