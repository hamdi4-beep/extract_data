from collections import defaultdict
import json

items = defaultdict(list)
heading = 'No heading'

try:
    with open('readme.md', 'r') as file:
        for line in file:
            if line.startswith('#'):
                heading = line.strip()

            if line.startswith('-'):
                line = line.strip()
                items[heading].append(line)
except FileNotFoundError as err:
    print(f'Something went wrong: {err}')

json_string = json.dumps(items, indent=4)
print(json_string)