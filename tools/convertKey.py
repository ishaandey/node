import json 
import io, os, sys

fpath = input('Input path to .ipynb answer key: ')
outdir = input('Output directory: ')
tags = input('Tags to remove (seperate by space): ').lower()

fname = fpath.split('/')[-1].split('.')[0]
outpath = outdir+'/'+fname.replace('_key','_notes')+'.ipynb'
print(outpath)

def main():
    with open(fpath) as f:  
        nb_key = json.load(f)

    nb_notes = nb_key 

    for index, cell in enumerate(nb_notes['cells']):
        for tag in tags.split():
            if tag in str(cell['metadata']):
                nb_notes['cells'][index]['source'] = ""

    with open(outpath, 'w') as outfile:
        json.dump(nb_notes, outfile)

if __name__ == "__main__":
    main()
