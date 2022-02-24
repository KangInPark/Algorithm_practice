class Queue {
    constructor(size) {
        this.arr = Array.from({ length: size });
        this.head = 0;
        this.tail = 0;
        this.size = size;
        this.len = 0;
    }
    push(n) {
        if (this.len === this.size) return -1;
        this.arr[this.tail] = n;
        this.tail = (this.tail + 1) % this.size;
        this.len++;
        return 1;
    }
    pop() {
        if (this.empty()) return -1;
        let ret = this.arr[this.head];
        this.head = (this.head + 1) % this.size;
        this.len--;
        return ret;
    }
    empty() {
        if (this.len == 0) return true;
        else return false;
    }
    clear() {
        this.arr = Array.from({ length: this.size });
        this.head = 0;
        this.tail = 0;
        this.len = 0;
    }
}