import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class BOJ_10845 {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = null;
        int head = 0;
        int tail = -1;
        int[] queue = new int[10001];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            String cmd = st.nextToken();
            if (cmd.equals("push")) {
                tail += 1;
                queue[tail] = Integer.parseInt(st.nextToken());
            } else if (cmd.equals("pop")) {
                if (tail < head) {
                    bw.write("-1\n");
                } else {
                    bw.write(queue[head] + "\n");
                    head += 1;
                }
            } else if (cmd.equals("size")) {
                bw.write((tail - head + 1) + "\n");
            } else if (cmd.equals("empty")) {
                if (tail < head) {
                    bw.write("1\n");
                } else {
                    bw.write("0\n");
                }
            } else if (cmd.equals("front")) {
                if (tail < head) {
                    bw.write("-1\n");
                } else {
                    bw.write(queue[head] + "\n");
                }
            } else {
                if (tail < head) {
                    bw.write("-1\n");
                } else {
                    bw.write(queue[tail] + "\n");
                }
            }
        }
        bw.close();
    }
}