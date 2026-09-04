# Electron Transport in Molecular Nanostructures

LaTeX source for Alessandro Lodi's 2022 DPhil thesis in Materials at the
University of Oxford (Trinity College).

- [Read the deposited thesis in the Oxford University Research Archive (ORA)](https://ora.ox.ac.uk/objects/uuid:efac5b76-bed2-4791-a0eb-685f8f3fc728)
- [DOI: 10.5287/ora-2z28m6qqk](https://doi.org/10.5287/ora-2z28m6qqk)
- [Alessandro Lodi on Google Scholar](https://scholar.google.com/citations?user=CbY3D9AAAAAJ&hl=it)

## About the thesis

This thesis investigates electron transport in electronic devices built from
molecularly defined graphene nanoribbons (GNRs). Unlike graphene and carbon
nanotubes, these atomically precise nanostructures can combine an intrinsic
bandgap with well-defined topology, making them promising building blocks for
low-power and quantum electronic devices.

The work focuses on three connected problems:

- integrating molecular GNRs into single-electron transistors and studying
  their transport regimes from cryogenic temperatures to room temperature;
- understanding how edge functionalisation and solubility affect aggregation,
  device cleanliness, and electron-vibration coupling; and
- controlling the electronic structure through chemical substituents and
  porphyrin units incorporated into the GNR backbone.

The thesis reports room-temperature Coulomb oscillations in a molecular GNR
single-electron transistor, exceptionally clean low-temperature transport with
signatures of strong Franck-Condon coupling, and ambipolar field-effect
transport in porphyrin-containing GNRs. Together, these results establish
practical routes for studying quantum, vibrational, and topological phenomena
in molecular nanoribbon devices.

## Repository contents

The document is assembled from `Oxford_Thesis.tex`. The main source is organised
by topic:

- `chapter_preintro/` and `chapter_introduction/` — motivation and background;
- `chapter_fabrication/` — nanodevice fabrication and measurement methods;
- `chapter_instr_dev/` — instrumentation development;
- `chapter_gnrset/` — molecular GNR single-electron transistors;
- `chapter_solubility/` — edge functionalisation, solubility, and transport;
- `chapter_doping/` — chemical doping and porphyrin-containing GNRs;
- `chapter_summary/` — conclusions and perspectives; and
- `text/` — front matter and appendices.

Figures are stored alongside their corresponding chapter. Bibliographic data is
in `references.bib` and `references_intro.bib`.

## Building the thesis

A TeX distribution with `pdflatex`, Biber, and the packages imported by
`Packages.tex` is required. From the repository root, run:

```sh
pdflatex Oxford_Thesis.tex
biber Oxford_Thesis
pdflatex Oxford_Thesis.tex
pdflatex Oxford_Thesis.tex
```

The generated `Oxford_Thesis.pdf` is a local build artifact. For the definitive
deposited version, use the ORA record linked above.

## Citation

```bibtex
@phdthesis{lodi2022electron,
  author = {Lodi, Alessandro},
  title = {Electron Transport in Molecular Nanostructures},
  school = {University of Oxford},
  year = {2022},
  doi = {10.5287/ora-2z28m6qqk}
}
```

## Template acknowledgement

The thesis uses the OxThesis class, derived from Keith Gillow's original Oxford
mathematics template and later adaptations by Sam Evans and John McManigle. See
the source comments and `LICENSE` for attribution and licensing details.
