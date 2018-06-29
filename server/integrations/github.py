from time import sleep
import numpy as np
import pandas as pd
from github import Github

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
    out_name = 'github__{0}__{1}'.format(owner, repo_name)

    r = github_user.get_user(owner).get_repo(repo_name)
    stats = r.get_stats_contributors()
    c_list = []
    for contributor in stats:
        c_list.append([contributor.author.login, contributor.total])
    out_df = pd.DataFrame(data=c_list, columns=['username', 'count'])
    out_df.set_index('username')
    repo_users = out_df.index.values
    keep_users = [user for user in usernames if user in repo_users]
    out_df = out_df.loc[keep_users]
    out_df.to_csv('../database/{0}.csv'.format(out_name), index_label='id')
