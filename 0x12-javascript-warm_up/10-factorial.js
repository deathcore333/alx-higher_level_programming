#!/usr/bin/node
function factorial (num) {
  if (isNaN(num)) {
    console.log('1');
  } else {
    let factorial = 1;
    for (let i = 2; i <= num; i++) {
      factorial *= i;
    }
    return factorial;
  }
}

const numf = parseInt(process.argv[2]);

console.log(factorial(numf));
