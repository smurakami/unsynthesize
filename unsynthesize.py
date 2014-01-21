# coding: utf-8

"""
iosアプリのリファクタリングツール
.mファイル中のsynthesizeを外して、
ソース中のプロパティ変数の先頭に"_"(アンダースコア)を
挿入する。
"""

import sys
import re

def getTargets(filename):
    """
    synthesizeを外す変数名を抽出
    """
    variables = []
    with open(filename, "r") as f:
        for line in f:
            m = re.match(r"@synthesize (\w+);", line)
            if m:
                var = m.group(1)
                variables.append(var)
    return variables

def getText(filename):
    """
    ファイルをとりあえず保存
    """
    text = []
    with open(filename, "r") as f:
        for line in f:
            text.append(line)
    return text

def unSynthesize(filename):
    """
    @synthesizeを外す
    """
    variables = getTargets(filename)
    text = getText(filename)
    for v in variables:
        print v,
    for line in text:
        print line,


if __name__ == "__main__":
    argv = sys.argv
    if len(argv) != 2:
        print 'Usage: # python %s filename' % argv[0]
        quit()

    filename = argv[1]
    unSynthesize(filename)



