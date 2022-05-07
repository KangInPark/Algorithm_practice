class disjoint {
	constructor(n) {
		this.arr = Array.from({ length: n }, (v, idx) => idx);
	}
	find(x) {
		if (x == this.arr[x]) {
			return x;
		} else {
			return (this.arr[x] = this.find(this.arr[x]));
		}
	}
	union(x, y) {
		x = this.find(x);
		y = this.find(y);
		if (x != y) {
			this.arr[y] = x;
		}
	}
}

const fs = require("fs");
const { parse } = require("path");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");
let [n, m] = input
	.shift()
	.trim()
	.split(" ")
	.map((x) => parseInt(x));
dj = new disjoint(n);
end = false;
console.log(input);
for (let i = 0; i < m; i++) {
	let [a, b] = input[i]
		.trim()
		.split(" ")
		.map((x) => parseInt(x));
	if (dj.find(a) == dj.find(b)) {
		console.log(i + 1);
		end = true;
		break;
	} else {
		dj.union(a, b);
	}
}
if (!end) {
	console.log(0);
}
