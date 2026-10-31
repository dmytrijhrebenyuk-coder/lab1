import math

def calculate_y(x, y_val):
    """Обчислення виразу y = (sqrt(x) + y^2) / 3."""
    if x < 0:
        raise ValueError("Значення x не може бути від'ємним (підкореневий вираз).")
    return (math.sqrt(x) + y_val ** 2) / 3