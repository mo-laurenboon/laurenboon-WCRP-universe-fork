

import cmipld
import json
repopath = './src-data/organisation/'


# # args needed
# ror = parsed_issue['ror']
# acronym = parsed_issue['acronym']





def get_institution(ror, acronym):

    mytype = 'institution'

    ror_template = 'https://api.ror.org/organizations/{}'

    url = ror_template.format(ror)

    ror_data = cmipld.utils.read_url(url)

    assert ror_data, f"ROR data not found for {ror},{acronym}"
    
    # ensure the acronym has no _
    cmip_acronym = acronym.replace('_','-')
    
    
    ror_data =  {
        "id": f"{cmip_acronym.lower()}",
        "type": ['wcrp:organisation',f'wcrp:{mytype}','universal'],
        "label": cmip_acronym,
        "ror": ror_data['id'].split('/')[-1],
        "long_label": ror_data['name'],
        "url": ror_data.get('links', []) ,
        "established": ror_data.get('established'),
        "kind": ror_data.get('types', [])[0] if ror_data.get('types') else None,
        "labels": [i['label'] for i in ror_data.get('lables', [])],
        "aliases": ror_data.get('aliases', []),
        "acronyms": ror_data.get('acronyms', []),
        "location": {
            "id": f"universal:location/{ror_data['id'].split('/')[-1]}",
            "type": "wcrp:location",
            "lat":  ror_data['addresses'][0].get('lat') if ror_data.get('addresses') else None,
            "lon":  ror_data['addresses'][0].get('lat') if ror_data.get('addresses') else None,
            "city": ror_data['addresses'][0].get('city') if ror_data.get('addresses') else None,
            "country": list(ror_data['country'].values())  if ror_data.get('country') else None
        
        }         
        #  can reverse match consortiums or members from here.    
    }
    
    return ror_data

    


if __name__ == '__main__':
    from p_tqdm import p_map
    import glob
    
    files = glob.glob(repopath+'*.json')
    # print(files)
    
    def update(file):
        
        data = json.load(open(file))
        
        match data:
            case {"type":ldtypes} if 'wcrp:institution' in ldtypes:
                # print('Institution')
                # print(data['acronym'])
                data = get_institution(data['ror'],data['label'])
                pass
            case {"type":ldtypes} if 'wcrp:consortium' in ldtypes:
                print('Consortium')
                print(data['label'])
                
                
    # run on all files
    p_map(update,files)   
        
    
        
        