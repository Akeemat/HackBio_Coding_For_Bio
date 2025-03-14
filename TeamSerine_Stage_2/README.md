**Overview**

In this stage, as a group of 6, we worked on four datasets with the aim of carrying out statistical analysis and visualization. The teammates brought in mixed skill sets in R and Python.

**Contributors**

Akeemat Ayinla

Emmanuel Uwidia

Olayinka Adesina

Oluwafisayo Abisoye

Samuel Badekale

Valerie Martins

**Dataset 2.1 (Microbiology)**

This [dataset](https://raw.githubusercontent.com/HackBio-Internship/2025_project_collection/refs/heads/main/Python/Dataset/mcgc.tsv) contained OD600 and time values of three strains and their biological and technical replicates. Each strain had three technical replicates, each for wild-type or knockin strain (-) and mutant or knockout strain (+). See description [here](https://github.com/HackBio-Internship/2025_project_collection/blob/main/Python/Dataset/mcgc_METADATA.txt)

First, we plotted growth curves (OD600 vs Time) for all different strains with the knock-out and knock-in strains overlaid on top of each other. The values used were the mean values of the knock-out and knock-in strains. Next, we determined the time to reach the carrying capacity for each strain/mutant using a previously defined function. After this, scatter plots and box plots were generated to visualize the time it takes to reach carrying capacity for the knockout and the knock in strains.

**Dataset 2.6 (Transcriptomics)**

This is a processed RNAseq dataset involving reading in quantitated gene expression data from an RNA-seq experiment. The [dataset](https://gist.githubusercontent.com/stephenturner/806e31fce55a8b7175af/raw/1a507c4c3f9f1baaa3a69187223ff3d3050628d4/results.txt) contains an experiment between a diseased cell line and diseased cell lines treated with compound X. Here, we generated a volcano plot. We then determined the upregulated genes (genes with Log2FC > 1 and pvalue < 0.01) and downregulated genes (genes with Log2FC < -1 and pvalue < 0.01). Using [genecards](https://www.genecards.org/), the functions of the top 5 upregulated genes and top 5 downregulated genes were documented.

**Dataset 2.7 (Public Health)**

This NHANES [dataset](https://raw.githubusercontent.com/HackBio-Internship/public_datasets/main/R/nhanes.csv) combines survey questions and physical examinations, including medical and physiological measurements and laboratory tests, and examines a representative sample of about 5,000 people each year. The data is used to determine the prevalence of diseases and risk factors, establish national standards, and support epidemiology studies and health sciences research. This information helps to develop public health policy, design health programs and services, and expand the nation's health knowledge. The data dictionary can be found [here](https://github.com/HackBio-Internship/public_datasets/blob/main/R/nhanes_dd.csv)

First, we visualized the distribution of BMI, Weight, Weight in pounds (weight \*2.2) and Age with a histogram. Then, we determined (i) the mean 60-second pulse rate for all participants in the data, (2) the range of values for diastolic blood pressure in all participants, and (3) the variance and standard deviation for income among all participants.

Next, we visualized the relationship between weight and height across variables such as gender, diabetes and smoking status.

Lastly, we conducted t-tests between the following variables and made conclusions on the relationships between them based on P-Value

<!--[if !supportLists]-->·         <!--[endif]-->Age and Gender

<!--[if !supportLists]-->·         <!--[endif]-->BMI and Diabetes

<!--[if !supportLists]-->·         <!--[endif]-->Alcohol Year and Relationship Status

 
