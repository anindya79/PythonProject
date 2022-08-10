import random

c_move, u_move = ("", "")
draw,win,lose,total_move = (0,0,0,0)

while True:
    u_move = input("Enter p for Paper, s for scissor, r for Rock, q for quit : ").lower().strip()
    if u_move not in ["p","s","r","q"]:
        continue

    elif u_move == "q":
        break

    else:
        c_move = random.choice(["p","s","r"])
        total_move += 1
        print(f"your move -> {u_move} and Computer {c_move}")
        if c_move == u_move:
            print("draw...!!!")
            draw+=1
        elif(u_move=="p" and c_move=="r") or (u_move=="s" and c_move=="p") or(u_move == "r" and c_move == "r"):
            print("You Win!!!!!")
            win += 1
        else:
            print("you lose")
            lose +=1
    print(f"You have {win} wins, {lose}loses, {draw} draws -> {total_move} total moves \n")
