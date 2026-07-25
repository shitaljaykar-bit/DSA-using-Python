class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Ensure nums1 is the smaller array to keep binary search time complexity O(log(min(m, n)))
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        half_len = (m + n + 1) // 2

        low, high = 0, m

        while low <= high:
            i = (low + high) // 2  # Partition point in nums1
            j = half_len - i       # Corresponding partition point in nums2

            # Left and right boundary values for nums1
            nums1_left_max = float('-inf') if i == 0 else nums1[i - 1]
            nums1_right_min = float('inf') if i == m else nums1[i]

            # Left and right boundary values for nums2
            nums2_left_max = float('-inf') if j == 0 else nums2[j - 1]
            nums2_right_min = float('inf') if j == n else nums2[j]

            # Check if partition is valid
            if nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min:
                # Total length is odd
                if (m + n) % 2 == 1:
                    return float(max(nums1_left_max, nums2_left_max))
                # Total length is even
                else:
                    return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2.0

            # Partition is too far right, move left
            elif nums1_left_max > nums2_right_min:
                high = i - 1
            # Partition is too far left, move right
            else:
                low = i + 1