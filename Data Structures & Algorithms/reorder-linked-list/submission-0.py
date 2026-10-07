class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = []
        cur = head

        while cur:
            nodes.append(cur)
            cur = cur.next # 다음칸으로 이동 

        left = 0
        right = len(nodes) - 1
        
        answer = []
        while left < right:
            # 왼쪽과 오른쪽 포인터가 일치하기 전까지 진행 - 필연적으로 짝수개일 수 밖에 없다.
            answer.append(nodes[left])
            answer.append(nodes[right])
            left += 1
            right -= 1
    
        if left == right: # nodes의 개수가 홀수일 때 고려 필요
            answer.append(nodes[left])

        for i in range(len(answer) - 1):
            answer[i].next = answer[i + 1]
    
        answer[-1].next = None