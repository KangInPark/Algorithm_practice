import java.util.Scanner;

public class BOJ_1436 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        long i = 0;
        int cnt = 0;
        while (true){
            i += 1;
            if (Long.toString(i).contains("666")){
                cnt += 1;
                if (cnt == n) {
                    System.out.println(i);
                    return;
                }
            }
        }
    }
}