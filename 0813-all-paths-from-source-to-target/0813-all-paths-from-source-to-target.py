class Solution:
    def traverse(self, node_value, node_children, path): 
        if node_value == self.target: 
            self.valid_paths.append(path)

        for child in node_children: 
            self.traverse(child, self.graph[child], path + [child])
            

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.valid_paths = [] 
        self.graph = graph
        self.target = len(graph) - 1

        self.traverse(0, graph[0], [0])

        return self.valid_paths