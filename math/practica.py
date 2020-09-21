precio_producto_1= input("cual es el precio del producto 1: ")
cantidad_producto_1= input("cual es la cantidad del producto 1: ")
precio_producto_2= input("cual es el precio del producto 2: ")
cantidad_producto_2= input("cual es la cantidad del producto 2: ")
precio_producto_3= input("cual es el precio del producto 3: ")
cantidad_producto_3= input("cual es la cantidad del producto 3: ")

resultado_producto_1= float(precio_producto_1)+float(cantidad_producto_1)
resultado_producto_2= float(precio_producto_2)+float(cantidad_producto_2)
resultado_producto_3= float(precio_producto_3)+float(cantidad_producto_3)

resultado= resultado_producto_1+resultado_producto_2+resultado_producto_3

print("tu resultado final es "+str(resultado))