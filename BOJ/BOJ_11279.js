class PriorityQueue {
    constructor(compare) {
        this.arr = [null];
        if (compare == undefined) {
            compare = (x, y) => {
                if (x > y) return 1;
                else if (x < y) return -1;
                else return 0;
            };
        }
        this.compare = compare;
    }
    push(n) {
        this.arr.push(n);
        let curr = this.arr.length - 1;
        while (curr > 1) {
            let parent = (curr / 2) >> 0;
            if (this.compare(this.arr[curr], this.arr[parent]) < 0) {
                [this.arr[curr], this.arr[parent]] = [this.arr[parent], this.arr[curr]];
                curr = (curr / 2) >> 0;
            }
            else break;
        }
    }
    pop() {
        if (this.arr.length == 1) return -1;
        const ret = this.arr[1];
        if (this.arr.length == 2) return this.arr.pop();
        this.arr[1] = this.arr.pop();
        let curr = 1;
        let target;
        while (((this.arr.length - 1) / 2) >> 0 >= curr) {
            target = curr * 2;
            if (this.compare(this.arr[target], this.arr[target + 1]) > 0) {
                target = target + 1;
            }
            if (this.compare(this.arr[curr], this.arr[target]) > 0) {
                [this.arr[curr], this.arr[target]] = [this.arr[target], this.arr[curr]];
                curr = target;
            }
            else {
                break;
            }
        }
        return ret;
    }
}

let h = new PriorityQueue((x, y) => {
    if (x < y) return 1;
    else if (x > y) return -1;
    else return 0;
});
const fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');
let n = parseInt(input.shift());
let ret = "";
for (let i = 0; i < n; i++) {
    let cmd = input[i].trim();
    if (cmd == '0') {
        let val = h.pop();
        if (val == -1) ret += "0\n";
        else ret += val + "\n";
    }
    else {
        h.push(parseInt(cmd));
    }
}
console.log(ret);