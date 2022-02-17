## Data repository for the manuscript arXiv.2106.05379

This repository is structured in the following way.

	./
	├── data
	│   ├── density_matrices
	│   └── time_series
	│
	├── figures
	├── results
	└── scripts

```data``` : Folder containing the density matrices and fMRI time series (each
in its own subfolder).

```figures``` : Folder containing .tex files that, when compiled with
TikZ/PGFPlots packages, renders the figures in the manuscript.

```results``` : Folder containing the resulting entropies; before, after,
and their difference.

```scripts``` : Folder containing all the main functions to handle the 
fMRI time series, to generate the density matrices, and to calculate
their entropies.


Contact: h.felippe at fisica.ufrn.br

H. Felippe, A. Viol, D. B. de Araujo, M. G. E. da Luz, F. Palhano-Fontes, H.
Onias, E. P. Raposo, G. M. Viswanathan. “The von Neumann entropy for the Pearson
correlation matrix: A test of the entropic brain hypothesis” 
[arxiv.org/2106.05379](https://arxiv.org/abs/2106.05379).
