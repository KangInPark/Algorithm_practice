import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class BOJ_10816 {
    public static void main(String[] args) throws NumberFormatException, IOException {
        int[] chk = new int[20000001];
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i = 0 ; i < n ; i++ ){
            chk[Integer.parseInt(st.nextToken())+10000000] += 1;
        }
        int m = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        for(int i = 0 ; i < m ; i++ ){
            bw.write(Integer.toString(chk[Integer.parseInt(st.nextToken())+10000000]) + " ");
        }
        bw.close();
    }
}