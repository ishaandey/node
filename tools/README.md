# Tools for GitHub

## `convertKey.py`
From bash, type `python3 tools/convertKey.py`, and follow the instructions to generate the notes notebook for a corresponding workshop key.
To identify cells to mark, edit the tags of each cell in the .ipynb file from Jupyter Lab. In the command line, specify which tags to remove to **clear the code only** - the output will still be displayed. 

## [files.node.ishaandey.com]([http://files.node.ishaandey.com])
The mirror for this repo is powered by Vercel (Formerly Zeit Now).
`vercel.json` controls config for the Vercel Git integration
`.nowignore` removes file from static hosting on the mirror