# code that check some PEP conventions, mixing the ast and re modules for

import re
import sys
import os
import ast


def string_remover(line):
    line = "".join(re.split("'.*'", line))
    line = "".join(re.split('".*"', line))
    return line


def S001(line):
    line = line.strip()
    if len(line) > 79:
        print(f'{file_path}: Line {line_number}: S001 Too long')


def S002(line):
    n = 0
    for string in line:
        if string != ' ':
            break
        else:
            n += 1
    if n % 4 != 0:
        print(f'{file_path}: Line {line_number}: S002 Indentation '
              f'is not a multiple of four')


def S003(line):
    new_line = ''.join(re.split('#.*', line))   # !!!!
    if new_line.find(';') > -1:
        print(f'{file_path}: Line {line_number}: S003 stop using ;')


def S004(line):
    index = line.find('#')
    if index > 0 and '  ' not in line[index - 2: index]:
        print(f'{file_path}: Line {line_number}: S004 Less than two spaces'
              f' before inline comments')


def S005(line):
    line = line.upper()
    index1 = line.find('TODO')
    index2 = line.find('#')
    if (index1 >= 0 and index2 >= 0) and index1 > index2:
        print(f'{file_path}: Line {line_number}: S005 TODO found')


def S006(line):
    global stack
    if stack > 2:
        print(f'{file_path}: Line {line_number}: S006 More than '
              f'two blank lines preceding a code line')
    if line.isspace():
        stack += 1
    else:
        stack = 0


def S007_S008(line):
    line = line.strip()
    if line[0:5] == 'class':
        if line[6] == ' ':
            print(f'{file_path}: Line {line_number}: '
                  f'S007 Too many spaces after "class"')
        line = line.lstrip('class').strip()
        if line[0].islower():
            print(f'{file_path}: Line {line_number}: '
                  f'S008 class name should use "CamelCase"')


def S007_S009(line):
    line = line.strip()
    if line[0:3] == 'def':
        if line[4] == ' ':
            print(f'{file_path}: Line {line_number}: '
                  f'S007 Too many spaces after "def"')
        line = line.lstrip('def').strip()
        if line[0].isupper():
            print(f'{file_path}: Line {line_number}: '
                  f'S009 class name should use snake_case"')


def S010(line):
    tree = ast.parse(line)
    generator = ast.walk(tree)
    for node in generator:
        if isinstance(node, ast.FunctionDef):
            args = node.args.args
            for arg in args:
                if not arg.arg.islower():
                    print(f'{file_path}: Line {arg.lineno}: '
                          f'S010 Argument name {arg.arg} should be written in snake_case')


def S011(line):
    tree = ast.parse(line)
    generator = ast.walk(tree)
    for node in generator:
        if isinstance(node, ast.Assign):
            variables = node.targets
            for var in variables:
                try:
                    if not var.id.islower():
                        print(f'{file_path}: Line {var.lineno}: '
                              f'S011 Variable {var.id} should be written in snake_case;')
                except Exception:
                    pass


def S012(line):
    tree = ast.parse(line)
    generator = ast.walk(tree)
    for node in generator:
        if isinstance(node, ast.FunctionDef):
            args = node.args.defaults
            for arg in args:
                if type(arg) == ast.List:
                    print(f'{file_path}: Line {arg.lineno}:'
                          f' S012 The default argument value is mutable.')


def PEP(file):
    global stack
    global line_number
    global file_path
    file_path = file
    with open(file, 'r', encoding='utf-8') as f:
        line_number = 1
        stack = 0
        for file_line in f.readlines():
            S001(file_line)
            file_line = string_remover(file_line)
            S002(file_line)
            S003(file_line)
            S004(file_line)
            S005(file_line)
            S006(file_line)
            S007_S008(file_line)
            S007_S009(file_line)
            line_number += 1
    with open(file) as f:
        read = f.read()
        S010(read)
        S011(read)
        S012(read)


def file_or_folder(path):
    try:
        os.chdir(path)
        for file_name in os.listdir():
            if file_name == 'tests.py':
                pass
            elif bool(re.match('.*\.py$', file_name)):
                file_name = path + '\\' + file_name
                PEP(file_name)
    except Exception:
        PEP(path)


inp = sys.argv[1]

file_or_folder(inp)
