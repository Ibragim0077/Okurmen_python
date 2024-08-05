"""
["rock", "paper", "scissors"]
["таш", "кагаз", "кайчы"]

Enter a choice (rock, paper, scissors):
Тандоо киргизиңиз (таш, кагаз, кайчы):

Invalid choice. Please try again.
Туура эмес тандоо. Сураныч, кайра аракет кылыңыз.

Your choice:
Сиздин тандоонуз:

Computer's choice:
Компьютердин тандоосу:
"""


def get_computer_choice():
    import random
    return random.choice(['таш', 'кагаз', 'кайчы'])



def get_player_input():
    data = input("Enter a choice (rock, paper, scissors): ").lower()
    if data not in ["таш", "кагаз", "кайчы"]:
        print("Invalid choice. Please try again.")
        return get_player_input()
    return data


def check_winner(computer, player):
    if computer == player:
        print("тен чыгуу!")
    elif (computer == 'таш' and player == 'кайчы') or \
         (computer == 'кагаз' and player == 'таш') or \
         (computer == 'кайчы' and player == 'кагаз'):
        print("компютер женди!")

    return "сен жендин"


def play():
    computer = get_computer_choice()
    player = get_player_input()

    print(f"Your choice: {player}")
    print(f"Computer's choice: {computer}")

    result = check_winner(computer, player)

    print(result)


play()
