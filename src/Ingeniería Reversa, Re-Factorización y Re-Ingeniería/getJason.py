# [GCC 13.1.1 20230429]
# Embedded file name: getJason.py
# Compiled at: 2022-06-14 16:15:55
import json, sys
jsonfile = sys.argv[1]
jsonkey = sys.argv[2]
with open(jsonfile, 'r') as (myfile):
    data = myfile.read()
obj = json.loads(data)
print str(obj[jsonkey])
# okay decompiling getJason.pyc