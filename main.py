import json

def read_file(filename):
    try:
        file = open(filename, 'r')
        lines = [line for line in file if not line == '\n']
    except FileNotFoundError as err:
        print(f'Something went wrong: {err}')
    finally:
        file.close()

    return lines


if __name__ == '__main__':
    lines = read_file('readme.md')
    items = {}
    
    for line in lines:
        if line.startswith('##'):
            heading = line[3:-1]
            list = []

        if line.startswith('-'):
            list.append(line[2:-1])
            items[heading] = list

    json_string = json.dumps(items, indent=4)
    print(json_string)