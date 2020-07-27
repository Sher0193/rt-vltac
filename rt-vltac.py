#!/usr/bin/env python
# Author Sher0193 

import sys

link = sys.argv[1]
if link.find("roosterteeth.com/watch/") >= 0:
    link = link.replace("roosterteeth.com/watch/", "svod-be.roosterteeth.com/api/v1/episodes/")
    link += "/videos"

print link
