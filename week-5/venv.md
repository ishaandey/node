# Virtual Environments

```
What's a nice girl        /""\              ====     
like you doing in a      / o o              o o~~    
place like this?         _\ -/_            _\- /_      Looks like I've run my code 
                        /\\  //\          / \ /  \     in the wrong... environment
                       |  \\//  \        //| |  |\\ 
                       ||  \/  |\\       \\| |__|//
            ---------------------\()------(---||//-----
           /                                  ||)      \
          /                                   ==        \
         /                                               \
        ---------------------------------------------------
```
## Conda Cheatsheet
##### Why do we use virtual environments?
- Helps us **collaborate**, by telling others exactly what packages they need to get our code to work on their machine.  
- Prevents **version conflicts**, by ensuring that our code can access exactly the functions they need to run

##### Managing Environments
- `conda create -n <env name>`: Create a new environment
- `conda activate <env name>`: Activate the environment 
- `conda deactivate`: Deactivate the current environment

##### Installing Specific Packages
- `conda install <package name>`: The safe way to install a package into an environment
- `pip install <package name>`: Works if conda isn't installed, or if conda doesn't have the package

##### Manage all packages 
- `pip install requirements.txt`: Install all packages listed in the requirements.txt file
- `pip freeze > requirements.txt`: List all packages in the current environment, and send it to requirements.txt

## Why Virtual Environents
### Why bother?
Whenever we import a library, we're gaining access to all the Python functions that another developer has written. 

For example, when we `import pandas as pd`, and then call `pd.read_csv()`, we're telling the computer to find the files under the library pandas, so that we can specifically use the function `read_csv()`. Quite often, as in the case of Pandas, those libraries will have *their own dependencies*, aka libraries they rely on. 

The issue comes from the fact that these libraries are often under active development- anything from quick bug fixes to entire changes to functions and their uses.

Let's say we've made our own library that generates specialized heatmaps using plotly express. Now, a user who wants to use our functions can just install the latest version of our library, BUT may encounter issues if their version of Plotly was too old- Plotly express itself only came out during summer 2019, so anyone who installed plotly prior to that would be unable to use our library.

On the flip side, our library could be using functions that may have gotten deprecated, or dropped outright from the dependency. If the user's version of the dependency is too recent, they could again be unable to run the code we've given, because our library uses that deprecated function.   

**TLDR: Libraries can  have their own dependencies. That can cause trouble**

### Where virtual environments come in
Let's say we've been working on two distinct projects, one for creating a visual dashboard for some friend's data, another to predict out case counts of COVID-19. As you'd imagine, we'd need to use different libraries each project. In addition, our viz project may require version 2.0.0 of SciPy, but the COVID project may require version 1.0.0 instead. 

Virtual environments help us **isolate dependencies for each project**. We can create a list of only the packages we do need, so there aren't any unnecessary version conflicts when installing packages that aren't relevant to the project. Instead of being installed to the same location, we can have multiple copies (and thus multiple versions) available for our projects to use

To create a virtual environment with Anaconda, we can either use the GUI or command line:
On a bash shell, you'll likely see `(base)` preceeding the machine name. That refers to the base conda environment on which all your packages have so far been installed to.

To create a new environment, we'll use `conda create -n "node"`

We can enter into that environment using `conda activate node`, and exit via `conda deactivate`. 
Note how the environment name in bash changes to reflect our environment

To install a new package, we'll use `conda install <packagename>`. Why not `pip install`? At the risk of oversimplifing what's going on under the hood, the **conda package manager ends up being the safer way to go**. It checks that *all* of the environment dependencies are satisfied simulataneously, instead of prioritizing the most recent package, as pip does. Reserve `pip install` only for if the package you're looking for isn't coming up with conda (or if the machine you're on doesn't have conda, i.e. Google Colab).  

### Collaboration
The biggest benefit of environments, by far, is helping to share our code with others. Even if we're able to work out the exact right version for all our projects, we still (A) don't want our collaborators to be downloading *all* the packages we've ever pip installed, and (B) we want to make sure they get the same exact package versions.

For this, we'll use a `requirements.txt` file, simply a list of packages and their versions in our environment. For example:
```
numpy==1.18.1
pandas==1.0.3
scikit-learn==0.22.1
scipy==1.4.1
```
To produce this, we can use `pip freeze`, and `pip freeze > requirements.txt` to pipe the output into the .txt file.
On the flip side, we can install a list of dependencies given to us using `conda install --file requirements.txt`

### Takeaways
- Environments prevent **version conflicts**, by ensuring that our code can access exactly the functions they need to run
- They also help us **collaborate**, by telling others exactly what packages they need to get our code to work on their machine.  

## Activity
For now, create a new environment, call it `node`. Use the `requirements.txt` file in this repo to setup the installation.