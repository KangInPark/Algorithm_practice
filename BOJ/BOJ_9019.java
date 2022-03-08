import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;
import java.util.Queue;

public class BOJ_9019 {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            String[] s = br.readLine().split(" ");
            int a = Integer.parseInt(s[0]);
            int b = Integer.parseInt(s[1]);
            Queue<Integer> q = new LinkedList<>();
            q.add(a);
            Map<Integer, String> dic = new HashMap<>();
            dic.put(a, a + " S");
            String ret = "";
            boolean end = false;
            while (!q.isEmpty()) {
                int curr = q.poll();
                if (curr == b) {
                    while (true) {
                        String[] tmp = dic.get(curr).split(" ");
                        if (tmp[1].equals("0")) {
                            ret = "D" + ret;
                        } else if (tmp[1].equals("1")) {
                            ret = "S" + ret;
                        } else if (tmp[1].equals("2")) {
                            ret = "L" + ret;
                        } else if (tmp[1].equals("S")){
                            ;
                        } 
                        else {
                            ret = "R" + ret;
                        }
                        curr = Integer.parseInt(tmp[0]);
                        if (dic.get(curr).split(" ")[1].equals("S")) {
                            System.out.println(ret);
                            end = true;
                            break;
                        }
                    }
                }
                if (end == true)
                    break;
                int next[] = { (2 * curr) % 10000, (curr + 10000 - 1) % 10000, (curr % 1000) * 10 + (int) (curr / 1000),
                        (curr % 10) * 1000 + (int) (curr / 10) }; // D S L R
                for (int j = 0; j < 4; j++) {
                    if (dic.get(next[j]) == null) {
                        q.add(next[j]);
                        dic.put(next[j], curr + " " + j);
                    }
                }
            }
        }
    }
}