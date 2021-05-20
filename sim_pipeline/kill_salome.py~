#!/usr/bin/env python3

from subprocess import run, DEVNULL

targets = ['salome', 'SALOME', 'omni']
for tar in targets:
    kstr = "ps x | grep {} | awk '{{print $1}}' | xargs -n1 kill".format(tar)
    print(kstr)
    run(kstr, shell=True, stdout=DEVNULL, stderr=DEVNULL)
