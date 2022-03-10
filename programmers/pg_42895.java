import java.util.ArrayList;
import java.util.List;

class Solution {
    public int solution(int N, int number) {
        int answer = -1;
        if (number == N)
            return 1;
        List<ArrayList<Integer>> arr = new ArrayList<>();
        arr.add(new ArrayList<>());
        ArrayList<Integer> e = new ArrayList<>();
        e.add(N);
        arr.add(e);
        for (int i = 2; i <= 8; i++) {
            e = new ArrayList<>();
            int tmp = func(i, N);
            if (tmp == number)
                return i;
            e.add(tmp);
            for (int j = 1; j <= i - 1; j++) {
                for (Integer a : arr.get(j)) {
                    for (Integer b : arr.get(i - j)) {
                        e.add(a + b);
                        e.add(a - b);
                        e.add(a * b);
                        if (b != 0)
                            e.add((int) (a / b));
                    }
                }
            }
            for (Integer item : e) {
                if (item == number)
                    return i;
            }
            arr.add(e);
        }
        return answer;
    }

    public int func(int i, int n) {
        String s = "";
        for (int j = 0; j < i; j++) {
            s += "" + n;
        }
        return Integer.parseInt(s);
    }
}