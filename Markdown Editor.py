def new_line():
    return '\n'


def header():
    while True:
        level = int(input('Level:'))
        if 1 <= level <= 6:
            text = input('Text:')
            return f'{level * "#"} {text}' + '\n'
        else:
            print('The level should be within the range of 1 to 6')
            continue


def list_rows():
    while True:
        rows = int(input('Number of rows:'))
        if rows < 1:
            print('The number of rows should be greater than zero')
            continue
        else:
            return rows


def ordered_list():
    rows = list_rows()
    text = ''
    for n in range(1, rows + 1):
        row = input(f'Row #{n}:')
        text += f'{n}. {row}\n'
    return text


def unordered_list():
    rows = list_rows()
    text = ''
    for n in range(1, rows + 1):
        row = input(f'Row #{n}:')
        text += f'* {row}\n'
    return text


def italic():
    text = input('Text:')
    return f'*{text}*'


def bold():
    text = input('Text:')
    return f'**{text}**'


def plain():
    text = input('Text:')
    return text


def link():
    label = input('Label:')
    url = input("URL:")
    return f'[{label}]({url})'


def inline_code():
    text = input('Text:')
    return f'`{text}`'


def available_formatters(formatter):
    if formatter == 'plain':
        text = plain()
    elif formatter == 'bold':
        text = bold()
    elif formatter == 'italic':
        text = italic()
    elif formatter == 'header':
        text = header()
    elif formatter == 'link':
        text = link()
    elif formatter == 'inline-code':
        text = inline_code()
    elif formatter == 'new-line':
        text = new_line()
    elif formatter == 'unordered-list':
        text = unordered_list()
    elif formatter == 'ordered-list':
        text = ordered_list()
    else:
        print('Unknown formatting type or command')
        text = None
    return text


final_text = ''

while True:
    formatter = input('Choose a formatter:')
    if formatter == "!help":
        print("""Available formatters: plain bold italic header \
linkinline-code ordered-list unordered-list and new-line
Special commands: !help !done""")
    elif formatter == '!done':
        break
    else:
        new_text = available_formatters(formatter)
        if new_text is None:
            pass
        else:
            final_text += new_text
            print(final_text)

with open('output.md', 'w') as markdown:
    markdown.writelines(final_text)
