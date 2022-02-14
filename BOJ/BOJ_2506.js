function dfs(v, chk, adj, cnt) {
    cnt[0] += 1;
    for (let next of adj[v]) {
        if (chk[next] == 0) {
            chk[next] = 1;
            dfs(next, chk, adj, cnt);
        }
    }
}

const fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');
let v = parseInt(input.shift());
let e = parseInt(input.shift());
let adj = Array.from({ length: v + 1 }, () => []);
let chk = Array.from({ length: v + 1 }, () => 0);
chk[1] = 1;
let cnt = [-1];
for (let i = 0; i < e; i++) {
    let [a, b] = input[i].split(" ").map(x => parseInt(x));
    adj[a].push(b);
    adj[b].push(a);
}
dfs(1, chk, adj, cnt);
console.log(cnt[0]);