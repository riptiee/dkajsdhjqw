# nueva contraseña
import getpass
password1 = getpass.getpass("Ingrese su nueva contraseña: ")
password2 = getpass.getpass("Repita su nueva contraseña: ")

while password1 != password2:
  print("Las contraseñas no coincinden.")
  password1 = getpass.getpass("Ingrese su nueva contraseña: ")
  password2 = getpass.getpass("Repita su nueva contraseña: ")

print("¡Contraseña cambiada exitosamente!")