# Mathematical Proofs

A collection of proofs and derivations written by me in LaTeX.

## Structure
```
.
├── *.tex          # LaTeX source files
└── pdf_outputs/   # Compiled PDFs
```

## Topics

<!-- List your proofs here, e.g.: -->
- Integrals from the family of Sophomore's Dream
- Products and Sums involving trigonometric, hyperbolic, algebraic functions
- Series involving the use of Gamma ($\Gamma$), Polygamma ($\psi$), Riemann-Zeta ($\zeta$) functions and the harmonic series. 

## Building

Although the PDF files are in the `pdf_outputs/` folder, the tex files can be compiled to PDF using

(I don't see why you'll have to compile them but anyway)

```bash
pdflatex proof_name.tex
```

Or compile all at once:

```bash
for f in *.tex; do pdflatex "$f"; done
mv *.pdf pdf_outputs/
```
