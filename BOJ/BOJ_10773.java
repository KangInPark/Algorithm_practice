import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class BOJ_10773 {
    public static void main(String[] args) throws NumberFormatException, IOException {
        Stack<Integer> st = new Stack<>();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            int num = Integer.parseInt(br.readLine());
            if (num != 0) {
                st.push(num);
            } else {
                st.pop();
            }
        }
        int sum = 0;
        while (!st.empty()) {
            sum += st.pop();
        }
        System.out.println(sum);
    }
}