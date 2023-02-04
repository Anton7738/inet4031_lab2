#!/usr/bin/env python3

import sys


print("Printing out User Data:\n")

for line in sys.stdin:
    userData = line.split(":")
    userData[3].rstrip()
    if (userData[0][0] == "#"):
        skippedUser = userData[0].replace("#", "")
        print("%s is skipped because it starts with a hashtag (is commented out)" % (skippedUser))
    else :
        userGroup = userData[3].replace("\n", "")
        print("The user %s has a password of %s and has userid %s and groupid %s" % (userData[0], userData[1], userData[2], userGroup))

print("\nEnd of User Data")


