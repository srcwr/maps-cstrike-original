# hashes & filesizes of many map/bsp files for Counter-Strike: Source

Collected mainly through scraping "FastDL" webhosts.

`unprocessed/*.csv` files were generated with https://github.com/srcwr/maps-hasher

## Usage in SQLite
TODO: Table keys so hash comparisons is faster...
```bash
$ sqlite3 new.db
CREATE TABLE maps (mapname TEXT NOT NULL, filesize INT NOT NULL, crc32ieee TEXT NOT NULL, md5 TEXT NOT NULL, sha1 TEXT NOT NULL, sha2_256 TEXT NOT NULL, sha2_512 TEXT NOT NULL, sha3_512 TEXT NOT NULL);
.mode csv
.import processed/lowercase.csv maps
CREATE TABLE compressed (filesize INT NOT NULL, sha3_512 TEXT NOT NULL);
.import processed/mixedcase.csv compressed
.exit
```
