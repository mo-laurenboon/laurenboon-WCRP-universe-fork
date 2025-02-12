import sys
sys.path.append(__file__)

import update_ror
import json
from cmipld.utils import git
from  cmipld.tests import jsonld as tests
from cmipld.tests.jsonld.organisation import ror


def similarity(name1, name2):
    '''
    This function looks at the similarity between two strings and returns a percentage similarity.
    
    NB Difflib should come bundled with the standard python pagages e.g. conda
    '''
    from difflib import SequenceMatcher
    
    matcher = SequenceMatcher(None, name1, name2)
    similarity = matcher.ratio() * 100

    return similarity




def run(issue,packet):
    print('issue',issue)
    
    ror = issue['ror']
    acronym = issue['acronym']
    id = acronym.lower()
    
    # update the issue title
    git.update_issue_title(f'{issue["issue_type"].capitalize()}: {acronym}')
    
    acronym_test = tests.field_test(tests.components.stringcheck.id_field)
    ror_test = tests.field_test(tests.organisation.ror.ror_field)
    
    if ror != 'pending':
        try:
            acronym_test(id)
            ror_test(ror)
        except Exception as e:
            git.close_issue(f"Warning: The {e['loc']} field is not valid. {e['msg']}")

        data = update_ror.get_institution(ror, acronym)

        ranking = similarity(data['full_name_of_the_organisation.'], data['long_label'])
        
        if ranking < 80:
            git.update_issue(f"Warning: The similarity between the full name of the organisation and the long label is {ranking}%")
            
    else:

        try:
            acronym_test(id)
        except Exception as e:
            git.close_issue(f"Warning: The {e['loc']} field is not valid. {e['msg']}")
        
        data = {
                    "id": f"{id}",
                    "type": ['wcrp:organisation',f'wcrp:{issue['issue_type']}','universal'],
                    "label": acronym,    
                }        

    git.update_summary(f"### data content\n ```json\n{json.dumps(data,indent=4)}\n```")
    
    
    # issue {'issue_type': 'institution', 'acronym': 'test', 'full_name_of_the_organisation.': 'test', 'ror': '1w897891273', 'other_notes': 'hello'}
    