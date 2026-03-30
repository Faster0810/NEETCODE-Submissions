class Solution:
    def topKFrequent(self, nums, k):
        
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # sort by frequency (descending)
        sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        result = []

        for i in range(k):
            result.append(sorted_items[i][0])

        return result