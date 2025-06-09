
<section id="description">

# Grid Label  (universal)

## Description
Provides labels for different grid configurations used in climate models, helping to identify and categorize the spatial grid arrangements for data output.

</section>

<section id="info">

|  | uri |
| --- | --- |
| Type | `wrcp:grid-label` |
| Pydantic class | [`grid_label`](https://github.com/ESGF/esgf-vocab/blob/main/src/esgvoc/api/data_descriptors/grid_label.py): GridLabel |
| | |
| JSON-LD | `universal:grid-label` |
| Content | [https://wcrp-cmip.github.io/WCRP-universe/grid-label](https://wcrp-cmip.github.io/WCRP-universe/grid-label) |
| Developer Reoo | [![Open in GitHub](https://img.shields.io/badge/Open-GitHub-blue?logo=github&style=flat-square)](https://github.com/wcrp-cmip/WCRP-universe/tree/main/src-data/grid-label) |

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
- **`short_name`** (**str**) 
  << No description in pydantic model (see esgvoc) >>
- **`name`** (**str**) 
  << No description in pydantic model (see esgvoc) >>
- **`region`** (**str**) 
  << No description in pydantic model (see esgvoc) >>

</section>

<section id="usage">

## Usage

### Online Viewer 
To view a file in a browser use the content link with `.json` appended. eg. https://github.com/wcrp-cmip/WCRP-universe/tree/main/src-data/grid-label/.json

### Getting a File. 

A short example of how to integrate the computed ld file into your code. 

### Framing
```js
frame = {
            "@context": "https://wcrp-cmip.github.io/WCRP-universe/grid-label/_context_",
            "@type": "wcrp:grid-label/",
            "keys we want": "",
            "@explicit": True

        }
        

print(usage)

```

```python

import cmipld
cmipld.frame( universal:grid-label )

```

</section>
