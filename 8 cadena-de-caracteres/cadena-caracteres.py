letra = 'a'
apellido = """texto textotextotextotextotextotextotextotextotextotextotextotextotextotextotextotextotextotextovtextotextotextotextotextotextotextotextotextotextotextotextotextov
textotextotextotextotextotextovtexto"""

x = 5.2
y = 10
a = "El numero es: %.2f y %d" %(x,y)
s = "El numero es: " + str(x)
ss = "El numero es: %d" %x

print(a)
print(s)
print(ss)

#ejemplos
j = "Los numeros son{} y {}" .format(5,10) 
k = "Los numeros son{a} y {b}" .format(a=5,b=10)  

a = 100
b = 5 
l = f"Los numeros son {a} y {b}"
#-------------------------------------------------------------------------------------------
kl = f"a + b = {a+b}"
print(kl)

#---------------------------------------------------------------------------------------
def funcion():
    return 20

s = f"El resultado de la fucion es {funcion()}"
print(s)
#--------------------------------------------------------------------------------------
texto = "este texto es muy largo resulta en un codigo significativamente mas largo"
 
if "corto" not in texto:
    print("No, 'corto'")

#SE PUEDE CONVERTIR A STRING OTRAS CLASES, COMO INT O FLOAT
x = str(10.4)

print(x)
print(type(x))

#-------------------------------------------------------------------
z = "abced"

print(z[-2])
#----------------------------------------------

x = "abcde"
print(x[0:2])
print(x[0:])

#---------------------------------------------------
#saltea letras

print(x[1::3])

#-----------------------------------------------
for caracter in "python":
    print(caracter)