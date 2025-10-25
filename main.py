from collections import defaultdict
import json

items = defaultdict(list)
heading = 'No heading'

try:
    with open('readme.md', 'r') as file:
        for line in file:
            if line.startswith('#'):
                # skips the first three hashtag characters
                heading = line[3:].strip()

            if line.startswith('-'):
                line = line[1:].strip()
                items[heading].append(line)

            if line[0].isdigit():
                # skips the digit number and period which accounts for numbered lists
                line = line[2:].strip()
                items[heading].append(line)
except FileNotFoundError as err:
    print(f'Something went wrong: {err}')

json_string = json.dumps(items, indent=4)
print(json_string)