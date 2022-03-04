const fs = require("fs");
const [n, ...arr] = fs.readFileSync("/dev/stdin").toString().trim().split(/\s/);

function test(n, arr) {
  arr.sort((a, b) => b - a);
  maxValue = arr[0];

  for (let i = maxValue; i >= 0; i -= 1) {
    let result = 0;
    for (const arr_ of arr) {
      if (arr_ >= i) {
        result += 1;
      }
      if (result >= i) {
        return i;
      }
    }
  }
}

console.log(test(n, arr));
