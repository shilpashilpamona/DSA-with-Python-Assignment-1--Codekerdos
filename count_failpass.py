pass_count = 0
fail_count = 0

file = open("test_log.txt", "r")

for line in file:
    if "PASS" in line:
        pass_count = pass_count + 1

    if "FAIL" in line:
        fail_count = fail_count + 1

file.close()

print("Passed:", pass_count)
print("Failed:", fail_count)
