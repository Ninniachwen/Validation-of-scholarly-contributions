# Validation of Scholarly Contributions

In this Project, we propose a machine-actionable format for scholarly contributions. Also, a method for validating scholarly contributions based on the parsed semantics is designed.

## Data and Class Structure of Ontology

```
class hirarchy

"owl:Thing"
├── "experimental_results"          # containing instances of quality properies
│   ├── new_property_1
│   ├── new_property_2
├── "model"
    ├── new_model_class             # new model or approach by the authors
    ├── "baseline_model"            # baseline model or approach, current state-of-the-art

"owl:topObjectProperty"         
├──experiment_op                    # op = object property
    ├── interpreteble               # Qualitative results like "linear Runtime"

"owl:topDataProperty"   
├── "experiment_larger_than"        # results like scores, when higher is better
│   ├── BLEU_score
├── "experiment_smaller_than"       # results like time, when lower is better
    ├── runtime
```

the classes in quotation marks need to be named exactly this, all other classes can be named according to the papers descriptions.

## data extraction

 1. download the [trial-data](https://github.com/ncg-task/trial-data)
 2. execute the data_extraction.py file in the directory in which "trial-data" is loacted

## references and sources

The papers used in this project were sampled from D'Souzas' [trial-data](https://github.com/ncg-task/trial-data)  

The Ontology Tool Protégé by Stanford University can be found [here](https://protege.stanford.edu/). I used Version 5.5 locally, which can be downloaded in the Protégé [Wiki](https://protegewiki.stanford.edu/wiki/Protege_Desktop_Old_Versions)