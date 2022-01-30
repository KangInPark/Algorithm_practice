import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_2805 {
    public static long calc(int[] list, long val){
        long ret = 0;
        for (int i : list) {
            ret += (i - val)>0 ? (i - val) : 0;
        }
        return ret;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int list[] = new int[n];
        st = new StringTokenizer(br.readLine());
        int max = 0;
        for(int i = 0 ; i < n; i++){
            list[i] = Integer.parseInt(st.nextToken());
            max = max < list[i] ? list[i] : max;
        }
        long start = 0;
        long end = max - m / n;
        long ret = 0;
        while(true){
            long mid = (start + end)/ 2;
            if(calc(list,mid) > m){
                start = mid + 1;
            }
            else if(calc(list,mid) < m){
                end = mid - 1;
            }
            else{
                ret = mid;
                break;
            }
            if(start>end){
                ret = start - 1;
                break;
            }
        }
        System.out.println(ret);
    }
}
