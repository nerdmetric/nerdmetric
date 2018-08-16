import os.path as op
from time import sleep
import numpy as np
import pandas as pd
import requests
import json

with open('/Users/tsalo/Documents/credentials/publons', 'r') as fo:
    token = fo.read().strip()

api_url = 'https://publons.com/api/v2/academic/{0}/'
score_keys = ['merit', 'editor_merit']


def populate_database():
    usernames = op.abspath(op.join(op.basename(__file__),
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

        response = requests.get(get_url,
                                headers={'Authorization': 'Token {0}'.format(token),
                                         'Content-Type': 'application/json'})
        if response.ok:
            user_dict = response.json()
            scores = [user_dict.get(key) for key in score_keys]
        else:
            scores = [None for _ in score_keys]

        out_df.loc[user_orcid] = scores

    # Save to csv
    out_file = op.abspath(op.join(op.basename(__file__),
                                  '../database/contributions/'
                                  'publons.csv'))
    out_df.to_csv(out_file, index_label='id')


if __name__ == '__main__':
    populate_database()
