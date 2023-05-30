import json
import os
import random
import string

def exporting():

    files = os.listdir('./jsonfiles/temporary/')

    finaldict = {}
    for file in files:
        with open('./jsonfiles/temporary/' + file, 'r') as f:
            finaldict.update(json.load(f))

    s = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=10))
    with open('./jsonfiles/' + s + '.json','w') as f:
        json.dump(finaldict, f, indent=4)
    return s + '.json'

