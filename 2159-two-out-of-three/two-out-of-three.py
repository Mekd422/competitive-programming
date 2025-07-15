class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        '''
            two out of three
        
        '''
        arr = []
        nums1.sort()
        nums2.sort()
        nums3.sort()
        p1, p2 = 0, 0
        while p1 < len(nums1) and p2 < len(nums2):

            if nums1[p1] == nums2[p2]:

                arr.append(nums1[p1])
                p1 += 1
                p2 += 1
            elif nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                p2 += 1
        s2, s3 = 0, 0
        while s2 < len(nums2) and s3 < len(nums3):
            if nums2[s2] == nums3[s3]:
                arr.append(nums2[s2])
                s2 += 1
                s3 += 1
            elif nums2[s2] < nums3[s3]:
                s2 += 1
            else:
                s3 += 1
        t1,t3 = 0, 0
        while t1 < len(nums1) and t3 < len(nums3):
            if nums1[t1] == nums3[t3]:
                arr.append(nums1[t1])
                t1 += 1
                t3 += 1
            elif nums1[t1] < nums3[t3]:
                t1 += 1
            else:
                t3 += 1

        return list(set(arr))