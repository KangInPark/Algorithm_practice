const fs = require('fs');
let [n, m] = fs.readFileSync('/dev/stdin').toString().split(" ").map(x => parseInt(x));
let q = [];
let chk = Array.from({ length: 200001 }, (v, idx) => 0);
q.push({ pos: n, cnt: 0 });
while (true) {
    curr = q.shift();
    if (curr.pos == m) {
        console.log(curr.cnt);
        return;
    }
    for (let next of [curr.pos - 1, curr.pos + 1, curr.pos * 2]) {
        if (chk[next] == 0 && next >= 0 && next <= 100000) {
            q.push({ pos: next, cnt: curr.cnt + 1 });
            chk[next] = 1;
        }
    }
}