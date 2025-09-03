def maximum_subarray_sum(nums: list[int], k: int) -> int:
    """
    Finds the maximum sum of all subarrays of length k with distinct elements.

    Args:
        nums (list[int]): The input list of integers.
        k (int): The length of the subarray

    Returns:
        int: The maximum sum of a subarray of length k with all distinct elements.
             Returns 0 if no such subarray exists.

    Examples:
        >>> maximum_subarray_sum(nums=[1,5,4,2,9,9,9,1], k=3)
        15
        >>> maximum_subarray_sum(nums=[4,4,4], k=3)
        0
        >>> maximum_subarray_sum(nums=[1,1,1,7,8,9,3], k=4)
        27

    References:
        - LeetCode: https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/
    """

    n: int = len(nums)
    left: int = 0
    right: int = k - 1
    global_sum: int = 0
    st = set()
    while right < n:
        # Step 1: Loop until find the next range of distinct items
        while len(st) < k and right < n:
            st = {nums[right]}
            local_sum: int = nums[right]
            for j in range(right - 1, right - k, -1):
                if nums[j] in st:
                    left = j + 1
                    right = left + k - 1
                    break
                else:
                    st.add(nums[j])
                    local_sum += nums[j]

        if right == n:
            break

        # Step 2: Set global sum to local sum if global sum is currently smaller
        if len(st) == k:
            global_sum = max(local_sum, global_sum)

        right += 1
        if right < n:
            # Step 3: Slide the range forward one item and calculate local sum for the next range
            st.add(nums[right])
            local_sum += nums[right]
            st.remove(nums[left])
            local_sum -= nums[left]
            left += 1

    return global_sum


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
