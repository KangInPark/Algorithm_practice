import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class BOJ_10828 {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = null;
        int idx = -1;
        int[] stack = new int[10001];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            String cmd = st.nextToken();
            if (cmd.equals("push")) {
                idx += 1;
                stack[idx] = Integer.parseInt(st.nextToken());
            } else if (cmd.equals("pop")) {
                if (idx == -1) {
                    bw.write("-1\n");
                } else {
                    bw.write(stack[idx] + "\n");
                    idx -= 1;
                }
            } else if (cmd.equals("size")) {
                bw.write((idx + 1) + "\n");
            } else if (cmd.equals("empty")) {
                if (idx == -1) {
                    bw.write("1\n");
                } else {
                    bw.write("0\n");
                }
            } else {
                if (idx == -1) {
                    bw.write("-1\n");
                } else {
                    bw.write(stack[idx] + "\n");
                }
            }
        }
        bw.close();
    }

}
