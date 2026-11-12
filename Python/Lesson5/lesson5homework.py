
students = {}
n = int(input("Кількість студентів: "))

for i in range(1, n + 1):
    while True:
        try:
            score = int(input(f"Оцінка Student {i}: "))
        except ValueError:
            print("Введіть ціле число.")
            continue
        if 0 <= score <= 100:
            break
        print("Оцінка має бути від 0 до 100.")

    while True:
        status = input(f"Passed чи Failed для Student {i}: ").strip().lower()
        if status in ("passed", "failed"):
            break
        print("Введіть 'Passed' або 'Failed'.")

    students[f"Student {i}"] = (score, status == "passed")

passed = [score for score, ok in students.values() if ok]
failed = [score for score, ok in students.values() if not ok]

if not students:
    print("Немає даних про студентів.")
elif not failed:
    print("Професор Грубл був послідовним.")
    print(f"Поріг складання іспиту знаходиться в діапазоні 0 – {min(passed)} балів.")
elif not passed:
    print("Професор Грубл був послідовним.")
    print(f"Поріг складання іспиту знаходиться в діапазоні {max(failed)} – 100 балів.")
else:
    max_failed = max(failed)
    min_passed = min(passed)
    if max_failed < min_passed:
        print("Професор Грубл був послідовним.")
        print(f"Поріг складання іспиту знаходиться в діапазоні {max_failed} – {min_passed} балів.")
    else:
        print("Професор Грубл був непослідовним.")
        for name_f, (s_f, ok_f) in students.items():
            for name_p, (s_p, ok_p) in students.items():
                if not ok_f and ok_p and s_f >= s_p:
                    print(f"{name_p} має 'Passed' з оцінкою {s_p}, а "
                          f"{name_f} має 'Failed' з оцінкою {s_f}.")
                    break
            else:
                continue
            break