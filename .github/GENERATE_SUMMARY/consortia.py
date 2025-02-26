import cmipld
from cmipld.utils.ldparse import *

me = __file__.split('/')[-1].replace('.py','')

def run(localhost,whoami,repopath,reponame):

    url = f'{localhost}/{whoami}/organisation/graph.jsonld'
    ctx = f'{localhost}/{whoami}/organisation/_context_'
    
    frame = {
        "@context": ctx,
        "@type": "wcrp:consortium"
    }
    
    data = cmipld.jsonld.frame(url,frame)["@graph"]
    
    summary = name_extract(data,['label','long_label','url','members'])
    
    
    for i in summary:
        summary[i] = set(summary[i]['members'].keys())
    
    cmipld.utils.io.wjsn(summary, f'{repopath}/{reponame}_{me}.json')