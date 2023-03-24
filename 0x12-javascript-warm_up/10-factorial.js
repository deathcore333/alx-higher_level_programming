#!/usr/bin/node
const num = parseInt(process.argv[2]);

if (isNaN(num)) {
  console.log('1');
} else {
  let factorial = 1;
  for (let i = 2; i <= num; i++) {
    factorial *= i;
  }
  console.log(factorial);
}
