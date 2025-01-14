

import cmipld
import json



# # args needed
# ror = parsed_issue['ror']
# acronym = parsed_issue['acronym']





def get_institution(ror, acronym):


    ror_template = 'https://api.ror.org/organizations/{}'

    url = ror_template.format(ror)

    ror_data = cmipld.utils.read_url(url)

    assert ror_data, f"ROR data not found for {ror},{acronym}"
    
    # ensure the acronym has no _
    cmip_acronym = acronym.replace('_','-')
    
    
    ror_data =  {
        "id": f"{cmip_acronym.lower()}",
        "type": ['wcrp:organisation','wcrp:institution','universal'],
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
            "@id": f"universal:location/{ror_data['id'].split('/')[-1]}",
            "@type": "wcrp:location",
            "lat":  ror_data['addresses'][0].get('lat') if ror_data.get('addresses') else None,
            "lon":  ror_data['addresses'][0].get('lat') if ror_data.get('addresses') else None,
            "city": ror_data['addresses'][0].get('city') if ror_data.get('addresses') else None,
            "country": list(ror_data['country'].values())  if ror_data.get('country') else None
        
        }         
        #  can reverse match consortiums or members from here.    
    }

    print(json.dumps(ror_data,indent=4))
    
    return ror_data

    
        
'''
{
    "@context": "_context_",
    "id": "cas",
    "acronyms": [
        "CAS"
    ],
    "aliases": [],
    "established": 1949,
    "labels": [],
    "location": {
        "id": "universal:location/034t30j35",
        "@nest": {
            "city": "Beijing",
            "country": [
                "China",
                "CN"
            ],
            "lat": 39.9075,
            "lon": 116.39723
        },
        "type": "location"
    },
    "ror": "034t30j35",
    "kind": "Government",
    "url": [
        "http://english.cas.cn/"
    ],
    "type": [
        "universal",
        "wcrp:institution",
        "wcrp:organisation"
    ],
    "long_label": "Chinese Academy of Sciences",
    "label": "CAS"
}

'''