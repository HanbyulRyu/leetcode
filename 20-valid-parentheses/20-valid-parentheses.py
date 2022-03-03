class Solution:
    def isValid(self, s: str) -> bool:
        brakets = []

        for i in range(len(s)):
            if s[i] in {"[","{","("}:
                brakets.append(s[i])
            elif len(brakets) > 0 and s[i] in {"]","}",")"}:
                if s[i] == "]" and brakets[-1] == "[":
                    brakets.pop()
                    continue
                elif s[i] == "}" and brakets[-1] == "{":
                    brakets.pop()
                    continue
                elif s[i] == ")" and brakets[-1] == "(":
                    brakets.pop()
                    continue
                else:
                    break
            else:
                brakets.append(s[i])
                
        return bool(len(brakets) == 0)

                