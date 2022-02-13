const fs = require('fs');
const internal = require('stream');
let input = fs.readFileSync('/dev/stdin').toString().split("\n");
let n = parseInt(input.shift());
let arr = [];
for (let string of input) {
    let tmp = string.split(' ').map(x => parseInt(x));
    arr.push({ s: tmp[0], e: tmp[1]});
}
arr.sort((a, b) => {
    if (a.e > b.e) return 1;
    else if (a.e < b.e) return -1;
    else {
        if (a.s > b.s) return 1;
        else if (a.s < b.s) return -1;
        else return 0;
    }
});
let start = 0;
let cnt = 0;
for(let obj of arr){
    if(obj.s >= start){
        start = obj.e;
        cnt += 1;
    }
}
console.log(cnt);