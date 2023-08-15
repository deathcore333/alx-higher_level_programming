#!/usr/bin/node
const txt = 'C is fun';
if (process.argv.length !== 3) {
  console.log('Missing number of occurrences');
}
for (let i = 0; i < process.argv[2]; i++) {
  console.log(txt);
}
