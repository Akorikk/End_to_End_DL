# End_to_End_DL

## Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py


## Data Ingestion

* IMPORTANT  when we do data ingestion task we should not keep our params.yaml file empty because whenever you will executing it will throw error, for that just take one key dummy value example i have taken key: val

Data Ingestion is the process of collecting and importing data from various sources into a system where it can be stored, processed, and analyzed.

It's like gathering raw ingredients before cooking. You're pulling data from different places so your data science models or analysis can use it.

🧩 Sources of Data:
Databases (SQL, NoSQL)

APIs (Twitter API, weather APIs)

Files (CSV, Excel, JSON, XML)

Cloud storage (AWS S3, Google Cloud Storage)

Web scraping

IoT devices or sensors




## Params.yaml

In data science projects, especially when you're following MLOps or a clean project structure, params.yaml is used to store and manage hyperparameters and configuration settings in a neat, organized, and version-controllable wa
It's just a YAML file (human-readable) used to define parameters like:

model hyperparameters (e.g., learning rate, max_depth)
preprocessing options
file paths
any values you want to keep configurable and not hardcoded in your scripts

Benefit	Explanation
✅ Reusability	You can easily reuse and change parameters across scripts
✅ Clean Code	Avoid hardcoding parameters in your Python files
✅ Version Control	Easily track changes to your experiments
✅ MLOps Friendly	Tools like DVC, Hydra, and MLflow integrate well with it