import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_2579 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n + 1];
        int[] val = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            val[i] = Integer.parseInt(br.readLine());
        }
        arr[1] = val[1];
        if (n > 1)
            arr[2] = arr[1] + val[2];
        for (int i = 3; i <= n; i++) {
            arr[i] = Math.max(arr[i - 3] + val[i - 1] + val[i], arr[i - 2] + val[i]);
        }
        System.out.println(arr[n]);
    }
}