class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for word in strs:
            s += str(len(word)) + '#' + word
        return s

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            
            # find '#'
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            i = j + 1
            
            word = s[i:i + length]
            res.append(word)
            
            i = i + length
        
        return res