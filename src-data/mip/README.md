

<section id="description">

# Mip  (universal)

[View in HTML](https://wcrp-cmip.github.io/WCRP-universe/mip/mip)

## Description
Identifies Model Intercomparison Projects (MIPs) that coordinate and define specific climate modeling experiments and data requirements within the CMIP framework.


</section>



<section id="info">


| Item | Reference |
| --- | --- |
| Type | `wrcp:mip` |
| Pydantic class | [`False`](https://github.com/ESGF/esgf-vocab/blob/main/src/esgvoc/api/data_descriptors/False.py):  Not yet implemented |
| | |
| JSON-LD | `universal:mip` |
| Expanded reference link | [https://wcrp-cmip.github.io/WCRP-universe/mip](https://wcrp-cmip.github.io/WCRP-universe/mip) |
| Developer Repo | [![Open in GitHub](https://img.shields.io/badge/Open-GitHub-blue?logo=github&style=flat-square)](https://github.com/WCRP-CMIP/WCRP-universe/tree/main/src-data/mip) |


</section>
    <section id="links">

 </section>

## External Contexts and Key Mappings

 </section>


## 🏛️ Organization and Repository Breakdown

<section id="schema">

## Content Schema

- **`validation-key`**  
  ? (**NoType**)
  No Linked Pydantic Model 
- **`url`**  
  ? (**NoType**)
  No Linked Pydantic Model 
- **`ui-label`**  
  ? (**NoType**)
  No Linked Pydantic Model 
- **`type`**  
  ? (**NoType**)
  No Linked Pydantic Model 
- **`start`**  
  ? (**NoType**)
  No Linked Pydantic Model 
- **`id`**  
  ? (**NoType**)
  No Linked Pydantic Model 
- **`end`**  
  ? (**NoType**)
  No Linked Pydantic Model 
- **`description`**  
  ? (**NoType**)
  No Linked Pydantic Model 
- **`@context`**  
  ? (**NoType**)
  No Linked Pydantic Model 





</section>   

<section id="usage">

## Usage

### Online Viewer 
To view a file in a browser use the content link with `.json` appended. 
eg. https://github.com/WCRP-CMIP/WCRP-universe/tree/main/src-data/mip/cmip5.json

### Getting a File. 

A short example of how to integrate the computed ld file into your code. 

```python

import cmipld
cmipld.get( "universal:mip/cmip5")

```

### Framing
Framing is a way we can filter the downloaded data to match what we want. 
```js
frame = {
            "@context": "https://wcrp-cmip.github.io/WCRP-universe/mip/_context_",
            "@type": "wcrp:mip",
            "keys we want": "",
            "@explicit": True

        }
        
```

```python

import cmipld
cmipld.frame( "universal:mip/cmip5" , frame)

```
</section>

    