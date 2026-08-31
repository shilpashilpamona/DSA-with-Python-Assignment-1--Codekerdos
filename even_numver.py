class Even:

    def occurence_target(self, arr):
        len1 = []
        for i in range(len(arr)):
            if arr[i] % 2 == 0:
                len1.append(arr[i])
        print("even numbers", len1)


odd = Even()
arr = [2, 3, 6, 2, 12, 15, 0, 2, 2, 2, 2, 22, 22.3, 2]
odd.occurence_target(arr)
