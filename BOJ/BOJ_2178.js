const fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');
let [n, m] = input.shift().split(" ").map(x => parseInt(x));
let q = [];
let chk = Array.from({ length: n }, () => Array.from({ length: m }, () => 0));
q.push({ x: 0, y: 0, cnt: 1 });
chk[0][0] = 1;
let dx = [0, 1, 0, -1];
let dy = [1, 0, -1, 0];
while (q.length != 0) {
    let curr = q.shift();
    if (curr.x == n - 1 && curr.y == m - 1) {
        console.log(curr.cnt);
        return;
    }
    for (let i = 0; i < 4; i++) {
        let nx = dx[i] + curr.x;
        let ny = dy[i] + curr.y;
        if (nx >= 0 && ny >= 0 && nx < n && ny < m && chk[nx][ny] == 0 && input[nx].charAt(ny) == '1') {
            chk[nx][ny] = 1;
            q.push({ x: nx, y: ny, cnt: curr.cnt + 1 });
        }
    }
}