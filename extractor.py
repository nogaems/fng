#!/usr/bin/env python3
# coding: utf-8
import requests
import re
import threading
import os
import time
import sys

baseurl = 'http://www.fantasynamegenerators.com/'
progress = 0
threads_max = 8
rewriting = False


def dl_error_wrapper(r):
    if r.status_code != 200:
        print('Page {} downloading error with status code {}'.format(
            r.url, r.status_code))
        exit(1)


def get_generators_links():
    r = requests.get(baseurl)
    dl_error_wrapper(r)
    html = r.text
    parsed = re.findall(r'.*<a href=\"(?!http)([\w\-\.\d]+)\".*', html)
    links = [baseurl + p for p in parsed]
    return(links)


def get_script_link(generator_link):
    r = requests.get(generator_link)
    parsed = re.findall(r'.*<script src=\"([\w\.\/\d]+)\".*', r.text)
    if len(parsed) != 0:
        return baseurl + parsed[0]
    else:
        return


def get_script_code(link):
    r = requests.get(link)
    return r.text


def save_script(text, name, rewrite=True):
    if not rewrite and os.path.isfile('js' + name):
        return
    f = open('js/' + name, 'w')
    f.write(text)
    f.close()


class ScriptGetter(threading.Thread):

    def __init__(self, generator_link, rewrite=True):
        threading.Thread.__init__(self)
        self.generator_link = generator_link
        self.rewrite = rewrite

    def run(self):
        global progress
        script_link = None
        while not script_link:
            time.sleep(1)
            script_link = get_script_link(self.generator_link)
        save_script(get_script_code(script_link), script_link.split('/')[-1],
                    rewrite=self.rewrite)
        progress += 1

if __name__ == '__main__':
    links = get_generators_links()
    if not os.path.isdir('js'):
        os.mkdir('js')
    threads = []
    for link in links:
        threads.append(ScriptGetter(link, rewrite=rewriting))
    total = len(threads)
    while len(threads) != 0:
        sys.stdout.write(
            '\r * progress: {} of {} ({} threads)        \r'.format(
                progress, total, threading.activeCount()))
        if threading.activeCount() <= threads_max - 1:
            t = threads.pop()
            t.start()

        else:
            time.sleep(.5)
    print("\nDone")
