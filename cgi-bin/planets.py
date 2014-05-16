#!/usr/bin/python

pagetemplate = """\
<html>
<head>
%s
</head>
<body>
%s
</body>
</html>
"""

import linkplanets
def index():
    print linkplanets.outputplanets_html().replace("\n", "<br>")

print "Content-Type: text/html"
print
index()
