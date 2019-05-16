#!/usr/bin/env python3
import sys
import os

def main():
    """
    Main function that is run when started.
    """
    arguments = sys.argv[1 : ]
    pdflatex = '-p' in arguments
    arguments = arguments[1 : ] if pdflatex else arguments

    if not arguments:
        print('No files selected')
    
    for argument in arguments:
        to_tex(argument)

    if pdflatex:
        for arg in arguments:
            filename = arg.split('.')
            os.system('pdflatex ' + '.'.join(filename[ : -1 ]) + '.tex')

def rem_spaces(input_string):
    """
    Removes spaces from the beginning of a string, returns an empty string if
    input is empty or a string containing only spaces.
    """
    return input_string.strip()

def read_to_list(input_string):
    """
    This function takes in a string and separates it into lines and multiline
    mathmode environments.
    """
    length_of_input_string = len(input_string)
    
    if length_of_input_string == 1:
        return [input_string]
    
    beginning_of_line = 0
    
    output_list = []
    
    in_mathmode = False
    
    i = 0
    
    while i < length_of_input_string - 1:
        if in_mathmode:
            if input_string[i : i + 2] == '$$':
                output_list.append(input_string[beginning_of_line : i + 2])
                beginning_of_line = i + 2
                in_mathmode = False
        else:
            if input_string[i] == '\n':
                output_list.append(input_string[beginning_of_line : i])
                beginning_of_line = i + 1
            elif input_string[i : i + 2] == '$$':
                beginning_of_line = i
                in_mathmode = True
        i += 1

    output_list.append(input_string[beginning_of_line : i + 1])
    
    return output_list

def to_bold_italic(input_string):
    """
    Given a line of text, replaces the *'s and _'s with LaTeX textbf and textit
    environments respectively.
    """
    temp_string = ''
    italic_mode, bold_mode = False, False
    
    for i in input_string:
        if i == '_' and italic_mode == False:
            temp_string += '\\textit{'
            italic_mode = True
        elif i == '_' and italic_mode == True:
            temp_string += '}'
            italic_mode = False
        elif i == '*' and bold_mode == False:
            temp_string += '\\textbf{'
            bold_mode = True
        elif i == '*' and bold_mode == True:
            temp_string += '}'
            bold_mode = False
        else:
            temp_string += i
    
    if italic_mode or bold_mode:
        temp_string += '}'
        
    return temp_string

def to_list(list_of, type_of, line_number, list_len):
    """
    Given a list of strings representing either an itemize or enumerate 
    environment, return the formatted version.
    """
    if type_of == 'enumerate':
        start_at = 2
        testing_str = '#.'
    elif type_of == 'itemize':
        start_at = 1
        testing_str = '-'
    
    if line_number == 0:
        output_str = (
            '\\begin{' + 
            type_of + 
            '}\n\\item ' + 
            to_bold_italic(rem_spaces(list_of[0][start_at : ])) + 
            '\n'
        )

        if list_of[1][0 : start_at] != testing_str:
            output_str += '\\end{' + type_of + '}\n'

    elif line_number == list_len - 1:
        if list_of[list_len - 2][0 : start_at] == testing_str:
            output_str = (
                '\\item ' + 
                to_bold_italic(
                    rem_spaces(list_of[list_len - 1][start_at : ])
                ) + 
                '\n\\end{' + 
                type_of + 
                '}\n'
            )
        else:
            output_str = (
                '\\begin{' + 
                type_of + 
                '}\n\\item ' + 
                rem_spaces(list_of[list_len - 1][start_at : ]) + 
                '\n\\end{' + 
                type_of + 
                '}\n'
            )
    else:
        prev_line = list_of[line_number - 1][0 : start_at]
        next_line = list_of[line_number + 1][0 : start_at]
        middle = to_bold_italic(rem_spaces(list_of[line_number][start_at : ]))
        
        if prev_line == next_line == testing_str:
            output_str = '\\item ' + middle + '\n'
        elif prev_line != testing_str and next_line != testing_str:
            output_str = (
                '\\begin{' + 
                type_of +
                '}\n\\item ' + 
                middle + 
                '\n\\end{' + 
                type_of + 
                '}\n'
            )
        elif prev_line == testing_str and next_line != testing_str:
            output_str = '\\item ' + middle + '\n\\end{' + type_of +'}\n'
        elif prev_line != testing_str and next_line == testing_str:
            output_str = '\\begin{' + type_of +'}\n\\item ' + middle + '\n'
    return output_str

