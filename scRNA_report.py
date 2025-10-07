# -*- coding: utf-8 -*-
"""
Generate a professional PDF report with embedded PCA plot
"""

import os
import pandas as pd
from fpdf import FPDF

# 1️⃣ Set working directory
os.chdir(r"C:\Users\PC\Desktop\Single cell RNA")

# 2️⃣ Load data
meta_file = "integrate.all.NS.all.KL.fib_cell.meta.data.csv"
cluster_file = "integrate.all.NS.all.KL.fib.main.clusters_cell.meta.data.csv"

meta_df = pd.read_csv(meta_file)
cluster_df = pd.read_csv(cluster_file)
merged_df = meta_df.merge(cluster_df[['Unnamed: 0','condition']], on='Unnamed: 0')

# 3️⃣ Basic Summary
total_cells = merged_df.shape[0]
sample_dist = merged_df['orig.ident'].value_counts()
subpop_dist = merged_df['condition'].value_counts()

# 4️⃣ Create PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", 'B', 16)

# Title
pdf.cell(0, 10, "Single-cell RNA-seq Analysis of Fibroblast Heterogeneity", ln=True, align="C")

pdf.ln(5)
pdf.set_font("Arial", '', 12)

# Objective
pdf.cell(0, 10, "1. Objective", ln=True)
pdf.multi_cell(0, 8, "Analyze fibroblast subpopulations in Keloid and Normal Scar tissues to understand heterogeneity and biological differences.")

pdf.ln(2)
# Dataset
pdf.cell(0, 10, "2. Dataset", ln=True)
pdf.multi_cell(0, 8, f"Total cells: {total_cells}\nSamples distribution:\n{sample_dist.to_string()}")

pdf.ln(2)
# Subpopulations
pdf.cell(0, 10, "3. Subpopulation Distribution", ln=True)
pdf.multi_cell(0, 8, subpop_dist.to_string())

pdf.ln(2)
# Methodology
pdf.cell(0, 10, "4. Methodology", ln=True)
pdf.multi_cell(0, 8, "- Data loading and merging\n- Subpopulation analysis (condition, orig.ident)\n- PCA analysis (nCount_RNA, nFeature_RNA, percent.mt)\n- 2D PCA scatter plot and interactive 3D PCA plot (external HTML)")

pdf.ln(2)
# Results
pdf.cell(0, 10, "5. Results", ln=True)
pdf.multi_cell(0, 8, f"Analysis identified {len(subpop_dist)} subpopulations with distinct distributions. PCA analysis enabled visualization of heterogeneity.")

pdf.ln(2)
# Visualizations
pdf.cell(0, 10, "6. Visualizations", ln=True)
pdf.multi_cell(0, 8, "- 2D PCA Plot embedded below\n- 3D Interactive PCA Simulation: Mini_3D_Fibroblast_Simulation.html (open in browser)")

pdf.ln(3)
# Embed 2D PCA Plot
pca_image = "PCA_2D_Fibroblast.png"
if os.path.exists(pca_image):
    pdf.image(pca_image, x=30, w=150)
else:
    pdf.multi_cell(0, 8, f"Could not find {pca_image} to embed.")

pdf.ln(5)
# Conclusion
pdf.cell(0, 10, "7. Conclusion", ln=True)
pdf.multi_cell(0, 8, "This report demonstrates the distribution and heterogeneity of fibroblast cells in keloid vs normal scar tissue and provides visualizations for further analysis and presentations.")

# 5️⃣ Save PDF
pdf_file = "Fibroblast_scRNA_Report_with_PCA.pdf"
pdf.output(pdf_file)
print(f"PDF Report created: {pdf_file}")
