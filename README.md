**[summary](#summary) |  [usage](#usage) | [issues](#issues) | [citation](#citation) | [license](#license)**


# A framework for simulation and inversion in electromagnetics
[![Build Status](https://travis-ci.org/simpeg-research/heagyetal-2017-simpegem.svg?branch=master)](https://travis-ci.org/simpeg-research/heagyetal-2017-simpegem)
[![Zenodo](https://zenodo.org/badge/124603211.svg)](https://zenodo.org/badge/latestdoi/124603211)
[![License](https://img.shields.io/github/license/simpeg-research/heagyetal-2017-simpegem.svg)](https://github.com/simpeg-research/heagyetal-2017-simpegem/blob/master/LICENSE)
[![SimPEG](https://img.shields.io/badge/powered%20by-SimPEG-blue.svg)](http://simpeg.xyz)

## Summary

Simulations and inversions of electromagnetic geophysical data are paramount for discerning meaningful information about the subsurface from these data. Depending on the nature of the source electromagnetic experiments may be classified as time-domain or frequency-domain. Multiple heterogeneous and sometimes anisotropic physical properties, including electrical conductivity and magnetic permeability, may need be considered in a simulation. Depending on what one wants to accomplish in an inversion, the parameters which one inverts for may be a voxel-based description of the earth or some parametric representation that must be mapped onto a simulation mesh. Each of these permutations of the electromagnetic problem has implications in a numerical implementation of the forward simulation as well as in the computation of the sensitivities, which are required when considering gradient-based inversions. This paper proposes a framework for organizing and implementing electromagnetic simulations and gradient-based inversions in a modular, extensible fashion. We take an object-oriented approach for defining and organizing each of the necessary elements in an electromagnetic simulation, including: the physical properties, sources, formulation of the discrete problem to be solved, the resulting fields and fluxes, and receivers used to sample to the electromagnetic responses. A corresponding implementation is provided as part of the open source simulation and parameter estimation project SimPEG (http://simpeg.xyz). The application of the framework is demonstrated through two synthetic examples and one field example. The first example shows the application of the common framework for 1D time domain and frequency domain inversions. The second is a field example that demonstrates a 1D inversion of electromagnetic data collected over the Bookpurnong Irrigation District in Australia. The final example is a 3D example which shows how the modular implementation is used to compute the sensitivity for a parametric model where a transmitter is positioned inside a steel cased well.

## Usage

Dependencies are specified in [requirements.txt](/requirements.txt)

```
pip install -r requirements.txt
```

To run the notebooks locally, you will need to have python installed,
preferably through [anaconda](https://www.anaconda.com/download/) .

You can then clone this repository. From a command line, run

```
git clone https://github.com/simpeg-research/heagyetal-2017-simpegem.git
```

Then `cd` into the `heagyetal-2017-simpegem` directory:

```
heagyetal-2017-simpegem
```

To setup your software environment, we recommend you use the provided conda environment

```
conda env create -f environment.yml
conda activate simpegem-2017
```


## Issues


Please [make an issue](https://github.com/simpeg-research/heagyetal-2017-simpegem/issues) if you encounter any problems while trying to run the notebooks.


## Citation 
Heagy, L. J., Cockett, R., Kang, S., Rosenkjaer, G. K., & Oldenburg, D. W. (2017). A framework for simulation and inversion in electromagnetics. Computers & Geosciences, 107, 1-19.

```
@article{heagy2017framework,
  title={A framework for simulation and inversion in electromagnetics},
  author={Heagy, Lindsey J and Cockett, Rowan and Kang, Seogi and Rosenkjaer, Gudni K and Oldenburg, Douglas W},
  journal={Computers \& Geosciences},
  volume={107},
  pages={1--19},
  year={2017},
  publisher={Elsevier}
}
```

## License
These notebooks are licensed under the [MIT License](/LICENSE) which allows academic and commercial re-use and adaptation of this work.
