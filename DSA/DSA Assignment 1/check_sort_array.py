class SortArrayCheck:

    def sort_array_check(self, arr):
        for i in range(len(arr) - 1):
            if arr[i] >= arr[i + 1]:
                print("Array not sorted")
                return False
        print("Array sorted")
        return True


sac = SortArrayCheck()
arr = [3, 6, 12, 15, 0]

sac.sort_array_check(arr)
