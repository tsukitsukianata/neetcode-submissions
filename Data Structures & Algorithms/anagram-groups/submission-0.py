class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}

        for i in range(len(strs)):
            sorted_w = "".join(sorted(strs[i]))
            if sorted_w in seen:
                seen[sorted_w].append(strs[i])
            else:
                seen[sorted_w] = [strs[i]]

        return list(seen.values())
            
        