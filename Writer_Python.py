Beginning = False
PreviousAddon = False

while True:
  if not Beginning:
    #Checks if there isn't a beginning
    Beginning = input()
    if Beginning:
      print(Beginning)
    elif not Beginning:
      break
  if Beginning:
    #Checks if there is a beginning
    if not PreviousAddon:
      #Checks if there isn't an Addon
      Addon = input()
      if Addon:
        print(Beginning + " " + Addon)
        PreviousAddon = Addon
      elif not Addon:
        break
    elif PreviousAddon:
      #Checks if there is an Addon
      Addon = input()
      if Addon:
        print(Beginning + " " + PreviousAddon + " " + Addon)
        PreviousAddon = PreviousAddon + " " + Addon
      elif not Addon:
        break
