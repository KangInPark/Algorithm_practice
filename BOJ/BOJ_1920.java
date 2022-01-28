import java.util.Arrays;
import java.util.Scanner;

public class BOJ_1920 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int list[] = new int[n];
        for(int i = 0 ; i < n ; i++){
            list[i] = sc.nextInt();
        }
        Arrays.sort(list);
        int m = sc.nextInt();
        for(int i = 0; i < m ; i++){
            int tmp = sc.nextInt();
            if(Arrays.binarySearch(list, tmp) >= 0){
                System.out.println("1");
            }
            else{
                System.out.println("0");
            } 
        }
    }
}