#!/usr/bin/env python
# -*- coding: utf-8 -*-
# To get commit and review
# Dependency packages: requests-futures==0.9.7
import json
from requests_futures.sessions import FuturesSession

user_id = 'namnh'
release = 'queens'
review_commit = ['marks', 'commits']
future_session = FuturesSession()
url_form = 'http://stackalytics.com/api/1.0/stats/engineers?user_id={}' \
      '&release={}&metric={}'

header = {
    'Content-type': 'application/dict'
}


def get_number_review():
    url = url_form.format(user_id, release, 'marks')
    output = future_session.get(url, headers=header)
    result_str = output.result().content
    result_dict = json.loads(result_str)
    try:
        review = result_dict['stats'][0]['metric']
    except Exception:
        return 0
    return review


def get_number_commit():
    url = url_form.format(user_id, release, 'commits')
    output = future_session.get(url, headers=header)
    result_str = output.result().content
    result_dict = json.loads(result_str)
    try:
        commit = result_dict['stats'][0]['metric']
    except Exception:
        return 0
    return commit


def main():
    review = get_number_review()
    commit = get_number_commit()
    review_str = 'The number of review from {} is: {}'.format(user_id, review)
    commit_str = 'The number of commit from {} is: {}'.format(user_id, commit)
    print review_str
    print '======================================'
    print commit_str
    print 'Thanks for using!'


if __name__ == '__main__':
    main()
