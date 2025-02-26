import cmipld
from cmipld.utils.ldparse import *

me = __file__.split('/')[-1].replace('.py','')

def run(localhost,whoami,repopath,reponame):

    url = f'{localhost}/{whoami}/{me}/graph.jsonld'
    ctx = f'{localhost}/{whoami}/{me}/_context_'
    
    data = cmipld.jsonld.frame(url,ctx)["@graph"]
    
    summary = name_extract(data,['description','long_label'])
    
    cmipld.utils.io.wjsn(summary, f'{repopath}/{reponame}_{me}.json')