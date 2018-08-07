#!/usr/bin/env python

import sys



def main():
    # main loop that is called when program is run
    
    # save all the files as a list
    arguments = sys.argv[1 : ]
    
    # if there are no files, print an error message
    if len(arguments) == 0:
        print('No file selected')
    
    for arg in arguments:
        to_tex(arg)



def to_tex(file_name):
    # takes file name, turns the file into text and then outputs a tex file file_name.tex

    # beginning of tex file that we will add to     
    top_string = '''\\documentclass{article}\n\\usepackage{amsfonts}\n\\usepackage{amsmath}\n\\usepackage{enumerate}\n\\usepackage[margin=1in]{geometry}\n\\setlength{\\parindent}{0in}\n\\begin{document}'''

    # open the file and save contents as read_data
    with open(file_name) as f:
        read_data = f.read()
    
    # count the number of instances of #T, #A and #D respectively
    title_count = read_data.count('#T')
    author_count = read_data.count('#A')
    date_count = read_data.count('#D')
    
    # find the total number of these instances
    total_count = title_count + author_count + date_count
    
    # check the document is well-formed (or sound)
    is_sound = True
    if title_count > 1:
        print('Too many title fields.')
        is_sound = False
    if author_count > 1:
        print('Too many author fields.')
        is_sound = False
    if date_count > 1:
        print('Too many date fields.')
        is_sound = False
    
    # if the document is sound, then start converting it
    if is_sound:
        # turn the string into a list of lines
        data_list = read_data.split('\n')
        
        # set title, author and date
        for i in data_list[0 : total_count]:
            if i[0 : 2] == '#T':
                title = i[3 : ]
            if i[0 : 2] == '#A':
                author = i[3 : ]
            if i[0 : 2] == '#D':
                date = i[2 : ]
        
        # if there is a title, author or date, then add them
        if title_count == 1:
            top_string += '\n\\title{' + title + '}'
        if author_count == 1:
            top_string += '\n\\author{' + author + '}'
        if date_count == 1 and date != '':
            top_string += '\n\\date{' + date + '}'
        
        # if there is a date, author or title, then display them
        if total_count > 0:
            top_string += '\n\\maketitle\n'
        
        # removes the author, title and date parts (if any)
        data_list = data_list[total_count : ]
        
        # remove all instances of '' from the data_list
        data_list = list(filter(lambda a: a != '', data_list))
        
        # find size of list to use in the following loop
        list_length = len(data_list)
        
        # run a loop that iterates over each line in the document
        for i in range(list_length - 1):
            if data_list[i][0 : 2] == '# ':
                top_string += '\section*{' + data_list[i][2 : ] + '}\n'
            elif data_list[i + 1][0 : 2] == '\[' or data_list[i][0 : 2] == '\[':
                top_string += data_list[i] + '\n'
            elif data_list[i + 1][0 : 2] == '# ':
                top_string += data_list[i] + '\n'
            else:
                top_string += data_list[i] + '\\\\\n\n'
        
        # repeat for the last line
        if data_list[list_length - 1][0 : 2] == '# ':
            top_string += '\n\\section*{' + data_list[list_length - 1][2 : ] + '}\n'
        elif data_list[list_length - 1][0 : 2] == '\[':
            top_string += data_list[list_length - 1] + '\n'
        else:
            top_string += data_list[list_length - 1]
        
        # declare a new file name (only works for txt files)
        new_file_name = file_name[ : -4] + '.tex'
        
        # write final tex file
        with open(new_file_name, 'w') as f:
            read_data = f.write(top_string + '\n\end{document}')



if __name__ == '__main__':
    main()
