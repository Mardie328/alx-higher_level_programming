#!/usr/bin/node
const args = Math.floor(Number(process.argv.length));
if (isNaN(args)) {
  console.log('Missing number of occurrences');
} else {
  for (let count = 0; count <= args; count++) {
    console.log('C is fun');
  }
}
