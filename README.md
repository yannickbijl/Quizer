# Quizer

A fun program to test your knowledge with multiple choice questions. I developed this mostly for myself to prepare for exams. I hope that those who use it will find it helpfull. One can give a file with questions and answers which Quizer will use to make randomized tests.

Files with the questions and answers should be made in the following format:
  * Question1? <tab> A\`B\`C\`D <tab> Answer

Example:
  * In which language is Quizer programmed? Python\`Java\`R\`Matlab  Python
  
An example of the file format can be seen in [example_test.txt](./example_test.txt)

The program uses the modules sys, datetime, random, and the third-party module wx-python 4.0 (Phoenix) WxPython

The executable was made using pyinstaller on Windows 10 Home-edition 64-bit.

In the project folder open the cmd and use the command: **pyinstaller -F --icon=Quizer.ico -w Quizer.py**

The icon was made in Adobe Illustrator and Adobe Photoshop.

Quizer.py is the main file, GUI_Quizer_Settings.py, GUI_Quizer_Test.py, GUI_Quizer__Results, and GUI_Quizer_End.py are used to generate the user interface. ESC_Quizer.py does the calculations.
