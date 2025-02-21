import getpass

def contraseña():
  contra1 = getpass.getpass("Ingrese su nueva contraseña: ")
  contra2 = getpass.getpass("Repita su nueva contraseña: ")

  while contra1 != contra2:
   print("Las contraseñas no coincinden.")
   contra1 = getpass.getpass("Ingrese su nueva contraseña: ")
   contra2 = getpass.getpass("Repita su nueva contraseña: ")

  print("¡Contraseña cambiada exitosamente!")
contraseña()
