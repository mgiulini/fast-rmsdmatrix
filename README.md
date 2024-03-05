# fast-rmsdmatrix
A dependency-free C code for parallel rmsd and il-rmsd matrix calculation

## installation

```bash
cd src/
chmod u+x Makefile
make
cd -
```

## Usage and examples

### RMSD matrix calculation

```bash
./src/fast-rmsdmatrix ./examples/traj.xyz 3 47 9 18 20 117
```
where the positional arguments represent:

-  the coordinates of the model in xyz format (./examples/traj.xyz)
-  the index of the used core (3)
-  the number of pairwise matrix elements to be calculated (47)
-  the index of the reference structure to start the calculation (9)
-  the index of the mobile structure to start the calculation (18)
-  the number of models (20)
-  the number of atoms (117). This must be consistent across different models

### ILRMSD matrix calculation:

```bash
./src/fast-rmsdmatrix ./examples/traj_rec.xyz 3 47 9 18 20 120 ./examples/traj_lig.xyz 57
```

The first seven arguments are the same as before, with the only difference that the number of atoms (120 now) refers to the number of atoms in the receptor trajectory. The two extra arguments are the ligand trajectory file (./examples/traj_lig.xyz) and the number of atoms in the ligand trajectory (here 57).
