import random 
com = random.randint(1,100)
tries = 0

while True:
    tries += 1
    hum = int(input("Enter the number between 1-100:"))


    if hum==com:
                    print(f"won in {tries} tries")
                    break 
    elif hum > com:
                print("wrong guess go lower")
    elif hum < com:
                print("wrong guess go up")