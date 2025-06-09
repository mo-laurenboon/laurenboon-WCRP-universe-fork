

<section id="description">

# Native Vertical Grid Coordinate  (universal)

## Description
Defines the vertical coordinate systems used by model components, based on the EMD coordinate controlled vocabulary (e.g., height, air_pressure, ocean_s_coordinate, land_ice_sigma_coordinate).


</section>



<section id="info">


| Item | Reference |
| --- | --- |
| Type | `wrcp:native-vertical-grid-coordinate` |
| Pydantic class | [`False`](https://github.com/ESGF/esgf-vocab/blob/main/src/esgvoc/api/data_descriptors/False.py):  Not yet implemented |
| | |
| JSON-LD | `universal:native-vertical-grid-coordinate` |
| Content | [https://wcrp-cmip.github.io/WCRP-universe/native-vertical-grid-coordinate](https://wcrp-cmip.github.io/WCRP-universe/native-vertical-grid-coordinate) |
| Developer Repo | [![Open in GitHub](https://img.shields.io/badge/Open-GitHub-blue?logo=github&style=flat-square)](https://github.com/WCRP-CMIP/WCRP-universe/tree/main/src-data/native-vertical-grid-coordinate) |


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
To view a file in a browser use the content link with `.json` appended. 
eg. https://github.com/WCRP-CMIP/WCRP-universe/tree/main/src-data/native-vertical-grid-coordinate/air-potential-temperature.json

### Getting a File. 

A short example of how to integrate the computed ld file into your code. 

```python

import cmipld
cmipld.get( "universal:native-vertical-grid-coordinate/air-potential-temperature")

```

### Framing
Framing is a way we can filter the downloaded data to match what we want. 
```js
frame = {
            "@context": "https://wcrp-cmip.github.io/WCRP-universe/native-vertical-grid-coordinate/_context_",
            "@type": "wcrp:native-vertical-grid-coordinate",
            "keys we want": "",
            "@explicit": True

        }
        
```

```python

import cmipld
cmipld.frame( "universal:native-vertical-grid-coordinate/air-potential-temperature" , frame)

```
</section>

    