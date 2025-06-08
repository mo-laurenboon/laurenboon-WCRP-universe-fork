

<section id="info">

# Grid Label  (universal)

|  | uri |
| --- | --- |
| Type | `wrcp:grid-label` |
| Pydantic class | [`grid_label`](https://github.com/ESGF/esgf-vocab/blob/main/src/esgvoc/api/data_descriptors/grid_label.py): GridLabel |
| | |
| JSON-LD | `universal:grid-label` |
| Content | [https://wcrp-cmip.github.io/WCRP-universe/grid-label](https://wcrp-cmip.github.io/WCRP-universe/grid-label) |
| Developer Reoo | [![Open in GitHub](https://img.shields.io/badge/Open-GitHub-blue?logo=github&style=flat-square)](https://github.com/wcrp-cmip/WCRP-universe/tree/main/src-data/grid-label) |


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
- **`short_name`** (**str**) 
  << No description in model >>
- **`name`** (**str**) 
  << No description in model >>
- **`region`** (**str**) 
  << No description in model >>





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

    