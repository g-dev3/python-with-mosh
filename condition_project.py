weight = input("Weight: ")

bs_g = input("(L)bs or (K)g: ")

if bs_g == "L" or bs_g == "l":
  print(f'You are {int(weight) * 0.4535} kilos')
elif bs_g == "K" or bs_g == "k":
  print(f'You are {int(weight) * 2.2} pounds')
else:
  print("please try again")

if bs_g.upper() == "L":
  print(f'You are {int(weight) * 0.45} kilos')
elif bs_g.upper() == "K":
  print(f'You are {int(weight) / 0.45} pounds')
else:
  print("please try again")