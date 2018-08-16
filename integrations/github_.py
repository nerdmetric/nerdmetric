"""
Pull contribution info for whitelisted GitHub repositories using pygithub,
GitHub IDs, and ORCIDs.
"""
import os.path as op
from time import sleep
import numpy as np
import pandas as pd
from github import Github
import json

with open('/Users/tsalo/Documents/credentials/github', 'r') as fo:
    pw = fo.read().strip()
github_user = Github('tsalo', pw)


def pull_contributors(repo, usernames):
    """
    TODO: Replace pygithub with something that can pull issues, comments,
    commits, lines, etc.
    LABHR/octohatrack might be the way to go
    """
    owner, repo_name = repo.split('/')
    out_name = '{0}__{1}'.format(owner, repo_name)

    # Load contributions from GitHub
    r = github_user.get_user(owner).get_repo(repo_name)
    stats = r.get_stats_contributors()
    c_list = []
    for contributor in stats:
        c_list.append([contributor.author.login, contributor.total])

    # Reduce set of users based on users in nerdmetric database
    out_df = pd.DataFrame(data=c_list, columns=['username', 'count'])
    repo_users = out_df['username'].values
    keep_users = [user for user in usernames.keys() if user in repo_users]
    out_df = out_df.loc[out_df['username'].isin(keep_users)]

    # Replace GitHub IDs with ORCIDs
    out_df['username'] = out_df['username'].replace(usernames)
    out_df.set_index('username', inplace=True)

    # Save to csv
    out_file = op.abspath(op.join(op.basename(__file__),
                          ('../database/contributions/'
                           'github/{0}.csv').format(out_name)))
    out_df.to_csv(out_file, index_label='id')


def populate_database():
    usernames = op.abspath(op.join(op.basename(__file__),
                           '../database/ids.json'))
    with open(usernames, 'r') as fo:
        usernames = json.load(fo)

    # Create dictionary of github: orcid pairs.
    usernames = {user: usernames[user]['github'] for user in usernames.keys()
                 if 'github' in usernames[user].keys()}
    usernames = {v: k for k, v in usernames.items()}

    whitelist = op.abspath(op.join(op.basename(__file__),
                           '../database/github_repositories.txt'))
    with open(whitelist, 'r') as fo:
        whitelist = [l.strip() for l in fo.readlines()]

    for repo in whitelist:
        pull_contributors(repo, usernames)
        sleep(5)


if __name__ == '__main__':
    populate_database()
