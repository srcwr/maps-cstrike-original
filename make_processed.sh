#!/bin/sh

# echo all files & skip first line (-n +2)
# then lowercase, sort, uniq, and DONE!

tail -n +2 --quiet unprocessed/*.csv \
	| tr '[:upper:]' '[:lower:]' \
	| sort \
	| uniq \
	> processed_lower.csv

tail -n +2 --quiet unprocessed/*.csv \
	| sort \
	| uniq \
	> processed_mixed.csv
