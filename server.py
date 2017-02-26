#!/usr/bin/env python3

import os
import signal
from threading import Thread
from datetime import datetime
from time import sleep
from subprocess import Popen
import shlex

from bottle import run, get, request, HTTPResponse


def fetch_unix_time():
    return int(datetime.now().timestamp())


def run_cmd(cmd, start_time, duration):
    unix_time = fetch_unix_time()
    sleep(start_time - unix_time)

    print(cmd, flush=True)
    cmd = "timeout {} {}".format(duration, cmd)

    p = Popen(cmd, shell=True)
    p.wait()


@get('/trigger')
def trigger():
    group_id = request.query.group_id
    start_time = request.query.start_time
    duration = request.query.duration
    hashtag = request.query.hashtag
    hashtag = hashtag.replace('#', '\#')

    start_time = fetch_unix_time()
    print(start_time, flush=True)

    cmd = 'php filter-oauth.php {} {}'.format(group_id, hashtag)
    Thread(target=run_cmd, args=(cmd, start_time, duration)).start()

    res = HTTPResponse(200)
    res.body = {}
    res.body['start_time'] = start_time

    return res

if __name__ == '__main__':
    run(host='0.0.0.0', port=80, debug=True, reloader=False)
