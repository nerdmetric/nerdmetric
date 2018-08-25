"""
Pull Publons contribution info using API and ORCIDs.
"""
import json
import os.path as op

import requests
import pandas as pd

with open('/Users/tsalo/Documents/credentials/osf', 'r') as fo:
    token = fo.read().strip()

api_url = 'https://api.osf.io/v2/users/me/'
score_keys = ['merit', 'editor_merit']


def populate_database():
    usernames = op.abspath(op.join(op.dirname(__file__),
                                   '../database/ids.json'))
    with open(usernames, 'r') as fo:
        usernames = json.load(fo)

    # Create dictionary of orcid: orcid pairs.
    usernames = {user: usernames[user]['orcid'] for user in usernames.keys()
                 if 'orcid' in usernames[user].keys()}
    usernames = {v: k for k, v in usernames.items()}

    out_df = pd.DataFrame(columns=score_keys, index=usernames.keys())
    for user_orcid in usernames.keys():
        get_url = api_url.format(user_orcid)
        print(get_url)

        response = requests.get(get_url,
                                headers={'Authorization': 'Token {0}'.format(token),
                                         'Content-Type': 'application/json'})
        if response.ok:
            user_dict = response.json()
            print(user_dict)
            scores = [user_dict.get(key) for key in score_keys]
        else:
            print(response)
            scores = [None for _ in score_keys]

        out_df.loc[user_orcid] = scores

    # Save to csv
    out_file = op.abspath(op.join(op.dirname(__file__),
                                  '../database/contributions/'
                                  'osf.csv'))
    out_df.to_csv(out_file, index_label='id')


if __name__ == '__main__':
    populate_database()
