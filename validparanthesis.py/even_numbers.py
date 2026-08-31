class Odd:

    def even_number(self, arr):
        # len1 = []
        # for i in range(len(arr)):
        for i in arr:
            if i % 2 == 0:
                # len1.append(arr[i])
                print("even numbers", i)


odd = Odd()
arr = [2, 3, 6, 2, 12, 15, 0, 2, 2, 2, 2, 22, 22.3, 2]
odd.even_number(arr)
