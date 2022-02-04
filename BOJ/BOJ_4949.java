import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Stack;

public class BOJ_4949 {
    public static void main(String[] args) throws IOException {
        Stack<String> stack = new Stack<>();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        while (true) {
            String s = br.readLine();
            int chk = 1;
            stack.clear();
            if (s.equals("."))
                break;
            for (String c : s.split("")) {
                if (c.equals("[") || c.equals("(")) {
                    stack.push(c);
                } else if (c.equals(")")) {
                    if (stack.empty()) {
                        bw.write("no\n");
                        chk = 0;
                        break;
                    }
                    String tmp = stack.pop();
                    if (!tmp.equals("(")) {
                        bw.write("no\n");
                        chk = 0;
                        break;
                    }
                } else if (c.equals("]")) {
                    if (stack.empty()) {
                        bw.write("no\n");
                        chk = 0;
                        break;
                    }
                    String tmp = stack.pop();
                    if (!tmp.equals("[")) {
                        bw.write("no\n");
                        chk = 0;
                        break;
                    }
                }
            }
            if (chk == 1) {
                if (stack.empty())
                    bw.write("yes\n");
                else
                    bw.write("no\n");
            }
        }
        bw.close();
    }
}
