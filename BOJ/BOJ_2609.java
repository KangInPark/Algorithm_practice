import java.util.Scanner;

public class BOJ_2609 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int p = a;
        int q = b;
        int r = p%q;
        while(r != 0){
            p = q;
            q = r;
            r = p%q;
        }
        System.out.println(q);
        System.out.println(a*b/q);
    }
}