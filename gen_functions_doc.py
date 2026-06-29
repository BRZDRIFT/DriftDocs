import os


g_driftLibs = 'C:/Users/mpo4/Dropbox/codename/binaries/Dev/DriftLibs/'
g_output = 'C:/GX/DriftDocs/docs/driftScript/'
g_functionInfos = []
g_enumInfos = []

# g_driftFiles = os.listdir(g_driftLibs)

g_driftFiles = [
    'Functions.DriftScript',
    'stubs.DriftScript',
    'builtin.DriftScript',
    'ComplexColor.DriftScript',
    'Expr.DriftScript',
    'Random.DriftScript',
    'Vec2.DriftScript',
    'Vec3.DriftScript',
    'Vec4.DriftScript',
    'AABR.DriftScript'
]

print(g_driftFiles)

def GetCommentsAbove(lines, i):
    outputLines = []
    idx = i-1;
    ignore = False
    if (lines[idx] != '*/'):
        return [], False
    while (True):
        idx -= 1;
        line = lines[idx];
        if (line == '/*'):
            break;
        if (line == '!'):
            ignore = True
            return [], True
        outputLines.append(line)

    outputLines.reverse()
    return outputLines, False

def GetEnumMemberInfos(lines, idx):
    outputLines = []
    bSkip = False
    while True:
        idx = idx+1;
        if '{' in lines[idx]:
            continue
        if '}' in lines[idx]:
            break
        if '/*' in lines[idx]:
            bSkip = True
            continue
        if '*/' in lines[idx]:
            bSkip = False
            continue
        if bSkip:
            continue
        outputLines.append(lines[idx])
    return outputLines

def ParseFuncton(lines, i):
    theLines, bIgnore = GetCommentsAbove(lines, i)

    prototype = ''
    comment = ''
    codeCommentCnt = 0

    for theLine in theLines:
        if (theLine == '!'):
            return '', ''
        if theLine.startswith('@ '):
            prototype = theLine[2:];
            continue
        if (theLine == '```'):
            if ((codeCommentCnt % 2) == 0):
                theLine = '```sq'
            else:
                theLine += '\n'
            codeCommentCnt += 1
        if (comment == ''):
            comment = theLine
        else:
            comment += '\n' + theLine

    return prototype, comment

def GetFunctionNameFromPrototype(prototype):
    return prototype.split(' ')[1].split('(')[0]

def AnalyzeFunction(lines, i):
    prototype, comment = ParseFuncton(lines, i)
    if prototype != '':
        g_functionInfos.append([prototype, comment, GetFunctionNameFromPrototype(prototype)])

def AnalyzeEnum(lines, i):
    theLines, bIgnore = GetCommentsAbove(lines, i)
    if bIgnore:
        return
    enumComment = GetCommentsAbove(lines, i)
    enumName = lines[i].split(' ')[1].split('{')[0]
    memberInfos = GetEnumMemberInfos(lines, i)
    g_enumInfos.append([enumName, memberInfos, theLines])

def Analyze(fnFile):
    lines = open(fnFile).readlines();
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()

    for i in range(len(lines)):
        line = lines[i]
        if line.startswith('function'):
            AnalyzeFunction(lines, i);
        if line.startswith('enum'):
            AnalyzeEnum(lines, i);

def GetFunctionText(fnInfo):
    finalOutput = '## ' + fnInfo[2] + '\n'
    finalOutput += '```sq\n'
    finalOutput += fnInfo[0] + '\n'
    finalOutput += '```\n\n'
    if fnInfo[1] != '':
        finalOutput += fnInfo[1]
    finalOutput += '\n'
    return finalOutput

def OutputFunctions():
    finalOutput = ''
    for fnInfo in g_functionInfos:
        if fnInfo[2].startswith('gx_'):
            finalOutput += GetFunctionText(fnInfo)
    for fnInfo in g_functionInfos:
        if not fnInfo[2].startswith('gx_'):
            finalOutput += GetFunctionText(fnInfo)
    fp = open(g_output + 'functions.md', 'w')
    fp.write(finalOutput)

def OutputEnums():
    finalOutput = ''
    finalOutput ='# Important!\n\n'
    finalOutput ='- Other than Enum Members named `Invalid` or `Unknown`, do not rely on their values staying the same across versions!\n\n'
    for enumInfo in g_enumInfos:
        finalOutput += '## ' + enumInfo[0] + '\n'
        finalOutput += '```sq\n'
        finalOutput += 'enum ' + enumInfo[0] + '\n{\n'
        for member in enumInfo[1]:
            finalOutput += member + '\n'
        finalOutput += '}\n'
        finalOutput += '```\n\n'
        finalOutput += '\n'.join(enumInfo[2])
        finalOutput += '\n'
    fp = open(g_output + 'enumerations.md', 'w')
    fp.write(finalOutput)

for filename in g_driftFiles:
    Analyze(g_driftLibs + filename)
OutputFunctions()
OutputEnums()
