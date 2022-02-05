import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_1012 {
    public static void func(int[][] arr, int x, int y, int m, int n) {
        int[] dx = { 1, 0, -1, 0 };
        int[] dy = { 0, 1, 0, -1 };
        int nx, ny;
        arr[x][y] = 0;
        for (int i = 0; i < 4; i++) {
            nx = x + dx[i];
            ny = y + dy[i];
            if (nx >= 0 && ny >= 0 && nx < m && ny < n && arr[nx][ny] == 1) {
                func(arr, nx, ny, m, n);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        int m, n, k, cnt;
        for (int p = 0; p < t; p++) {
            String[] s = br.readLine().split(" ");
            m = Integer.parseInt(s[0]);
            n = Integer.parseInt(s[1]);
            k = Integer.parseInt(s[2]);
            cnt = 0;
            int[][] arr = new int[m][n];
            for (int j = 0; j < k; j++) {
                String[] ss = br.readLine().split(" ");
                arr[Integer.parseInt(ss[0])][Integer.parseInt(ss[1])] = 1;
            }
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    if (arr[i][j] == 1) {
                        func(arr, i, j, m, n);
                        cnt += 1;
                    }
                }
            }
            System.out.println(cnt);
        }
    }
}
