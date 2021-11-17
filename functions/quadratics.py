from math import sqrt

def quad(a, b, c):
  delta = b*b -4 * a * c
  if a == 0:
    print("Om a = 0 så är det inte en andragradsekvation, vänligen ange ett annat värde för a")
  elif delta < 0:
    print("Det finns inga reella lösningar för denna andragradsekvation")
  elif delta == 0:
    print("x = {}".format(-b/(2*a)))
  else:
    print("x1 = {0:.2f} x2 = {1:.2f}".format((-b + sqrt(delta))/(2*a), (-b - sqrt(delta))/(2*a) ))


def quad_run():
 while True:   
    try:
      a = float(input("Skriv a:"))
      b = float(input("Skriv b:"))
      c = float(input("Skriv c:"))
    except:
      print("Ang ett giltligt tal")
    quad(a, b, c)
    break
 while True:
    cont = input("Vill du fortsätta?(Ja/Nej)")
    if cont == "Ja":
      quad_run()
    elif cont == "Nej":
      print("Program avbrutet")
      break
    else:
      print("Ange ett giltligt svar")
