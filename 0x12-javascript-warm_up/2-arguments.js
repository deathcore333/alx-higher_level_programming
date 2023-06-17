#!/usr/bin/node
const inputs = process.argv.length;

if (inputs < 3) {
  console.log('No argument');
} else if (inputs === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