def to_mathmode(input_string):
    """
    Takes a string contained within a multiline mathmode environment and
    formats it as an align environment. If there is exactly one equals
    sign in each line, then it aligns the equals signs.
    """
    list_of_maths = [
        rem_spaces(x) for x in input_string.split('\n') if rem_spaces(x)
    ]

    align_equals = all(1 == line.count('=') for line in list_of_maths)

    if align_equals:
        list_of_maths = [line.replace('=', '&=') for line in list_of_maths]

    length_of_list = len(list_of_maths)
    
    if length_of_list == 1:
        return '\\begin{align*}\n' + list_of_maths[0] + '\n\\end{align*}\n'
    
    output_str = '\\begin{align*}\n'
    
    for i in range(length_of_list - 1):
        output_str += list_of_maths[i] + '\n'
    output_str += list_of_maths[length_of_list - 1] + '\n\\end{align*}\n'
    
    return output_str

def to_tex(file_name):
    """
    This function is run for each file that is passed to it, and creates a
    new file with the same name but with a .tex extension.
    """
    top_string = (
        '\\documentclass{article}\n\\usepackage{enumerate}\n\\usepackage{amsfon'
        'ts}\n\\usepackage{amsmath}\n\\usepackage{enumerate}\n\\usepackage[marg'
        'in=1in]{geometry}\n'
    )
    
    content = ''

    is_author, is_title, is_date = False, False, False
    
    with open(file_name) as f:
        read_data = f.read()
    
    data_list = [x for x in read_to_list(read_data) if rem_spaces(x) != '']
    
    list_length = len(data_list)
    
    for i in range(list_length):
        if data_list[i][0 : 2] == '#T':
            is_title = True
            title = rem_spaces(data_list[i][2 : ])
        elif data_list[i][0 : 2] == '#A':
            is_author = True
            author = rem_spaces(data_list[i][2 : ])
        elif data_list[i][0 : 2] == '#D':
            is_date = True
            date = rem_spaces(data_list[i][3 : ])
        elif data_list[i][0 : 2] == '# ':
            content += (
                '\section*{' + 
                to_bold_italic(rem_spaces(data_list[i][2 : ])) + 
                '}\n'
            )
        elif data_list[i][0 : 3] == '## ':
            content += (
                '\subsection*{' +
                to_bold_italic(rem_spaces(data_list[i][3 : ])) +
                '}\n'
            )
        elif data_list[i][0 : 2] == '#.':
            content += to_list(data_list, 'enumerate', i, list_length)
        elif data_list[i][0] == '-':
            content += to_list(data_list, 'itemize', i, list_length)
        elif data_list[i][0 : 2] == '$$':
            content += to_mathmode(data_list[i][2 : -2])
        else:
            content += to_bold_italic(rem_spaces(data_list[i])) + '\n\n'
    
    if is_title:
        top_string += '\\title{' + title + '}\n'
    if is_author:
        top_string += '\\author{' + author + '}\n'

    if is_date:
        if date:
            top_string += '\\date{' + date + '}\n'
    else:
        top_string += '\\date{}\n'

    #else:
        #top_string += '\\date{}'
    
    top_string += '\\begin{document}\n'
    
    if is_title or is_author or is_date:
        top_string += '\\maketitle\n'
    
    final = top_string + content + '\\end{document}'
    
    if file_name[-4 : ] == '.txt':
        new_file_name = file_name[ : -4] + '.tex'
    elif file_name[-3 : ] == '.md':
        new_file_name = file_name[ : -3] + '.tex'
        
    with open(new_file_name, 'w') as f:
        f.write(final)

if __name__ == '__main__':
    main()
