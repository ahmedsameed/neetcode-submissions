class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result={}

        for st in strs:
            sortedst=''.join(sorted(st))
            if sortedst not in result:
                result[sortedst]=[]
                result[sortedst].append(st)
            else:
                result[sortedst].append(st)
        
        return list(result.values())