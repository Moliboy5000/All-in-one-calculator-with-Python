#Benjamin är välkommen att lägga till sin kod här, glöm inte att lägga in det i en funktion som heter arit_run

def arit_run():
  print_answer = lambda answer: print(f"\nAnswer:\n{answer}")

  #Stringen som är en beräkning från användaren
  prompted_calculation = input("Skriv den aritmetiska beräkningen du vill göra:\n")

  #Beräkningsformatisering/standardisering för python
  if "," in prompted_calculation:
    prompted_calculation = prompted_calculation.replace(",",".")

  #Den faktiska beräkningen samt output printen för respektive aritmetisk operation
    #Partition delar upp en string i en lista med olika entries baserad på stringen man specificerar (före, specificerad, efter).

  #För division
  if "/" in prompted_calculation:
    output = float(prompted_calculation.partition('/')[0]) / float(prompted_calculation.partition('/')[2])

    print_answer(output)

  elif "*" in prompted_calculation:
    output = float(prompted_calculation.partition('*')[0]) * float(prompted_calculation.partition('*')[2])

    print_answer(output)

  elif "-" in prompted_calculation:
    output = float(prompted_calculation.partition('-')[0]) - float(prompted_calculation.partition('-')[2])

    print_answer(output)

  elif "+" in prompted_calculation:
    output = float(prompted_calculation.partition('+')[0]) + float(prompted_calculation.partition('+')[2])

    print_answer(output)

  #Del som hanterar när man skrivit fel input
  else:
    print("Det kan hända att vi inte stödjer denna funkktion. Testa att använda ett synonymt tecken, om det inte fungerar stöds funktionen ej.")