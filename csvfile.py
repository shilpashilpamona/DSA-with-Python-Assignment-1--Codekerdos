import csv

file = open("test_log.csv", "r")

reader = csv.DictReader(file)
fail_count = 0
for row in reader:
    if row["Status"] == "FAIL":
        fail_count = fail_count + 1
    print("failed count", fail_count + 1)
file.close()
