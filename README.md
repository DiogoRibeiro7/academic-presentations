# Academic Presentations

**Diogo Ribeiro**<br>
_ESMAD - Escola Superior de Média Arte e Design_<br>
_Lead Data Scientist, Mysense.ai_

[![ORCID](https://img.shields.io/badge/ORCID-0009--0001--2022--7072-green.svg)](https://orcid.org/0009-0001-2022-7072) [![Email](https://img.shields.io/badge/Email-dfr%40esmad.ipp.pt-blue.svg)](mailto:dfr@esmad.ipp.pt) [![Institution](https://img.shields.io/badge/Institution-ESMAD-orange.svg)](https://www.esmad.ipp.pt/) [![Company](https://img.shields.io/badge/Company-Mysense.ai-purple.svg)](https://mysense.ai/)

## 🎯 Overview

This repository contains a collection of academic presentations covering advanced topics in statistics, machine learning, and data science. The materials are designed for graduate-level courses, research seminars, and professional training programs.

## 📚 Presentations

### Statistical Methods & Theory

- **[Advanced MCMC Methods](./mcmc/)** - Comprehensive coverage from theory to modern implementations

  - 📄 LaTeX Beamer source
  - 📊 Implementation examples
  - 📖 Comprehensive bibliography
  - 🎯 Level: Graduate/Professional

### Machine Learning & AI

_Coming soon..._

### Data Science Applications

_Coming soon..._

### Financial Modeling

_Coming soon..._

## 🏗️ Repository Structure

```
academic-presentations/
├── README.md
├── LICENSE
├── presentations/
│   ├── mcmc-advanced/
│   │   ├── slides/
│   │   │   ├── advanced_mcmc_beamer.tex
│   │   │   ├── advanced_mcmc_beamer.pdf
│   │   │   └── figures/
│   │   ├── code/
│   │   │   ├── advanced_mcmc_implementation.py
│   │   │   └── examples/
│   │   ├── bibliography/
│   │   │   └── mcmc_bibliography.md
│   │   └── README.md
│   └── template/
│       ├── beamer-template.tex
│       └── style-guide.md
├── assets/
│   ├── logos/
│   └── templates/
└── docs/
    ├── contribution-guide.md
    └── presentation-standards.md
```

## 🎨 Presentation Standards

### Technical Requirements

- **Format**: LaTeX Beamer for mathematical content
- **Aspect Ratio**: 16:9 for modern displays
- **Theme**: Professional academic themes (Madrid, Bergen, etc.)
- **Typography**: Computer Modern or professional sans-serif fonts

### Content Guidelines

- **Mathematical Rigor**: Formal definitions and proofs where appropriate
- **Practical Focus**: Real-world applications and implementations
- **Code Examples**: Working implementations in Python/R
- **References**: Comprehensive bibliographies with primary sources

### Quality Standards

- ✅ Peer-reviewed content accuracy
- ✅ Professional visual design
- ✅ Accessible mathematical exposition
- ✅ Reproducible code examples
- ✅ Comprehensive documentation

## 📖 How to Use

### For Students

1. Browse presentations by topic area
2. Download PDF for viewing or LaTeX source for customization
3. Follow along with code examples
4. Use bibliographies for further reading

### For Educators

1. Fork or download materials for course use
2. Customize content for your specific needs
3. Attribution required (see License section)
4. Contributions welcome via pull requests

### For Researchers

1. Use as reference for methodology
2. Cite materials in your work
3. Contribute improvements or corrections
4. Collaborate on new presentations

## 🔧 Building Presentations

### Prerequisites

```bash
# LaTeX distribution (TeX Live recommended)
sudo apt-get install texlive-full  # Ubuntu/Debian
brew install --cask mactex         # macOS

# Python environment (for code examples)
pip install numpy scipy matplotlib seaborn pandas
```

### Compilation

```bash
# Navigate to presentation directory
cd presentations/mcmc-advanced/slides/

# Compile LaTeX
pdflatex advanced_mcmc_beamer.tex
pdflatex advanced_mcmc_beamer.tex  # Run twice for references

# Or use latexmk for automatic compilation
latexmk -pdf advanced_mcmc_beamer.tex
```

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](./docs/contribution-guide.md) for guidelines.

### How to Contribute

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/new-presentation`)
3. **Commit** your changes (`git commit -am 'Add new ML presentation'`)
4. **Push** to the branch (`git push origin feature/new-presentation`)
5. **Create** a Pull Request

### Contribution Types

- 🐛 **Bug fixes** in existing presentations
- 📚 **New presentations** on relevant topics
- 💡 **Improvements** to existing content
- 📖 **Documentation** enhancements
- 🧪 **Code examples** and implementations

## 📄 License

### Academic Use

This work is licensed under [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).

**You are free to:**

- **Share** -- copy and redistribute the material
- **Adapt** -- remix, transform, and build upon the material

**Under the following terms:**

- **Attribution** -- You must give appropriate credit
- **ShareAlike** -- If you remix or transform the material, you must distribute under the same license

### Code Components

Code examples and implementations are licensed under [MIT License](https://opensource.org/licenses/MIT).

## 📞 Contact & Collaboration

### Professional Inquiries

- **Email**: dfr@esmad.ipp.pt
- **Institution**: ESMAD - Escola Superior de Média Arte e Design
- **Company**: Mysense.ai (Lead Data Scientist)
- **ORCID**: [0009-0001-2022-7072](https://orcid.org/0009-0001-2022-7072)

### Research Interests

- Markov Chain Monte Carlo methods
- Bayesian statistics and computation
- Machine learning applications
- Financial risk modeling
- Computational statistics

### Collaboration Opportunities

- 🎓 **Guest lectures** at universities
- 🏢 **Corporate training** programs
- 🔬 **Research collaborations**
- 📝 **Joint publications**
- 🌐 **Conference presentations**

## 🌟 Acknowledgments

- **ESMAD** for institutional support
- **Mysense.ai** for industry applications
- **Students and colleagues** for feedback and suggestions
- **Open source community** for tools and inspiration

## 📊 Statistics

![GitHub stars](https://img.shields.io/github/stars/diogoribeiro7/academic-presentations?style=social) ![GitHub forks](https://img.shields.io/github/forks/diogoribeiro7/academic-presentations?style=social) ![GitHub watchers](https://img.shields.io/github/watchers/diogoribeiro7/academic-presentations?style=social)

--------------------------------------------------------------------------------

**Last Updated**: October 2025<br>
**Repository Maintainer**: Diogo Ribeiro<br>
**Status**: Actively maintained ✅
