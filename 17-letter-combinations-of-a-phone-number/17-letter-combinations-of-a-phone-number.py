class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {2:["a","b","c"],3:["d","e","f"],4:["g","h","i"],5:["j","k","l"],6:["m","n","o"],7:["p","q","r","s"],8:["t","u","v"],9:["w","x","y","z"]}
        
        output = []
        
        for digit in digits:
            if not output:
                # ['a'], ['b'], ['c']
                output = letters[int(digit)]
            else:
                mappings = []
                for o in output:
                    for l in letters[int(digit)]:
                        #['ad']
                        #['ad', 'ae']
                        #['ad', 'ae', 'af']
                        #['ad', 'ae', 'af', 'bd']
                        #['ad', 'ae', 'af', 'bd', 'be']
                        #['ad', 'ae', 'af', 'bd', 'be', 'bf']
                        #['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd']
                        #['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce']
                        #['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
                        mappings.append(o+l)
                output = mappings

        return output