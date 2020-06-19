import random

money = 100 



def heads_tails(bet_amount, bet):
    global money
    if bet_amount <= money:
        result = random.randint(1, 2)
        if result == 1:
            result = 'heads'
        else:
            result = 'tails'
        if bet.lower() == result:
            money += bet_amount
            return print(money)
        else:
            money -= bet_amount
            return print(money)
    else:
        return print('No bet, what do I look like a bank??')

    

def cho_han(bet_amount, bet):
    global money
    if bet_amount <= money:
        die_1 = random.randint(1, 6)
        die_2 = random.randint(1, 6)
        result = die_1 + die_2
        if result % 2 == 0:
            result = 'even'
        else:
            result = 'odd'
        if bet.lower() == result:
            money += bet_amount
            return print(money)
        else:
            money -= bet_amount
            return print(money)
    else:
        return print('No bet, what do I look like a bank??')

def war(my_bet, plyr_two_bet):
    global money
    if my_bet <= money:
        pot = my_bet + plyr_two_bet
        deck_of_cards = list(range(1, 14)) * 4
        my_result = random.choice(deck_of_cards)
        index = deck_of_cards.index(my_result)
        if my_result == 1:
            deck_of_cards.pop(deck_of_cards[index])
        else:
            deck_of_cards.pop(deck_of_cards[index-1])
        plyr_two_result = random.choice(deck_of_cards)
        if my_result == plyr_two_result:
            return print('Tie Game. You are returned ' + str(my_bet) + ' dollars, and still have ' + str(money) + 'dollars. Player two is returned ' + str(plyr_two_bet) + ' dollars.')
        elif my_result > plyr_two_result:
            money += plyr_two_bet
            return print('You win the pot and now have ' + str(money) + ' dollars.')
        else:
            money -= my_bet
            return print('You lost and now have ' + str(money) + ' dollars. Player 2 wins, and now has ' + str(pot) + ' dollars.')
    else:
        return print('No bet, what do I look like a bank??')
    






def roulette(bet_amount, bet):
    global money
    if bet_amount <= money:
        wheel = list(range(0,41))
        spin = random.choice(wheel)
        integer_win = bet_amount * 35
        if type(bet) == str:
            if bet.lower() == 'odd':
                if spin == 0:
                    money -= bet_amount
                    return print('The ball landed on Zero, you lose. You now have ' + str(money) + ' dollars.')
                if spin == 40:
                    money -= bet_amount
                    return print('The ball landed on double zero, you lose. You now have ' + str(money) + ' dollars.')
                if spin % 2 == 0:
                    money -= bet_amount
                    return print('The ball landed on ' + str(spin) + ' an Even number, you lose. You now have ' + str(money) + ' dollars.')
                else:
                    money += bet_amount
                    return print("Congratulations! The ball landed on " + str(spin) + " which is an Odd number, you've won and you now have " + str(money) + ' dollars.')

            if bet.lower() == 'even': 
                if spin == 0:
                    money -= bet_amount
                    return print('The ball landed on Zero, you lose. You now have ' + str(money) + ' dollars.')
                if spin == 40:
                    money -= bet_amount
                    return print('The ball landed on double zero, you lose. You now have ' + str(money) + ' dollars.')
                if spin % 2 == 1:
                    money -= bet_amount
                    return print('The ball landed on ' + str(spin) + ' an Odd number, you lose. You now have ' + str(money) + ' dollars.')
                else:
                    money += bet_amount
                    return print("Congratulations! The ball landed on " + str(spin) + " which is an Even number, you've won and you now have " + str(money) + ' dollars.')
            else:
                return print("Sorry, but you did not place a valid bet. Please try again")
        elif type(bet) == int:
            if bet == spin:
                money += integer_win
                return print("WOW! Congratulations you just hit on " + str(spin) + "! You've won and you now have " + str(money) + " dollars!")
            else:
                money -= bet_amount
                return print("There's a sucker born everyday. You now have " + str(money) + ' dollars.')
        else:
            return print("Stop wasting our time, either you're in or out!")
    else:
        return print('No bet, what do I look like a bank??')



       
      
