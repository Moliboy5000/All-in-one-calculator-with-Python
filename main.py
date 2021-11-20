import os
from functions.arithmetics import arit_run
from functions.quadratics import quad_run
from typing import List, Dict

def main() -> None:
  #Dictionary where the name of a feature corresponds to its respective function.
  functions_dict: Dict[str,Callable[[],None]] = {
    "Arithmetic Calculator": arit_run,
    "Quadratic Equation Calculator": quad_run,
  }

  keys: List[str] = list(functions_dict.keys())

  def prompt_welcome_message() -> None:
    print("Hej och välkommen till Roccos fantastiska")
    print("kalkylator, med stöd för massor av roliga")
    print("uträkningar!")
    print("")
    print("För nuvarande har programmet dessa funktioner:")

    for key in keys:
      print(f"- {key}")

    new_line = "\n"
    print(new_line)

  def prompt_input() -> str:
    return input("Skriv in vilken funktion du vill använda (Enter avbryter): ")

  def clear() -> None:
    os.system("clear")

  def prompt_cancelation() -> None:
    print("Programmet avbrutet, ha en bra dag!")

  def prompt_choice(choice: str) -> None:
    print("Du har valt:", choice) 

  def prompt_unsupported() -> None:
    print("Den inskrivna funktionen stöds inte i programmet!")

  prompt_welcome_message()

  while True:
    func_choice: str = prompt_input()
    if func_choice == "":
      clear()
      prompt_cancelation()
      break
    elif func_choice in functions:
      clear()
      prompt_choice(func_choice)
      functions[func_choice]() #The function corresponding to the written name will be called.
    else:
      prompt_unsupported()
  #If the function is not found in the dictionary, this message is returned and the loop continues

if __name__ == "__main__":
  main()