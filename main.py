#!/usr/bin/python
# encoding: utf-8

from workflow import Workflow
import sys


def main(wf):
    keyword = sys.argv[1].lower()
    keywords = keyword.split(' ')
    with open('src/source.txt') as f:
        texts = f.readlines()
        searchedTexts = [t.strip() for t in texts if len(
            [k for k in keywords if k in t.lower()]) == len(keywords)]
        for text in searchedTexts:
            wf.add_item(text, arg=text, valid=True)

        wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))
