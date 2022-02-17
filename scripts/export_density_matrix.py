# -*- coding: utf-8 -*-

from important_functions import *

path_to_data = str("./data/time_series/")

def export_density_matrix(path_to_data):
	"""
	Export the density matrices as TXT files (the same ones found in
	./data/density_matrices/).
	
	Parameters
	----------
	path_to_data : str  
		The path to the directory containing the time series. 
	"""
	folder = [
				file for file in sorted(
									glob(path_to_data + '\*',
                               recursive=True), 
				key=numericalSort)
			]

	before = [file for file in sorted(
									glob(folder[1] + '\*',
								recursive=True),
				key=numericalSort)
			]

	after = [file for file in sorted(
									glob(folder[0] + '\*',
								recursive=True),
				key=numericalSort)
			]


	n, m = len(before), len(after)	


	def export(path, subject, before=False, after=False):

		X = array_of_time_series(path) 
	
		A = density_matrix(X)

		if before == True:
			return np.savetxt(
					'density_matrix_subject_' + str(subject) + '_before.txt', A)

		if after == True:
			return np.savetxt(
					'density_matrix_subject_' + str(subject) + '_after.txt', A)

	for i in np.arange(7, 8): 
		export(
				before[i]+'**/timeCourse*.mat', i + 1,
						before=True,
				after=False
			)

	for i in np.arange(7, 8): 
		export(
				after[i]+'**/timeCourse*.mat', i + 1,
						before=False,
				after=True
			)
