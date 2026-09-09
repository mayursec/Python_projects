import time
x = int(input("Set timer:"))

if x <=0:
        print("please enter valid number")
else:
    while x>0:
        if x ==1:
            print(f"{x} second remaining")
        else:
            print(f"{x} seconds remaining")
        time.sleep(1)
        x -=1
    print("time up")

                    
        

    