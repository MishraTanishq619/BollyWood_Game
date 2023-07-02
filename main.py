## start


import os , random


def wait():
    t=input()


def preface_statements():
    print("\t\t\t Welcome to Our Bollywood Film Name Guessing Game!!!")
    print("\n\n\n")

def exit_line():
    print("Wow Youve Done it")
    print("Press Enter to Exit ...")



def game_over_line():
    print("OOps ! You lost the game. \n")
    print("Press Enter to Exit...")


def play():
    
    fptr = open("data.txt", "r")
    l=fptr.readlines()
    
    i = random.randint(0,len(l)-1)
    while(len(l[i]) <=2):
        i = random.randint(0,len(l)-1)
    
    word = l[i]

    j = random.randint(0,len(word)-2)

    ch = [word[0],word[j],word[-2],word[(len(word)-1)//2]]

     
    life = 3   # life

    while True:
        # os.system("cls")
        op = []
        for i in range(len(word)-1):
            if word[i] in ch:
                op.append(word[i])
            elif word[i]==' ':
                op.append("_")
            else:
                op.append("-")
        print(*op)
        
        if op.count('-') > 0:
            c = input("Guess a Character: ")
            if c.upper() in word:
                ch.append(c.upper())
                print("nice Guess ...")
            else:
                life -= 1
                print("Wrong guess ... \nLife is Decreased to ",life," ... \n")
            
            if life > 0:
                print("Press Enter to continue ...")
                wait()
            else:
                game_over_line()
                wait()
                break
        else:
            exit_line()
            wait()
            break
    os.system("exit")
    
def add_movie():
    pass



if __name__ == '__main__':
    preface_statements()


    print("\t\t Choose from Following Statements : ")
    print("\n\t\t1. Play the Game.")
    print("\n\t\t2. Contribute a Movie Name.")
    choice = int(input("Type a Nummber for Your Choice: "))
    if choice==1:
        play()
    elif choice==2:
        add_movie()
    else:
        print("Wrong Option")
        # __main__()