import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class BOJ_7568 {
    public static class pair {
        private int x;
        private int y;

        public pair(String x, String y) {
            this.x = Integer.parseInt(x);
            this.y = Integer.parseInt(y);
        }

        public int getX() {
            return x;
        }

        public int getY() {
            return y;
        }
    }

    public static void main(String[] args) throws NumberFormatException, IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        pair[] arr = new pair[n];
        for (int i = 0; i < n; i++) {
            String[] s = br.readLine().split(" ");
            arr[i] = new pair(s[0], s[1]);
        }
        int[] chk = new int[n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i == j)
                    continue;
                if (arr[i].getX() < arr[j].getX() && arr[i].getY() < arr[j].getY())
                    chk[i] += 1;
            }
        }
        for (int i : chk) {
            bw.write(i+1+" ");                        
        }
        bw.close();
    }
}
