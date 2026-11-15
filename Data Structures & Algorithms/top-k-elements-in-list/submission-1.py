from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent = defaultdict(int)
        for num in nums:
            frequent[num] += 1

        sorted_desc = sorted(frequent.items(), key=lambda item: item[1], reverse=True)
        return [num for num, _ in sorted_desc[:k]]
