[![](https://zenodo.org/badge/DOI/10.5281/zenodo.10639702.svg)](https://doi.org/10.5281/zenodo.10639702)

# Floralens supplementary material

This repository provides supplementary material to "[_Floralens: a Deep Learning Model for the Portuguese Native Flora_](https://arxiv.org/abs/2403.12072)", a paper draft by António Filgueiras, [Eduardo R. B. Marques](https://www.dcc.fc.up.pt/~edrdo), [Luís M. B. Lopes](https://www.dcc.fc.up.pt/~lblopes), Miguel Marques, and Hugo Silva from [CRACS / INESC-TEC](https://www.inesctec.pt/en/centres/cracs) and [DCC/FCUP](https://www.dcc.fc.up.pt).

The code and data artifacts are as follows:

- Jupyter notebooks that derive all the plots of Section 4 ("Results") in the paper (see links to notebooks in list below)
- the Floralens, PlantCLEF and Wikipedia datasets described in the paper, and;
- Data files containing results derived using the Floralens model or through the Pl@ntNet API. 


## Notebooks

Notebooks can be found in the [`notebooks`](notebooks) folder, and notebook-derived plot images used in the paper can be found in [`notebooks/plot_images`](notebooks/plot_images).

- Baseline results (section 4.1 in the paper)
    - [Precision and recall](notebooks/Baseline_Precision_And_Recall.ipynb)
    - [Top-1, Top-5, MRR - overall and by data source ](notebooks/Baseline_Top1_Top5_And_MRR.ipynb)
    - [Top-1, Top-5, MRR - boxplots](notebooks/Baseline_Top1_Top5_And_MRR-Boxplots.ipynb)
    - [Top-1, Top-5, MRR - by growth form and species' special status](notebooks/Baseline_GrowthForm_And_SpecialStatus.ipynb)

- [PlantCLEF/Wikipedia and genus/family results](notebooks/Species_Genus_And_Family_Results.ipynb) (sections 4.2 and 4.3)
- [Multiple image classification](notebooks/Multiple_image_classification.ipynb) (section 4.4)
- [Geographical filter](notebooks/Geographical_Filter.ipynb) (section 4.5)
- Pl@ntNet comparison (section 4.6)
    - [MRR value comparison](notebooks/PlantNetComparison.ipynb)
    - [MRR value comparison by species' growth form and special status](notebooks/PlantNetComparison_GrowthForm_And_SpecialStatus.ipynb)


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
PN'22 | [plantclef/plantclef_pn22.tsv](plantclef/plantclef_pn22.tsv)   
PN'23 | [plantclef/plantclef_pn23.tsv](plantclef/plantclef_pn23.tsv)   
PN'23 SWE | [plantclef/plantclef\_pn23\_swe.tsv](plantclef/plantclef_pn23_swe.tsv)

### Wikipedia

Model | File
--------|-----------
Floralens | [wikipedia/wikipedia_floralens.tsv](floralens/flts_floralens.tsv)
PN'22 | [wikipedia/wikipedia_pn22.tsv](wikipedia/wikipedia_pn22.tsv)
PN'23 | [wikipedia/wikipedia_pn23.tsv](wikipedia/wikipedia_pn23.tsv)
PN'23 SWE | [wikipedia/wikipedia\_pn23\_swe.tsv](wikipedia/wikipedia_pn23_swe.tsv)
