# Azure ML and Customer Insights - Custom Models
Azure ML :hearts: Customer Insights

![repots](https://github.com/ekote/azure-architect/blob/master/images/Flame_Remote_Working_transparent_by_Icons8.gif?raw=true)


Bring in your custom machine learning models to Dynamics 365 Customer Insights to make predictions on your unified customer data.

Objective: add custom model created and served by Azure Machine Learning to Customer Insights.

# General steps (Customer Dataset)
1. Create Azure Machine Learning (Azure ML) service
2. Add Dynamics365(multiple services) to Azure ML in a Contributor Role
3. Go to the Azure ML Workspace
4. Create Compute Instance (in that case size doesn't matter :cactus:)
5. During a compute instance creation, follow the next steps
6. Register the model (model.pkl, type: AutoML) and name it `MaxAbsScalerExtremeRandomTrees`
7. Create Azure ML Dataset (Tabular) from the file Customer_1.csv and name it `CustomerDataDataset`
8. Check if your blob name is `workspaceblobstore`. If not - change that value in the notebook.
9. Once compute instance is created, clone the repo via terminal `git clone htt`
10. Run the notebook cells, one by one.
11. Go to Customer Insights > Intelligence > Custom models
12. Create new workflow 
    1. What is `name`? This is a name that will be visible under AzureML experiments, e.g. `CIAMLexp`.
13. Run (refresh) a newly created model
14. Ta dam :tada:! You should see the predictions :blush:

VIDEO - https://youtu.be/SMXjyap-fZM 

# Model training
To be documented
## AutoML
## Notebooks

# FAQ
- What is `output_datastore`?
  - It's the name of the datastore (Storage Account) e.g. `workspaceblobstore`
- What is `output_path`?
  - It's a path to a result file (see file score.py, line 68)
- Shouldn't score.py contain the init() and run() methods? 
  - No. The file just have to return the dataframe with the results (without an index column - see score.py, line 54) 
- How to debug the scirpt?
  - Run `!python scripts/score.py --mode DEBUG --output_datastore workspaceblobstore --output_path CustomerIncomeOutput/CustomerIncomeOutput.csv`
- How to train own model?
- What is my columns have different names?
  - :trollface:

## Resources
- https://docs.microsoft.com/en-us/dynamics365/customer-insights/audience-insights/custom-models
- https://docs.microsoft.com/en-us/azure/machine-learning/how-to-deploy-pipelines
