function func(x, y, size, map) {
    let chk = map[x].charAt(y);
    let is = 0;
    for (let i = x; i < x + size; i++) {
        for (let j = y; j < y + size; j++) {
            if (chk != map[i].charAt(j)) {
                is = 1;
                break;
            }
        }
        if (is == 1) break;
    }
    if (is == 0) return chk;
    let tmp = (size / 2) >> 0;
    let ret = "(";
    ret += func(x, y, tmp, map);
    ret += func(x, y + tmp, tmp, map);
    ret += func(x + tmp, y, tmp, map);
    ret += func(x + tmp, y + tmp, tmp, map);
    return ret + ")";
}

const fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');
let size = parseInt(input.shift());
console.log(func(0, 0, size, input));