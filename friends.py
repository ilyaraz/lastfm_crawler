#!/usr/bin/python

from lxml import etree 
import sys

def getFriendsPage(userName, page):
    tree = etree.parse("http://ws.audioscrobbler.com/2.0/?method=user.getfriends" + 
                                                        "&page=" + str(page) +
                                                        "&user=" + userName +
                                                        "&api_key=da7830aae6f7057573c018bcd2ec2b10")
    friends = []
    for elem in tree.findall(".//name"):
        friends.append(elem.findtext("."))
    return (int(tree.find(".//friends").attrib.get("totalPages")), friends)

def getFriendsList(userName):
    (numPages, friends) = getFriendsPage(userName, 1)
    print numPages
    for i in xrange(2, numPages + 1):
        (_, newFriends) = getFriendsPage(userName, i)
        friends += newFriends
    return friends

print getFriendsList(sys.argv[1])
