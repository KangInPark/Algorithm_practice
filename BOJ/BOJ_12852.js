const fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString();
let n = parseInt(input);
let arr = Array.from({ length: n + 1 }, () => {
	return { val: Number.MAX_SAFE_INTEGER, idx: 0 };
});
arr[1].val = 0;
arr[1].idx = 1;
for (let i = 2; i <= n; i++) {
	arr[i].val = arr[i - 1].val + 1;
	arr[i].idx = i - 1;
	if (i % 2 == 0) {
		if (arr[i].val > arr[i / 2].val) {
			arr[i].val = arr[i / 2].val + 1;
			arr[i].idx = i / 2;
		}
	}
	if (i % 3 == 0) {
		if (arr[i].val > arr[i / 3].val) {
			arr[i].val = arr[i / 3].val + 1;
			arr[i].idx = i / 3;
		}
	}
}
console.log(arr[n].val);
curr = n;
let s = "";
while (curr != 1) {
	s += curr + " ";
	curr = arr[curr].idx;
}
s += "1";
console.log(s);
