class Solution:
    def removeNodes(self, head: ListNode) -> ListNode:
        if not head.next:
            return head
        
        prev_node = head
        current_node = head.next

        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        
        head.next = None
        head = prev_node

        prev_node = head
        current_node = head.next
        while current_node:
            if current_node.val < prev_node.val:
                current_node = current_node.next
            else:
                next_node = current_node.next
                current_node.next = prev_node
                prev_node = current_node
                current_node = next_node
        
        head.next = None
        head = prev_node
        return head