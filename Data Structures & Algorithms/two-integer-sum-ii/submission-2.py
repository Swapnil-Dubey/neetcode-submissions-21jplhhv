class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0 # 0
        r = len(numbers)-1 # 3

        while l<r:
            if numbers[l]+numbers[r]==target:
                return [l+1, r+1]
            else:
                if r==l+1:
                    l+=1
                    r = len(numbers)-1
                else:
                    r-=1
        return []