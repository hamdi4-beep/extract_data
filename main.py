from collections import defaultdict
import json

lines: list[str] = []

try:
    with open('readme.md', 'r') as file:
        for line in file:
            if not line == '\n': lines.append(line)
except FileNotFoundError as err:
    print(f'Something went wrong: {err}')

items = defaultdict(list)
heading = 'No heading'

for line in lines:
    if line.startswith('##'):
        heading = line[3:-1].strip()

    if line.startswith('-'):
        items[heading].append(line[:-1])

json_string = json.dumps(items, indent=4)
print(json_string)