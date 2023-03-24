#!/usr/bin/node
const iter = process.argv[2];
const num = parseInt(iter);

if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else if (num < 0) {
  process.exit();
} else {
  for (let i = 0; i !== num; i++) { console.log('C is fun'); }
}
