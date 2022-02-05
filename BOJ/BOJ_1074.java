import java.util.Scanner;

public class BOJ_1074 {
    public static void func(int x, int y, int n, int size, int r, int c, int[] cnt) {
        if (n == 0) {
            cnt[0] += 1;
            if (x == r && y == c)
                System.out.println(cnt[0]);
            return;
        }
        if (n > 0) {
            int tmp = size / 2;
            if (r < x + tmp && c < y + tmp) {
                func(x, y, n - 1, size / 2, r, c, cnt);
                return;
            } else
                cnt[0] += tmp * tmp;
            if (r < x + tmp && c >= y + tmp) {
                func(x, y + size / 2, n - 1, size / 2, r, c, cnt);
                return;
            } else
                cnt[0] += tmp * tmp;
            if (r >= x + tmp && c < y + tmp) {
                func(x + size / 2, y, n - 1, size / 2, r, c, cnt);
                return;
            } else {
                cnt[0] += tmp * tmp;
                func(x + size / 2, y + size / 2, n - 1, size / 2, r, c, cnt);
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int r = sc.nextInt();
        int c = sc.nextInt();
        int size = (int) Math.pow(2, n);
        int cnt[] = { -1 };
        func(0, 0, n, size, r, c, cnt);
    }
}
