class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        visited = set()
        for i in range(len(strs)):
            if i in visited:
                continue

            toAppend = []
            countString = Counter(strs[i])

            for j in range(i, len(strs)):
                if j not in visited and Counter(strs[j]) == countString:
                    toAppend.append(strs[j])
                    visited.add(j)
            
            res.append(toAppend)

        return res