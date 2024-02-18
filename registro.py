import os
import time

print("\033[0;33m" + "Vamos a iniciar sesion ;)" + "\033[0;0m")

time.sleep(1)

usuario = input("Escriba su nombre de usuario de instagram: ")
os.system("instaloader --login " + (usuario))
