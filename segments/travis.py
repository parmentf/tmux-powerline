#!/usr/bin/env python
import requests
import os, sys
import re
from xml.dom import minidom

def main(argv):
    repository1 = re.search('(\/\w+\/\D+)$', sys.argv[1])
    repository2 = re.search('^([^\/]+)\/?(.*)(\/\D+\/\D+)(.git)$', sys.argv[1])
    repository = ""

    if repository1 and not repository2:
        repository = repository1.group(1)
    elif not repository1 and repository2:
        repository = repository2.group(3)

    # print(repository)
    request = requests.get("https://api.travis-ci.org/repositories" + repository + ".xml?branch=" + sys.argv[2])
    if request.status_code != 200:
        return 0

    value = ""
    try:
        xmlData = minidom.parseString(request.text)
        value = xmlData.getElementsByTagName("Project")[0].attributes['lastBuildStatus'].value
    except:
        pass
    print(value)
    pass

if __name__ == "__main__":
    main(sys.argv)