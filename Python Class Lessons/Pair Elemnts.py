class pair_elements:
    
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def twoSum(self):
        lookup = {}

        for i, num in enumerate(self.nums):
            if self.target - num in lookup:
                return (lookup[self.target - num], i)
            lookup[num] = i

values = int(input("Enter the sum for which you want to make this search: "))
print("index1=%d, index2=%d" % pair_elements().twoSum((10, 20, 10, 40, 50, 60, 70), values))