import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

public class BOJ_9375 {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        for (int i = 0; i < t; i++) {
            Map<String, Integer> dic = new HashMap<>();
            int n = Integer.parseInt(br.readLine());
            for (int j = 0; j < n; j++) {
                String[] input = br.readLine().split(" ");
                if (dic.get(input[1]) == null)
                    dic.put(input[1], 1);
                else {
                    dic.put(input[1], dic.get(input[1])+1);
                }
            }
            int ret = 1;
            for (String key : dic.keySet()) {
                ret *= dic.get(key) + 1;
            }
            System.out.println(ret-1);
        }
    }
}