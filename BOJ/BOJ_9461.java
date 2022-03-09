import java.util.Scanner;

public class BOJ_9461 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        long[] arr = new long[101];
        arr[1] = 1;
        arr[2] = 1;
        arr[3] = 1;
        arr[4] = 2;
        arr[5] = 2;
        int last = 6;
        for (int i = 0; i < t; i++) {
            int n = sc.nextInt();
            if (last > n)
                System.out.println(arr[n]);
            else {
                for (int j = last; j <= n; j++) {
                    arr[j] = arr[j - 1] + arr[j - 5];
                }
                System.out.println(arr[n]);
                last = n + 1;
            }
        }
    }
}
