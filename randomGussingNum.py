import random 

target=random.randint(1,100)

while True:
    userCoice=input("Guess the number or Quit(Q):")

    if userCoice== "Q" :
        break

    userCoice=int(userCoice)
    if userCoice == target:
        print(f"You have succesfully guess the number {target}")
        break

    elif userCoice<target:
        print(f"{userCoice} too small,Guess the bigger number ")

    else:
        print(f"{userCoice} too big ,Guess the smaller number")

print("----- Game over ----")