# larkdown
A _very_ basic markdown-esque text-to-tex tool that allows for the easy creation of LaTeX documents. Mostly used by myself to quickly write up homework solutions.

# Using larkdown
To start, open a plain text file and save it as _filename.txt_. The first three lines of the file are reserved for the title, author and date declarations. To add a title, author or date, add the following
```
#T Title
#A Author
#D Date
```
to the top of the file, where you replace (for example) 'Title' with whatever you wish your title to be. If you do not wish to have any of the above three, then simply leave out the desired line. The date field can simply be left as '#D' and the current date will be automatically filled in by LaTeX.

To add a section heading, simply begin a line with '# ' followed by your desired section heading.

You can also use bullet points or numbered lists. These will use the itemize and enumerate environments in LaTeX respectively. To use bullet points, simply start each line with `- ` and to use numbered lists start each line with `#.` followed by some text.

Each line of text will be treated as a separate paragraph, and blank lines will be ignored. However, if a line starts with '\[' it will be treated as a math mode line.

# Example
Below is a very simple example.
```
#T Working example of larkdown
#A mgrnls
#D
# This is a section heading!
This is the first paragraph in the text.

This is another paragraph! Here we can use inline math mode like this $4x + 3$ or
\[4x+3\]
to have it on a seperate line.

Just remember to put all your mathmode on the same line!

Below is a numbered list:
#. first thing
#. second thing 
#. third thing

Below is a bulleted list:
- first thing
- second thing
- third thing
```

# Compiling to LaTeX
Open the terminal in the directory of your file and type `python3 larkdown.py filename.txt` and it will create a new file in the directory called `filename.tex` which you can then use to generate a pdf using pdflatex with `pdflatex filename.tex`. Note that you may pass the script multiple file names, so `python3 larkdown.py filename1.txt filename2.txt` will return `filename1.tex` and `filename2.tex`.
