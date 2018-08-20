"""
Looks up contributions for a users, grabbing from database, which is split into
three app types: 'code', 'data', and 'resources'.
"""
import json
import os.path as op

import pandas as pd

from resource_schemata import CODE_SCHEMA, DATA_SCHEMA, RESOURCE_SCHEMA

global IDS
with open('database/ids.json', 'r') as fo:
    IDS = json.load(fo)


def get_app_contributions(id_, app_name, columns):
    df = pd.read_csv('database/contributions/{0}.csv'.format(app_name), index_col='id')
    if id_ not in df.index:
        return {}
    else:
        contributions = df.loc[id_, columns].to_dict()
        return contributions


def get_contributions(orcid):
    if orcid not in IDS.keys():
        raise ValueError('ORCID not found in database.')

    contribs = {}
    # Code first
    contribs['code'] = {}
    for app in CODE_SCHEMA.keys():
        id_type = CODE_SCHEMA[app]['id_type']
        id_ = IDS[orcid].get(id_type, None)
        contrib_types = CODE_SCHEMA[app]['scores']
        if id_ is not None:
            contribs['code'][app] = get_app_contributions(id_, app,
                                                          contrib_types)
        else:
            contribs['code'][app] = {t: 0 for t in contrib_types}

    # Data next
    contribs['data'] = {}
    for app in DATA_SCHEMA.keys():
        id_type = DATA_SCHEMA[app]['id_type']
        id_ = IDS[orcid].get(id_type, None)
        contrib_types = DATA_SCHEMA[app]['scores']
        if id_ is not None:
            contribs['data'][app] = get_app_contributions(id_, app,
                                                          contrib_types)
        else:
            contribs['data'][app] = {t: 0 for t in contrib_types}

    # Resources last
    contribs['resources'] = {}
    for app in RESOURCE_SCHEMA.keys():
        id_type = RESOURCE_SCHEMA[app]['id_type']
        id_ = IDS[orcid].get(id_type, None)
        contrib_types = RESOURCE_SCHEMA[app]['scores']
        if id_ is not None:
            contribs['resources'][app] = get_app_contributions(id_, app,
                                                               contrib_types)
        else:
            contribs['resources'][app] = {t: 0 for t in contrib_types}

    return contribs


def merge_contributions():
    orcids = IDS.keys()
    df = pd.DataFrame(index=orcids)

    # Code first
    for app in CODE_SCHEMA.keys():
        f = 'database/contributions/{0}.csv'.format(app)
        if op.isfile(f):
            temp_df = pd.read_csv(f,
                                  index_col='id')
            temp_df = temp_df[CODE_SCHEMA[app]['scores']]
            col_prefix = 'code_____' + app.replace('/', '___') + '____'
            temp_df.columns = [col_prefix + col for col in temp_df.columns]
            df = df.join(temp_df, how='outer')

    # Data next
    for app in DATA_SCHEMA.keys():
        temp_df = pd.read_csv('database/contributions/{0}.csv'.format(app),
                              index_col='id')
        temp_df = temp_df[DATA_SCHEMA[app]['scores']]
        col_prefix = 'data_____' + app.replace('/', '___') + '____'
        temp_df.columns = [col_prefix + col for col in temp_df.columns]
        df = df.join(temp_df, how='outer')

    # Resources last
    for app in RESOURCE_SCHEMA.keys():
        temp_df = pd.read_csv('database/contributions/{0}.csv'.format(app),
                              index_col='id')
        temp_df = temp_df[RESOURCE_SCHEMA[app]['scores']]
        col_prefix = 'resource_____' + app.replace('/', '___') + '____'
        temp_df.columns = [col_prefix + col for col in temp_df.columns]
        df = df.join(temp_df, how='outer')

    df.to_csv('all_contributions.csv', index=True, index_label='orcid')


if __name__ == '__main__':
    merge_contributions()
