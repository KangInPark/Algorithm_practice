import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_10026 {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        char[][] s1 = new char[n][n];
        char[][] s2 = new char[n][n];
        for (int i = 0; i < n; i++) {
            s1[i] = br.readLine().strip().toCharArray();
            s2[i] = s1[i].clone();
        }
        int cnt1 = 0;
        int cnt2 = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (s1[i][j] != '0') {
                    func(s1, i, j, s1[i][j], 0);
                    cnt1 += 1;
                }
                if (s2[i][j] != '0') {
                    func(s2, i, j, s2[i][j], 1);
                    cnt2 += 1;
                }
            }
        }
        System.out.println(cnt1 + " " + cnt2);
    }

    private static void func(char[][] s, int x, int y, char c, int mod) {
        s[x][y] = '0';
        int dx[] = { 1, 0, -1, 0 };
        int dy[] = { 0, 1, 0, -1 };
        for (int i = 0; i < 4; i++) {
            int nx = dx[i] + x;
            int ny = dy[i] + y;
            if (nx >= 0 && ny >= 0 && nx < s.length && ny < s.length && s[nx][ny] != '0') {
                if (s[nx][ny] == c) {
                    func(s, nx, ny, c, mod);
                } else if (mod == 1) {
                    if (c == 'R' || c == 'G') {
                        if (s[nx][ny] == 'R' || s[nx][ny] == 'G') {
                            func(s, nx, ny, c, mod);
                        }
                    }
                }
            }
        }
    }
}