class Solution:
    def numComponents(self, head, G):
        g = set()
        for e in G:
            g.add(e)
        prev = None
        curr = head
        num = 0
        while curr != None:
            if prev == None:
                continue
            if prev.val in g and curr.val in g:
                num += 1
            prev = curr
            curr = curr.next
        return num

