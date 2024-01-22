# Floralens datasets

This repository provides companion datasets to "_Floralens: a Deep Learning Model for the Portuguese Native Flora_".

...TODO brief summary ....

## Labelled image datasets

Dataset | Description | # Species | # Images
--------|-------------|-----------|---------
Floralens dataset | Images used for training and testing the Floralens model. | ... | ...
Wikipedia dataset | Wikipedia images | ... | ...
PlantCLEF dataset | Images from the PlantCLEF dataset | ... | ...

### Floralens dataset

[Download](TODO)

CSV Field | Description
----------|------------
`species` | Plant species.
`filename`| Filename.
`url`     | URL for download.
`source_url`| Source URL.
`set`     | Data split: `TRAIN`, `VALIDATION` and `TEST`. 
`repos`  | Repository: `FloraOn`, `iNaturalist`, `Observation.org`, or `Pl@ntNet`
`gbif-id` | GBIF id or `NA` (not applicable) for `FloraOn` images.


Notes:

- `TRAIN` and `VALIDATION` images were
used for deriving the Floralens model using Google AutoML Vision. `TEST` images define the Floralens test suite (FLTS).

### Wikipedia dataset

[Download](TODO)

CSV Field | Description
----------|------------
`species` | Plant species.
`filename`| Filename.
`url`     | URL for download.
`source_url`| Source URL.

### PlantCLEF dataset

[Download](TODO)

CSV Field | Description
----------|------------
`species` | Plant species.
`filename`| Filename.
`url`     | URL for download.
`source_url`| Source URL.


## Result data sets (TODO)

### Format (TODO)

### Floralens test suite

### PlantCLEF

### Wikipedia
