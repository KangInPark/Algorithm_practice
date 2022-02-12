class heap {
    constructor() {
        this.arr = [null];
    }
    push(n) {
        this.arr.push(n);
        let curr = this.arr.length - 1;
        while (curr > 1) {
            let parent = (curr / 2) >> 0;
            if (this.arr[curr] < this.arr[parent]) {
                [this.arr[curr], this.arr[parent]] = [this.arr[parent], this.arr[curr]];
                curr = (curr / 2) >> 0;
            }
            else break;
        }
    }
    pop() {
        if (this.arr.length == 1) return 0;
        const ret = this.arr[1];
        if (this.arr.length == 2) return this.arr.pop();
        this.arr[1] = this.arr.pop();
        let curr = 1;
        let target;
        while (((this.arr.length - 1) / 2) >> 0 >= curr) {
            target = curr * 2;
            if (this.arr[target] > this.arr[target + 1]) {
                target = target + 1;
            }
            if (this.arr[curr] > this.arr[target]) {
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

const fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split("\n").map(x => parseInt(x));
input.shift();
let h = new heap();
let string = "";
for (let n of input) {
    if (n == 0) {
        string += h.pop() + "\n";
    }
    else {
        h.push(n);
    }
}
console.log(string)