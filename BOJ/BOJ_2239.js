function func(arr, end, chk) {
	for (let i = 0; i < 9; i++) {
		for (let j = 0; j < 9; j++) {
			if (arr[i][j] == 0) {
				for (let k = 1; k <= 9; k++) {
					if (end[0]) {
						if (
							chk[0][i][k] == 0 &&
							chk[1][j][k] == 0 &&
							chk[2][parseInt(i / 3) * 3 + parseInt(j / 3)][k] == 0
						) {
							chk[0][i][k] = 1;
							chk[1][j][k] = 1;
							chk[2][parseInt(i / 3) * 3 + parseInt(j / 3)][k] = 1;
							arr[i][j] = k;
							func(arr, end, chk);
							chk[0][i][k] = 0;
							chk[1][j][k] = 0;
							chk[2][parseInt(i / 3) * 3 + parseInt(j / 3)][k] = 0;
							arr[i][j] = 0;
						}
					}
				}
				return;
			}
		}
	}
	arr.map((x) => {
		console.log(x.join(""));
	});
	end[0] = false;
	return;
}
const fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");
input = input.map((x) =>
	x
		.trim()
		.split("")
		.map((x) => parseInt(x))
);
end = [true];
let chk = Array.from({ length: 3 }, () =>
	Array.from({ length: 9 }, () => Array.from({ length: 10 }, () => 0))
);
input.forEach((x, i) =>
	x.forEach((val, j) => {
		chk[0][i][val] = 1;
		chk[1][j][val] = 1;
		chk[2][parseInt(i / 3) * 3 + parseInt(j / 3)][val] = 1;
	})
);
func(input, end, chk);
