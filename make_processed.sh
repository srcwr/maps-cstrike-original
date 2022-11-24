#!/bin/sh

# echo all files & skip first line (-n +2)
# then lowercase, sort, uniq, and DONE!

tail -n +2 --quiet unprocessed/*.csv \
	| tr '[:upper:]' '[:lower:]' \
	| sort | uniq \
	| comm -23 - other/filtered_for_csgo.csv | sort \
	| comm -23 - other/filtered_for_likely_trolls.csv | sort \
	| comm -23 - other/filtered_for_not_bsp.csv | sort \
	> processed/lowercase.csv

tail -n +2 --quiet unprocessed/*.csv \
	| sort | uniq \
	| comm -23 - other/filtered_for_csgo.csv | sort \
	| comm -23 - other/filtered_for_likely_trolls.csv | sort \
	| comm -23 - other/filtered_for_not_bsp.csv | sort \
	> processed/mixedcase.csv

if [ -d "../hashed" ]; then
	echo "filesize,sha3_512" > processed/compressed_filesizes.csv
	du -ab ../hashed/*.bz2 | sed -e s/".bz2"// -e s/"..\/hashed\/"// | tr -s '[:blank:]' ',' >> ../maps-cstrike/processed/compressed_filesizes.csv
fi
