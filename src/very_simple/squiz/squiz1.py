score = 0

def answer_yes_no(ans, msg):
    if ans.lower() == msg:
        print('Верно!')
        global score
        score += 1
    else:
        print("Вы ошиблись!")

if __name__=='__main__':
    print("Добро пожаловать в программку тестов!")
    playing = input("Хотите пройти тест? (да/нет) ")

    if playing.lower() != "да":
        quit()
    print("Хорошо! Давай поиграем :)")


    print("-= Первый вопрос =-")
    print("Сколько месяцев в году?")
    print("- одиннадцать")
    print("- двенадцать")
    print("- десять")
    answer = input("Поле ввода: ")
    answer_yes_no(answer, "двенадцать")

    print("-= Второй вопрос =-")
    print("Сколько дней в неделе?")
    print("- восемь")
    print("- три")
    print("- семь")
    answer = input("Поле ввода: ")
    answer_yes_no(answer, "семь")

    print("-= Третий вопрос =-")
    print("Сколько дней в году?")
    print("- триста шестьдесят пять")
    print("- триста двенадцать")
    print("- триста девять")
    answer = input("Поле ввода: ")
    answer_yes_no(answer, "триста шестьдесят пять")

    print("-= Четвертый вопрос =-")
    print("Сколь минут в одном часе?")
    print("- шестьсот")
    print("- шестьдесят шесть")
    print("- шестьдесят")
    answer = input("Поле ввода: ")
    answer_yes_no(answer, "шестьдесят")

    print("У вас " + str(score) + " правильных ответов!")
    print("У вас " + str((score / 4) * 100) + "%.")