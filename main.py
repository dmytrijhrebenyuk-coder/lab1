import module_expr
import module_runner

def main():
    while True:
        print("\n=== ГОЛОВНЕ МЕНЮ ===")
        print("1 — Обчислити значення виразу y = (sqrt(x) + y^2) / 3")
        print("2 — Задача про спортсмена (дистанція 50 км)")
        print("0 — Вихід")

        choice = input("Оберіть дію (0-2): ").strip()

        if choice == "1":
            try:
                x = float(input("Введіть значення x (x >= 0): "))
                y_val = float(input("Введіть значення y: "))
                res = module_expr.calculate_y(x, y_val)
                print(f"Результат: y = {res:.4f}")
            except ValueError as e:
                print(f"Помилка введення: {e}")

        elif choice == "2":
            days_tot, tot_km, days_sng, sng_km = module_runner.calculate_days()
            print(f"• Сумарно спортсмен подолає 50 км за {days_tot} дн. (загалом пробіжить {tot_km} км).")
            print(f"• За один день спортсмен пробігатиме понад 50 км на {days_sng}-й день ({sng_km} км).")

        elif choice == "0":
            print("Роботу програми завершено.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()