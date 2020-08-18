import random
import math

money = 100

#Write your game of chance functions here
randNum = random.randint(1, 10)

def coin_flip(amount_bet, bet_on):
    coin = random.randint(1, 2)
    if(coin == 1):
        print("It's heads!")
    else:
        print("It's tails!")

    if (coin == 1 and bet_on == "heads"):
        print("You have won on your bet of " + str(amount_bet) + "and won " + str(amount_bet*2) + "!")
        return str(amount_bet*2)
    elif(coin == 2 and bet_on == "tails"):
        print("You have won on your bet of " + str(amount_bet) + "and won " + str(amount_bet*2) + "!")
        return str(amount_bet*2)
    else:
        print("You have lost your bet of " + str(amount_bet) + ".")
        return amount_bet-(amount_bet*2)
        
def cho_han(amount_bet, bet_on):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice_tot = dice1 + dice2
    print("The dice have rolled " + dice1 + " and " + dice2 + " making a total of " + dice_tot)
    if(dice_tot % 2 == 0 and bet_on == "Even"):
        print("You have won " + str(amount_bet*2) + " Congratulations!")
        return str(amount_bet*2)
    elif(dice_tot % 2 != 0 and bet_on == "Odd"):
        print("You have won " + str(amount_bet*2) + " Congratulations!")
        return str(amount_bet*2)
    else:
        print("You have lost your bet of " + str(amount_bet) + ".")
        return amount_bet-(amount_bet*2)

def card_battle(amount_bet):
    play1_card = random.randint(1, 14)
    play2_card = random.randint(1, 14)
    if(play1_card > play2_card):
        print("You have won " + str(amount_bet*2) + " Congratulations!")
        return amount_bet*2
    elif(play1_card == play2_card):
        print("It's a tie, no win or loss!")
    else:
        print("You have lost your bet of " + str(amount_bet) + ".")
        return amount_bet-(amount_bet*2)

def hardcore_roulette(amount_bet, bet_on):
    roulette = random.randint(0, 36)
    if(bet_on == roulette):
        print("Congratulations! You have won " + str(amount_bet*36) + "on number " + str(roulette) + "!")
        return amount_bet*36
    else:
        print("You have lost your bet of " + str(amount_bet) + ".")



#Call your game of chance functions here
coin_flip(100, "heads")
coin_flip(100, "heads")
coin_flip(100, "heads")
