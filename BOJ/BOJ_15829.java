import java.util.Scanner;

public class BOJ_15829 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine());
        char[] s = sc.nextLine().toCharArray();
        long sum = 0;
        long pow = 1;
        int m = 1234567891;
        for (int i = 0; i < n; i++) {
            sum += (s[i] - 'a' + 1) * pow;
            sum %= m;
            pow *= 31;
            pow %= m;
        }
        System.out.println(sum);
    }
}