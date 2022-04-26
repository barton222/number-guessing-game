import random
money = 300

def jackpot():
    global money
    money += 10000
    print("YOU WON A JACKPOT!!!")

def win(rate=0):
    global money
    if rate == 0:
        jackpot()
    elif rate < 4:
        money += rate*100
        print("You won!")
    else:
        print("You lost...")

def play():
    global money
    money -= 100
    num = random.randint(1,30)
    choice = input("Choose a number between 1 and 30: ")
    try:
        win(abs(num - int(choice)))
    except:
        win()

def mon():
    print(money)

while True:
    mon()
    play()
