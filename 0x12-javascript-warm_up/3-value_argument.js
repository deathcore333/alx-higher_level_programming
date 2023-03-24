#!/usr/bin/node
const [,, arg] = process.argv;

if (arg) {
  console.log(arg);
} else {
  console.log('No argument');
}
