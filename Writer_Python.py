Beginning = False
PreviousAddon = False

while True:
  if not Beginning:
    #Checks if there isn't a beginning
    Beginning = input()
    print(Beginning)
  if Beginning:
    #Checks if there is a beginning
    if not PreviousAddon:
      #Checks if there isn't an Addon
      Addon = input()
      print(Beginning + Addon)
      PreviousAddon = Addon
    elif PreviousAddon:
      #Checks if there is an Addon
      Addon = input()
      print(Beginning + PreviousAddon + Addon)
      PreviousAddon = Addon
