name=input("enter name :")
print("welcome "+name,"play")
word="paramesh"

guesses=""
turn=10
while turn>0:
    fail = 0
    for x in word:
        if x in guesses:
            print(x)
        else:
            print("-")
            fail+=1
    if fail==0:
        print("winner")
        break
    print()
    guess=input("enter x value:")
    guesses+=guess
    if guess not in word:
        turn-=1
        print("wrong guess")
        print("you have ",+turn)
    if turn==0:
        print("losser")