Native horizontal grid temporal refinement types, i.e. How the distribution of grid cells varies with time.

<details>
<summary>Click the arrow to learn more.</summary>

  - static: the total number of grid points stays constant during the model run and there is no grid refinement, i.e. the grid is held fixed.
  - dynamically_stretched: the total number of grid points stays constant, but grid points can be dynamically relocated.
  - adaptive: the total number of grid points varies during the model run. The grid is refined locally when important physical processes occur that need additional grid resolution, and coarsened when the additional resolution is no longer needed.

</details>
