class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 3,3 -> 2,2,1,1 -> 2,1,1,2 -> 1,1,2,2 -> 1,1,1,1,1,1
        # 위 순서를 봤을 때 dfs 문제임을 알 수 있음
        # left[ 3 ] (
        # left[ 2 ] ((
        # left[ 1 ] (((
        # right[ 3 ] >  left[ 0 ] ((()
        # right[ 2 ] >  left[ 0 ] ((())
        # right[ 1 ] >  left[ 0 ] ((()))
        # right[ 3 ] >  left[ 1 ] (()
        # left[ 1 ] (()(
        # right[ 2 ] >  left[ 0 ] (()()
        # right[ 1 ] >  left[ 0 ] (()())
        # right[ 2 ] >  left[ 1 ] (())
        # left[ 1 ] (())(
        # right[ 1 ] >  left[ 0 ] (())()
        # right[ 3 ] >  left[ 2 ] ()
        # left[ 2 ] ()(
        # left[ 1 ] ()((
        # right[ 2 ] >  left[ 0 ] ()(()
        # right[ 1 ] >  left[ 0 ] ()(())
        # right[ 2 ] >  left[ 1 ] ()()
        # left[ 1 ] ()()(
        # right[ 1 ] >  left[ 0 ] ()()()
        def pairsOfParentheses(s, left, right, result):
            if left:
                #print("left[",left,"]", s+"(",)
                pairsOfParentheses(s+"(", left-1, right, result)
            if right > left:
                #print("right[", right, "] > ", "left[",left,"]", s+")")
                pairsOfParentheses(s+")", left, right-1, result)
                
            if not right:
                result.append(s)
            return result
        
        return pairsOfParentheses("", n, n, [])
    
        