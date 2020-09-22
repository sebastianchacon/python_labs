# created by: sebastian chacon
# description: simple python program to sum products

# validate inputs (positive floats)
while True:
    try:
        p1 = float(input("precio del producto 1: "))
        c1 =  float(input("cantidad del producto 1: "))

        p2 = float(input("precio del producto 2: "))
        c2 =  float(input("cantidad del producto 2: "))
    except ValueError:
        print("Debes escribir un número.")
        continue
    # validate is a positive number
    if (p1 or c1 or p2 or c2) < 0:
        print("Debes escribir un número positivo.")
        continue
    else:
        break


# operartions
r1 = p1*c1
r2 = p2*c2

# sum result
r = r1 + r2

#print result as string 
print("tu resultado final es "+str(r)) 