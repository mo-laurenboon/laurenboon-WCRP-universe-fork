

<section id="info">

# Product  (universal)

|  | uri |
| --- | --- |
| Type | `wrcp:product` |
| Pydantic class | [`product`](https://github.com/ESGF/esgf-vocab/blob/main/src/esgvoc/api/data_descriptors/product.py): Product |
| | |
| JSON-LD | `universal:product` |
| Content | [https://wcrp-cmip.github.io/WCRP-universe/product](https://wcrp-cmip.github.io/WCRP-universe/product) |
| Developer Reoo | [![Open in GitHub](https://img.shields.io/badge/Open-GitHub-blue?logo=github&style=flat-square)](https://github.com/wcrp-cmip/WCRP-universe/tree/main/src-data/product) |


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
- **`kind`** (**str**) 
  << No description in model >>





</section>   

<section id="usage">

## Usage

### Online Viewer 
To view a file in a browser use the content link with `.json` appended. eg. https://github.com/wcrp-cmip/WCRP-universe/tree/main/src-data/product/.json

### Getting a File. 

A short example of how to integrate the computed ld file into your code. 

### Framing
```js
frame = {
            "@context": "https://wcrp-cmip.github.io/WCRP-universe/product/_context_",
            "@type": "wcrp:product/",
            "keys we want": "",
            "@explicit": True

        }
        

print(usage)

```

```python

import cmipld
cmipld.frame( universal:product )

```
</section>

    