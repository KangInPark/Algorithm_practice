import java.util.Scanner;

public class BOJ_2798 {
    private static int max = -1;
    public static void permutation(int[] list, int cnt, int sum, int[] chk, int m){
        if(cnt == 3){
            if(sum <= m){
                max = max<sum ? sum : max;
            }
            return;
        }
        for(int i = 0 ; i < list.length; i++){
            if(chk[i] == 1)continue;
            chk[i] = 1;
            permutation(list,cnt+1, sum+list[i], chk, m);
            chk[i] = 0;
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m= sc.nextInt();
        int list[] = new int[n];
        for(int i = 0 ; i < n ; i++){
            list[i] = sc.nextInt();
        }
        permutation(list,0,0,new int[n],m);
        System.out.println(max);    
    }
}
