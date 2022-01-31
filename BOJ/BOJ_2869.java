import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_2869 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String l[] = br.readLine().split(" ");
        int[] list = new int[3];
        for(int i = 0 ; i < 3; i++){
            list[i] = Integer.parseInt(l[i]);
        }
        int ret = 1;
        ret += (int)Math.ceil((double)(list[2]-list[0])/(list[0]-list[1]));
        System.out.println(ret);
    }
}