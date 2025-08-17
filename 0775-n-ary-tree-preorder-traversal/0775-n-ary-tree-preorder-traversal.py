class Solution(object):
    def preorder(self, root):
        output = []
        self.traverse(root, output)
        return output
    def traverse(self, root, output):
        if root is None: return
        output.append(root.val)
        for child in root.children:
            self.traverse(child, output)