import json 
import io, os, sys

fpath = input('Input path to .ipynb answer key: ')
outdir = input('Output directory: ')
fname = fpath.split('/')[-1].split('.')[0]
outpath = outdir+'/'+fname.replace('_key','_notes')+'.ipynb'
print(outpath)

def main():
    with open(fpath) as f:  
        nb_key = json.load(f)

    nb_notes = nb_key 

    for index, cell in enumerate(nb_notes['cells']):
        if 'answer' in str(cell['metadata']):
            nb_notes['cells'][index]['source'] = ""

    with open(outpath, 'w') as outfile:
        json.dump(nb_notes, outfile)

if __name__ == "__main__":
    main()


# @click.group()
# def main():
#     """
#     Simple CLI for converting answer keys into workshop-ready interactive Python notebooks
#     """
#     pass

# @main.command()
# @click.argument('fpath', help='File path of answer key')
# # @click.argument('--outdir', help='Directory to output notebook')

# def create(fpath):
#     """
#     Remove cells w/ metadata marked as key
#     """
#     with open(fpath, 'r') as f:  
#         nb = json.load(fpath)
#     print(nb)
#     click.echo(nb)

# if __name__ == "__main__":
#     main()