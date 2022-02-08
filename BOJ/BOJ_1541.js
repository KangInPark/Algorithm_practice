const fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString();
let arr = [];
let prev = 0;
for (let i = 0; i < input.length; i++) {
    if (input[i] == '-' || input[i] == '+') {
        arr.push(Number(input.substring(prev, i)));
        prev = i;
    }
}
arr.push(Number(input.substring(prev, input.length)));
let chk = 0;
let sum = 0;
for (n of arr) {
    if (n >= 0) {
        if (chk == 1) sum -= n;
        else sum += n;
    }
    else {
        if (chk == 0) {
            chk = 1;
        }
        sum += n;
    }
}
console.log(sum)