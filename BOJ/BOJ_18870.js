const fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split("\n");
let n = parseInt(input.shift());
let s = input[0].split(" ").map(x => parseInt(x));
let dic = new Map();
let arr = [];
for (let i = 0; i < s.length; i++) {
    let val = s[i];
    if (dic.get(val) != undefined) {
        dic.set(val, dic.get(val) + 1);
    }
    else {
        dic.set(val, 1);
    }
    arr.push({ val: val, idx: i });
}
arr.sort((a, b) => b.val - a.val);
let chk = 0;
for (let i = 0; i < arr.length; i++) {
    if (dic.get(arr[i].val) > 1) {
        chk = dic.get(arr[i].val) - 1;
        dic.set(arr[i].val, 0);
    }
    arr[i].val = arr.length - i - 1 - chk;
    chk = chk > 0 ? chk - 1 : 0;
}
arr.sort((a,b)=>a.idx-b.idx)
let ret = "";
for(let i = 0 ; i < arr.length; i++){
    ret += arr[i].val + " ";
}
console.log(ret);

