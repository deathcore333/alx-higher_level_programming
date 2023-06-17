#!/usr/bin/node
const inputs = process.argv.length;

if (inputs < 3) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
