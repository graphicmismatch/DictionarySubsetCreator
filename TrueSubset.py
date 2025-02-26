import sys

n = len(sys.argv)
if n < 2:
    print("Please input the file path")
    quit()
try:
    if sys.argv[1].lower() == "help":
        print(
            "This tool makes sure that the input file does not have any words not found in the reference file.\nUsage:\npython TrueSubset.py <input_file_path> <superset_file_path> <input_file_delimiter> <superset_file_delimiter>"
        )
        print(
            "This tool replaces the original input file. Please keep a backup if important"
        )
        quit()
    idelim = sys.argv[3]
    if idelim == "\\n":
        idelim = "\n"
    elif idelim == "\\t":
        idelim = "\t"
    elif idelim == "\\w":
        idelim = " "

    sdelim = sys.argv[4]
    if sdelim == "\\n":
        sdelim = "\n"
    elif sdelim == "\\t":
        sdelim = "\t"
    elif sdelim == "\\w":
        sdelim = " "
    outp = ""
    inpfile = open(sys.argv[1], "r")
    inp = inpfile.read().split(idelim)
    inpfile.close()
    reffile = open(sys.argv[2], "r")
    ref = reffile.read().split(sdelim)
    reffile.close()
    for s in inp:
        if s in ref:
            outp += s + idelim
    file = open(sys.argv[1], "w")
    file.write(outp)
    file.close()

except Exception as e:
    print(e.with_traceback)
    print("Please input the correct parameters")
