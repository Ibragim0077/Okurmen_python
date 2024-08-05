import random

def get_random_move():
    moves = ['камень', 'ножницы', 'бумага']
    return random.choice(moves)

def play_rock_paper_scissors():
    user_move = input("Введите свой ход (камень, ножницы или бумага): ").lower()
    while user_move not in ['камень', 'ножницы', 'бумага']:
        print("Неверный ввод. Попробуйте снова.")
        user_move = input("Введите свой ход (камень, ножницы или бумага): ").lower()

    computer_move = get_random_move()
    print(f"Кomпьютер выбрал: {computer_move}")

    if user_move == computer_move:
        print("Ничья!")
    elif (user_move == 'камень' and computer_move == 'ножницы') or \
         (user_move == 'ножницы' and computer_move == 'бумага') or \
         (user_move == 'бумага' and computer_move == 'камень'):
        print("Вы выиграли!")
    else:
[
    print(f"Your choice: {player}")
    print(f"Computer's choice: {computer}")

    result = check_winner(computer, player)

    print(result)


play()
        print("Кomпьютер выиграл!")

