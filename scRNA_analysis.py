# -*- coding: utf-8 -*-
"""
Single-cell RNA-seq Analysis + CV-ready Summary + Mini 3D Simulation
Dataset: GSE163973 (Fibroblast heterogeneity in Keloid vs Normal Scar)
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import plotly.graph_objects as go

# ----------------------------------------
# 1️⃣ Set working directory
# ----------------------------------------
os.chdir(r"C:\Users\PC\Desktop\Single cell RNA")

# ----------------------------------------
# 2️⃣ Load CSV files
# ----------------------------------------
meta_file = r"integrate.all.NS.all.KL.fib_cell.meta.data.csv"
cluster_file = r"integrate.all.NS.all.KL.fib.main.clusters_cell.meta.data.csv"

meta_df = pd.read_csv(meta_file)
cluster_df = pd.read_csv(cluster_file)

# ----------------------------------------
# 3️⃣ Merge for unified analysis
# ----------------------------------------
merged_df = meta_df.merge(cluster_df[['Unnamed: 0','condition']], on='Unnamed: 0')

# ----------------------------------------
# 4️⃣ Basic Summary Analysis
# ----------------------------------------
total_cells = merged_df.shape[0]
print("\nTotal number of cells:", total_cells)
print("\nSample-wise distribution:")
print(merged_df['orig.ident'].value_counts())
print("\nSubpopulation distribution:")
print(merged_df['condition'].value_counts())

# ----------------------------------------
# 5️⃣ PCA for dimensionality reduction (3D)
# ----------------------------------------
# Use 3 features for PCA
features = ['nCount_RNA', 'nFeature_RNA', 'percent.mt']
x = merged_df.loc[:, features].values
x_scaled = StandardScaler().fit_transform(x)
pca = PCA(n_components=3)
principal_components = pca.fit_transform(x_scaled)

merged_df['PC1'] = principal_components[:,0]
merged_df['PC2'] = principal_components[:,1]
merged_df['PC3'] = principal_components[:,2]

# ----------------------------------------
# 6️⃣ 3D Scatter Plot (interactive, mini simulation)
# ----------------------------------------
fig = go.Figure()
subpops = merged_df['condition'].unique()
colors = ['red','blue','green','orange','purple']

for i, subpop in enumerate(subpops):
    df_sub = merged_df[merged_df['condition']==subpop]
    fig.add_trace(go.Scatter3d(
        x=df_sub['PC1'],
        y=df_sub['PC2'],
        z=df_sub['PC3'],
        mode='markers',
        name=subpop,
        marker=dict(size=4, color=colors[i % len(colors)], opacity=0.8)
    ))

fig.update_layout(title='Mini 3D Fibroblast Simulation (PCA)', 
                  scene=dict(xaxis_title='PC1', yaxis_title='PC2', zaxis_title='PC3'))
fig.write_html("Mini_3D_Fibroblast_Simulation.html")

# ----------------------------------------
# 7️⃣ Optional: Save a static PCA 2D plot
# ----------------------------------------
plt.figure(figsize=(8,6))
sns.scatterplot(data=merged_df, x='PC1', y='PC2', hue='condition', palette='Set2', s=20)
plt.title('2D PCA of Fibroblast Cells')
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.tight_layout()
plt.savefig("PCA_2D_Fibroblast.png")
plt.close()

# ----------------------------------------
# 8️⃣ CV-ready Summary
# ----------------------------------------
subpopulations = merged_df['condition'].unique()
cv_summary = f"""
Single-cell RNA-seq Analysis of Fibroblast Heterogeneity in Keloid and Normal Scar Tissues
- Processed and analyzed {total_cells} fibroblast cells from keloid and normal scar samples.
- Identified {len(subpopulations)} distinct fibroblast subpopulations: {', '.join(subpopulations)}.
- Quantified subpopulation distributions and performed PCA-based mini 3D simulation.
- Generated interactive 3D visualization and static PCA 2D plot for CV and presentation purposes.
"""

with open("CV_Fibroblast_Analysis.txt","w") as f:
    f.write(cv_summary)

print("\nCV-ready summary file created: CV_Fibroblast_Analysis.txt")
print("Mini 3D simulation saved: Mini_3D_Fibroblast_Simulation.html")
print("Static 2D PCA plot saved: PCA_2D_Fibroblast.png")
