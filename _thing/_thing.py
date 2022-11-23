import os.path
import json
import sqlite3

conn = None
try:
    conn = sqlite3.connect("new.db")
except:
    conn = sqlite3.connect("../new.db")

cur = conn.cursor()
cur.execute("SELECT mapname, filesize FROM maps;")
rows = cur.fetchall()

things = {}
for row in rows:
    name = row[0] + ".bsp"
    if not name in things:
        things[name] = []
    things[name].append(int(row[1]))
file = None
if os.path.exists("_thing"):
    file = open("_thing/_thing.json", "w")
else:
    file = open("_thing.json", "w")
json.dump(things, file)
