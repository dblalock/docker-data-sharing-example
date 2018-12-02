#!/usr/bin/env python

from __future__ import print_function

import os
import shutil
import tempfile

# Note: macOS uses /var by default, which is off limits to docker unless you
# add it in the docker settings
HOST_TEMP_DIR_ROOT = '/tmp'

CONT_APP_HOME = '/home/appuser/app'
CONT_IN_DIR = CONT_APP_HOME + '/in'
CONT_OUT_DIR = CONT_APP_HOME + '/out'
CONT_NAME = 'foo'


def run_cmd(cmd):
    print(cmd)
    os.system(cmd)


def make_container():
    run_cmd('docker build container -t {}'.format(CONT_NAME))


def run_container():
    in_dir = tempfile.mkdtemp(dir=HOST_TEMP_DIR_ROOT)
    out_dir = tempfile.mkdtemp(dir=HOST_TEMP_DIR_ROOT)

    input_file = os.path.join(in_dir, 'input.txt')
    with open(input_file, 'w') as f:
        f.write("hello container, I'm the host!")

    mount_in_args = "type=bind,source={},target={},readonly".format(in_dir, CONT_IN_DIR)
    mount_out_args = "type=bind,source={},target={}".format(out_dir, CONT_OUT_DIR)

    cmd = 'docker run --rm --network="none" --mount {} --mount {} {}'.format(
        mount_in_args, mount_out_args, CONT_NAME)

    run_cmd(cmd)

    with open(os.path.join(out_dir, 'out.txt'), 'r') as f:
        print("HOST: read back data:\n'{}'".format(f.read()))

    shutil.rmtree(in_dir)
    shutil.rmtree(out_dir)


if __name__ == '__main__':
    make_container()
    run_container()
