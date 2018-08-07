# larkdown
A _very_ basic markdown-esque text-to-tex tool that allows for the easy creation of LaTeX documents.

# Using larkdown
To start, open a plain text file and save it as _filename.txt_. The first three lines of the file are reserved for the title, author and date declarations. To add a title, author or date, add the following
```
#T Title
#A Author
#D Date
```
to the top of the file, where you replace (for example) 'Title' with whatever you wish your title to be. If you wish do not wish to have any of the above three, then simply leave out the desired line. The date field can simply be left as '#D' and the current date will be automatically filled in by LaTeX.

To add a section heading, simply begin a line with '# ' followed by your desired section heading.

Each line of text will be treated as a separate paragraph, and blank lines will be ignored. However, if a line starts with '\[' it will be treated as a math mode line.

# Example
Below is a very simple example.
```
#T Working example of larkdown
#A mgrnls
#D
# This is a section heading!
This is the first paragraph in the text.

This is another paragraph! Here we can use inline math mode like this $4x + 3$ or we can use math mode on a separate line like below
\[4x+3\]
Just remember to put all your mathmode on the same line!
```
