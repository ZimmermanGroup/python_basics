#!/export/apps/CentOS7/anaconda/3.5.3.0/bin/python

import os

with open('confs.xyz','r') as f:
	flines = f.readlines()

	natoms = int(flines[0])
	nlines = natoms + 2

	for i,n in enumerate(range(0,len(flines),nlines)):
		if not os.path.exists(f'{i:03d}'):
			os.mkdir(f'{i:03d}')
		with open(f'{i:03d}/geom.xyz','w') as g:
			outstr = ''.join(flines[n:n+nlines])
			g.write(outstr)
		with open(f'{i:03d}/qchem.in','w') as h:
			h.write('$rem\n')
			h.write('method hf\n')
			h.write('basis 6-31G\n')
			h.write('$end\n')
			h.write('$molecule\n 0 1\n')
			h.write(''.join(flines[n+2:n+nlines]))
			h.write('$end')
