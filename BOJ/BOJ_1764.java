import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;

public class BOJ_1764 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split(" ");
        int n = Integer.parseInt(s[0]);
        int m = Integer.parseInt(s[1]);
        HashMap<String, Integer> h = new HashMap<>();
        for (int i = 0; i < n; i++) {
            h.put(br.readLine(), 1);
        }
        ArrayList<String> arr = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            String tmp = br.readLine();
            if (h.containsKey(tmp)) {
                arr.add(tmp);
            }
        }
        Collections.sort(arr);
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(arr.size() + "\n");
        for (String string : arr) {
            bw.write(string + "\n");
        }
        bw.close();
    }
}
