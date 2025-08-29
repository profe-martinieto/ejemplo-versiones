from archivo1 import leer_nombre
from archivo2 import leer_edad
from archivo3 import leer_ciudad

# Leer las variables usando las funciones de los otros archivos
var1 = leer_nombre()
var2 = leer_edad()
var3 = leer_ciudad()

# Guardar las variables en datos.txt
with open("datos.txt", "w") as archivo:
    archivo.write(f"{var1}\n{var2}\n{var3}\n")