

<section id="description">

# Model Family  (universal)

[View in HTML](https://wcrp-cmip.github.io/WCRP-universe/model-family/model-family)

## Description
Groups related climate models into families that share similar code bases or modeling approaches, as defined by the EMD specification for tracking model genealogies.


</section>



<section id="info">


| Item | Reference |
| --- | --- |
| Type | `wrcp:model-family` |
| Pydantic class | [`False`](https://github.com/ESGF/esgf-vocab/blob/main/src/esgvoc/api/data_descriptors/False.py):  Not yet implemented |
| | |
| JSON-LD | `universal:model-family` |
| Expanded reference link | [https://wcrp-cmip.github.io/WCRP-universe/model-family](https://wcrp-cmip.github.io/WCRP-universe/model-family) |
| Developer Repo | [![Open in GitHub](https://img.shields.io/badge/Open-GitHub-blue?logo=github&style=flat-square)](https://github.com/WCRP-CMIP/WCRP-universe/tree/main/src-data/model-family) |


</section>
    <section id="links">

 </section>

## External Contexts and Key Mappings

 </section>

- **origin** → `@type: @id`
 </section>

  - Context: [https://wcrp-cmip.github.io/WCRP-universe/organisation/_context_](https://wcrp-cmip.github.io/WCRP-universe/organisation/_context_)
 </section>

  - Source: `WCRP-universe/organisation/_context_`

 </section>


## 🏛️ Organization and Repository Breakdown

 </section>

- **Organization:** `WCRP-universe`
 </section>

  - Repository: `organisation`
 </section>

    - Path: `/_context_`
 </section>


<section id="schema">

## Content Schema

- **`validation-key`**  
  ? (**NoType**)
  No Linked Pydantic Model 
- **`ui-label`**  
  ? (**NoType**)
  No Linked Pydantic Model 
- **`type`**  
  ? (**NoType**)
  No Linked Pydantic Model 
- **`origin`**  
  ? (**NoType**)
  No Linked Pydantic Model 
- **`id`**  
  ? (**NoType**)
  No Linked Pydantic Model 
- **`description`**  
  ? (**NoType**)
  No Linked Pydantic Model 
- **`@context`**  
  ? (**NoType**)
  No Linked Pydantic Model 
- **`permissible_realms`**  
  ? (**NoType**)
  No Linked Pydantic Model 





</section>   

<section id="usage">

## Usage

### Online Viewer 
To view a file in a browser use the content link with `.json` appended. 
eg. https://github.com/WCRP-CMIP/WCRP-universe/tree/main/src-data/model-family/acce.json

### Getting a File. 

A short example of how to integrate the computed ld file into your code. 

```python

import cmipld
cmipld.get( "universal:model-family/acce")

```

### Framing
Framing is a way we can filter the downloaded data to match what we want. 
```js
frame = {
            "@context": "https://wcrp-cmip.github.io/WCRP-universe/model-family/_context_",
            "@type": "wcrp:model-family",
            "keys we want": "",
            "@explicit": True

        }
        
```

```python

import cmipld
cmipld.frame( "universal:model-family/acce" , frame)

```
</section>

    