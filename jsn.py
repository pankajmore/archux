import json
import cPickle
obj = cPickle.load(open('save.p', 'rb'))
with open("save.json", "w") as out: json.dump(obj, out,sort_keys=True, indent=4)
ob = cPickle.load(open('dict.p', 'rb'))
with open("dict.json", "w") as outfile: json.dump(ob, outfile,sort_keys=True, indent=4)
