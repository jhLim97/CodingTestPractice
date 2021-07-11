import java.util.*;

class Solution {
    public int solution(int n, int[][] computers) {
        int answer = 0;

        int xLength = computers.length;
        int yLength = computers[0].length;
        boolean[] visited = new boolean[xLength + 1];
        Arrays.fill(visited, false);

        Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int i = 0; i < xLength; i++) {
            for (int j = 0; j < yLength; j++) {
                if (computers[i][j] == 1) {
                    makeGraph(graph, i, j);
                }
            }
        }

        for (int i = 1; i <= xLength; i++) {
            if (!visited[i]) {
                dfs(computers, graph, visited, i);
                answer++;
            }
        }

        return answer;
    }

    private void makeGraph(Map<Integer, List<Integer>> graph, int i, int j) {
        if (graph.containsKey(i + 1)) {
            List<Integer> tempList = graph.get(i + 1);
            tempList.add(j + 1);
            graph.put(i + 1, tempList);
            return;
        }
        graph.put(i + 1, new ArrayList<>(Collections.singletonList(j + 1)));
    }

    private void dfs(int[][] computers, Map<Integer, List<Integer>> graph, boolean[] visited, int i) {
        visited[i] = true;
        for (int value : graph.get(i)) {
            if (!visited[value]) {
                dfs(computers, graph, visited, value);
            }
        }
    }
}
