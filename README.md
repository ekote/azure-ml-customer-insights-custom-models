# Azure ML Customer Insights Custom Models
Bring in your custom machine learning models to Dynamics 365 Customer Insights to make predictions on your unified customer data.

Context: Customer Insights ...

Objective: add custom model created and served by Azure Machine Learning to Customer Insights.

# General steps
1. Create Azure Machine Learning (Azure ML) service
2. Add Customer Insights to Azure ML in a Contrubutor Role
4. Go to the Azure ML Workspace
5. Create Compute Instance (in that case size doesn't matter :cactus:)
6. Clone the repo via terminal
7. Register the model.pkl (type: AutoML) and name it `MaxAbsScalerExtremeRandomTrees`
8. Create Azure ML Dataset (Tabular) from the file Customer_1.csv
9. Run the notebook


## Resources
- https://docs.microsoft.com/en-us/dynamics365/customer-insights/audience-insights/custom-models
