import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class BOJ_11650 {
    public static class pair implements Comparable<pair> {
        private int x;
        private int y;

        public pair(int x, int y) {
            this.x = x;
            this.y = y;
        }

        public int getX() {
            return x;
        }

        public int getY() {
            return y;
        }

        @Override
        public int compareTo(pair o) {
            if (this.x > o.getX())
                return 1;
            else if (this.x < o.getX())
                return -1;
            else {
                if (this.y > o.getY())
                    return 1;
                else if (this.y < o.getY())
                    return -1;
                else
                    return 0;
            }
        }
    }

    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = null;
        ArrayList<pair> list = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            list.add(new pair(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())));
        }
        Collections.sort(list);
        for (pair pair : list) {
            bw.write(String.format("%d %d\n", pair.getX(), pair.getY()));
        }
        bw.close();
    }

}