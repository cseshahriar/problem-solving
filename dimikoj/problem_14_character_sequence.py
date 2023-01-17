T = int(input())

for i in range(T):
    string = input()
    special_characters = input()[0]
    count = 0
    for j in string:
        if special_characters == j:
            count += 1

    print(f"Occurrence of '{special_characters}' in '{string}' = {count}")
