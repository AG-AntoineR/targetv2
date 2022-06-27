import git

rw_dir = '/home/antoine/Bureau/targetrepo'
repo = git.Repo(rw_dir)

def commit(repo):
    repo.git.add('--all')
    repo.git.commit('-m', 'python commit')
    repo.git.push()

commit(repo)
#git_push = "git add -A ; git commit -m 'Python commit' ; git push --repo  https://AG-AntoineR:Megalovania2000@bitbucket.org/targetv2.git --all "
#git.push("--repo https://AG-AntoineR:Megalovania2000@bitbucket.org/targetv2.git --all")