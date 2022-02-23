class Queue {
    constructor(size) {
        this.arr = Array.from({ length: size });
        this.head = 0;
        this.tail = 0;
        this.size = size;
        this.len = 0;
    }
    push(n) {
        if (this.len === this.size) return -1;
        this.arr[this.tail] = n;
        this.tail = (this.tail + 1) % this.size;
        this.len++;
        return 1;
    }
    pop() {
        if (this.empty()) return -1;
        let ret = this.arr[this.head];
        this.head = (this.head + 1) % this.size;
        this.len--;
        return ret;
    }
    empty() {
        if (this.len == 0) return true;
        else return false;
    }
    clear() {
        this.arr = Array.from({ length: this.size });
        this.head = 0;
        this.tail = 0;
        this.len = 0;
    }
}

function bfs(q, input, n, m, i, j, color) {
    let chk = Array.from({ length: n }, () => Array.from({ length: m }, () => 0));
    q.clear();
    q.push({ x: i, y: j, h: i, w: j, color: color });
    chk[i][j] = 1;
    let cnt = 0;
    while (!q.empty()) {
        curr = q.pop();
        let dx = [1, 0, -1, 0];
        let dy = [0, 1, 0, -1];
        let next = curr.color == 'W' ? 'B' : 'W';
        for (let idx = 0; idx < 4; idx++) {
            nx = dx[idx] + curr.x;
            ny = dy[idx] + curr.y;
            if (nx >= curr.h && nx < curr.h + 8 && ny >= curr.w && ny < curr.w + 8 && chk[nx][ny] == 0) {
                if (input[nx][ny] != next) cnt++;
                q.push({ x: nx, y: ny, h: curr.h, w: curr.w, color: next });
                chk[nx][ny] = 1;
            }
        }
    }
    return cnt;
}

const fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split("\n");
let [n, m] = input.shift().split(" ").map(x => parseInt(x));
let min = 100;
let q = new Queue(100);
for (let i = 0; i <= n - 8; i++) {
    for (let j = 0; j <= m - 8; j++) {
        let color = input[i][j] == 'W' ? 'B' : 'W';
        cnt = bfs(q, input, n, m, i, j, input[i][j]);
        min = min > cnt ? cnt : min;
        cnt = bfs(q, input, n, m, i, j, color) + 1;
        min = min > cnt ? cnt : min;
    }
}
console.log(min)