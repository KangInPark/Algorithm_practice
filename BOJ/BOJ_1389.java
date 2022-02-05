import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class BOJ_1389 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split(" ");
        int n = Integer.parseInt(s[0]);
        int m = Integer.parseInt(s[1]);
        int[][] arr = new int[n + 1][n + 1];
        for (int[] r : arr) {
            Arrays.fill(r, Integer.MAX_VALUE / 10);
        }
        for (int i = 1; i <= n; i++) {
            arr[i][i] = 0;
        }
        for (int i = 0; i < m; i++) {
            s = br.readLine().split(" ");
            arr[Integer.parseInt(s[0])][Integer.parseInt(s[1])] = 1;
            arr[Integer.parseInt(s[1])][Integer.parseInt(s[0])] = 1;
        }
        int d;
        for (int k = 1; k <= n; k++) {
            for (int i = 1; i <= n; i++) {
                for (int j = 1; j <= n; j++) {
                    d = arr[i][k] + arr[k][j];
                    arr[i][j] = arr[i][j] > d ? d : arr[i][j];

                }
            }
        }
        int min = Integer.MAX_VALUE;
        int ret = 0, sum;
        for (int i = 1; i <= n; i++) {
            sum = 0;
            for (int j = 1; j <= n; j++) {
                sum += arr[i][j];
            }
            if (min > sum) {
                min = sum;
                ret = i;
            }
        }
        System.out.println(ret);
    }
}