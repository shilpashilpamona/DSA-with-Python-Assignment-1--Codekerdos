class Search:

    def search_element(self, arr, target):
        for i in range(len(arr)):
            if arr[i] == target:
                print("found searched Item", arr[i])

        print("Item not found", -1)


search = Search()
arr = [3, 6, 90, 12, 15]
target = 901
search.search_element(arr, target)
