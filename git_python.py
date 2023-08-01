import git
import os
path = os.getcwd()+ "sameple_repo"

git_clone_url = "url"

branch_name = "automation_branch"

# clone step
try:
    repo = git.Repo.clone_from(git_clone_url,path) #when we run this again this will give error because this folder is not empty
except git.exc.GitCommandError:
    print("Repo already exist")
    repo = git.Repo(path)

try:
    repo.git.checkout("-b","new_branch") # this will create new branch if this branch this will raise error
except git.exc.GitCommandError:
    repo.git.checkout("new_branch")

try:
    repo.git.add("--all")
    repo.git.commit('-m',"sample_commit", authour = "mailid")
except git.GitCommandError:
    print("nothing to add")

origin = repo.remote(name ="origin")
origin.push()
