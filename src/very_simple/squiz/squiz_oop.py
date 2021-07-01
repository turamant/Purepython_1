import json
import random
import sys
import time

class Timer:

    def __init__(self, limit):
        self.time_limit = limit
        self.start_time = time.time()

    @property
    def time_left(self):
        time_passed = time.time() - self.start_time
        return self.time_limit - time_passed

    @property
    def expired(self):
        return self.time_left < 0


class Question:
    all_quest = []
    all_answer = []
    def __init__(self, quest="Вопрос", answer="Ответы"):
        self.quest = quest
        self.answer = answer

    def add_quest(self):
        with open('questions/python.json') as f:
            self.questions = json.load(f)
            self.all_quest.append(self.questions)

    def shuffle(self):
        """
        Возвращает перемешанные ответы и индекс правильного ответа,
        предполагается, что первый answer(ответ) всегда правильный(0).
        """
        indices = list(range(len(self.answers)))
        random.shuffle(indices)
        correct = indices.index(0)
        answers = [answers[i] for i in indices]
        return answers, correct


    def ask_question(self):
        """
        Функция Вопрос-ответ.
        Ответ верный - return True,
        Ответ не верный - return False
        """
        print("\n\n{}\n".format(self.question["question"]))
        answers, correct = self.shuffle(self.question["answers"])
        correct = str(correct + 1)
        for i, text in enumerate(answers):
            print("[{}] {}".format(i + 1, text))
        ans = input("\nВведите номер вашего ответа: ")
        if ans == correct:
            return True
        return False


    def quiz(self):
        n_correct = 0
        for q in self.questions:
            print('-' * 79)
            print('\nОсталось времени: {:4.1f}'.format(Timer.time_left))
            if self.ask_question():
                n_correct += 1
            if Timer.expired:
                break
        return n_correct




q1 = Question()
q1.add_quest()
q1.show_all_quest()
