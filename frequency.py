names = ["Login", "Payment", "Login", "Search", "Payment", "sunil", "sunil"]

frequency = {}

for name in names:
    if name in frequency:
        frequency[name] += 1
    else:
        frequency[name] = 1
print(frequency)
