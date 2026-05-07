class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = 0
        index2 = len(numbers)-1 # numbers is sorted in non decreasing order #does that help us?

        while index1<index2:
            currsum = numbers[index1]+numbers[index2]
            if currsum==target:
                return [index1+1,index2+1]
            elif currsum<target:
                index1+=1
            else:
                index2-=1
        return [-1,-1]
