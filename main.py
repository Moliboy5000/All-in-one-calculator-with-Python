import os
from functions.arithmetics import arit_run
from functions.quadratics import quad_run

functions = {
"Arithmetic Calculator": arit_run,
"Quadratic Equation Calculator": quad_run,
}
keys = list(functions.keys())

print("Hej och välkommen till Roccos fantastiska kalkylator, med stöd för massor av roliga uträkningar")
print("För nuvarande har programmet dessa funktioner:")
print(*keys, "\n")

while True:
  func_choice = input("Vänligen skriv vilken funktion du vill använda (Enter avbryter)")
  if func_choice == "":
    print("Programmet avbrutet, ha en bra dag!")
    break
  elif func_choice in functions:
    os.system("clear")
    print("Du har valt:", func_choice)
    functions[func_choice]()
  else:
    print("Den inskrivna funktionen stöds inte i programmet")

