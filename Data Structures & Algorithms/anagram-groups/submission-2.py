class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()

        for text in strs:
            sortedText = "".join(sorted(list(text)))
            if sortedText in anagrams:
                anagrams[sortedText].append(text)
            else:
                anagrams[sortedText] = [text]
        
        return [val for val in anagrams.values()]