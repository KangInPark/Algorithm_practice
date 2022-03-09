import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashMap;
import java.util.Map;

public class BOJ_17219 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String[] s = br.readLine().split(" ");
        int n = Integer.parseInt(s[0]);
        int m = Integer.parseInt(s[1]);
        Map<String, String> dic = new HashMap<>();
        for (int i = 0; i < n; i++) {
            s = br.readLine().split(" ");
            dic.put(s[0], s[1]);
        }
        for (int i = 0; i < m; i++) {
            String in = br.readLine();
            bw.write(dic.get(in) + "\n");
        }
        bw.flush();
        br.close();
        bw.close();
    }
}
