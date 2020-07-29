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

Git is a fantastic versioning system, and there are *tons* of resources available online to help you learn / practice. This page will just cover the basics to get you on your feet, and is by no means a full list of all the amazing things Git and GitHub allow you to do. 

## The Big Picture

### Git 
Let's say we want to start a new project, looking at some star wars data. We start out with an empty project folder `star-wars/`, and add `characters.csv`, `planets.csv`, & `viz.ipynb`. Currently, our local directory (our laptop's folder) looks like this: 

```
└── star-wars
    ├── datasets
    │   ├── characters.csv
    │   └── planets.csv
    └── viz.ipynb
```

As we're cleaning the datasets, we accidentally write over some data in `planets.csv`, and the correct data is permanently lost. Luckily, we've been using a Git repository, so we just rollback to a previous version, and continue coding.

**Git** is a version control system. Much in the way Microsoft Word or Google Docs allow us to look back at previous versions of a document, Git gives us the ability to track changes to a project.

Git does this by taking a **series of snapshots** of the project over time. Everytime we save the state of the project, or **commit**, Git takes a picture of what all the files looked like just in that moment of time. It stores this information in a "database" of sorts. 

When we take a look at these changes, we can view a quick summary of what changed. For example with `planets.csv`:
```diff
name, climate, terrain, population
Alderaan, temperate, grasslands, 2 billion
Hoth, frozen, tundra, NA
Endor, temperate, forests, 30 million
- Naboo, temperate, grassy hills, 4.5 billion
+ Naboo, temperate, forests, 4.2 billion
```

In fact, every time a file in our project changes at all, git recognizes and remembers the change. That information gets stored into a hidden git "database", also known as a **git repository**.

```
└── star-wars
    ├── .git
    │   └── ...
    ├── datasets
    │   ├── characters.csv
    │   └── planets.csv
    └── viz.ipynb
```

### GitHub
Let's say we'd like to share our project with a friend, who wants to build a machine learning model from our data. 

**GitHub** makes collaboration super easy. To be clear, *GitHub* is entirely seperate from *git*. GitHub is an *online platform* that hosts repositories, using the git version control system.

Getting our existing code online is increadibly easy. Since we've already initialized the repository locally, we just create a corresponding repo on GitHub, and tell our local repo to connect to that particular remote repo. 

All our friend has to do is **clone**, or download a copy of the remote repo to her laptop. 

Whenever she's made edits that she'd like to share, she can **push** those commits from (her) local to the remote repo. To bring her changes into my local repo, I can **pull** her commits down.

![Source: Git-It](../screenshots/remotes.png)

That's it! There's a lot more to Git, including Branching and Pull Requests, but this is enough to get us started.

___

## The Basic Workflow
We've already covered most, if not all of the basics of working with Git. Let's walk through an example:

At any point, use `git --help` or `git <command> --help` to pull up help pages

### Set Up Remote
1. Let's start by **navigating** to your node directory:
  1. Open the bash shell of your choice (For MacOS: use `Terminal`; For Windows: use `Git Bash`)
  2. Usig the commands from [bash.md](bash.md), `cd` into your directory for node (use `mkdir` if you don't have a node folder). 
2. **Initialize** the repository with `git init`:
    1. This creates a hidden `.git` directory, which we can now reveal with `ls -la`
3. **Stage** all changes using `git add .`. What is staging, you ask? When Git detects a change to a file, we must place it into one of 3 distinct stages:
    a. **Modified** means that the file is changed, but isn't yet *saved to the repo*. This occurs by default.
    b. **Staged** means we've *marked the modified file* *as ready* to enter into the next commit.
    c. **Committed** means that the snapshot, containing only the staged edits, is now saved to the repo.

![Source: Git SCM](../screenshots/staging.png)

4. **Commit** these changes to the *local* repo using `git commit -m "First commit"` 

5. In order to push our changes up to a remote repository, we first need to **create a GitHub repo**
    1. Open up `GitHub Desktop`. On the top left, hit `Add`, then `Add existing repository`
    2. Hit `choose`, then navigate to the directory where you've been working     
    3. Click `Publish repository`, add a description and make the repo public if you'd like, then publish.

6. Now that we have a `remote` repo set up, we can confirm its location using `git remote -v`
    1. This should now point to a link, something like <https://github.com/ishaandey/node.git>

7. **Push** the commits to remote using `git push`

### Add Changes
1. Head over to your online GitHub repository (github.com/username/reponame) 
    *  Make sure you're signed in properly

2. Create a new file online by clicking the `new file` button: call it `hello.txt`
    *  GitHub will ask you to save your changes with a commit (it automatically staged them)
    *  Because this is already the remote repo, there's no need to push/pull: the changes are directly commited to remote

3. However, our local directory doesn't have those changes just yet. We need to **pull** those commits down to local. 
    - We could either: (a) go to GitHub Desktop, and click the `fetch & pull` icon
    - Or (b) from the command line, type `git pull`

4. With a text editor, add a few lines to `hello.txt`. Be sure to save!
    - Git now knows a file has been changed, but hasn't yet saved that snapshot to the local repo

5. **Stage** these changes using `git add hello.txt`
    - If we modified multiple files, all of which we'd like to stage, we could simply use `git add .`

6. **Commit** these changes, using `git commit -m "Added some lines"`
    - The `-m` flag allows us to attach a message to the commit- This is super helpful for annotating edits

6. Finally, **push** these changes to the remote rep using `git push`. 
    - If all is well, you should now be able to see those new lines online!

You're done! This is the basic workflow of Git. We modify files, stage then commit them. We push changes to remote, and pull changes to local.

**Draw a quick diagram of this workflow**, just to make sure you understand the basic idea here. Draw your laptop (local), the GitHub server (remote), the commands to interact between the two, as well as the commands to save changes locally.

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
- https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F
- https://nvie.com/posts/a-successful-git-branching-model/
- https://github.com/jlord/git-it-electron

