
import os
import csv
import glob
from pathlib import Path

compressed_filesizes = {}
with open("processed/compressed_filesizes.csv", newline="") as other:
    reader = csv.reader(other)
    for row in reader:
        compressed_filesizes[row[1]] = row[0]

for filename in glob.glob("unprocessed/*.csv"):
    with open(filename, newline="") as csvin:
        reader = csv.reader(csvin)
        with open("unprocessed2/" + Path(filename).stem, "w", newline="") as csvout:
            writer = csv.writer(csvout)
            for row in reader:
                if row[1] == "filesize":
                    continue
                if row[7] in compressed_filesizes:
                    writer.writerow([row[0],row[1],compressed_filesizes[row[7]],row[4]])
                    if os.path.exists("../hashed/{}.bsp".format(row[7])):
                        os.rename("../hashed/{}.bsp".format(row[7]), "../hashed/{}.bsp".format(row[4]))
                        os.rename("../hashed/{}.bsp.bz2".format(row[7]), "../hashed/{}.bsp.bz2".format(row[4]))
