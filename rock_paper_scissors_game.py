import random

answer = random.choice(['rock','paper','scissors'])

while True:

    try:
        guess = input('choose your operation')
        if guess=='rock'and answer=='rock':
            print("draw match")
            print(answer)
            break
        elif guess=='rock' and answer=='paper':
            print("computer wins")
            print(answer)
            break
        elif guess=='rock' and answer=='scissors':
            print("user wins")
            print(answer)
            break

        elif guess=='paper'and answer=='paper':
            print("draw match")
            break
        elif guess=='paper' and answer=='scissors':
            print("computer wins")
            break
        elif guess=='paper' and answer=='rock':
            print("user wins")
            break

        elif guess=='scissors'and answer=='rock':
            print("computer wins")
            break
        elif guess=='scissors' and answer=='paper':
            print("user wins")
            break
        elif guess=='scissors' and answer=='scissors':
            print("draw match")
            break
        else:
            print("invalid input")
    except ValueError:
        print('please enter number')
        continue
