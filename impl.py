import re
import os

# (void|int|char|short|long|float|double)
# \s+
# (\w+)
# \s*
# \(
# [^)]*\)


# (void|int|char|short|long|float|double)
# \s+(\w+)\s*\([^)]*\)"

my_re= re.compile("(void|int|char|short|long|float|double)\s+(\w+)\s*\([^)]*\)")

input_sf = "./pcre2/src/pcre2_jit_compile.c"
input_s = "./pcre2"
target_s = "./mongo"

### Parsing functions of pcre2_jit_compile
with open(input_sf, "r") as fp:
    fileContent = fp.read()
    
    ### Detect matching using regex
    PCRE_list = my_re.findall(fileContent)
    
# ### Parsing all functions of PCRE
# PCRE_list = []
# for path, dir, files in os.walk(input_s):
#     for file in files:
#         filePath = os.path.join(path, file)
#         ### Check if the file has exstension of .c
#         if file.endswith((".c", ".cpp", ".cc")):
#             with open(filePath, "r") as fp:
#                 fileContent = fp.read()
#                 tmpList = my_re.findall(fileContent)
#                 ### Make function list for PCRE
#                 for eachF in tmpList:
#                     if eachF not in PCRE_list:
#                         PCRE_list += [eachF]

detectedFiles = []
### Detecting Parsed functions in MongoDB
for path, dir, files in os.walk(target_s):
    ### Traverse files in mongodb
    for file in files:
        filePath = os.path.join(path, file)
        ### Check if the file has exstension of .c
        if file.endswith((".c", ".cpp", ".cc")):
            with open(filePath, "r") as fp:
                fileContent = fp.read()
                mongoFuncs = my_re.findall(fileContent)
                ### Check PCRE function exists
                for eachFunction in mongoFuncs:
                    if eachFunction in PCRE_list\
                        and filePath not in detectedFiles:
                        detectedFiles += [filePath]

### Print out Detected Files
for _ in detectedFiles:
    print(_)
    
print("Number of files detected: {}".format(len(detectedFiles)))