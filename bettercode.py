colors = ["blue", "green", "yellow", "red", "black", "white", "cyan", "magenta"]
fruits = ["apple", "lemon", "banana", "ananas", "orange"]

for color in colors:
    print(color)

for color in reversed(colors):
    print(color)

for i, color in enumerate(colors):
    print(i, '--->', color)

for color, fruit in zip(colors, fruits):
    print(color, '--->', fruit)

print('---')

for color in sorted(colors, reverse=True):
    print(color)

print('---')

print(sorted(colors, key=len))
#time -f "Memory used (kB): %\nUser time (seconds): %U" python bettercode.py