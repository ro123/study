from random import randint

x = randint(1,100)

print("Guess game \nRules: Guess the number, which was randomly picked by a program")

guesses_list = [0,0]

while guesses_list[-1] != x:

    guesses_list+=[int(input('Guess the number '))]

    if guesses_list[-1]==x:

        break

    else:

        if len(guesses_list) <= 3:

            if abs(x-guesses_list[-1])<10:

                print("WARM!")

                continue

            else:

                print('COLD!')

                continue

        elif len(guesses_list) > 3:

            if abs(x-guesses_list[-1])<abs(x-guesses_list[-2]):

                print("WARMER!")

                continue

            else :

                print("COLDER!")

                continue

                

print('You are right!!! Congratulations!!!')

print(f"You've got {len(guesses_list)-2} attempts to find the number")
