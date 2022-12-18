
# About the Project

This project has been made as part of the coursework required for CS 250 Data Structures and Alogrithms. The group members include: 


* Taha Mukhtar

* Shalina Riaz

* Muhammad Hassan Bin Adeel

## Project Goals 

The main goal of this project is to develop a scalable and good performance search engine. The main challenges are algorithmic; in compactly representing a large data-set while supporting fast searches on it. 


The Project has been extended over various parts as below:
*  **Task 1**
    
    To summarize the paper "*The Anatomy of a Large-Scale Hypertextual Web Search Engine.* "
*  **Task 2**

    To submit a project proposal concerning the group members, dataset, languages and frameworks to be used.
*  **Task 3**

    To submit the code for generation of *Forward and Inverted Index* on a part of dataset.
*  **Complete Submission**

    To submit the complete code of project along with the documentation.

* **Presentation**

    To present the project in class for explanation and feedback from Instructor and students.



## Table of Contents
* [DataSet](#Dataset)
* [Implementation](#Implementation)
* [Authors](#Authors)
* [FeedBack](#FeedBack)
## Dataset
As described in our project proposal we are using around 150,000 articles from the dataset in HAVARD DATAVERSE named "NELA-GT-2021". It is a Large Multi-Labelled News Dataset for the Study of Misinformation in News Articles".
## Implementation

* **Parsing**

    The json files in dataset are read and tokenized. And then stopwords (i.e, words like 'a','and','the','but' etc) are removed using following libraries.
    * json
    * nltk.tokenize
    * nltk.corpus
    
    Now, we have a list of words from the documents. But for efficient search stemming is applied. As recognizing, searching and retrieving more forms of words for  more results. When a form of a word is recognized, it's possible to return search results that otherwise might have been missed. That additional information retrieved so stemming is integral to search queries and information retrieval. 

    Finally, a list of keywords is formed for searching the articles.
* **Forward Indexing**

* **Inverted Indexing**
## Authors

- [Shalina Riaz](https://github.com/shalinaariaaz)
- [Taha Mukhtar](https://github.com/tahamukhtar20)
- [Muhammad Hassan Bin Adeel](https://github.com/mhba18094)

## FeedBack
In case of any queries or feedback, please reach out to us at: sriaz.bscs21seecs@seecs.edu.pk