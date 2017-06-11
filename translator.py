#!/usr/bin/env python3
# coding: utf-8
import js2py
import io
import os
import sys

if not os.path.isdir('generators'):
    os.mkdir('generators')
    f = open('generators/__init__.py', 'w')
    f.close()

replacements = [
    ('''var br = "";''', ''),
    ('''('#placeholder').css('textTransform', 'capitalize');''', ''),
    ('''var element = document.createElement("div");''', 'var result = [];'),
    ('''element.setAttribute("id", "result");''', ''),
    ('''br = document.createElement('br');''', ''),
    ('''element.appendChild(document.createTextNode(names));''',
     'result.push(names);'),
    ('''element.appendChild(br);''', ''),
    ('''document.getElementById("placeholder").appendChild(element);''',
     'return result;')
]

generators = [name for name in os.listdir(
    'js') if os.path.isfile('js/' + name)]


def prepare(code):
    result = []
    for line in code.split('\n'):
        for f, t in replacements:
            if line.find(f) != -1:
                line = t
                break
        result += [line]
    return '\n'.join(result)


def finalize(code):
    result = []
    for line in code.split('\n'):
        if line == '':
            continue
        if line.find('document') != -1 or line.find('element') != -1:
            if line.find('{') != -1:
                result += ['{']
            elif line.find('}') != -1:
                result += ['}']
        else:
            result += [line]
    return '\n'.join(result)
if __name__ == "__main__":
    progress = 1
    total = len(generators)
    broken = []

    for name in sorted(generators):
        sys.stdout.write('\r {} out of {} ({})                \r'.format(
            progress, total, name))
        code = open('js/' + name).read()
        code = finalize(prepare(code))
        buf = io.StringIO(code)
        try:
            js2py.translate_file(
                buf, 'generators/{}.py'.format(name.split('.')[0]))
        except Exception as e:
            broken += [name]
        progress += 1
    if broken != 0:
        print('\n Done! List of files that cannot be translated (total: \
    {}): {}'.format(len(broken), broken))
    print('\nDone!')
