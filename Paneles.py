def calculate_panels(x,y):
    a = 1
    b = 2
    techo=x*y
    panels = a*b
    if (a>x and b>x or a>y and b>y):
        resultado = 0
        return resultado
    else:
        resultado = techo/panels
        return resultado

ancho=input("Cual es el ancho del techo  ")
x=int(ancho)
largo=input("Cual es el largo del techo  ")
y=int(largo)
resultado  = int(calculate_panels(x,y))
print (resultado)