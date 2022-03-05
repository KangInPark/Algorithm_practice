const fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split("\n");
let n = parseInt(input.shift());
let l = input[0].split(" ").map(x => parseInt(x));
let arr = Array.from(new Set(l));
arr.sort((a, b) => a - b);
let dic = new Map();
for (let i = 0; i < arr.length; i++) {
    dic.set(arr[i], i);
}
let ret = "";
for (const val of l) {
    ret += dic.get(val) + " ";
}
console.log(ret)