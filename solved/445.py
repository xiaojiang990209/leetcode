class Solution:
    def addTwoNumbers(self, l1, l2):
        def build_list(stack1, stack2):
            next_node = None
            curr_node = None
            add = 0
            while len(stack1) != 0 or len(stack2) != 0:
                val1 = 0 if len(stack1) == 0 else stack1.pop()
                val2 = 0 if len(stack2) == 0 else stack2.pop()
                val = val1 + val2 + add
                curr_node = ListNode(val%10)
                add = val // 10
                curr_node.next = next_node
                next_node = curr_node
            if add != 0:
                curr_node = ListNode(add)
                curr_node.next = next_node
            return curr_node
        l1_stack, l2_stack = [], []
        temp1, temp2 = l1, l2
        while temp1 != None:
            l1_stack.append(temp1.val)
            temp1 = temp1.next
        while temp2 != None:
            l2_stack.append(temp2.val)
            temp2 = temp2.next
        return build_list(l1_stack, l2_stack)
