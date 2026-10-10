class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))
            # if key not in my_dict:
            #     my_dict[key] = []
            my_dict[key].append(s)
        print(my_dict)
        return list(my_dict.values())
                    

            