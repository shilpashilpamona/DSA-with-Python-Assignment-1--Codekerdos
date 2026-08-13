class OT:

    def occurence_target(self, arr, target):
        count = 0
        for i in range(len(arr)):
            if arr[i] == target:
                count = count + 1

        print(count)


ot = OT()
arr = [2, 3, 6, 2, 12, 15, 0, 2, 2, 2, 2, 22, 22.3, 2]
target = 2

ot.occurence_target(arr, target)
