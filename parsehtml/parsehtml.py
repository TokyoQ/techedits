import pandas as pd
import sys
import getopt
import yaml

# Arguments
if len(sys.argv) != 2:
    print('Usage parsehtml.py <inputfile>')
    sys.exit()

inputfile = sys.argv[1]

if not inputfile.endswith('.html'):
    print('Input file needs to be .html. Found : {}'.format(inputfile))
    sys.exit()

# Main
infile=open(inputfile, "r+")

tables = pd.read_html(infile, match='Prefix')

for table in tables:
    #print(table)
    prefixes = table["Prefix"]

    if ':' in prefixes[0]:
        # IPv6
        print('Skipping ipv6 table')
        continue
    if not '.' in prefixes[0]:
        print('Skipping unknown table')
        continue

    # IPv4
    outputfile = inputfile.replace('.html', '.yml')
    print('Writing to {}'.format(outputfile))
    with open(outputfile, 'w') as outfile:
        outfile.write(yaml.dump(prefixes.tolist()))
    
