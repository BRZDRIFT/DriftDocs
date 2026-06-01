import os

def define_env(env):

    baseUrl = ''

    bGitHub = (os.getenv('GX_GITHUB', 0) == "1")
    if bGitHub:
        baseUrl = '/DriftDocs'

    @env.macro
    def fn(fnName):
        return '[' + fnName +']('+baseUrl+'/driftScript/functions/#' + fnName.lower() +')'

    @env.macro
    def enum(enumName):
        return '[' + enumName +']('+baseUrl+'/driftScript/enumerations/#' + enumName.lower() +')'

    @env.macro
    def entry(entryName):
        return '[' + entryName +']('+baseUrl+'/driftScript/scriptEntryPoints/#' + entryName.lower() +')'

    @env.macro
    def eventQueue():
        return '[Event Queue]('+baseUrl+'/driftScript/eventQueue/#event_queue)'

    @env.macro
    def type(typeName):
        return '[' + typeName + ']('+baseUrl+'/driftScript/builtinTypes/#'+typeName.lower()+')'

    @env.macro
    def math(mathHeader):
        return '[' + mathHeader + ']('+baseUrl+'/driftScript/math/#'+mathHeader.lower()+')'

    @env.macro
    def event(header):
        return '[' + header + ']('+baseUrl+'/driftScript/eventQueue/#'+header.lower()+')'

    @env.macro
    def entryPoints(header):
        return '[' + header + ']('+baseUrl+'/driftScript/scriptEntryPoints/#'+header.lower()+')'

    @env.macro
    def mode(header):
        return '[' + header + ']('+baseUrl+'/driftEdit/modes/'+header+')'

    @env.macro
    def sideControls(header):
        return '[' + header + ']('+baseUrl+'/driftEdit/sideControls/#'+header.lower()+')'

    @env.macro
    def texSplatting(header):
        return '[' + header + ']('+baseUrl+'/driftEdit/modes/texSplatting/#'+header.lower()+')'
