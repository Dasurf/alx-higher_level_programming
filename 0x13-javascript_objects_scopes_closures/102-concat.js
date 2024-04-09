#!/usr/bin/node
const fs = require('fs');

// Check if correct number of arguments are provided
if (process.argv.length !== 5) {
  console.log('Usage: node script.js <inputFile1> <inputFile2> <outputFile>');
  process.exit(1);
}

const inputFile1 = process.argv[2];
const inputFile2 = process.argv[3];
const outputFile = process.argv[4];

// Read the contents of the first input file
try {
  const fArg = fs.readFileSync(inputFile1, 'utf8');

  // Read the contents of the second input file
  try {
    const sArg = fs.readFileSync(inputFile2, 'utf8');

    // Concatenate the contents of both files
    const concatenatedContent = fArg + sArg;

    // Write the concatenated content to the output file
    try {
      fs.writeFileSync(outputFile, concatenatedContent);
      console.log(`Successfully concatenated ${inputFile1} and ${inputFile2} into ${outputFile}`);
    } catch (error) {
      console.error(`Error writing to ${outputFile}: ${error.message}`);
    }
  } catch (error) {
    console.error(`Error reading ${inputFile2}: ${error.message}`);
  }
} catch (error) {
  console.error(`Error reading ${inputFile1}: ${error.message}`);
}
