import java.util.Scanner;

public class BOJ_2231 {
    public static int calc(int n){
        int sum = n;
        while(n > 0){
            sum += n%10;
            n/=10;
        }
        return sum;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for(int i = 1; i < n; i++){
            if(calc(i) == n){
                System.out.println(i);
                return;
            }
        }
        System.out.println('0');
        return;
    }
}
