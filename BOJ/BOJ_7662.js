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
        if (this.arr.length == 1) return null;
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
const fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');
let T = parseInt(input.shift());
let idx = 0;
for (let t = 0; t < T; t++) {
    let K = parseInt(input[idx++]);
    let minh = new PriorityQueue();
    let maxh = new PriorityQueue((x, y) => {
        if (x < y) return 1;
        else if (x > y) return -1;
        else return 0;
    });
    let dic = new Map();
    for (let k = 0; k < K; k++) {
        let cmd = input[idx++].split(" ");
        cmd[1] = parseInt(cmd[1]);
        if (cmd[0] === "I") {
            maxh.push(cmd[1]);
            minh.push(cmd[1]);
            if (dic.has(cmd[1])) dic.set(cmd[1], dic.get(cmd[1]) + 1);
            else dic.set(cmd[1], 1);
        }
        else {
            if (cmd[1] == 1) {
                while (1) {
                    let tmp = maxh.pop();
                    if (tmp === null) break;
                    if (dic.get(tmp) > 0) {
                        dic.set(tmp, dic.get(tmp) - 1);
                        break;
                    }
                }
            }
            else {
                while (1) {
                    let tmp = minh.pop();
                    if (tmp === null) break;
                    if (dic.get(tmp) > 0) {
                        dic.set(tmp, dic.get(tmp) - 1);
                        break;
                    }
                }
            }
        }
    }
    let s = "";
    while (1) {
        let tmp = maxh.pop();
        if (tmp === null) {
            s += "EMPTY";
            break;
        }
        if (dic.get(tmp) > 0) {
            s += tmp.toString() + " ";
            break;
        }
    }
    while (1) {
        let tmp = minh.pop();
        if (tmp === null) {
            break;
        }
        if (dic.get(tmp) > 0) {
            s += tmp.toString();
            break;
        }
    }
    console.log(s);
}