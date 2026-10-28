from functools import cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def check(i):
            # s 배열의 길이만큼 도달했는지 확인
            if i == len(s):
                return True

            for word in wordDict: # 단어 하나 선택
                if s.startswith(word,i): # 현재 위치에서 일치하는지 확인
                    if check(i+len(word)): # 다음 위치를 확인하고 결과를 기다림
                        return True 
            return False
        
        return check(0)