import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_18111 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split(" ");
        int n = Integer.parseInt(s[0]);
        int m = Integer.parseInt(s[1]);
        int b = Integer.parseInt(s[2]);
        int[][] arr = new int[n][m];
        int min = 260;
        int max = -1;
        int anst = Integer.MAX_VALUE;
        int ansh = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            s = br.readLine().split(" ");
            for (int j = 0; j < m; j++) {
                arr[i][j] = Integer.parseInt(s[j]);
                min = min > arr[i][j] ? arr[i][j] : min;
                max = max < arr[i][j] ? arr[i][j] : max;
            }
        }
        for (int i = max; i >= min; i--) {
            int sum = 0;
            int time = 0;
            for (int[] is : arr) {
                for (int a : is) {
                    sum += a - i;
                    if (a - i > 0)
                        time += 2 * Math.abs(a - i);
                    else if (a - i < 0)
                        time += Math.abs(a - i);
                }
            }
            if (sum + b >= 0) {
                if (anst > time) {
                    anst = time;
                    ansh = i;
                } else if (anst == time) {
                    if (ansh < i) {
                        ansh = i;
                    }
                }
            }
        }
        System.out.println(String.format("%d %d", anst, ansh));
    }
}