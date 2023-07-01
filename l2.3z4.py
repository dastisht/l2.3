items_dict = {
    'Книга': 1,
    'Фонарик': 2,
    'Палатка': 4,
    'Спальный мешок': 3,
    'Еда': 5
}

max_weight = 10
backpack = []
total_weight = 0
for item, weight in items_dict.items():
    if total_weight + weight <= max_weight:
        backpack.append(item)
        total_weight += weight
print("Вещи, которые влезут в рюкзак:")
print(backpack)
