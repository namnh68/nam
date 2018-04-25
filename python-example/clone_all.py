# -*- coding: utf-8 -*-
import requests
import commands
import os


OWNER = raw_input('Github user: ')
# FOLDER = raw_input('Folder to save: ')
URL = 'https://api.github.com/users/%s/repos' % OWNER
FILE = '%s_repos.txt' % OWNER
try:
    TOKEN = os.environ['token_github']
except KeyError:
    print("You must add your token as variable enviroment by running this 
          "command on bash shell: export token_github=your_token")



def get_repo_from_api():
    page = 1
    repos = []
    headers = {
        "Authorization": "token {}".format(TOKEN)}

    requests.packages.urllib3.disable_warnings()
    print('Collecting data from Github...')
    while True:
        print('Collecting page %s' % page)
        r = requests.get(URL + '?page=%s' % page, headers=headers)
        if not r.ok:
            print('Failed to connect to Github')
            print('Try again...')
            continue
        content = r.json()
        repos += [i['clone_url'] for i in content]
        if len(content) == 30:
            page += 1
            continue
        break
    with open(FILE, 'w') as f:
        for repo in repos:
            f.write(repo + '\n')
    return repos

def create_folder(name_folder):
    full_path = os.path.join(os.getcwd(), name_folder)
    if os.path.exists(full_path):
        print('No need to create the {0} folder'.format(name_folder))
        os.chdir(full_path)
    else:
        print('Need to create the {0} folder first'.format(name_folder))
        os.makedirs(full_path)
        os.chdir(full_path)

def get_repo_from_file(file):
    repos = []
    with open(file) as f:
        for line in f:
            repos.append(line.strip())
    return repos


def clone_repo(repos):
    print('There are %s repos.' % len(repos))
    for repo in repos:
        cmd = 'git clone ' + repo
        print(cmd)
        print(commands.getstatusoutput(cmd)[1])


def main():
    if os.path.isfile(FILE):
        repos = get_repo_from_file(FILE)
    else:
        repos = get_repo_from_api()
    create_folder(OWNER)
    clone_repo(repos)


if __name__ == '__main__':
    main()
