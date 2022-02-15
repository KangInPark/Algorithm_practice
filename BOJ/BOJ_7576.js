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
}

const fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split("\n");
let [m, n] = input.shift().split(" ").map(x => parseInt(x));
for (let i = 0; i < n; i++) {
    input[i] = input[i].split(" ").map(x => parseInt(x));
}
let q = new Queue(m * n + 1);
let chk = Array.from({ length: n }, () => Array.from({ length: m }, () => 0));
for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
        if (input[i][j] === 1) {
            q.push({ x: i, y: j, cnt: 0 });
            chk[i][j] = 1;
        }
    }
}
if (q.length === n * m) {
    console.log("0");
    return;
}
let max = -1;
while (!q.empty()) {
    curr = q.pop();
    input[curr.x][curr.y] = 1;
    if (max < curr.cnt) max = curr.cnt;
    let dx = [0, 1, 0, -1];
    let dy = [-1, 0, 1, 0];
    for (let i = 0; i < 4; i++) {
        let nx = dx[i] + curr.x;
        let ny = dy[i] + curr.y;
        if (nx >= 0 && ny >= 0 && nx < n && ny < m && chk[nx][ny] === 0 && input[nx][ny] === 0) {
            q.push({ x: nx, y: ny, cnt: curr.cnt + 1 });
            chk[nx][ny] = 1;
        }
    }
}
for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
        if (input[i][j] === 0) {
            console.log("-1");
            return;
        }
    }
}
console.log(max);