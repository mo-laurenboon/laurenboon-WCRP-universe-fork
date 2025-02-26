import cmipld
from cmipld.utils.ldparse import *

me = __file__.split('/')[-1].replace('.py','')

def run(localhost,whoami,repopath,reponame):

    url = f'{localhost}/{whoami}/organisation/graph.jsonld'
    ctx = f'{localhost}/{whoami}/organisation/_context_'
    
    frame = {
        "@context": ctx,
        "@type": "wcrp:institution"
    }
    
    data = cmipld.jsonld.frame(url,frame)["@graph"]
    
    summary = name_extract(data,['acronyms', 'long_label','url','ror'])
    
    cmipld.utils.io.wjsn(summary, f'{repopath}/{reponame}_{me}.json')