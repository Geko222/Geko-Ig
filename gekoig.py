import os
import time

print("""
  ________        __           .___        
 /  _____/  ____ |  | ______   |   | ____  
/   \  ____/ __ \|  |/ /  _ \  |   |/ ___\ 
\    \_\  \  ___/|    <  <_> ) |   / /_/  >
 \______  /\___  >__|_ \____/  |___\___  / 
        \/     \/     \/          /_____/  
      
     """)

usuario = input("\033[0;33m" + "Ingrese tu nombre de usuario:" + "\033[0;0m")
victima = input("\033[0;33m" + "Ingrese el nombre de usuario de la victima:" + "\033[0;0m")
time.sleep(2)
print("\033[0;32m" + "Se comenzara la descarga de archivos :)" + "\033[0;0m")
os.system("instaloader --login="+usuario +" --comments --geotags --stories --highlights --tagged --igtv " + victima)
