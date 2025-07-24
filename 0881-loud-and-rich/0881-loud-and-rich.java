class Solution {
    public int[] loudAndRich(int[][] richer, int[] quiet) {
        int n = quiet.length;
        List<List<Integer>> adjList = new ArrayList<>();
        for(int i = 0; i < n; i++) {
            adjList.add(new ArrayList<>());
        }

        for(int[] edge : richer) {
            adjList.get(edge[1]).add(edge[0]); // poor -> rich
        }

        int[] dp = new int[n];
        Arrays.fill(dp, -1);
        for(int i = 0; i < n; i++) {
            dfs(i, adjList, quiet, dp);
        }

        return dp;
    }

    private int dfs(int node, List<List<Integer>> adjList, int[] quiet, int[] dp) {

        if(dp[node] != -1) return dp[node];

        int minQ = node;
        for(int neighbor : adjList.get(node)) {
            int curr = dfs(neighbor, adjList, quiet, dp);
            if(quiet[curr] < quiet[minQ]) {
                minQ = curr;
            }
        }

        return dp[node] = minQ;
    }
}