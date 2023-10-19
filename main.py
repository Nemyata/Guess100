import numpy as np

def score_game(random_predict) -> int:
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")

def game_core_v3(number: int = 1) -> int:

    start = 0
    end = 101
    count = 1
    while True:
        predict = (start + end) // 2
        if number == predict:
            break
        count += 1
        if number > predict:
            start = predict
        elif number < predict:
            end = predict


    return count

print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)