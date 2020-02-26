from random import randint

answer = randint(1, 10)
print(answer)

while True:
    try:
        guess = int(input('guess no. from 1-10  '))
        if 0<guess<11:
            if guess==answer:
                print("genius")
                break
        else:
            print('please enter from 1-10')
    except ValueError:
        print('please enter number')
        continue
