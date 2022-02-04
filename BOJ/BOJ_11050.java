import java.util.Scanner;

public class BOJ_11050 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int ret = 1;
        for (int i = 0; i < k; i++) {
            ret *= (n - i);
        }
        for (int i = k; i >= 1; i--) {
            ret /= i;
        }
        System.out.println(ret);
        sc.close();
    }

}