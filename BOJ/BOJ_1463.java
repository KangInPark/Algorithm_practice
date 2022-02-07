import java.util.Scanner;

public class BOJ_1463 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n + 1];
        arr[1] = 0;
        int a, b, c;
        for (int i = 2; i <= n; i++) {
            a = arr[i - 1] + 1;
            if (i % 2 == 0) {
                b = arr[i / 2] + 1;
            } else {
                b = Integer.MAX_VALUE;
            }
            if (i % 3 == 0) {
                c = arr[i / 3] + 1;
            } else {
                c = Integer.MAX_VALUE;
            }
            arr[i] = a;
            if (arr[i] > b)
                arr[i] = b;
            if (arr[i] > c)
                arr[i] = c;
        }
        System.out.println(arr[n]);
    }
}