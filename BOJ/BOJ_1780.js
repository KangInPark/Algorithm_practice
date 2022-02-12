function func(x, y, n, arr, info) {
    let chk = arr[x][y];
    for (let i = x; i < x + n; i++) {
        for (let j = y; j < y + n; j++) {
            if (arr[i][j] != chk) {
                let size = n / 3;
                func(x, y, size, arr, info);
                func(x + size, y, size, arr, info);
                func(x + 2 * size, y, size, arr, info);
                func(x, y + size, size, arr, info);
                func(x + size, y + size, size, arr, info);
                func(x + 2 * size, y + size, size, arr, info);
                func(x, y + 2 * size, size, arr, info);
                func(x + size, y + 2 * size, size, arr, info);
                func(x + 2 * size, y + 2 * size, size, arr, info);
                return;
            }
        }
    }
    if (chk == -1) info[0] += 1;
    else if (chk == 0) info[1] += 1;
    else info[2] += 1;
}

const fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split("\n");
n = parseInt(input.shift());
for (let idx in input) {
    input[idx] = input[idx].split(' ').map(x => parseInt(x));
}
let info = [0, 0, 0];
func(0, 0, n, input, info);
console.log(`${info[0]}
${info[1]}
${info[2]}`);