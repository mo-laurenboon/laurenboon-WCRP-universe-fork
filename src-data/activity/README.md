

<section id="info">

# Activity  (universal)

|  | uri |
| --- | --- |
| Type | `wrcp:activity` |
| Pydantic class | [`activity`](https://github.com/ESGF/esgf-vocab/blob/main/src/esgvoc/api/data_descriptors/activity.py): Activity |
| | |
| JSON-LD | `universal:activity` |
| Content | [https://wcrp-cmip.github.io/WCRP-universe/activity](https://wcrp-cmip.github.io/WCRP-universe/activity) |
| Developer Reoo | [![Open in GitHub](https://img.shields.io/badge/Open-GitHub-blue?logo=github&style=flat-square)](https://github.com/wcrp-cmip/WCRP-universe/tree/main/src-data/activity) |


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
- **`name`** (**str**) 
  << No description in model >>
- **`long_name`** (**str**) 
  << No description in model >>
- **`url`** (**str | None**) 
  << No description in model >>





</section>   

<section id="usage">

## Usage

### Online Viewer 
To view a file in a browser use the content link with `.json` appended. eg. https://github.com/wcrp-cmip/WCRP-universe/tree/main/src-data/activity/.json

### Getting a File. 

A short example of how to integrate the computed ld file into your code. 

### Framing
```js
frame = {
            "@context": "https://wcrp-cmip.github.io/WCRP-universe/activity/_context_",
            "@type": "wcrp:activity/",
            "keys we want": "",
            "@explicit": True

        }
        

print(usage)

```

```python

import cmipld
cmipld.frame( universal:activity )

```
</section>

    