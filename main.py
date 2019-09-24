import os
import sys
import pyperclip

os.system("touch " + sys.argv[1])
os.system("%windir%\system32\mspaint.exe " + sys.argv[1])
pyperclip.copy('\\begin{center}\n\t\\includegraphics[width=200pt]{' + sys.argv[1] + '}\n\\end{center}')
