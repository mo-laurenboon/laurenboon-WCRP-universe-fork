

<section id="description">

# Native Vertical Grid Units  (universal)

## Description
Specifies the physical units for vertical grid measurements, following the EMD vertical_units controlled vocabulary (e.g., m for metres, Pa for pascals, K for kelvin).


</section>



<section id="info">


| Item | Reference |
| --- | --- |
| Type | `wrcp:native-vertical-grid-units` |
| Pydantic class | [`False`](https://github.com/ESGF/esgf-vocab/blob/main/src/esgvoc/api/data_descriptors/False.py):  Not yet implemented |
| | |
| JSON-LD | `universal:native-vertical-grid-units` |
| Content | [https://wcrp-cmip.github.io/WCRP-universe/native-vertical-grid-units](https://wcrp-cmip.github.io/WCRP-universe/native-vertical-grid-units) |
| Developer Repo | [![Open in GitHub](https://img.shields.io/badge/Open-GitHub-blue?logo=github&style=flat-square)](https://github.com/WCRP-CMIP/WCRP-universe/tree/main/src-data/native-vertical-grid-units) |


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
  - **`id`**  
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
To view a file in a browser use the content link with `.json` appended. eg. https://github.com/WCRP-CMIP/WCRP-universe/tree/main/src-data/native-vertical-grid-units/k.json

### Getting a File. 

A short example of how to integrate the computed ld file into your code. 

```python

import cmipld
cmipld.get( "universal:native-vertical-grid-units/k")

```

### Framing
Framing is a way we can filter the downloaded data to match what we want. 
```js
frame = {
            "@context": "https://wcrp-cmip.github.io/WCRP-universe/native-vertical-grid-units/_context_",
            "@type": "wcrp:native-vertical-grid-units",
            "keys we want": "",
            "@explicit": True

        }
        
```

```python

import cmipld
cmipld.frame( "universal:native-vertical-grid-units/k" , frame)

```
</section>

    