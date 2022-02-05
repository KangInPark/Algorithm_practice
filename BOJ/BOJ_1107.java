import java.util.ArrayList;
import java.util.Scanner;

public class BOJ_1107 {
    public static void combi(String s, String[] arr, int len, int[] min, int n) {
        if (Math.abs(s.length() - len) <= 1 && !s.equals("")) {
            int tmp = Math.abs(Integer.parseInt(s) - n) + s.length();
            min[0] = min[0] > tmp ? tmp : min[0];
        }
        if (s.length() <= len) {
            for (int i = 0; i < arr.length; i++) {
                combi(s + arr[i], arr, len, min, n);
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        ArrayList<String> l = new ArrayList<>();
        for (int i = 0; i < 10; i++) {
            l.add(Integer.toString(i));
        }
        for (int i = 0; i < m; i++) {
            l.remove(sc.next());
        }
        String[] arr = l.toArray(new String[0]);
        int[] min = { Math.abs(100 - n) };
        combi("", arr, Integer.toString(n).length(), min, n);
        System.out.println(min[0]);
    }
}