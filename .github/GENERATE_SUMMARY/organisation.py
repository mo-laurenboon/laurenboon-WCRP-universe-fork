import cmipld
from cmipld.utils.ldparse import *

me = __file__.split('/')[-1].replace('.py','')

def run(localhost,whoami,repopath,reponame):

    url = f'{localhost}/{whoami}/{me}/graph.jsonld'
    ctx = f'{localhost}/{whoami}/{me}/_context_'
    
    frame = {
        "@context": ctx,
        "@type": "wcrp:organisation"
    }
    
    
    data = cmipld.jsonld.frame(url,frame)["@graph"]
    
    summary = name_entry(data,'long_label')
    
    cmipld.utils.io.wjsn(summary, f'{repopath}/{reponame}_{me}.json')