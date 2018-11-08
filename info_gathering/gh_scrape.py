#!/usr/bin/env python
'''
Example of information gathering from 
a targeted github user.
[Dependency]
    pip install github3.py
[Usage]
    python gh_scrapy.py <gh_username>
'''
from github3 import login

def gh_usr_stats(gh_username, gh):
    gh_usr = gh.user(gh_username)
    print(gh_usr.name)
    print(gh_usr.login)
    print(gh_usr.followers_count)
    print('Users followed by %s:' % gh_username)
    for f in gh.followed_by(gh_username):
        print(f)
    print('Users %s following:' % gh_username)
    for f in gh.followers_of(gh_username):
        print(f)
    try:
        print('Organization: ' + gh_usr.organization(gh_username))
    except:
        pass



if __name__ == '__main__':
    import sys
    gh_usr = sys.argv[1]
    gh_pwd = sys.argv[2]
    gh = login(gh_usr, password=gh_pwd)
    gh_username = sys.argv[3]
    gh_usr_stats(gh_username, gh)

