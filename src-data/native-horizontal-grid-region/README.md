

<section id="info">

# Native Horizontal Grid Region  (universal)

|  | uri |
| --- | --- |
| Type | `wrcp:native-horizontal-grid-region` |
| Pydantic class | [`False`](https://github.com/ESGF/esgf-vocab/blob/main/src/esgvoc/api/data_descriptors/False.py):  Not yet implemented |
| | |
| JSON-LD | `universal:native-horizontal-grid-region` |
| Content | [https://wcrp-cmip.github.io/WCRP-universe/native-horizontal-grid-region](https://wcrp-cmip.github.io/WCRP-universe/native-horizontal-grid-region) |
| Developer Reoo | [![Open in GitHub](https://img.shields.io/badge/Open-GitHub-blue?logo=github&style=flat-square)](https://github.com/wcrp-cmip/WCRP-universe/tree/main/src-data/native-horizontal-grid-region) |


</section>
    

<section id="description">

## Description

Defines the geographical regions over which model components operate, based on the EMD region controlled vocabulary (e.g., global, antarctica, greenland, limited_area).

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





</section>   

<section id="usage">

## Usage

### Online Viewer 
To view a file in a browser use the content link with `.json` appended. eg. https://github.com/wcrp-cmip/WCRP-universe/tree/main/src-data/native-horizontal-grid-region/.json

### Getting a File. 

A short example of how to integrate the computed ld file into your code. 

### Framing
```js
frame = {
            "@context": "https://wcrp-cmip.github.io/WCRP-universe/native-horizontal-grid-region/_context_",
            "@type": "wcrp:native-horizontal-grid-region/",
            "keys we want": "",
            "@explicit": True

        }
        

print(usage)

```

```python

import cmipld
cmipld.frame( universal:native-horizontal-grid-region )

```
</section>

    