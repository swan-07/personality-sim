import os
import json

root_dir = 'folder'

output_file = 'combined_contents.txt'

def gather_contents(root_dir):
    all_contents = []
    for foldername, subfolders, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename == 'message.json':
                filepath = os.path.join(foldername, filename)
                with open(filepath, 'r') as f:
                    data = json.load(f)
                    for message in data:
                        if 'Contents' in message:
                            all_contents.append(message['Contents'])
    return all_contents

def write_to_file(contents, output_file):
    with open(output_file, 'w') as f:
        for content in contents:
            f.write(content + '\n')


def main():
    contents = gather_contents(root_dir)
    write_to_file(contents, output_file)

if __name__ == "__main__":
    main()
