class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age
        print(f"The cat's name is: {self.name}")
        print(f"The cat's age is: {self.age}")


cat1 = Cat('mimi', 5)
cat2 = Cat('gabi', 7)
cat3 = Cat('biji', 9)

def find_oldest_cat(cat1, cat2, cat3):
    oldest = cat1
    if cat2.age > oldest.age:
        oldest = cat2
    if cat3.age > oldest.age:
        oldest = cat3
    return oldest

oldest_cat = find_oldest_cat(cat1, cat2, cat3)
print(f"\nThe oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")