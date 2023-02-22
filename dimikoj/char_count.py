T = int(input())

for i in range(T):
    string = input()
    letter_counts = {}

    for char in string:
        if char.isalpha():
            char = char.lower()
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1

    for letter, count in letter_counts.items():
        print("%s = %d" % (letter, count))

    if i < T - 1:
        print()