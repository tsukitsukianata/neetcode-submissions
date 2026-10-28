class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mydictS = {}
        mydictT = {}
        if (len(s) == len(t)):
            for i in range (len(s)):
                #doing for string s
                if (mydictS.get(s[i], 0) == 0):
                    mydictS[s[i]] = 1
                else:
                    mydictS[s[i]] = mydictS.get(s[i]) + 1



                #doing for string t
                if (mydictT.get(t[i], 0) == 0):
                    mydictT[t[i]] = 1
                else:
                    mydictT[t[i]] = mydictT.get(t[i]) + 1

                #comparing the two dictionaries
            return (mydictS == mydictT)
        else:
            return False

