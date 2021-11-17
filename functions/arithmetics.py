#Benjamin är välkommen att lägga till sin kod här, glöm inte att lägga in det i en funktion som heter arit_run

def arit_run():
  #Stringen som är en beräkning från användaren
  Beräkning = input("Skriv den aritmetiska beräkningen du vill göra:\n")

  #Beräkningsformatisering/standardisering för python
  if "," in Beräkning:
    Beräkning = Beräkning.replace(",",".")

  #Den faktiska beräkningen samt output printen för respektive aritmetisk operation
    #Partition delar upp en string i en lista med olika entries baserad på stringen man specificerar (före, specificerad, efter).

  #För division
  if "/" in Beräkning:
    Output = float(Beräkning.partition('/')[0]) / float(Beräkning.partition('/')[2])

    print("\nAnswer:\n{}".format(Output))

  elif "*" in Beräkning:
    Output = float(Beräkning.partition('*')[0]) * float(Beräkning.partition('*')[2])

    print("\nAnswer:\n{}".format(Output))

  elif "-" in Beräkning:
    Output = float(Beräkning.partition('-')[0]) - float(Beräkning.partition('-')[2])

    print("\nAnswer:\n{}".format(Output))

  elif "+" in Beräkning:
    Output = float(Beräkning.partition('+')[0]) + float(Beräkning.partition('+')[2])

    print("\nAnswer:\n{}".format(Output))

  #Del som hanterar när man skrivit fel input
  else:
    print("Det kan hända att vi inte stödjer denna funkktion. Testa att använda ett synonymt tecken, om det inte fungerar stöds funktionen ej.")
