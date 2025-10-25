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

            if not line.startswith('#') and line != '\n':
                line = line.strip()
                items[heading].append(line)
except FileNotFoundError as err:
    print(f'Something went wrong: {err}')

json_string = json.dumps(items, indent=4)
filename = 'output.json'

with open(filename, 'w') as output_file:
    output_file.write(json_string)

print(f'{filename} saved!')