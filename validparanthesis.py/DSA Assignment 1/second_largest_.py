class SortArrayCheck:

    def second_largest(self, arr):
        largest = arr[0]
        self.second_largest = arr[0]
        for i in range(len(arr)):
            arr[i] > largest
            largest = arr[i]
            self.second_largest = largest
        print(self.second_largest)


sac = SortArrayCheck()
arr = [3, 6, 12, 15, 0]

sac.second_largest(arr)
