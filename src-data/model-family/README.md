

<section id="info">

# Model Family  (universal)

|  | uri |
| --- | --- |
| Type | `wrcp:model-family` |
| Pydantic class | [`False`](https://github.com/ESGF/esgf-vocab/blob/main/src/esgvoc/api/data_descriptors/False.py):  Not yet implemented |
| | |
| JSON-LD | `universal:model-family` |
| Content | [https://wcrp-cmip.github.io/WCRP-universe/model-family](https://wcrp-cmip.github.io/WCRP-universe/model-family) |
| Developer Reoo | [![Open in GitHub](https://img.shields.io/badge/Open-GitHub-blue?logo=github&style=flat-square)](https://github.com/wcrp-cmip/WCRP-universe/tree/main/src-data/model-family) |


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
- **`description`** (**str**) 
  << No description in model >>
- **`name`** (**str**) 
  << No description in model >>





</section>   

<section id="usage">

## Usage

### Online Viewer 
To view a file in a browser use the content link with `.json` appended. eg. https://github.com/wcrp-cmip/WCRP-universe/tree/main/src-data/model-family/.json

### Getting a File. 

A short example of how to integrate the computed ld file into your code. 

### Framing
```js
frame = {
            "@context": "https://wcrp-cmip.github.io/WCRP-universe/model-family/_context_",
            "@type": "wcrp:model-family/",
            "keys we want": "",
            "@explicit": True

        }
        

print(usage)

```

```python

import cmipld
cmipld.frame( universal:model-family )

```
</section>

    