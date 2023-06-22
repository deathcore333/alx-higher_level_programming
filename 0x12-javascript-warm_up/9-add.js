#!/usr/bin/node
function add (a, b) {
  const sum = Number(a) + Number(b);
  console.log(sum);
}

const a = process.argv[2];
const b = process.argv[3];
add(a, b);
