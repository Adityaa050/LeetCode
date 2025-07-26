
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string."""
        if not root:
            return ""
        
        queue = deque([root])
        serialized = []
        
        while queue:
            node = queue.popleft()
            if node:
                serialized.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                serialized.append("#")
        
        return ",".join(serialized)

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        if not data:
            return None
            
        nodes = data.split(',')
        root = TreeNode(int(nodes[0]))
        queue = deque([root])
        index = 1
        
        while queue and index < len(nodes):
            node = queue.popleft()
            
            # Process left child
            if nodes[index] != "#":
                node.left = TreeNode(int(nodes[index]))
                queue.append(node.left)
            index += 1
            
            # Process right child
            if index < len(nodes) and nodes[index] != "#":
                node.right = TreeNode(int(nodes[index]))
                queue.append(node.right)
            index += 1
        
        return root