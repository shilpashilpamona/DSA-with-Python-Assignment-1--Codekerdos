names = ["Login", "Payment", "Login", "Search", "Payment", "sunil", "sunil"]
count = 0
printed = set()
for dup in names:
    if names.count(dup) > 1 and dup not in printed:
        printed.add(dup)
        count = count + 1
        
print(printed)