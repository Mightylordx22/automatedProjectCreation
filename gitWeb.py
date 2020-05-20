import os
import sys
from github import Github as gUser
from time import sleep

folderName = str(sys.argv[1])
projectName = str(sys.argv[2])

access_token = os.environ.get("gAccess")
username = os.environ.get("gUsername")
path = os.environ.get("projectPath")

directory = f"{path}/{folderName}/{projectName}"

auth = gUser(access_token)
user = auth.get_user()
login = user.login
repo = user.create_repo(f"{projectName}", private=True)

commands = [f'echo # {repo.name} >> README.md',
            'git init',
            f'git remote add origin https://github.com/{username}/{projectName}.git',
            'git add .',
            'git commit -m "Initial commit"',
            'git push -u origin master']

os.mkdir(directory)
os.chdir(directory)

for i in commands:
    os.system(i)

os.system("code .")
