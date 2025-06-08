

<section id="info">

# License  (universal)

|  | uri |
| --- | --- |
| Type | `wrcp:license` |
| Pydantic class | [`license`](https://github.com/ESGF/esgf-vocab/blob/main/src/esgvoc/api/data_descriptors/license.py): License |
| | |
| JSON-LD | `universal:license` |
| Content | [https://wcrp-cmip.github.io/WCRP-universe/license](https://wcrp-cmip.github.io/WCRP-universe/license) |
| Developer Reoo | [![Open in GitHub](https://img.shields.io/badge/Open-GitHub-blue?logo=github&style=flat-square)](https://github.com/wcrp-cmip/WCRP-universe/tree/main/src-data/license) |


</section>
    

<section id="description">

## Description

</section>


<section id="schema">

## Content Schema

- **`id`** (**str**) 
  << No description in model >>
- **`type`** (**str**) 
  << No description in model >>
- **`drs_name`** (**str**) 
  << No description in model >>
- **`kind`** (**str**) 
  << No description in model >>
- **`license`** (**str | None**) 
  << No description in model >>
- **`url`** (**str | None**) 
  << No description in model >>





</section>   

<section id="usage">

## Usage

### Online Viewer 
To view a file in a browser use the content link with `.json` appended. eg. https://github.com/wcrp-cmip/WCRP-universe/tree/main/src-data/license/.json

### Getting a File. 

A short example of how to integrate the computed ld file into your code. 

### Framing
```js
frame = {
            "@context": "https://wcrp-cmip.github.io/WCRP-universe/license/_context_",
            "@type": "wcrp:license/",
            "keys we want": "",
            "@explicit": True

        }
        

print(usage)

```

```python

import cmipld
cmipld.frame( universal:license )

```
</section>

    