
<section id="description">

# Native Vertical Grid Units  (universal)

## Description
Specifies the physical units for vertical grid measurements, following the EMD vertical_units controlled vocabulary (e.g., m for metres, Pa for pascals, K for kelvin).

</section>

<section id="info">

|  | uri |
| --- | --- |
| Type | `wrcp:native-vertical-grid-units` |
| Pydantic class | [`False`](https://github.com/ESGF/esgf-vocab/blob/main/src/esgvoc/api/data_descriptors/False.py):  Not yet implemented |
| | |
| JSON-LD | `universal:native-vertical-grid-units` |
| Content | [https://wcrp-cmip.github.io/WCRP-universe/native-vertical-grid-units](https://wcrp-cmip.github.io/WCRP-universe/native-vertical-grid-units) |
| Developer Reoo | [![Open in GitHub](https://img.shields.io/badge/Open-GitHub-blue?logo=github&style=flat-square)](https://github.com/wcrp-cmip/WCRP-universe/tree/main/src-data/native-vertical-grid-units) |

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
- **`name`** (**str**) 
  << No description in pydantic model (see esgvoc) >>





</section>   

<section id="usage">

## Usage

### Online Viewer 
To view a file in a browser use the content link with `.json` appended. eg. https://github.com/wcrp-cmip/WCRP-universe/tree/main/src-data/native-vertical-grid-units/.json

### Getting a File. 

A short example of how to integrate the computed ld file into your code. 

### Framing
```js
frame = {
            "@context": "https://wcrp-cmip.github.io/WCRP-universe/native-vertical-grid-units/_context_",
            "@type": "wcrp:native-vertical-grid-units/",
            "keys we want": "",
            "@explicit": True

        }
        

print(usage)

```

```python

import cmipld
cmipld.frame( universal:native-vertical-grid-units )

```
</section>

    