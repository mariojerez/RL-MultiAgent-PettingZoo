# RL-MultiAgent-PettingZoo
A Reinforcement Learning model of muliple agents simulated in PettingZoo

We are building off of the Simple Spread environment in the pettingzoo library.
https://pettingzoo.farama.org/environments/mpe/simple_spread/

# Getting Started as a Contributor
Be sure that your version of Python is between 3.8 and 3.11. 3.12 is not supported yet. To get started, clone this git repository. Within it, create a virtual environment. Once you're running the virtual environment, install the dependencies found in requirements.txt. For example, if using venv from the mac terminal,
```console
> cd RL-MultiAgent-PettingZoo # change directory to the repo
> python -m venv venv # create a virtual environment (venv) in a folder called venv.
> source venv/bin/activate # activate virtual environment
> python -m pip install -r requirements.txt # install dependencies listed in requirements.txt
```

## Useful git commands
```console
## Create new branch
git clone [url]
git pull # pulls changes from repo. Do this frequently and before making changes.
git branch [branch_name] # Create a new branch
git branch # shows what branch you're on
git switch [branch_name] #switch to new branch

## Stage files to be committed
git status # See changes you've made, and changes you've added, and changes that are uncommitted. Use frequently.
git add [file_name] # Stage changes you made to a spefific file.
git add --all # Stage all changes you made, preparing to be committed
git reset # undoes git add if you decide you don't want to stage something
git commit -m "[enter commit comment, maybe mention issue #[issuenum]]

## merge changes to main
git switch main # switch to main branch
git merge [other_branch] # merges changes from other_branch to main.
git branch -d [other_branch] # delete the branch when you're done using it.

## move local changes to the repository
git push # pushes changes to repository
```

A good practice is to create an issue for whatever you want to fix or work on, and then create a branch to work on that specific issue. Mention the issue number in the commit message and close the issue after you've merged to the main branch. Thoughtful comments are always helpful.