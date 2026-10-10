class Solution:

    def encode(self, strs: List[str]) -> str:
        single = ''
        for s in strs:
            single += f"{len(s)}|{s}"
        print(single)
        return single
    def decode(self, s: str) -> List[str]:
        arr = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '|':
                j +=1
            length = int(s[i:j])
            start = j+1
            end = start + length
            str_out = s[start : end]
            arr.append(str_out)
            i = end
        print(arr)
        return arr