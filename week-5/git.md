# Getting into Git
       
```
     git clone    git clone   git clone         git remote -v   

        /__\        /__\        /__\                 /__\    
       | <><|      | <><|      | <><|               |><> |   
       (__/\)      (__/\)      (__/\)            .  (/\__)   
      /      \    /      \    /      \           | /      \  
      ||/(===o    ||/(===o    ||/(===o           I || __ |\\ 
      | /  \ |    | /  \ |    | /  \ |           I// /  \| ||
      \/][][\/    \/][][\/    \/][][\/          (I/ [][][] ||
       |\  /|      |\  /|      |\  /|           ,]  |\  /| ' 
       |_||_|      |_||_|      |_||_|           []  |_||_|   
       [ ][ ]      [ ][ ]      [ ][ ]           []  [ ][ ]   
       | || |      | || |      | || |           /|  | || |   
       |_||_|      |_||_|      |_||_|          / |  |_||_|   
_______[_][_]______[_][_]______[_][_]____________|__[_][_]____
```

Git is a fantastic versioning system, and there are *tons* of resources available online to help you learn / debug (see Acknowledgements below). This document will just cover the basics to get you on your feet, and is by no means a full list of all the amazing things Git and GitHub allow you to do. 

## How Does Git Work?

**Git** is a version control system. Much in the way MS Excel or Google Docs allow us to look back at previous versions of a document, Git tracks changes to a project over time. 

Git "thinks of its data more like a **series of snapshots** of a miniature filesystem. With Git, every time you commit, or save the state of your project, Git basically takes a picture of what all your files look like at that moment and stores a reference to that snapshot."

When we take a look at these snapshots, we can see quick summaries of what changes were made: 
```diff
Sandtrooper: How long have you had these droids?
Luke Skywalker: About three or four seasons.
Ben Kenobi: They're for sale if you want them.
Sandtrooper: Let me see your identification.
- Ben Kenobi: These aren't the droids you're looking for.
+ Sandtrooper: These aren't the droids we're looking for.
```

We can think about changes to our files occuring in 3 distinct stages.
From the [handbook](https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F):
1. **Modified** means that you have changed the file but have not committed it to your database yet.
2. **Staged** means that you have marked a modified file in its current version to go into your next commit snapshot.
3. **Committed** means that the data is now safely stored in your local database.

This "database" we refer to is called a local git repository (repo for short).

![areas](screenshots/areas.png)
___
In practice, this workflow isn't all that complicated.
Let's say we make a couple of modifications to our project: We add a few lines to `resistance.py`. We also made some additions to `princessleia.csv`, but we don't have those changes yet complete.

1. All of these changes are currently just showing as 'modified' in our working tree
2. We can selectively choose which files we want to be part of our next commit, by "staging them".
        For example, we can stage `resistance.py` only, using `git add resistance.py`
3. We can `commit` these changes, which takes all files from the staging area, and stores that snapshot permanently into the Git directory.
        With the command line, we can commit these changes (and describe it) using `git commit -m "Finish Episode VII"` 

## GitHub
This is all wonderful and great, but how exactly does this allow us to collaborate with others? This is where tools like GitHub come in.
To be extra clear, GitHub is NOT the same as Git. If git is a versioning control software, GitHub is a cloud-based tool that uses Git in order to mainitain repositories online.

GitHub allows us to do some amazing things, including allowing for easy collaboration with folks outside the team (Pull Requests, Issues). In fact, this repository uses a third party integration to deploy all the files to a mirror using GitHub Actions.

Conceptually, the only addition here is that every so often we can `pull` changes from a central Git repo hosted online at GitHub, and `push` changes that we make back onto that same server. This diagram from [Git-It](https://github.com/jlord/git-it-electron) does a great job explaining it.

![remotes](screenshots/remotes.png)

### Practice!
Using the command line & the GitHub Desktop application, we can do everything we need from git commands. 
At any point, use `git --help` or `git <command> --help` to pull up help pages
##### Initializing the Repo
1. Let's start by **navigating** to your node directory
        1. Open the bash shell of your choice (For MacOS: use `Terminal`; For Windows: use `Git Bash`)
        2. Using the commands from [bash.md](bash.md), `cd` into your directory for node (use `mkdir` if you don't have one). 
2. **Initialize** the repository with `git init`
        1. Alternatively, we could use `git clone <somelinkfromgithub.git>` to copy a remote repo to our local disk
3. **Stage** all files using `git add .`
4. **Commit** these to the local repo using `git commit -m "First commit"` 
5. In order to push our changes to a remote origin, we first need to **create a github repo**
        1. Open up `GitHub Desktop`. On the top left, hit `Add`, then `Add existing repository`
        2. Hit `choose`, then navigate to the directory where you've been working
        3. Click `Publish repository`, add a description and make the repo public if you'd like, then publish.
6. Now that we have a `remote` repo set up, we can confirm its location using `git remote -v`
        1. This should now point to a link, something like <https://github.com/ishaandey/node.git>
7. **Push** these changes to remote using `git push`. Check out your githib repo at github.com/username/reponame!

##### Adding changes to the repository
1. Before we do this, first head over to your online GitHub repository (github.com/username/reponame) 
2. Create a new file there, let's call it `hellothere.txt`
3. Now going back to the command line, we need to **pull** those changes down to local
        1. We could also go to GitHub Desktop, and click the fetch & pull icon
4. With a text editor, open up the file, and add a few lines to `hellothere.txt`. We've now made an edit that isn't yet online.
5. Following the steps from above, **stage** and **commit** these changes 
        1. Remember that `git add .` stages all the files that have been changes
        2. Don't forget to add a commit message with ` -m "message"`
6. Finally, **push** these changes to the remote repo. If all is well, you should now be able to see those new lines online!

## Branching
Branching is a key feature that allows us to keep production-ready, stable code seperate from the development code, where we're likely to experiment and break things as we go along. 

There are tons of workflows that describe this process. The one I've been using for the node repository uses `master`/`develop`/`feature` branches, based on the model [described here](https://nvie.com/posts/a-successful-git-branching-model/).

```
.          __---__
    .   .-'...:...'-.               .          .
       / .  . : .__ .\                                         .
.     /........./  \ .\  .   .              git checkout -b         .
     / :  :   :| () | :\                  .        .
    :...........\__/....:         .                             .
    |___________________|              .        |    |  .                .
    |...................|               .       |    |
    :  :  :   :   :   : :                       |=()=|          .
  .  \................./      .            .    |    |
      \  .  . : .  .  /                         |  . |           .
   .   \._........._./  .        .                   .
          -..___..-                .         .             .                .
                      .                                               .
    .    origin/master                   .               .       
                                 .              .                         .    
```  

## Practice on your own:
[Git-It](https://github.com/jlord/git-it-electron)

## Acknowledgements
The diagrams here are taken from the following sources:
- https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F
- https://nvie.com/posts/a-successful-git-branching-model/
- https://github.com/jlord/git-it-electron

