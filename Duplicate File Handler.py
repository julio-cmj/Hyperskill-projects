import os
import sys
import hashlib


def one_command_line():
    root_path = sys.argv
    try:
        return root_path[1]
    except IndexError:
        print('Directory is not specified\n')


def list_duplicate(any_list):
    unique = []
    for entry in any_list:
        if entry not in unique:
            unique.append(entry)
    return unique


def sorting_option():
    print("""Size sorting options:
    1. Descending
    2. Ascending\n""")
    while True:
        choice = input("Enter a sorting option:")
        if choice in ['1', '2']:
            print()
            return int(choice)
        else:
            print('Wrong option')
            continue


def duplicate_option():
    while True:
        choice = input("Check for duplicates?")
        if choice in ['yes', 'no']:
            print()
            return choice
        else:
            print('Wrong option')
            continue


def delete_option():
    while True:
        choice = input("Delete files?")
        if choice == 'yes':
            print()
            return choice
        else:
            print('Wrong option')
            continue


def list_to_delete():
    global repeted_files
    while True:
        try:
            string_index = input('Enter file numbers to delete:').split()
            files_index = [int(number) for number in string_index]
            if max(files_index) > len(repeted_files):
                print('Wrong format')
                continue
            else:
                print()
                return files_index
        except Exception:
            print('Wrong format')
            continue


root = one_command_line()

file_format = input("Enter file format:")
print()

sorting_type = sorting_option()

files = []

# walking files in root and selecting those with the selected format
for filepath, dirname, filename in os.walk(root, topdown=False):
    for file in filename:
        if len(file_format) == 0:
            files.append(f"{filepath}\{file}")
        elif file[len(file) - len(file_format):] == file_format:
            files.append(f"{filepath}\{file}")

# creating dictionary with files and their size and a
sizes = {file: os.stat(file).st_size for file in files}

# creating list with all the unique sizes
unique_sizes = list_duplicate(sizes.values())

# sorting sizes for selected option
if sorting_type == 1:
    unique_sizes.sort(reverse=True)
else:
    unique_sizes.sort()

# printing files with same size and taking then into dictionaries
duplicates = {}
hash_duplicates = {}

for n in unique_sizes:
    print(n, 'bytes')
    for key in sizes.keys():
        if sizes[key] == n:
            with open(key, 'rb') as f:
                h = hashlib.md5(f.read())
                hash_duplicates.update({key: h.hexdigest()})
                duplicates.update({h.hexdigest(): n})
            print(key)
    print()

# taking unique hashes and duplicated hashes
unique_hashes = []
duplicate_hashes = []

for hash_value in hash_duplicates.values():
    if hash_value not in unique_hashes:
        unique_hashes.append(hash_value)
    elif hash_value in unique_hashes:
        duplicate_hashes.append(hash_value)

# printing duplicates
duplicate_check = duplicate_option()

index = 1
byte_size = 0
repeted_files = []
if duplicate_check == 'yes':
    for hash_value in duplicate_hashes:
        size = duplicates.get(hash_value)
        if byte_size != size:
            print(f'\n {size} bytes')
        print('Hash:', hash_value)
        for key in hash_duplicates.keys():
            if hash_duplicates[key] == hash_value:
                repeted_files.append(key)
                print(f'{index}. {key}')
                index += 1
        byte_size = size

# deleting duplicates
delete_check = delete_option()

freed_space = 0
if delete_check == 'yes':
    to_delete = list_to_delete()
    for index in to_delete:
        file_deleted = repeted_files[index - 1]
        freed_space += int(os.stat(file_deleted).st_size)
        os.remove(file_deleted)

    print(f"Total freed up space: {freed_space} bytes")
