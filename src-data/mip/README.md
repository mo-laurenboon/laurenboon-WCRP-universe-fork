
<section id="description">

# Mip  (universal)

## Description
Identifies Model Intercomparison Projects (MIPs) that coordinate and define specific climate modeling experiments and data requirements within the CMIP framework.

</section>

<section id="info">

|  | uri |
| --- | --- |
| Type | `wrcp:mip` |
| Pydantic class | [`False`](https://github.com/ESGF/esgf-vocab/blob/main/src/esgvoc/api/data_descriptors/False.py):  Not yet implemented |
| | |
| JSON-LD | `universal:mip` |
| Content | [https://wcrp-cmip.github.io/WCRP-universe/mip](https://wcrp-cmip.github.io/WCRP-universe/mip) |
| Developer Reoo | [![Open in GitHub](https://img.shields.io/badge/Open-GitHub-blue?logo=github&style=flat-square)](https://github.com/wcrp-cmip/WCRP-universe/tree/main/src-data/mip) |

</section>

<section id="schema">

## Content Schema

- **`id`** (**str**) 
  << No description in pydantic model (see esgvoc) >>
- **`type`** (**str**) 
  << No description in pydantic model (see esgvoc) >>
- **`drs_name`** (**str**) 
  << No description in pydantic model (see esgvoc) >>
- **`description`** (**str**) 
  << No description in pydantic model (see esgvoc) >>
- **`kind`** (**str**) 
  << No description in pydantic model (see esgvoc) >>

</section>

<section id="usage">

## Usage

### Online Viewer 
To view a file in a browser use the content link with `.json` appended. eg. https://github.com/wcrp-cmip/WCRP-universe/tree/main/src-data/mip/.json

### Getting a File. 

A short example of how to integrate the computed ld file into your code. 

### Framing
```js
frame = {
            "@context": "https://wcrp-cmip.github.io/WCRP-universe/mip/_context_",
            "@type": "wcrp:mip/",
            "keys we want": "",
            "@explicit": True

        }
        

print(usage)

```

```python

import cmipld
cmipld.frame( universal:mip )

```

</section>
