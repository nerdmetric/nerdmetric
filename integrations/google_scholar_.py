"""
Pull number of preprints for different archives using Google Scholar and
Google Scholar IDs.
"""
import json
import os.path as op

import requests
import pandas as pd
import scholarly


score_keys = ['arXiv', 'bioRxiv', 'psyRxiv']


def populate_database():
    usernames = op.abspath(op.join(op.basename(__file__),
                                   '../database/ids.json'))
    with open(usernames, 'r') as fo:
        usernames = json.load(fo)

    # Create dictionary of orcid: orcid pairs.
    usernames = {user: usernames[user]['scholar'] for user in usernames.keys()
                 if 'scholar' in usernames[user].keys()}
    usernames = {v: k for k, v in usernames.items()}

    out_df = pd.DataFrame(columns=score_keys, index=usernames.keys())
    for user_orcid in usernames.keys():
        pass

        out_df.loc[user_orcid] = scores

    # Save to csv
    out_file = op.abspath(op.join(op.basename(__file__),
                                  '../database/contributions/'
                                  'scholar.csv'))
    out_df.to_csv(out_file, index_label='id')


if __name__ == '__main__':
    populate_database()
