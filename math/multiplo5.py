#programa que detecta numeros multiplos de cinco
# reciben valor ingresado por el usuario
x =int(raw_input("ingrese el numero que quire evaluar :"))

while x < 1:
     x =int(raw_input("ingrese el numero que quire evaluar :"))

if x%5==0:
    print "Es multiplo de 5"
else:
    print "No es multiplo de 5"
