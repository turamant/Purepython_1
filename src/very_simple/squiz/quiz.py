"""
Простой инструмент с коммандной строкой для проведения тестирования.
"""

import json
import random
import sys
from timer import Timer


DEFAULT_INPUT = 'questions/python.json'
TIME_LIMIT = 120


def shuffle(answers):
    """
    Возвращает перемешанные ответы и индекс правильного ответа,
    предполагается, что первый answer(ответ) всегда правильный(0).
    """
    indices = list(range(len(answers)))
    random.shuffle(indices)
    correct = indices.index(0)
    answers = [answers[i] for i in indices]
    return answers, correct


def ask_question(question):
    """
    Функция Вопрос-ответ.
    Ответ верный - return True,
    Ответ не верный - return False
    """
    print("\n\n{}\n".format(question["question"]))
    answers, correct = shuffle(question["answers"])
    correct = str(correct + 1)
    for i, text in enumerate(answers):
        print("[{}] {}".format(i+1, text))
    ans = input("\nВведите номер вашего ответа: ")
    if ans == correct:
        return True
    return False


def quiz(questions):
    """
    Подсчет правильных ответов
    """
    n_correct = 0
    timer = Timer(TIME_LIMIT)
    for q in questions:
        print('-' * 79)
        print('\nОсталось времени: {:4.1f}'.format(timer.time_left))
        if ask_question(q):
            n_correct += 1
        if timer.expired:
            break
    return n_correct


if __name__ == '__main__':
    print('-' * 79)
    if len(sys.argv) == 2:
        fn = sys.argv[1]
    else:
        fn = DEFAULT_INPUT

    with open(fn) as f:
        questions = json.load(f)
        all_question = len(questions)
        print("Добро пожаловать на тестирование!")
        print("Всего вопросов в тесте: ", all_question)
        print("На все тесты дается 120 секунд")
        n_correct = quiz(questions)
        print('\nПравильных ответов: {0} из {1}'.format(n_correct, all_question))
        print("Процент правильных: %.2f" % (n_correct/all_question*100), '%')
