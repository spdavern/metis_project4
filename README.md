## Unsupervised Learning and Natural Language Processing (NLP)

Author: Sean Davern

Description: This project aims at analyzing the ways TED talk authors use the word love and its variants using unsupervised learning and NLP for interesting insights.

## Project Documentation

Documentation for this project is represented by Jupyter Notebook (.ipynb files) comments, the slide presentation in `./reports/slide_deck.pptx (and .pdf)` and in the summary report in `./reports/summary.pages (and .pdf)`.  Finally, see brief explanations of what project work each file is associated with below.

## Data

Data used for this project came from [Rounak Banik's TED Talks dataset on Kaggle](https://www.kaggle.com/rounakbanik/ted-talks).

## Project Organization 
------------

(generated with [datasciencemvp](https://github.com/cliffclive/datasciencemvp/))

(modified from [cookiecutter-datascience](https://drivendata.github.io/cookiecutter-data-science/))

```
.
├── AWS_setup
│   ├── README.md       Notes on setting up, connecting to, and managing the AWS instance
│   └── environment.yml Capture of the 'metis' environment on my mac
├── LICENSE
├── README.md  This file
├── assignment.md  Content provided by Metis describing the assignment
├── data
│   ├── processed
│   │   └── love_snippets  The pickled dataframe as analyzed in all models
│   └── raw
│       ├── ted-talks  The unzipped data files
│       │   ├── ted_main.csv
│       │   └── transcripts.csv  The file primarily analyzed in this project
│       └── ted-talks.zip  The data as downloaded from Kaggle
├── fix_run_together_sents.ipynb  Final data cleaning:notebook that writes love_snippets
├── love_not_glove.ipynb  Notebook used to work out code to select love words
├── main.py  Not used
├── models
│   ├── cv-lsa.ipynb  Topic modeling using CountVectorizer and LSA
│   ├── cv_binary-lsa.ipynb  Topic modeling using CountVectorizer(Binary=True) and LSA
│   ├── mvp.ipynb  Minimum Viable Product
│   └── tfidf-lsa.ipynb Topic modeling using tf-idf and LSA
├── normalize_vs_unit_norm.ipynb  Comparison of my unit_norm function and normalize
├── proposal.md  My project proposal in markdown format
├── proposal.pdf My project proposal in pdf format
├── proposal_EDA.ipynb  Some early exploratory data analysis I did for the proposal
├── reports
│   ├── figures  Figures created in modeling notebooks
│   │   ├── CV_binary-lsa_2topic.svg
│   │   ├── LoveMentionsInTEDTalks.svg
│   │   ├── TEDTalkLengthDensityPlot.svg
│   │   ├── cv_binary-lsa_4topic.svg
│   │   ├── cv_binary-lsa_animation.mp4
│   │   ├── cv_binary_lsa_4Elbow.svg
│   │   └── tfidf_binary-lsa_animation.mp4
│   ├── slide_deck.pdf  My presentation in pdf format
│   ├── slide_deck.pptx My presentation in PowerPoint format
│   ├── summary.pages  My summary report in Apple Pages format
│   ├── summary.pdf    My summary report in pdf format
│   └── templates  The PowerPoint template used for the presentation
│       └── 10216-love-and-hearts-ppt-template-0003.pptx
├── scikit-learn_examples  Code from each tool's documentation used to understand them
│   ├── KElbowVisualizer_example.ipynb
│   └── scikit-learn_KMeans_example
│       ├── README.md
│       └── plot_document_clustering.ipynb
└── src  The module I created to support this project
    ├── __init__.py
    └── functions.py  Functions I created to do transcript pre-processing and analysis

13 directories, 40 files

```

