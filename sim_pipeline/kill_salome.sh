#!/usr/bin/env bash
ps x | grep salome | awk '{print $1}' | xargs -n1 kill
ps x | grep SALOME | awk '{print $1}' | xargs -n1 kill
ps x | grep omni | awk '{print $1}' | xargs -n1 kill
