from typing import List

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index_map = {}
        for i, restaurant in enumerate(list1):
            index_map[restaurant] = i
        
        min_index_sum = float('inf')
        result = []
        
        for j, restaurant in enumerate(list2):
            if restaurant in index_map:
                index_sum = index_map[restaurant] + j
                
                if index_sum < min_index_sum:
                    min_index_sum = index_sum
                    result = [restaurant]
                elif index_sum == min_index_sum:
                    result.append(restaurant)
        
        return result
