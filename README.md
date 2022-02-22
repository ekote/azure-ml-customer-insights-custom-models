# Azure ML Customer Insights Custom Models
Bring in your custom machine learning models to Dynamics 365 Customer Insights to make predictions on your unified customer data.

Context: Customer Insights ...

Objective: add custom model created and served by Azure Machine Learning to Customer Insights.

# General steps
1. Create Azure Machine Learning (Azure ML) service
2. Add Customer Insights to Azure ML in a Contrubutor Role
3. Go to the Azure ML Workspace
4. Create Compute Instance (in that case size doesn't matter :cactus:)
5. Clone the repo via terminal
6. Register the model.pkl (type: AutoML) and name it `MaxAbsScalerExtremeRandomTrees`
7. Create Azure ML Dataset (Tabular) from the file Customer_1.csv and name it `CustomerDataDataset`
8. Check if your blob name is `workspaceblobstore`. If not - change that value in the notebook.
9. Run the notebook cells one by one.


# Model training
To be documented

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


## Resources
- https://docs.microsoft.com/en-us/dynamics365/customer-insights/audience-insights/custom-models
