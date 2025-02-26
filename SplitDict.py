import sys

n = len(sys.argv)
if n < 2:
    print("Please input the file path")
    quit()

try:
    if sys.argv[1].lower() == "help":
        print(
            "This tool splits a dictionary file into multiple based on the first letter of the word.\nUsage:\npython SplitDict.py <file_path> <input_file_delimiter> <output_file_delimiter>"
        )
        quit()
    idelim = sys.argv[2]
    if idelim == "\\n":
        idelim = "\n"
    elif idelim == "\\t":
        idelim = "\t"
    elif idelim == "\\w":
        idelim = " "
    odelim = sys.argv[3]
    if odelim == "\\n":
        odelim = "\n"
    elif odelim == "\\t":
        odelim = "\t"
    elif odelim == "\\w":
        odelim = " "
    outp = dict({})
    file = open(sys.argv[1], "r")
    content = file.read().split(idelim)
    file.close()
    for i in content:
        if outp.get(i[0], None) == None:
            outp.update({i[0]: []})
        outp[i[0]].append(i)
    for i in outp:
        pp = ""
        for j in outp[i]:
            pp += j + "\n"
        file = open("./" + i + ".txt", "w")
        file.write(pp)
        file.close()
except Exception as e:
    print(e)
    print("Please input the correct parameters")
