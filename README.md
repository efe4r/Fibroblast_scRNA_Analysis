# Single-cell RNA-seq Analysis of Fibroblast Heterogeneity

This repository contains a comprehensive analysis of fibroblast heterogeneity in human skin fibrotic diseases (Keloid and Normal Scar tissues) using single-cell RNA sequencing (scRNA-seq). The project demonstrates both computational analysis and interactive visualizations, suitable for bioinformatics, computational biology, and data visualization purposes.

## 🧬 Dataset
- **GEO Accession:** [GSE163973](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE163973)
- **Organism:** Homo sapiens
- **Cells:** 12,177 fibroblast cells
- **Samples:** NF1, NF2, NF3 (normal scar); KF1, KF2, KF3 (keloid)
- **Subpopulations:** NF (normal fibroblasts), KF (keloid fibroblasts)

## 📂 Repository Contents
| File | Description |
|------|-------------|
| `scRNA_analysis.py` | Python script performing data loading, merging, subpopulation analysis, PCA, and generating summary outputs. |
| `PCA_2D_Fibroblast.png` | Static 2D PCA plot showing fibroblast heterogeneity. |
| `Mini_3D_Fibroblast_Simulation.html` | Interactive 3D PCA simulation of fibroblast subpopulations. |
| `Fibroblast_scRNA_Report_with_PCA.pdf` | PDF report summarizing analysis, results, and visualizations. |
| `README.md` | Project overview and instructions. |

## ⚙️ Methodology
1. **Data preprocessing**: Loaded and merged scRNA-seq metadata and cluster assignments.  
2. **Subpopulation analysis**: Counted cells per sample and per fibroblast subpopulation.  
3. **PCA analysis**: Applied PCA on key QC metrics (`nCount_RNA`, `nFeature_RNA`, `percent.mt`) to visualize heterogeneity.  
4. **Visualizations**:  
   - Static 2D PCA scatter plot (`PCA_2D_Fibroblast.png`)  
   - Interactive 3D PCA simulation (`Mini_3D_Fibroblast_Simulation.html`)  
5. **Report generation**: Summary report generated as PDF with embedded figures (`Fibroblast_scRNA_Report_with_PCA.pdf`).

## 📊 Results
- **Total cells analyzed:** 12,177  
- **Subpopulations:** 2 main fibroblast groups (NF and KF) with distinct distributions.  
- PCA analysis clearly separates NF and KF cells, demonstrating heterogeneity.  
- Interactive 3D simulation allows further exploration of subpopulation structure.

## 🖥️ How to Run
1. Install required packages:
```bash
pip install pandas matplotlib scikit-learn fpdf
