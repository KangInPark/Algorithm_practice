class Deque {
  constructor(size) {
    this.size = size;
    this.arr = Array.from({ length: size }, () => 0);
    this.head = 0;
    this.tail = this.size - 1;
    this.num = 0;
  }
  push_front(x) {
    if (this.num === this.size) return false;
    this.head = (this.head - 1 + this.size) % this.size;
    this.arr[this.head] = x;
    this.num += 1;
  }
  push_back(x) {
    if (this.num === this.size) return false;
    this.tail = (this.tail + 1) % this.size;
    this.arr[this.tail] = x;
    this.num += 1;
  }
  pop_front() {
    if (this.empty()) return false;
    let ret = this.arr[this.head];
    this.head = (this.head + 1) % this.size;
    this.num -= 1;
    return ret;
  }
  pop_back() {
    if (this.empty()) return false;
    let ret = this.arr[this.tail];
    this.tail = (this.tail - 1 + this.size) % this.size;
    this.num -= 1;
    return ret;
  }
  size() {
    return this.num;
  }
  empty() {
    if (this.num == 0) return true;
    else return false;
  }
}
const fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");
let n = parseInt(input.shift());
for (let i = 0; i < n; i++) {
  let cmd = input[3 * i].trim();
  let size = parseInt(input[3 * i + 1]);
  let d = new Deque(size);
  let arr = input[3 * i + 2]
    .trim()
    .substring(1, input[3 * i + 2].length - 1)
    .split(",")
    .forEach((x) => d.push_back(parseInt(x)));
  let reversed = false;
  let err = false;
  for (const c of cmd) {
    if (c === "R") reversed = !reversed;
    else if (c === "D") {
      if (reversed === false) {
        tmp = d.pop_front();
        if (tmp === false) {
          err = true;
          break;
        }
      } else {
        tmp = d.pop_back();
        if (tmp === false) {
          err = true;
          break;
        }
      }
    }
  }
  let ret = "";
  if (err) {
    ret = "error";
  } else {
    if (reversed === false) {
      ret = "[";
      while (!d.empty()) {
        ret += d.pop_front() + ",";
      }
      if (ret[ret.length - 1] == ",") {
        ret = ret.substring(0, ret.length - 1) + "]";
      } else {
        ret = "[]";
      }
    } else {
      ret = "[";
      while (!d.empty()) {
        ret += d.pop_back() + ",";
      }
      if (ret[ret.length - 1] == ",") {
        ret = ret.substring(0, ret.length - 1) + "]";
      } else {
        ret = "[]";
      }
    }
  }
  console.log(ret);
}