#!/usr/bin/node
const iter = process.argv[2];
const size = parseInt(iter);

if (isNaN(size)) {
  console.log('Missing size');
} else if (size < 0) {
  process.exit();
} else {
  let i = 0;
  while (i < size) {
    console.log('X'.repeat(size));
    i++;
  }
}
