import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collections;

public class BOJ_11651 {
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
        ArrayList<pair> arr = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            String[] s = br.readLine().split(" ");
            arr.add(new pair(s[0], s[1]));
        }
        Collections.sort(arr, (pair a, pair b) -> {
            if (a.getY() == b.getY()) {
                return Integer.compare(a.getX(), b.getX());
            } else {
                return Integer.compare(a.getY(), b.getY());
            }
        });
        for (pair pair : arr) {
            bw.write(Integer.toString(pair.getX()) + " " + Integer.toString(pair.getY()) + "\n");
        }
        bw.close();
    }
}