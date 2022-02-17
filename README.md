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

```data```: Folder containing the datasets used. , i.e., the scaled correlation
matrices (```density_matrices```) and the fMRI BOLD time series 
(```time_series```). 

```figures```: Folder containing .tex files that, when compiled using the 
TikZ/PGFPlots packages, give the figures in the manuscript. **Warning**:
Both the files Fig2a.tex and Fig2b.tex must be compiled with the following
options:

	```$ pdflatex --enable-write18 --extra-mem-top=1000000000 --synctex=1```

```results```: Folder containing the resulting entropies $S_{\rm before}$,
$S_{\rm after}$, and the difference $\Delta S$.

```scripts```: Folder containing all the main functions to handle the 
fMRI time courses, as well as generating the density matrices and calculating
their entropies.
