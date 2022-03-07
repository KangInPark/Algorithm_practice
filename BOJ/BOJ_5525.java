import java.util.Scanner;

public class BOJ_5525 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        String s = sc.next();
        int idx = 0;
        int cnt = 0;
        int ret = 0;
        while (idx < s.length() - 1) {
            if (s.charAt(idx) == 'I' && s.charAt(idx + 1) == 'O') {
                cnt += 1;
                if (cnt > n) {
                    cnt -= 1;
                    ret += 1;
                }
                idx += 2;
            } else {
                if (s.charAt(idx) == 'I' && cnt == n) {
                    ret += 1;
                }
                cnt = 0;
                idx += 1;
            }
        }
        if (s.charAt(s.length() - 1) == 'I' && cnt == n)
            ret += 1;
        System.out.println(ret);
    }
}