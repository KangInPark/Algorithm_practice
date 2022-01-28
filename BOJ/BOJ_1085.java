import java.util.Arrays;
import java.util.Scanner;

public class BOJ_1085 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        int y = sc.nextInt();
        int w = sc.nextInt();
        int h = sc.nextInt();
        int val[] = new int[4];
        val[0] = x;
        val[1] = y;
        val[2] = w-x;
        val[3] = h-y;
        System.out.println(Arrays.stream(val).min().getAsInt());
    }
}
