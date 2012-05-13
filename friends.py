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
    for i in xrange(2, numPages + 1):
        (_, newFriends) = getFriendsPage(userName, i)
        friends += newFriends
    return friends

def crawlGraph(userName, depth):
    print "depth 0"
    print userName
    users = [set([userName])]
    for i in xrange(1, depth + 1):
        users.append(set())
        print "depth %d" % i
        for user in users[i - 1]:
            print "processing %s" % user
            friends = getFriendsList(user)
            for friend in friends:
                new = True
                for j in xrange(i + 1):
                    if friend in users[j]:
                        new = False
                        break
                if new:
                    users[i].add(friend)
    return users

users = crawlGraph(sys.argv[1], int(sys.argv[2]))
for (layerID, layer) in enumerate(users):
    print "layer %d: %d users" % (layerID, len(layer))
