class Solution:
    def oddEvenList(self, head):
        def move(from_n, to):
            temp = from_n.next
            from_n.next = temp.next
            temp.next = to.next
            to.next = temp
        if head == None: return head
        index, node, insert = 1, head, head
        while node.next != None:
            if index % 2 == 0:
                move(node, insert)
                insert = insert.next
                index += 1
            if node.next == None:
                break
            node = node.next
            index += 1
        return head
