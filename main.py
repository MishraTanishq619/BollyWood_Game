## start


import os , random


def wait():
    t=input()


def preface_statements():
    print("\n\n\n\t\t\t Welcome to Our Bollywood Film Name Guessing Game!!!")
    print("\n\n\n")

def choice_to_play_again():
    print("Wow Youve Done it")
    print("\nTo play again, Type  '1' ...\nTo exit , type anything else...")
    r = input("Type : ")
    return 1 if r==str(1) else 0

def exit_line():
    print("Press Enter to Exit for Sure ...")



def game_over_line():
    print("OOps ! You lost the game. \n")
    print("Press Enter to Exit...")


def play():
    
    fptr = open("data.txt", "r")
    l=fptr.readlines()
    
    i = random.randint(0,len(l)-1)
    while(len(l[i]) <=2):
        i = random.randint(0,len(l)-1)
    
    film = list(map(str,l[i].split(',')))

    film_name = film[0]
    actor_name = film[1]

    j = random.randint(0,len(film_name)-2)

    ch = [film_name[0],film_name[j],film_name[-1],film_name[(len(film_name)-1)//2]]

     
    life = 3   # life

    while True:
        os.system("clear")
        
        print("\n\n")
        print("\t\t\t\t\tActor is ",actor_name,"\n\n")

        op = []
        for i in range(len(film_name)):
            if film_name[i]==' ':
                op.append("_")
            elif film_name[i] in ch:
                op.append(film_name[i])
            else:
                op.append("-")
        
        print("\t\t\t\t\t",*op,"\n\n\n")
        
        if op.count('-') > 0:
            c = input("\t\tGuess a Character: ")
            if c.upper() in film_name:
                if c.upper() in ch:
                    print("nice Guess ...\n But That character is Already Done....")
                    life -= 1
                    print("\nLife is Decreased to ",life," ... \n")
                else:
                    ch.append(c.upper())
                    print("nice Guess ...")
            else:
                life -= 1
                print("Wrong guess ... \nLife is Decreased to ",life," ... \n")
            
            if life > 0:
                print("Press Enter to continue ...")
                print("................................................................................................................................")
                wait()
            else:
                game_over_line()
                wait()
                print("................................................................................................................................")
                break
        else:
            if choice_to_play_again():
                os.system('cls')
                play()
            exit_line()
            wait()
            print("................................................................................................................................")
            break
    os.system("exit")
    



def movie_added():
    print("\n\n\t\tThanks for Contributing this...\n\n")
    t = input("\n\n\t\t Press Enter to continue...")
    main()


def login():
    from authentication import Users
    print("For Logging in ;")
    
    uname = input("Type your Username : ")
    if not uname in Users.keys():
        i=input("Username error...,Try again...")
        login()
    passwd = input("Type your password : ")
    
    t=3
    while(t and passwd!=Users[uname][0]):   # and (uname not in Users.keys())
        t-=1
        print("Only {} tries left .".format(t))
        uname = input("Type correct Username : ")
        passwd = input("Type Correct password : ")
    
    if t:
        print("Welcome ...")
        return [uname]+Users[uname]
    else:
        print("Come After some time ...")
        return None




def add_movie():
    fptr = open("data.txt", "a")
    print("\n\n")

    film_name = input("\t\tEnter The Name of Film : ")
    actor_name = input("\t\tEnter The Name of Actor : ")
    
    fptr.write((film_name+','+actor_name).upper() + "\n")
    fptr.close()
    
    movie_added()


def main():
    os.system("clear")
    preface_statements()

    user = login()
    if user is None:
        print("Error login ...")
        exit()


    print("\t\t Choose from Following Statements : ")
    print("\n\t\t1. Play the Game.")
    print("\n\t\t2. Contribute a Movie Name.\n\n\t\t")
    choice = int(input("Type a Nummber for Your Choice: "))
    if choice==1:
        play()
    elif choice==2:
        add_movie()
    else:
        print("Wrong Option")
        main()


if __name__ == '__main__':
    main()