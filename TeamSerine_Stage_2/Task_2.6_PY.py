#Task 2.6_Py
#import libraries

import pandas as pd
import numpy as np
import seaborn as sns

#read data into pandas dataframe. NB: The separator in this file is a whitespace (indicated with "\s+")
df = pd.read_csv("https://gist.githubusercontent.com/stephenturner/806e31fce55a8b7175af/raw/1a507c4c3f9f1baaa3a69187223ff3d3050628d4/results.txt", sep = r"\s+")

df.head()

#create new column, -nlog10 (where n = padj)
df['nlog10'] = -np.log10(df.padj)

#upregulated and downregulated genes
upregulated_genes = df[(df.log2FoldChange > 1) & (df.pvalue < 0.01) ]
downregulated_genes = df[(df.log2FoldChange < -1) & (df.pvalue < 0.01) ]

#sort upregulated and downregulated genes according to their expression levels
upregulated_genes = upregulated_genes.sort_values(by = 'log2FoldChange', axis = 0, ascending = False)
downregulated_genes = downregulated_genes.sort_values(by = 'log2FoldChange', axis = 0, ascending = True)

ax = sns.scatterplot(data = df, x = 'log2FoldChange', y = 'nlog10') #create volcano plot with seaborn

#create dictionary with up- and downregulated genes and their functions
t5_upregulated_genes  ={"DTHD1": "This gene encodes a protein which contains a death domain. Death domain-containing proteins function in signaling pathways and formation of signaling complexes, as well as the apoptosis pathway. Alternative splicing results in multiple transcript variants", "EMILIN2": "Predicted to enable extracellular matrix constituent conferring elasticity. Involved in several processes, including positive regulation of angiogenesis; positive regulation of defense response to bacterium; and positive regulation of platelet aggregation. Located in extracellular region.", "PI16": "Predicted to enable peptidase inhibitor activity. Predicted to be involved in negative regulation of peptidase activity. Predicted to act upstream of or within negative regulation of cell growth involved in cardiac muscle cell development. Predicted to be located in extracellular region. Predicted to be active in extracellular space.", "C4orf45": "SPMIP2 (formerly C4orf45) (Sperm Microtubule Inner Protein 2) is a Protein Coding gene. Diseases associated with SPMIP2 include Hyperekplexia.", "FAM180B": "FAM180B (Family With Sequence Similarity 180 Member B) is a Protein Coding gene. Diseases associated with FAM180B include Borderline Leprosy and Mosaic Variegated Aneuploidy Syndrome."}

t5_downregulated_genes = {"TBX5": "TBX5 (T-Box Transcription Factor 5) is a Protein Coding gene. It codes for a DNA-binding protein that regulates the transcription of several genes and is involved in heart development and limb pattern formation", 'IFITM1': "IFITM1 (Interferon Induced Transmembrane Protein 1) is a Protein Coding gene. Diseases associated with IFITM1 include Influenza and West Nile Virus. Among its related pathways are Cytokine Signaling in Immune system and Antiviral mechanism by IFN-stimulated genes. Gene Ontology (GO) annotations related to this gene include obsolete signal transducer activity, downstream of receptor.", "TNN": "Predicted to enable integrin binding activity. Involved in positive regulation of sprouting angiogenesis; regulation of cell adhesion; and regulation of cell migration. Part of tenascin complex.", "COL13A1": "This gene encodes the alpha chain of one of the nonfibrillar collagens. The function of this gene product is not known, however, it has been detected at low levels in all connective tissue-producing cells so it may serve a general function in connective tissues.", "IFITM3": "Codes for the IFN-induced antiviral protein which disrupts intracellular cholesterol homeostasis. Inhibits the entry of viruses to the host cell cytoplasm by preventing viral fusion with cholesterol depleted endosomes. May inactivate new enveloped viruses which buds out of the infected cell, by letting them go out with a cholesterol depleted membrane." }

#print out the top 5 upregulated genes
print("TOP 5 UNREGULATED GENES AND THEIR FUNCTIONS\n--------------------------------")
for i in range(5):
    for key, value in t5_upregulated_genes.items():
        gene = key
        function = value
    print(f"Gene{i+1}. Name: {gene} \nFunction{function}\n")

#print out the top 5 downregulated genes
print("TOP 5 DOWNREGULATED GENES AND THEIR FUNCTIONS\n--------------------------------")
for i in range(5):
    for key, value in t5_downregulated_genes.items():
        gene = key
        function = value
    print(f"Gene{i+1}. Name: {gene} \nFunction{function}\n")
