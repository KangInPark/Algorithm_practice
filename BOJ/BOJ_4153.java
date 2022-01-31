import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_4153 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] list = new int[3];
        while(true){
            StringTokenizer st = new StringTokenizer(br.readLine());
            list[0] = Integer.parseInt(st.nextToken());
            list[1] = Integer.parseInt(st.nextToken());
            list[2] = Integer.parseInt(st.nextToken());
            if(list[0] == 0 && list[1] == 0 && list[2] == 0) break;
            Arrays.sort(list);
            if(list[0]*list[0] + list[1]*list[1] == list[2]*list[2]){
                System.out.println("right");
            }
            else{
                System.out.println("wrong");
            }
        }
    }
}