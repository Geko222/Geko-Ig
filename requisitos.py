import os
import time

print("\033[0;33m" + "Vamos a proceder a instalar los requisitos" + "\033[0;0m")

time.sleep(1)

try:
    os.system("pip install isntaloader")
except:
    print("\033[0;31m" + "Algo ha fallado o ya tienes los requisitos instalados anteriormente" + "\033[0;32m")
else:
    print("\033[0;32m" + "Los requisitos se an isntalado correctamente" + "\033[0;0m" )
