

<section id="info">

# Model Calendar  (universal)

|  | uri |
| --- | --- |
| Type | `wrcp:model-calendar` |
| Pydantic class | [`False`](https://github.com/ESGF/esgf-vocab/blob/main/src/esgvoc/api/data_descriptors/False.py):  Not yet implemented |
| | |
| JSON-LD | `universal:model-calendar` |
| Content | [https://wcrp-cmip.github.io/WCRP-universe/model-calendar](https://wcrp-cmip.github.io/WCRP-universe/model-calendar) |
| Developer Reoo | [![Open in GitHub](https://img.shields.io/badge/Open-GitHub-blue?logo=github&style=flat-square)](https://github.com/wcrp-cmip/WCRP-universe/tree/main/src-data/model-calendar) |


</section>
    

<section id="description">

## Description

Specifies the calendar system used by climate models to define valid dates and time periods. Based on the EMD calendar controlled vocabulary, including options like standard, 360_day, 365_day, and others.

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
To view a file in a browser use the content link with `.json` appended. eg. https://github.com/wcrp-cmip/WCRP-universe/tree/main/src-data/model-calendar/.json

### Getting a File. 

A short example of how to integrate the computed ld file into your code. 

### Framing
```js
frame = {
            "@context": "https://wcrp-cmip.github.io/WCRP-universe/model-calendar/_context_",
            "@type": "wcrp:model-calendar/",
            "keys we want": "",
            "@explicit": True

        }
        

print(usage)

```

```python

import cmipld
cmipld.frame( universal:model-calendar )

```
</section>

    