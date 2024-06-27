#!/usr/bin/node
const countArgs = process.argv.length;
console.log(countArgs === 2 ? 'No argument' : countArgs === 3 ? 'Argument found' : 'Arguments found');
