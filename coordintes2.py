def calculate_distance(coordinate_list, points):
    if len(coordinate_list) <= 1:
        return 0  # Порожній список або список з однією координатою

    total_distance = 0

    for i in range(len(coordinate_list) - 1):
        # Створюємо кортеж для пошуку в словнику
        point1 = [coordinate_list[i], coordinate_list[i+1]]
        point1.sort()
        point1 = tuple(point1)
        print(point1)
        
        # Додаємо відстань між точками до загальної відстані
        if point1 in points:
            total_distance += points[point1]
        else:
            # Якщо ключ не знайдений в словнику, можна обробити помилку чи обрати якусь заміну за необхідності
            print(f"Відстань для координат {point1} не знайдено у словнику!")

    return total_distance

# Приклад використання:
points = {(0, 1): 2, (0, 2): 3.8, (0, 3): 2.7, (1, 2): 2.5, (1, 3): 4.1, (2, 3): 3.9}
coordinate_list = [0, 1, 3, 2, 0]
distance = calculate_distance(coordinate_list, points)
print(f"Загальна відстань: {distance}")