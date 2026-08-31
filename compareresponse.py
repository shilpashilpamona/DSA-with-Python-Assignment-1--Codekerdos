import requests

expected = {"status": "active", "role": "admin", "age": 30}
"""
response = requests.get(https://)
result = response.status_code
print("response code", result)
actual = result.json()
print("actual resonse", actual)"""

actual = {"status": "inactive", "role": "admin1", "age": 31}


def differnces(expected, actual):
    diff = []

    for key in expected:
        if key not in actual:
            diff.append(f"Missing Key, {key}")

        elif expected[key] != actual[key]:
            diff.append(
                f"MISMATCH at {key}: "
                f"expected={expected[key]}, "
                f"actual={actual[key]}"
            )

    return diff


diffs = differnces(expected, actual)


for d in diffs:
    print(d)  # MISMATCH at status: expected=active, actual=inactive
