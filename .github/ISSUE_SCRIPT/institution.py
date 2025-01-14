import update_ror




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
    
    
    
update_ror.get_institution('046rm7j60','acronym')