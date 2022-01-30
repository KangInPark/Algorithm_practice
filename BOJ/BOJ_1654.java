import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_1654 {
    public static long calc(int[] list, long val){
        long tmp = 0;
        for(int i: list){
            tmp += i / val;
        }
        return tmp;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tk = new StringTokenizer(br.readLine());
        int k =Integer.parseInt(tk.nextToken());
        int n =Integer.parseInt(tk.nextToken());
        int list[] = new int[k];
        long sum = 0;
        for(int i = 0 ; i < k ; i++){
            list[i] = Integer.parseInt(br.readLine());
            sum += list[i];
        }
        long ret = sum / n;
        int rank = 1;
        while(true){
            long tmp = calc(list,ret);
            if(tmp >= n) break;
            ret -= rank;
            rank += 1;
        }
        long ans = ret;
        for(long i = ret + 1; i<= ret + rank; i++){
            if(calc(list,i) >= n){
                ans = i;
            }
        }
        System.out.println(ans);
    }
}
