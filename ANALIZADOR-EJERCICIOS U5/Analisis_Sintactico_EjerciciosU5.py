import re
path = "tema1.java"
try:
    archivo = open(path, 'r')
except:
    print("XXXXXXXXXXX-No se encontro ningun archivo-XXXXXXXXXXXXX")
    quit()
texto = " "
for linea in archivo:
    texto += linea

print("---------ANALIZADOR SINTACTICO UNIDAD 5-------------")
regex = re.compile('[A-Za-z]\w*[ ]*[=][ ]*\w+[.]?\d*')
result = re.findall(regex, texto)
print("\n 1-Las sentencias de asignación encontradas son: ", result)

regex2 = re.compile('[A-Za-z]\w*[ ]*[=][ ]*\w+[.]?\d*[ ]*[+-\/\*][ ]*\w+')
result2 = re.findall(regex2, texto)
print("\n 2-Las operaciones aritméticas básicas encontradas son: ", result2)

regex3 = re.compile('[A-Za-z]\w*[ ]*[<>!=][=][ ]*[A-Za-z0-9]|[A-Za-z]\w*[ ]*[<>][ ]*[A-Za-z0-9]')
result3 = re.findall(regex3, texto)
print("\n 3-Las expresiones booleanas básicas encontradas son: ", result3)

regex4 = re.compile('[A-Za-z][\w]*[ ]*[=][ ]*\w+[.]?\d*[ ]*[+-\/*%][ ]*\([ ]*\w+[.]?[\d]*[ ]*[+-\/*%][ ]*\w+[.]?[\d]*[ ]*\)')
result4 = re.findall(regex4, texto)
print("\n 4-Las formulas más complejas encontradas son: ", result4)

regex5 = re.compile('if[ ]*\(.+\)|else[ ]*\(.+\)|do[ ]*\(.+\)|while[ ]*\(.+\)|for[ ]*\(.+\)|switch[ ]*\(.+\)')
result5 = re.findall(regex5, texto)
print("\n 5-los encabezados de estructuras de control encontrados son: ", result5)
print("\n Hecho por HENRY FROYLAN CHUC TEC")
