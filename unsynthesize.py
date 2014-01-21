# coding: utf-8

"""
iosアプリのリファクタリングツール
.mファイル中の@synthesizeを外して、
それまでに@synthesizeされていたプロパティ変数の先頭に
"_"(アンダースコア)を挿入する。
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
    with open(filename, "w") as f:
        for line in text:
            if re.match(r"@synthesize (\w+);", line):
                continue
            for var in variables:
                if var in line:
                    line = line.replace(var, "_%s" % var )
            f.write(line)


if __name__ == "__main__":
    argv = sys.argv
    if len(argv) != 2:
        print 'Usage: # python %s filename' % argv[0]
        quit()

    filename = argv[1]
    unSynthesize(filename)



