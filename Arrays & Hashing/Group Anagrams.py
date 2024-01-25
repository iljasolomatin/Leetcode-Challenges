from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        if len(strs) == 0:
            return [[""]]
        elif len(strs) == 1:
            return [strs]
        
        anagrams = defaultdict(list)

        for word in strs:
            sortedWord = "".join(sorted(word))
            anagrams[sortedWord].append(word)

        return anagrams.values()