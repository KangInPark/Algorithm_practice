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

const fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");
let [m, n, h] = input
	.shift()
	.split(" ")
	.map((x) => parseInt(x));
let arr = Array.from({ length: h }, (v, i) =>
	Array.from({ length: n }, (val, idx) =>
		input[n * i + idx].split(" ").map((x) => parseInt(x))
	)
);
let q = new Queue(m * n * h + 1);
for (let i = 0; i < h; i++) {
	for (let j = 0; j < n; j++) {
		for (let k = 0; k < m; k++) {
			if (arr[i][j][k] == 1) {
				q.push({ z: i, x: j, y: k, cnt: 0 });
			}
		}
	}
}
let max = 0;
while (!q.empty()) {
	let curr = q.pop();
	let dx = [1, -1, 0, 0, 0, 0];
	let dy = [0, 0, 1, -1, 0, 0];
	let dz = [0, 0, 0, 0, 1, -1];
	for (let i = 0; i < 6; i++) {
		let nx = curr.x + dx[i];
		let ny = curr.y + dy[i];
		let nz = curr.z + dz[i];
		if (
			nx >= 0 &&
			ny >= 0 &&
			nz >= 0 &&
			nx < n &&
			ny < m &&
			nz < h &&
			arr[nz][nx][ny] == 0
		) {
			arr[nz][nx][ny] = 1;
			q.push({ z: nz, x: nx, y: ny, cnt: curr.cnt + 1 });
			max = max < curr.cnt + 1 ? curr.cnt + 1 : max;
		}
	}
}
for (let i = 0; i < h; i++) {
	for (let j = 0; j < n; j++) {
		for (let k = 0; k < m; k++) {
			if (arr[i][j][k] == 0) {
				console.log(-1);
				return;
			}
		}
	}
}
console.log(max);