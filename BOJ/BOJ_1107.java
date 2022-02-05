import java.util.ArrayList;
import java.util.Scanner;

public class BOJ_1107 {
    public static void combi(String s, String[] arr, ArrayList<String> l, int len) {
        if (Math.abs(s.length() - len) <= 1 && !s.equals("")) {
            l.add(s);
        }
        if (s.length() <= len) {
            for (int i = 0; i < arr.length; i++) {
                combi(s + arr[i], arr, l, len);
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
        l.clear();
        l.add("100");
        combi("", arr, l, Integer.toString(n).length());
        int min = Integer.MAX_VALUE;
        for (String s : l) {
            int tmp = Math.abs(Integer.parseInt(s) - n) + s.length();
            if (s.equals("100"))
                tmp -= 3;
            min = min > tmp ? tmp : min;
        }
        System.out.println(min);
    }
}
