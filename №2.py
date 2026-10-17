#Функция проверяет, вошел ли ученик в тройку лидеров.
def check_winners():
    # Запрашивает список баллов всех участников.
    scores = set([int(x) for x in input("Введите баллы всех участников через пробел.").split()])

    # Требует ввести баллы ученика, которого нужно проверить.
    student_score = int(input("Введите баллы конкретного ученика."))

    #Сортируем список по возрастанию.
    sorted_scores = sorted(scores)

    #Проверяем вошел ли ученик в тройку лидеров.
    if student_score == sorted_scores[-1] or student_score == sorted_scores[-2] or student_score == sorted_scores[-3]:
        print("Вы в тройке победителей!")
    else:
        print("Вы не попали в тройку победителей.")

check_winners()