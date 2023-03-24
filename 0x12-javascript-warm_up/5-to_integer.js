#!/usr/bin/node

const numString = process.argv[2];
const num = parseInt(numString);
if (isNaN(numString)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + num);
}
