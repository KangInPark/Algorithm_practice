const fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');
let n = parseInt(input.shift());
input = input[0].split(" ").map(x=>parseInt(x)).sort((x,y)=>x-y);
let sum = 0;
let acc = 0;
for(let i = 0 ; i < n; i++){
    acc += input[i];
    sum += acc;
}
console.log(sum);