class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)<=len(nums2):
            A = nums1
            B = nums2
        else:
            A = nums2
            B = nums1
        

        total = len(nums1)+len(nums2)
        half = total//2


        l = 0
        r = len(A)-1

        while True:
            mid = (l+r)//2
            j = half-mid-2 #pointer for arr b

            Aleft = A[mid] if mid>=0 and mid<=len(A)-1 else float('-inf')
            Aright = A[mid+1] if mid+1>=0 and mid+1<=len(A)-1 else float('inf')

            Bleft = B[j] if j>=0 and j<=len(B)-1 else float('-inf')
            Bright = B[j+1] if j+1>=0 and j+1<=len(B)-1 else float('inf')


            if Aleft<=Bright and Bleft<=Aright:
                #odd length case
                if total%2==1:
                    return min(Aright,Bright)
 

                #even length case
                else:
                    return (max(Aleft,Bleft)+min(Aright,Bright))/2
            elif Aleft>Bright:
                r = mid-1
            else:
                l = mid+1




