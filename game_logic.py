def determine_winner(user, ai):
    if user == ai:
        return "Tie"
    elif (user == "rock" and ai == "scissors") or \
         (user == "paper" and ai == "rock") or \
         (user == "scissors" and ai == "paper"):
        return "You Win!"
    else:
        return "AI Wins!"

def counter_move(predicted_user_move):
    if predicted_user_move == "rock":
        return "paper"
    elif predicted_user_move == "paper":
        return "scissors"
    elif predicted_user_move == "scissors":
        return "rock"
    else:
        return "rock"
