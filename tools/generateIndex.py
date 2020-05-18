import io, os, sys

fpath = input('Input path to README.md: ')
outpath = fpath.replace('README','index')
print(outpath)

def main():
    with open(fpath) as f:  
        file_ = f

    with open(outpath, 'w') as outfile:
        outfile = file_

if __name__ == "__main__":
    main()
