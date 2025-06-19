my_name = "Hanae"
user_name = input("What's your name? ")
if user_name.strip().lower() == my_name.lower():
    print("Wow! We have the same name! Are we long-lost twins?")
else:
    print(f"Oh no, you're {user_name}? I was hoping for another {my_name}!")