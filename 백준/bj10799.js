const fs = require("fs");
const inputs =
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString().trim()
    : `()(((()())(())()))(())`;

function test(inputs) {
  result = 0;
  stack = [];
  Array.from(inputs).forEach((input, index) => {
    if (input === "(") {
      stack.push("(");
    } else {
      stack.pop();
      if (inputs[index - 1] === "(") {
        result += stack.length;
      } else {
        result += 1;
      }
    }
  });
  return result;
}

console.log(test(inputs));
