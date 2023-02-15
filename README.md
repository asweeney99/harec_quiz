# harec_quiz

IRTS HAREC multiple choice quiz.

## Requirements

Windows 10, Windows 11 or Linux.

Python 3.9.X

You need the Python programming language on your computer, specifically release 3.9.X where X is any release number. While other Python versions might also work, they haven't been specifically tested. You can download Python 3.9.16 [here](https://www.python.org/downloads/). You can follow the detailed instructions on how to download Python [here](https://www.ics.uci.edu/~pattis/common/handouts/pythoneclipsejava/python.html).


## Download source code 

You can download the source code if you have the git version control system. Alternatively, you can just download the zipped files from the Github address given below.

### Option 1: Git

```
git clone https://github.com/asweeney99/harec_quiz.git
```

### Option 2: Download Zipped files

1. Go to https://github.com/asweeney99/harec_quiz.git
2. Click the green button Code, then Download Zip.
3. Extract all the contents of the downloaded folder.


### Install dependencies

Now you have the source code, you need to install the python module *playsound* to play the startup mp3 file. Pip is a package manager that comes with Python and you can use it to install *playsound*.

Open the command prompt application by typing *cmd* in your Windows search bar. In the command prompt type:

```
pip install playsound==1.2.2
```

If you received no errors, you're good to go! If you got an error, most likely you haven't installed pip correctly when you downloaded Python. If you're sure you've done everything correctly, go to Issues below.


## How to Play

To launch the game, open a Command Prompt (see above), and type:

```
py harec.py
```

The quiz tests your knowledge of country prefixes, Q-Codes and the IARU Region 1 band plan.
    
Type a, b, c or d then enter. Type q to quit.
	
The game keeps a record of your high score to beat when you play.
	
## Issues 

Bugs or suggestions for improvement can be notified to the developer on [Github](https://github.com/asweeney99/harec_quiz/issues)

### Tips

Command Prompt (cmd) text too small? 

You can increase font size by right clicking the top bar, choose Properties, then select the Font tab and choose your font size.
	
