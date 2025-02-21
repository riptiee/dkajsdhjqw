# año bisiesto
import calendar
from calendar import isleap
año = int(input("Decime un año: "))

if isleap(año):
  print(f"{año} es bisiesto")
else:
  print(f"{año} no es bisiesto")