import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class BOJ_2667 {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int arr[][] = new int[n][n];
        for (int i = 0; i < n; i++) {
            arr[i] = Arrays.stream(br.readLine().strip().split("")).mapToInt(Integer::parseInt).toArray();
        }
        ArrayList<Integer> ret = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (arr[i][j] == 1) {
                    ret.add(0);
                    func(arr, ret, i, j, ret.size() - 1);
                }
            }
        }
        Collections.sort(ret);
        System.out.println(ret.size());
        for (Integer integer : ret) {
            System.out.println(integer);
        }
    }

    private static void func(int[][] arr, ArrayList<Integer> ret, int x, int y, int idx) {
        arr[x][y] = 0;
        ret.set(idx, ret.get(idx) + 1);
        int dx[] = { 0, 1, 0, -1 };
        int dy[] = { 1, 0, -1, 0 };
        for (int i = 0; i < 4; i++) {
            int nx = dx[i] + x;
            int ny = dy[i] + y;
            if (nx >= 0 && ny >= 0 && nx < arr.length && ny < arr.length && arr[nx][ny] == 1) {
                func(arr, ret, nx, ny, idx);
            }
        }
    }
}