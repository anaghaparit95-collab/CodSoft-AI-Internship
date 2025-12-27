print("Simple Recommendation System")

items = {
    "mobile": ["iPhone", "Samsung", "OnePlus"],
    "laptop": ["Dell", "HP", "Lenovo"],
    "earphones": ["Boat", "JBL", "Sony"]
}

print("Available categories:")
for category in items:
    print("-", category)

choice = input("Enter category: ").lower()

if choice in items:
    print("\nRecommended items:")
    for item in items[choice]:
        print("-", item)
else:
    print("Category not found.")
