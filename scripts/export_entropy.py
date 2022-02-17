# -*- coding: utf-8 -*-

from functions import *

path_to_data = str("./data/density_matrices/")

mat_before = [
				np.loadtxt(file) for file in sorted(
					glob(path_to_data + "density*before.txt",
						recursive=True),
					key=numericalSort
				) 
			]

mat_after = [
				np.loadtxt(file) for file in sorted(
					glob(path_to_data + "density*after.txt",
						recursive=True),
					key=numericalSort
				) 
			]


S_before = np.array(
					[von_neumann_entropy(X) for X in mat_before]
				)

S_after = np.array(
					[von_neumann_entropy(X) for X in mat_after]
				)

dS = S_before - S_after

print("",
	"S_before = [ subject_1 , subject_2, ... , subject_9 ]",
		"         = "+str(S_before), "",sep="\n\n")

print("",
	"S_after = [ subject_1 , subject_2, ... , subject_9 ]",
		"        = "+str(S_after), "",sep="\n\n")

print("",
	"dS = [ subject_1 , subject_2, ... , subject_9 ]",
		"   = "+str(dS), "",sep="\n\n")

# Optional: save to disk:
#np.savetxt("S_before.txt", S_before)
#np.savetxt("S_after.txt", S_after)
#np.savetxt("dS.txt", dS)
