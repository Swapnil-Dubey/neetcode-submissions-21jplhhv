class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)): #0,    1,2,3
            for j in range(i+1,len(numbers)): #1,     2,3
                if numbers[j]+numbers[i]==target:
                    return [i+1,j+1]
        return []