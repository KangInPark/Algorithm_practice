import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class BOJ_10866 {
    public static class Deque {
        private int head;
        private int tail;
        private int size;
        private int num;
        private int[] arr;

        public Deque(int size) {
            this.size = size;
            this.arr = new int[size];
            this.head = 0;
            this.tail = size - 1;
            this.num = 0;
        }

        public void push_front(int x) {
            head = (head - 1 + size) % size;
            arr[head] = x;
            num += 1;
        }

        public void push_back(int x) {
            tail = (tail + 1) % size;
            arr[tail] = x;
            num += 1;
        }

        public int pop_front() {
            if (empty())
                return -1;
            int ret = arr[head];
            head = (head + 1) % size;
            num -= 1;
            return ret;
        }

        public int pop_back() {
            if (empty())
                return -1;
            int ret = arr[tail];
            tail = (tail - 1 + size) % size;
            num -= 1;
            return ret;
        }

        public int size() {
            return num;
        }

        public boolean empty() {
            if (num == 0)
                return true;
            else
                return false;
        }

        public int front() {
            if (empty())
                return -1;
            return arr[head];
        }

        public int back() {
            if (empty())
                return -1;
            return arr[tail];
        }
    }

    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = null;
        Deque deque = new Deque(n);

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            String cmd = st.nextToken();
            if (cmd.equals("push_front")) {
                deque.push_front(Integer.parseInt(st.nextToken()));
            } else if (cmd.equals("push_back")) {
                deque.push_back(Integer.parseInt(st.nextToken()));
            } else if (cmd.equals("pop_front")) {
                bw.write(deque.pop_front() + "\n");
            } else if (cmd.equals("pop_back")) {
                bw.write(deque.pop_back() + "\n");
            } else if (cmd.equals("size")) {
                bw.write(deque.size() + "\n");
            } else if (cmd.equals("empty")) {
                if (deque.empty()) {
                    bw.write("1\n");
                } else {
                    bw.write("0\n");
                }
            } else if (cmd.equals("front")) {
                bw.write(deque.front() + "\n");
            } else {
                bw.write(deque.back() + "\n");
            }
        }
        bw.close();
    }
}