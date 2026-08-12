from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hash_map = defaultdict(list)
        
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            clave_conteo = tuple(count)
            hash_map[clave_conteo].append(word)
            
        return list(hash_map.values())