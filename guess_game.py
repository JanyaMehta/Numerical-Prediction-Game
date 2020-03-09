from random import randint

answer = randint(1, 10)
i=1
while i<=3:
    try:
        guess = int(input('guess no. from 1-10  '))
        if 0<guess<11:
            if guess==answer:
                print("genius")
                break
            elif guess>answer:
                if (i == 3):
                    print('''It's OK!! 
                        Try Again..''')
                    break
                else:
                    print("number is less than this")
            else:
                 if(i==3):
                    print('''It's OK!! 
Try Again..''')
                    break
                else:
                    print("number is more than this")
 
                
               
        else:
            print('please enter from 1-10')
    except ValueError:
        print('please enter number')
        continue
    i=i+1
    
