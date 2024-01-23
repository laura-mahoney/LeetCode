class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums.sort()
        arr = []

        i = 0
        while i < len(nums)-2:

            start = i + 1
            end = len(nums) - 1

            while start < end:

                sum_trip = nums[i] + nums[start] + nums[end]

                if sum_trip == 0:
                    arr.append([nums[i], nums[start], nums[end]])

                    while nums[end-1] == nums[end]:
                        end -= 1
                        if start >= end:
                            break
                    end -= 1

                    while nums[start+1] == nums[start]:
                        start += 1
                        if start >= end:
                            break
                    start += 1

                elif sum_trip > 0:
                    while nums[end-1] == nums[end]:
                        end -= 1
                        if start >= end:
                            break
                    end -= 1
                else:
                    while nums[start+1] == nums[start]:
                        start += 1
                        if start >= end:
                            break
                    start += 1

            while nums[i+1] == nums[i] and i < len(nums)-2:
                i += 1
            i += 1

        print(arr)
        return arr