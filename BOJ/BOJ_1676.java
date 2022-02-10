import java.util.Scanner;

public class BOJ_1676 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        long f = 1;
        int cnt = 0;
        for (int i = 1; i <= n; i++) {
            f *= i;
            while (f % 10 == 0) {
                cnt += 1;
                f /= 10;
            }
            f %= 1000;
        }
        System.out.println(cnt);
    }
}