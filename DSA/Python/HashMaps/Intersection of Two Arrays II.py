class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        Map = {}
        res = []
        for i in nums1:
            if i in Map:
                Map[i] += 1
            else:
                Map[i] = 1
        for j in nums2:
            if j in Map and Map[j] > 0:
                res.append(j)
                Map[j] -= 1
        return res
    
# 1. If the Given Array is Already Sorted:

def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    nums1.sort()  # Ensure nums1 is sorted
    nums2.sort()  # Ensure nums2 is sorted
    i, j = 0, 0
    result = []

    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            result.append(nums1[i])
            i += 1
            j += 1

    return result
# 2. If nums1's Size is Small Compared to nums2's Size:
# If nums1 is significantly smaller than nums2, it would be more efficient to iterate through the smaller array and use the larger array as a hash map. This minimizes memory usage and improves performance.

def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1  # Ensure nums1 is always smaller

    count_map = {}
    result = []

    for num in nums1:
        if num in count_map:
            count_map[num] += 1
        else:
            count_map[num] = 1

    for num in nums2:
        if num in count_map and count_map[num] > 0:
            result.append(num)
            count_map[num] -= 1

    return result
# 3. If Elements of nums2 are Stored on Disk and Memory is Limited:
# If nums2 cannot be fully loaded into memory, we need to handle it in chunks. A common approach is to use a generator to process the file in chunks, leveraging efficient data streaming. Here's an example using a file for nums2:

def read_in_chunks(file_path: str, chunk_size: int = 1024):
    with open(file_path, 'r') as file:
        while True:
            data = file.read(chunk_size)
            if not data:
                break
            yield data.strip().split()

def intersect(nums1: list[int], file_path: str) -> list[int]:
    count_map = {}
    result = []

    # Count occurrences of each element in nums1
    for num in nums1:
        if num in count_map:
            count_map[num] += 1
        else:
            count_map[num] = 1

    # Process nums2 in chunks from the file
    for chunk in read_in_chunks(file_path):
        for num_str in chunk:
            num = int(num_str)
            if num in count_map and count_map[num] > 0:
                result.append(num)
                count_map[num] -= 1

    return result
# Explanation:
# Two-pointer technique: Efficiently traverses both sorted arrays with two pointers.

# Smaller array optimization: Uses the smaller array to minimize memory usage and improve performance.

# Chunk processing: Handles large datasets by processing them in manageable chunks from disk, avoiding memory overflow.