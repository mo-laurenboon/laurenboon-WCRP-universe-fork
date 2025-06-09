

<section id="info">

# Native Horizontal Grid Temporal Refinement  (universal)

|  | uri |
| --- | --- |
| Type | `wrcp:native-horizontal-grid-temporal-refinement` |
| Pydantic class | [`False`](https://github.com/ESGF/esgf-vocab/blob/main/src/esgvoc/api/data_descriptors/False.py):  Not yet implemented |
| | |
| JSON-LD | `universal:native-horizontal-grid-temporal-refinement` |
| Content | [https://wcrp-cmip.github.io/WCRP-universe/native-horizontal-grid-temporal-refinement](https://wcrp-cmip.github.io/WCRP-universe/native-horizontal-grid-temporal-refinement) |
| Developer Reoo | [![Open in GitHub](https://img.shields.io/badge/Open-GitHub-blue?logo=github&style=flat-square)](https://github.com/wcrp-cmip/WCRP-universe/tree/main/src-data/native-horizontal-grid-temporal-refinement) |


</section>
    

<section id="description">

## Description

Defines how horizontal grid cell distribution varies over time, based on the EMD temporal_refinement controlled vocabulary (e.g., static, dynamically_stretched, adaptive).

</section>


<section id="schema">

## Content Schema

- **`id`** (**str**) 
  << No description in pydantic model (see esgvoc) >>
- **`type`** (**str**) 
  << No description in pydantic model (see esgvoc) >>
- **`drs_name`** (**str**) 
  << No description in pydantic model (see esgvoc) >>
- **`name`** (**str**) 
  << No description in pydantic model (see esgvoc) >>
- **`long_name`** (**str**) 
  << No description in pydantic model (see esgvoc) >>
- **`url`** (**str | None**) 
  << No description in pydantic model (see esgvoc) >>





</section>   

<section id="usage">

## Usage

### Online Viewer 
To view a file in a browser use the content link with `.json` appended. eg. https://github.com/wcrp-cmip/WCRP-universe/tree/main/src-data/native-horizontal-grid-temporal-refinement/.json

### Getting a File. 

A short example of how to integrate the computed ld file into your code. 

### Framing
```js
frame = {
            "@context": "https://wcrp-cmip.github.io/WCRP-universe/native-horizontal-grid-temporal-refinement/_context_",
            "@type": "wcrp:native-horizontal-grid-temporal-refinement/",
            "keys we want": "",
            "@explicit": True

        }
        

print(usage)

```

```python

import cmipld
cmipld.frame( universal:native-horizontal-grid-temporal-refinement )

```
</section>

    