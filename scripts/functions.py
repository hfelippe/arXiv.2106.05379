# -*- coding: utf-8 -*-

import scipy.linalg as linalg
import scipy.io as io
import numpy as np

from glob import glob
import re


# -----------------------------------------------------------------------------
# 				The following is to sort files in numerical order

numbers = re.compile(r'(\d+)')

def numericalSort(value):

    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts
# -----------------------------------------------------------------------------



def matlab_to_python(file):
	"""
	Convert MATLAB arrays into Python arrays. 

	The original dataset is composed of BOLD fMRI time series as MATLAB
	arrays, that is, files with the .m extension. This function is thus
	necessary for the Pythonic analysis of the time series.

	Parameters
	----------
	file : MATLAB array
		Files with .m extension.

	Returns
	-------
	py_arr : ndarray
		The converted MATLAB array.
	"""
	m_arr  = io.loadmat(file)['X_3']
	n = len(m_arr)
	py_arr = m_arr.reshape(1, n)[0]

	return py_arr


def array_of_time_series(PATH):
	"""
	Amalgamate the time series in a given folder (of a subject in a 
	particular condition, "before" or "after"). Returns an array 
	containing a set of vectors of observations (time series).

	Again, since this analysis requires Python arrays, we invoke the
	function  matlab_to_python  to convert MATLAB arrays into Python
	ones.

	Parameters
	----------
	PATH: str
		The path to the dataset.

	Returns
	-------
	X : ndarray
		A 1-D containing multiple variables.
	"""
	X = np.array(
					[
						matlab_to_python(file) for file in sorted(
					glob(PATH, recursive=True), 
				key=numericalSort
				)
			]
		)
	return X


def density_matrix(X):
	"""
	Calculate the density matrix from a set of vectors.

	Parameters
	----------
	X : array_like
		A 1-D or 2-D array containing multiple variables.

	Returns
	-------
	A : ndarray
		The scaled correlation matrix (density matrix) of X.
	"""
	N = len(X)
	R = np.corrcoef(X)
	A = R / N	

	return A


def von_neumann_entropy(A, norm=False):
	"""
	Calculate the von Neumann entropy of a density matrix.

	Parameters
	----------
	A : array_like
		Density matrix whose von Neumann entropy to evaluate.

	norm : bool, optional
		Evaluates the normalized von Neumann entropy of A. (Default: False)

	Returns
	-------
	S : ndarray
		The von Neumann entropy of A.
	"""
	logA  = linalg.logm(A)
	AlogA = np.matmul(A, logA)

	N = len(A)
	S = -np.trace(AlogA)

	if norm == True:
		return S / np.log(N)

	else:
		return S
