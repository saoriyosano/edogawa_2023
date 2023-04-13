import os

commands = []

file = open("data/ids.txt")

for line in file:
    line = line.replace('\n', '')
    commands.append(f'touch data/{line}.csv\n')
    commands.append(f"python Optimized-Modified-GetOldTweets3-OMGOT/GetOldTweets3-0.0.10/cli.py --username '{line}' --output 'data/{line}.csv' --since 2019-04-21 --until 2023-04-12\n")
    
if os.path.exists('helpers/commands.sh'):
    mode = 'w'
else:
    mode = 'w+'

file_2 = open('helpers/commands.sh', mode)
for c in commands:
    file_2.write(c)