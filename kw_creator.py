import json
import datetime
import os
from collections import Counter
from hh_loader import get_info_from_hh

from_file = True
if not(from_file):
    langs = ("Java", "JavaScript",
             "Visual basic", "Python",
             "C", "C++",
             "C#", "Objective-C",
             "Perl", "Ruby",
             "PHP"
             )

    par = {"text": "", "search_field": "name", "area": 2, "period": 30}
    o = {"skills": 1, "urls": 0, "vacs": 0}
    for l in langs:
        par["text"] = "Программист " + l
        with open("data\data_" + par["text"] + str(datetime.date.today())
                  + ".json", "w") as f:
            json.dump(get_info_from_hh(par, 10, o), f, indent=4, ensure_ascii=False)

    data = Counter()
    for fn in os.listdir("data"):
        if os.path.isfile("data/" + fn):
            with open("data/" + fn, "r") as rf:
                data += Counter(json.load(rf)["skills"])

for item in data.most_common(150):
    print(item)
jsdict = {item[0]: item[0] for item in data.most_common(150)}
with open("kw.json", "w") as wf:
    json.dump(jsdict, wf, indent=4, ensure_ascii=False, sort_keys=True)