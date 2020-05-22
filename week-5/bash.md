# Bash for Beginners

## First, a bit of background
Back in the day, like wayyy back in the day, computers were nothing more than simple command line interfaces, a big black screen with a blinking cursor. Instead of dragging and dropping files, you'd need to explicitly type out the file to move, from where to where.

These operating systems were typically on Unix, a family of similar operating systems developed originally in the 1970s. To interact with those operating sytems, users would write their commands in a "shell", named as such because it was the "outermost layer around the operating system". The first such shell to be used with Unix was the "Bourne Shell", or just `sh`. Plenty more exist nowadays, but by far the most common is `bash`, or the "Bourne Again Shell".

On modern machines, MacOS and Linux systems are derived from Unix, while Windows systems are not. As such, we can use the `terminal` application on Mac to access a bash shell, and the `ubuntu` terminal on Windows (you'll have to install this seperately).

## Star Wars with Bash
In your folders, go to the mirror at [files.node.ishaandey.com](http://files.node.ishaandey.com), and download `bash-tutorial.zip` from the `week-5` folder. 

There are 7 steps in their own folders. Open them up using your file navigator and favorite text editor, and follow the instructions.

## A quick reference of commands 
#### Navigating Files & Directories
- `ls` lists content of a directory. We can add flags, like `ls -l` or `ls -la` to list all files, and all hidden files, respectively
- `cd` changes the directory to a subfolder. If we want to move *up* a level, we can use `cd ..`
- `pwd` present working directory. By default. our working dir is the "root" directory, usually `/Users/ishaandey/`
- `rm` removes the file we specify
- `mv` moves the file we specify. It can also be used for *renaming* files, if we place it back in the same directory.
- `cat` renders the content of a file as text 

#### Python-y things we'll use
- `pip install`  
- `conda activate`

#### General things to know
- `*` wild cards: Matches anything
- `~` root direcory:
- `-flag` flags:
- `--option` options:
- `>` the pipe operator: 
- `^C` clear: 


## Acknowledgements
S/o to [Christian Jung](https://github.com/ChristianFJung) for help on today's lesson!