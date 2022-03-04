import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class BOJ_11724 {
    public static void dfs(ArrayList<ArrayList<Integer>> adj, int curr, int[] chk) {
        for (int i : adj.get(curr)) {
            if (chk[i] == 0) {
                chk[i] = 1;
                dfs(adj, i, chk);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split(" ");
        int n = Integer.parseInt(s[0]);
        int m = Integer.parseInt(s[1]);
        ArrayList<ArrayList<Integer>> adj = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            adj.add(new ArrayList<>());
        }
        for (int i = 0; i < m; i++) {
            String[] input = br.readLine().split(" ");
            int u = Integer.parseInt(input[0]);
            int v = Integer.parseInt(input[1]);
            adj.get(u).add(v);
            adj.get(v).add(u);
        }
        int[] chk = new int[n + 1];
        int ret = 0;
        for (int i = 1; i <= n; i++) {
            if (chk[i] == 0) {
                ret += 1;
                dfs(adj, i, chk);
            }
        }
        System.out.println(ret);
    }
}
