class Card():

    def __init__(self, suit, value):
        self.suit = str(suit)
        self.value = value

    def __str__(self):
        return f'{self.value} of {self.suit}'


class Deck():

    def __init__(self):
        amount = 0
        self.amount = amount
        deck = [''] * self.amount
        self.deck = deck

    def __getitem__(self, index):
        try:
            return self.deck[index]
        except IndexError:
            return None

    def shuffle(self):
        from random import shuffle
        shuffle(self.deck)

    def getcard(self):
        appendcard = self.deck[0]
        self.deck = self.deck[1:]
        return appendcard

    def blackjackdeck(self):
        self.amount = 52
        deck = [''] * self.amount
        self.deck = deck
        suits = ['♠', '♦', '♥', '♣']
        values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
        deck_index = 0
        for x in suits:
            for y in values:
                deck[deck_index] = Card(x, y)
                deck_index += 1

    def inputcard(self, card):
        self.card = card
        (self.deck).append(card)

    def points(self):
        summ = 0
        self.summ = summ
        for x in self.deck:
            if x.value in range(2, 11):
                self.summ = self.summ + x.value
            elif x.value != 'Ace':
                self.summ = self.summ + 10
            elif x.value == 'Ace':
                self.summ = self.summ + 11
            else:
                continue
        if self.summ > 21:
            for x in self.deck:
                if x == 'Ace':
                    self.summ = self.summ - 10
        return self.summ

    def __len__(self):
        self.length = len(self.deck)
        return self.length


class Account():

    def __init__(self, balance=0):
        self.balance = int(balance)

    def __str__(self):
        return f'{self.balance}''

    def __int__(self):
        return self.balance

    def bet(self, withdraw):
        self.withdraw = int(withdraw)
        self.balance = self.balance - self.withdraw
        return Account(self.balance)

    def inputmoney(self, inp=0):
        self.inp = int(inp)
        self.balance = self.balance + self.inp
        return Account(self.balance)


def winchecking(playerdeck, dealerdeck):
    if len(playerdeck) == 2 and playerdeck.points() == 21:
        if dealerdeck[0] not in range(2, 10):
            x = 0
            while x != 'Y' and x != 'N':
                x = input('\nDo you want to take your money 1:1? (Y/N)     ')
            if x == 'Y':
                print('\nCongratulations, you have a blackjack. You win 1:1!')
                return 2
            else:
                if dealerdeck.points() == 21:
                    print('\nDealer has blackjack too. You get back your bet')
                    return 1
                else:
                    print(
                        '\nCongratulations, dealer does not have blackjack. You win 3:2!')
                    return 2.5
        else:
            return 1.5
    elif len(playerdeck) > 2 or len(dealerdeck) > 2:
        if playerdeck.points() > 21:
            print('\nToo much points in your cards. You lose your bet')
            return 0
        elif dealerdeck.points() > 21:
            print('\nDealer has too much points. You are win')
            return 2
        elif dealerdeck.points() == 21 and dealerdeck.points() > playerdeck.points():
            print('\nDealer has a blackjack. You lose your bet')
            return 0
        elif dealerdeck.points() > playerdeck.points() and dealerdeck.points() < 21:
            print('\nDealer has more points then you. You lose your bet')
            return 0
        elif dealerdeck.points() < playerdeck.points() and playerdeck.points() < 21:
            print(
                '\nCongratulations, you have more points then dealer. You win 1:1!')
            return 2
    else:
        pass


def visio(playerdeck, dealerdeck, gamestatus):
    # gamestatus 0 - в ходе игры 1 после вскрытия
    print('\nThese is your cards:')
    for card in playerdeck:
        if card != None:
            print(card)
        else:
            break
    if gamestatus == 0:
        print('\nThese is dealer cards:')
        print('This card is hidden')
        for card in dealerdeck[1:]:
            if card != None:
                print(card)
            else:
                break
    if gamestatus == 1:
        print('\nThese is dealer cards:')
        for card in dealerdeck:
            if card != None:
                print(card)
            else:
                break


if __name__ == '__main__':

    print('Hi, this is blackjack game')
    gamestatus = 'Y'

    purse = Account()
    purse = purse.inputmoney(input('Input your balance:  '))

    while gamestatus == 'Y':
        maindeck = Deck()
        maindeck.blackjackdeck()
        maindeck.shuffle()
        mydeck = Deck()
        dealerdeck = Deck()
        deskbet = Account()

        while True:
            deskbet = deskbet.inputmoney(input('Input your bet: '))

            if int(deskbet) > int(purse):
                deskbet = Account()
                print('You dont have enough money')
                continue

            else:
                print('Bet have been done')
                purse = purse.bet(int(deskbet))
                break

        mydeck.inputcard(maindeck.getcard())
        dealerdeck.inputcard(maindeck.getcard())
        mydeck.inputcard(maindeck.getcard())
        dealerdeck.inputcard(maindeck.getcard())

        visio(mydeck, dealerdeck, 0)
        if mydeck.points == 21 or dealerdeck.points == 21:
            purse.inputmoney(
                int(deskbet) * int(winchecking(mydeck, dealerdeck)))
            print('\nFinal situation:')
            visio(mydeck, dealerdeck, 1)
            break

        else:
            hit = ''

            while hit != 'Y' and hit != 'N':
                hit = input('Do you wish to hit? Y/N   ')

                if hit == 'Y':
                    mydeck.inputcard(maindeck.getcard())

                    if mydeck.points() >= 21:
                        purse.inputmoney(
                            int(deskbet) * int(winchecking(mydeck, dealerdeck)))
                        print('\nFinal situation:')
                        visio(mydeck, dealerdeck, 1)
                        break

                    else:
                        hit = ''
                        visio(mydeck, dealerdeck, 0)
                        continue

                elif hit == 'N':

                    while dealerdeck.points() <= 21:
                        dealerdeck.inputcard(maindeck.getcard())
                        visio(mydeck, dealerdeck, 0)

                    purse.inputmoney(
                        int(deskbet) * int(winchecking(mydeck, dealerdeck)))
                    print('\nFinal situation:')
                    visio(mydeck, dealerdeck, 1)
                    break

        if int(purse) > 0:
            print(f'\nYour balance: {int(purse)}$'')
            gamestatus = input('Do you want to play again?  Y/N    ')
        else:
            print('\nYou lose all your money. Good luck')
            gamestatus = 'N'
