import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class BOJ_2751 {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        int list[] = new int[2000001];
        for(int i = 0 ; i < n; i++){
            int tmp = Integer.parseInt(br.readLine());
            list[tmp+1000000] = 1;
        }
        for (int i=0; i<=2000000; i++){
            if(list[i] == 1) bw.write(Integer.toString(i-1000000)+"\n");
        }
        br.close();
        bw.close();
    }
}
