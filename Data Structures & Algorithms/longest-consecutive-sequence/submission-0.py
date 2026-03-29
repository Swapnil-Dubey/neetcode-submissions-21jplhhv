class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longestseq = []
        currseq = []
        sortedlist = sorted(set(nums))
        for i in range(len(sortedlist)):
            if len(currseq) == 0:
                currseq.append(sortedlist[i])
            elif sortedlist[i]-1 == currseq[-1]:
                currseq.append(sortedlist[i])
            else:
                if len(currseq)>len(longestseq):
                    longestseq = currseq.copy()
                currseq = [sortedlist[i]]
            if len(currseq)>len(longestseq):
                longestseq = currseq.copy()
        return len(longestseq)




        