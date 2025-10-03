const input = "SUM &0 2 2";

function tokenize(str: string) {
  return input.trim().split("\n").map(i => i.split(" ")).filter(i => i !== "")
}

console.log(tokenize(input));
