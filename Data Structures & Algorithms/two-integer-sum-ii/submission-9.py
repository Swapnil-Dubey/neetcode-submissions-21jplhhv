class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #input = int [] numbers sorted asc
        #output = int [i1,i2] 1 based

        l = 0
        r = len(numbers)-1

        while l<r: #becuse index1<index2
            curr = numbers[l]+numbers[r]
            if curr==target:
                return [l+1,r+1]
            elif curr<target:
                l+=1
            else:
                r-=1
        return False   