sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
for s in sandwich_orders:
    if(s=="Pastrami sandwich"):
        sandwich_orders.remove(s)
print(sandwich_orders)
finished_sandwich=[]
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0) 
    finished_sandwich.append(current_sandwich)
for sandwich in finished_sandwich:
    print(f"I made your {sandwich.lower()}")