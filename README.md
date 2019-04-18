# larkdown
A _very_ basic markdown-esque text-to-tex tool that allows for the easy creation of LaTeX documents. Mostly used by myself to quickly write up homework solutions.

# Using larkdown
To start, open a plain text file and save it as `filename.txt` or `filename.md`.

To add a title to your document, start a line with `#T` followed by a space the title you wish to use. If you have more than one line beginning with `#T` then only the last one will be used. Similarly, you can add an author (or many) by starting a line with `#A` followed by a space and the author(s) name(s), and you can add a date by starting a line with `#D` followed by a space and the date you would like to use. If you wish to use the current date, you can add a line which has only `#D` and LaTeX will take care of it for you.

To add a section heading, simply begin a line with `#` followed by a space and your desired section heading. To add a subsection heading, begin a line with `##` followed by a space and your desired subheading.

You can also use bullet points or numbered lists. These will use the itemize and enumerate environments in LaTeX respectively. To use bullet points, simply start each line with `-` and to use numbered lists start each line with `#.` followed by some text.

Each line of text will be treated as a separate paragraph, and blank lines will be ignored.

To make a word or sequence of words bold or italic, simply surround the text in question with \*asterisks\* or \_underscores\_ respectively. 

If you wish to use an equation inline, simply surround it by two single $'s, and to use an equation on a new line, simply surround it by two $$ (where each of the $$'s is on its own line).

# Example
Below is a very simple example.
```
#T Working example of larkdown
#A mgrnls
#D
# This is a section heading!
This is the first paragraph in the text.

## This is a subsection heading!
This is another paragraph! Here we can use inline math mode like this $4x + 3$ or
$$
4x + 3
$$
to have it on a seperate line.

If you have exactly one equals sign in each line in a math mode environment, it will automatically align them vertically using the LaTeX align environment.

Below is a numbered list:
#. first thing
#. second thing 
#. third thing

Below is a bulleted list:
- first thing
- second thing
- third thing

Some things in _italics_ and *bold*.
```
Hopefully it should be clear that the above is much clearer to read and easier to write than a standard (short) LaTeX document.

# Compiling to LaTeX
Open the terminal in the directory of your file and type `python3 larkdown.py filename.txt` and it will create a new file in the directory called `filename.tex` which you can then use to generate a pdf using pdflatex with `pdflatex filename.tex`. Note that you may pass the script multiple file names, so `python3 larkdown.py filename1.txt filename2.txt` will return `filename1.tex` and `filename2.tex`.

You can also use the -p flag when running larkdown, this will automatically run pdflatex for you. To do this, run `python3 larkdown.py -p filename.txt`. Again, you must have pdflatex installed for this to work.
