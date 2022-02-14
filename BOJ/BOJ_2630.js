function func(x, y, size, arr, cnt) {
    let chk = arr[x][y];
    let is = 0;
    for (let i = x; i < x + size; i++) {
        for (let j = y; j < y + size; j++) {
            if (arr[i][j] != chk) {
                is = 1;
                break;
            }
        }
    }
    if (is == 0) {
        cnt[chk] += 1;
        return;
    }
    let dx = [0, 0, 1, 1];
    let dy = [0, 1, 0, 1];
    let tmp = (size / 2) >> 0;
    for (let i = 0; i < 4; i++) {
        func(x + tmp * dx[i], y + tmp * dy[i], tmp, arr, cnt);
    }
}

const fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split("\n");
let size = parseInt(input.shift());
for (const idx in input) {
    input[idx] = input[idx].split(" ").map(x => parseInt(x));
}
cnt = [0, 0];
func(0, 0, size, input, cnt);
console.log(`${cnt[0]}\n${cnt[1]}`)