import art
import game_data
import random
print(art.logo)
game_over=False
count=0
while not game_over:
    print("Compare A: ")
    a=random.choice(game_data.data)
    print(a["name"], "," ,a["description"],",",a["country"],"\n")
    print(art.vs)
    print("Against B: ")
    b=random.choice(game_data.data)
    print(b["name"], "," ,b["description"],",",b["country"],"\n")
    choose=input("Who has more followers? Type A or B\n")
    if (choose.upper()=="A" and a["follower_count"]>b["follower_count"]) or (choose.upper()=="B" and b["follower_count"]>a["follower_count"]):
        print("You Got It!")
        count+=1
    else:
        game_over=True
        print("You Lose!")
print("Your Score is: ", count)

