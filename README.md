[![](https://zenodo.org/badge/DOI/10.5281/zenodo.10639702.svg)](https://doi.org/10.5281/zenodo.10639702)

# Floralens datasets

This repository provides companion datasets to "_Floralens: a Deep Learning Model for the Portuguese Native Flora_".

## Labelled image datasets

Dataset | Description | # Species | # Images
--------|-------------|-----------|---------
Floralens dataset | Images used for training and testing the Floralens model. | 1,678 | 293,601
PlantCLEF dataset | Images from the PlantCLEF dataset | 1,593 | 10,000
Wikipedia dataset | Wikipedia images | 1,351 | 1,351


### Floralens dataset

[floralens/floralens_dataset.tsv](floralens/floralens_dataset.tsv)

TSV Field | Description
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


### PlantCLEF dataset

[plantclef/plantclef_dataset.tsv](plantclef/plantclef_dataset.tsv)

TSV Field | Description
----------|------------
`species` | Plant species.
`filename`| Filename.
`url`     | URL for download.
`source_url`| Source URL.

### Wikipedia dataset

[Download](wikipedia/wikipedia_dataset.tsv)

TSV Field | Description
----------|------------
`species` | Plant species.
`filename`| Filename.
`url`     | URL for download.
`source_url`| Source URL.


## Result data sets 

### Format 


TSV Field | Description
----------|------------
`filename`| Filename.
`species` | Plant species (ground truth).
`rank1`     | Rank 1 (highest confidence label).
`c1`        | Confidence for rank 1 (0 to 1).
`rank2` | Rank 2.
`c2`    | Confidence for rank 2.
`rank3` | Rank 3.
`c3`    | Confidence for rank 3.
`rank4` | Rank 4.
`c4`    | Confidence for rank 4.
`rank5` | Rank 5.
`c5`    | Confidence for rank 5.


### Floralens test suite (FLTS)

Model | File 
--------|-----------
Floralens | [floralens/flts_floralens.tsv](floralens/flts_floralens.tsv)
PN'22 | [floralens/flts_pn22.tsv](floralens/flts_pn22.tsv)   
PN'23 | [floralens/flts_pn23.tsv](floralens/flts_pn23.tsv)   
PN'23 SWE | [floralens/flts\_pn23\_swe.tsv](floralens/flts_pn23_swe.tsv)

### PlantCLEF

Model | File 
--------|-----------
Floralens | [plantclef/plantclef_floralens.tsv](floralens/flts_floralens.tsv)
PN'22 | [plantclef/plantclef_pn22.tsv](plantclef/flts_pn22.tsv)   
PN'23 | [plantclef/plantclef_pn23.tsv](plantclef/flts_pn23.tsv)   
PN'23 SWE | [plantclef/plantclef\_pn23\_swe.tsv](plantclef/plantclef_pn23_swe.tsv)

### Wikipedia

Model | File
--------|-----------
Floralens | [wikipedia/wikipedia_floralens.tsv](floralens/flts_floralens.tsv)
PN'22 | [wikipedia/wikipedia_pn22.tsv](wikipedia/flts_pn22.tsv)
PN'23 | [wikipedia/wikipedia_pn23.tsv](wikipedia/flts_pn23.tsv)
PN'23 SWE | [wikipedia/wikipedia\_pn23\_swe.tsv](wikipedia/wikipedia_pn23_swe.tsv)
