class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        i = 0
        j = 0

        # 같은 길이의 영역까지 돌림
        while i < len(word1) and j < len(word2):
            result.append(word1[i])
            result.append(word2[j])
            i += 1
            j += 1
            
        # word1의 길이가 더 긴 경우
        while i < len(word1):
            result.append(word1[i])
            i += 1

        # word2의 길이가 더 긴 경우
        while j < len(word2):
            result.append(word2[j])
            j += 1

        return "".join(result)