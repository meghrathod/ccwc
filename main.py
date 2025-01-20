import argparse
from stat import ST_SIZE
from os import stat

parser = argparse.ArgumentParser(description='Coding Challenges: wc')
parser.add_argument('filename', help='The file to count characters in')
parser.add_argument('-c', '--size', action='store_true',  help="size of file in bytes")
parser.add_argument('-w', '--words', action='store_true', help="count the number of words in the file")
parser.add_argument('-l', '--lines', action='store_true', help="count the number of lines in the file")
parser.add_argument('-m', '--chars', action='store_true', help="count the number of characters in the file")
args = parser.parse_args()


filename, c, w, l, m = args.filename, args.size, args.words, args.lines, args.chars

try:
    with open(filename) as file:
        text = file.read()
        size = stat(filename).st_size

        if c:
            print(f"\t{size}\t{filename}")
        if m:
            print(f"\t{len(text)}\t{filename}")
        if l:
            print(f"\t{text.count("\n")}\t{filename}")
        if w:
            print(f"\t{len(text.split())}\t{filename}")
        if not (c or w or l or m):
            print(f"\t{text.count("\n")}\t{len(text.split())}\t{len(text)}\t{filename}")
except FileNotFoundError:
    print("Error: File not found in given path")
    
    
# Run the script
# python main.py test.txt
