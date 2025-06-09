

<section id="info">

# Native Horizontal Grid Type  (universal)

|  | uri |
| --- | --- |
| Type | `wrcp:native-horizontal-grid-type` |
| Pydantic class | [`False`](https://github.com/ESGF/esgf-vocab/blob/main/src/esgvoc/api/data_descriptors/False.py):  Not yet implemented |
| | |
| JSON-LD | `universal:native-horizontal-grid-type` |
| Content | [https://wcrp-cmip.github.io/WCRP-universe/native-horizontal-grid-type](https://wcrp-cmip.github.io/WCRP-universe/native-horizontal-grid-type) |
| Developer Reoo | [![Open in GitHub](https://img.shields.io/badge/Open-GitHub-blue?logo=github&style=flat-square)](https://github.com/wcrp-cmip/WCRP-universe/tree/main/src-data/native-horizontal-grid-type) |


</section>
    

<section id="description">

## Description

Specifies the horizontal grid types used by model components, following the EMD grid controlled vocabulary (e.g., regular_latitude_longitude, cubed_sphere, unstructured_triangular).

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
To view a file in a browser use the content link with `.json` appended. eg. https://github.com/wcrp-cmip/WCRP-universe/tree/main/src-data/native-horizontal-grid-type/.json

### Getting a File. 

A short example of how to integrate the computed ld file into your code. 

### Framing
```js
frame = {
            "@context": "https://wcrp-cmip.github.io/WCRP-universe/native-horizontal-grid-type/_context_",
            "@type": "wcrp:native-horizontal-grid-type/",
            "keys we want": "",
            "@explicit": True

        }
        

print(usage)

```

```python

import cmipld
cmipld.frame( universal:native-horizontal-grid-type )

```
</section>

    