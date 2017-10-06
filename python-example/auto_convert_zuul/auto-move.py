#!/usr/bin/python

import os
import yaml
import shutil
import sys

HEADER_FILE = '/home/stack/infra-openstack/openstack-zuul-jobs'
CURRENT_PATH = os.getcwd()


def read_yaml(name_file):
    with open(name_file, 'r') as f:
        content_dict = yaml.safe_load(f)
    return content_dict


def copy_file(srs, des):
    if not os.path.exists(os.path.dirname(des)):
        try:
            os.makedirs(os.path.dirname(des))
        except OSError as exc:
            raise exc
    # Copy file:
    shutil.copyfile(srs, des)


def auto_move(contents):
    """
    :param contents: This content that is loaded from .zuul.yaml
    """
    i = 0
    for job in contents:
        run = job.get('job').get('run') + '.yaml'
        path_run_src = HEADER_FILE + '/' + run
        path_run_des = CURRENT_PATH + '/' + run
        path_run_des_rename = path_run_des.replace('dsvm', 'devstack')
        # Start moving
        copy_file(path_run_src, path_run_des)
        post = job.get('job').get('post-run') + '.yaml'
        path_post_src = HEADER_FILE + '/' + post
        path_post_des = CURRENT_PATH + '/' + post
        path_post_des_rename = path_post_des.replace('dsvm', 'devstack')
        # Start moving
        copy_file(path_post_src, path_post_des)


def main():
    input_file = CURRENT_PATH + '/' + sys.argv[1]
    content_dict = read_yaml(input_file)
    auto_move(content_dict)


if __name__ == '__main__':
    main()

