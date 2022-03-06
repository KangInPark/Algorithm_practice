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
  front() {
    if (this.empty()) return false;
    return this.arr[this.head];
  }
  back() {
    if (this.empty()) return false;
    return this.arr[this.tail];
  }
  toString() {
    let ret = "";
    let i = this.head;
    while (true) {
      ret += this.arr[i] + " ";
      i = (i + 1) % this.size;
      if (i === this.head) break;
    }
    return ret;
  }
}
