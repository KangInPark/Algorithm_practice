import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.regex.Pattern;

public class BOJ_1620 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String[] input = br.readLine().split(" ");
        int n = Integer.parseInt(input[0]);
        int m = Integer.parseInt(input[1]);
        Map<String, Integer> dic = new LinkedHashMap<>();
        String s;
        for (int i = 1; i <= n; i++) {
            s = br.readLine();
            dic.put(s, i);
        }
        String[] keys = dic.keySet().toArray(new String[0]);
        for (int i = 0; i < m; i++) {
            s = br.readLine();
            if (Pattern.matches("^[0-9]*$", s)) {
                bw.write(keys[Integer.parseInt(s) - 1] + "\n");
            } else {
                bw.write(dic.get(s) + "\n");
            }
        }
        bw.close();
    }
}