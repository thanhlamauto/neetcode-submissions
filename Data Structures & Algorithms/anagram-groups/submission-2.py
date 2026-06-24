class Solution:
    from collections import defaultdict
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # def check(s1, s2):
        #     count = [0] * 26
        #     if len(s1) != len(s2):
        #         return False
        #     for i in range(len(s1)):
        #         count[ord(s1[i]) - ord("a")] += 1
        #         count[ord(s2[i]) - ord("a")] -= 1
        #     for val in count:
        #         if val != 0:
        #             return False
        #     return True

        # visited = set()
        # res = []
        # for i in range(len(strs)):
        #     group = [strs[i]]
        #     if strs[i] in visited:
        #         continue
        #     for j in range(i+1, len(strs)):
        #         if check(strs[i], strs[j]) == True:
        #             group.append(strs[j])
        #             visited.add(strs[j])
        #     res.append(group)
        # return res

        str_map = defaultdict(list)
        for str_ in strs:
            count = [0] * 26
            for s in str_:
                count[ord(s) - ord("a")] += 1
            str_map[tuple(count)].append(str_)
        return list(str_map.values())



        

