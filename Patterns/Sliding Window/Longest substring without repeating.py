class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charmap = {}
        longestsublen = 0
        start = 0

        for end in range(len(s)):
            c = s[end]

            if not charmap[c]:
                charmap[c] = True
                longestsublen = max(longestsublen,end-start+1)

            else:
                while(charmap[c]):
                    charmap[s[start]] = False
                    start+=1

                charmap[c] = True


        return longestsublen
