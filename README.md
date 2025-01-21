# Coding Challenges: wc

I am working on the challenges at [codingchallenges.fyi](https://codingchallenges.fyi). As a part of that, I have implemented various sections of the challenges to mimic the functionality of the `wc` (word count) command.

This script provides functionality to count the number of characters, words, lines, and the size of a file in bytes.

### Usage

To use this script, run it from the command line with the following options:

### Options
filename: The file to count characters, words, lines, or size in.
- `-c`, `--size`: Display the size of the file in bytes.
- `-w`, `--words`: Count the number of words in the file.
- `-l`, `--lines`: Count the number of lines in the file.
- `-m`, `--chars`: Count the number of characters in the file.
- **Default**: If no options are provided, the script will display the number of lines, words, and size of the file.

**Example**

```
python main.py test.txt example.txt
```

**Output**
```
7145    58164   332147  test.txt
```

> Disclaimer: This README is entirely generated using AI. No source code was generated using AI.