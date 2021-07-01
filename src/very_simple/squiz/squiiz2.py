question = {"quest1": "Сколько в году месяцев",
            "answer1": {"ans1": "один",
                        "ans2": "двенадцать",
                        "ans3": "десять",
                        },
            "quest2": "Сколько дней в году",
            "answer2": {"ans1": "365",
                        "ans2": "289",
                        "ans3": "500",
                        },
            }


print(question["quest1"]+" ? ")
for _, v in question["answer1"].items():
    print("- " + v)

inter = str(input("Поле ввода: "))
if inter == "один":
    print("Верно")
else:
    print("Error")