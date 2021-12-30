import argparse
import logging
import os
import tempfile

import joblib
import pandas as pd
from azureml.automl.core.shared import logging_utilities, log_server
from azureml.core import Dataset, Datastore, Run
from azureml.core.model import Model
from azureml.telemetry import INSTRUMENTATION_KEY

try:
    log_server.enable_telemetry(INSTRUMENTATION_KEY)
    log_server.set_verbosity('INFO')
    logger = logging.getLogger('azureml.automl.core.scoring_script')
except:
    pass

def init():
    global output_path
    global output_datastore
    global model
    global run_ctx
    global ws
    global df_to_predict
    global df
    global datastore

    parser = argparse.ArgumentParser("score")

    parser.add_argument("--input_data", type=str, help="input data")
    parser.add_argument('--output_path', dest='output_path', required=True)
    parser.add_argument('--output_datastore', dest='output_datastore', required=True)

    args = parser.parse_args()

    output_path = args.output_path
    output_datastore = args.output_datastore

    logger.info("Output Location", args.output_datastore + args.output_path)

    run_ctx = Run.get_context()
    ws = run_ctx.experiment.workspace
    model_name = 'AutoMLbb88e09f11'
    
    run_ctx.log("OutputDatastore", args.output_datastore)
    run_ctx.log("OutputPath", args.output_path)
    run_ctx.log("Model", model_name)

    logger.info("geting datasets ...")
    # dataset = Dataset.get_by_name(ws, name='customer_tabular')
    dataset = run_ctx.input_datasets['CustomerInference_dataset']
    logger.info('dataset ', dataset)
    df = dataset.to_pandas_dataframe()
    df_to_predict = df.loc[:, df.columns != 'Income']

    log_server.update_custom_dimensions({'model_name': model_name, 'model_version': 1})
    model_path = Model.get_model_path(model_name, _workspace=ws, version=1)

    datastore = Datastore.get(ws, output_datastore)

    try:
        logger.info("Loading model from path.")
        model = joblib.load(model_path)
        logger.info("Loading successful.")
    except Exception as e:
        logging_utilities.log_traceback(e, logger)
        raise


def run():
    df_result = pd.Series(model.predict(df_to_predict), name="income_prediction")
    df_result_renamed = pd.Series(df['CustomerId'], name="customer_id")
    df_final_res = pd.concat([df_result_renamed, df_result], axis=1)
    df_final_res.set_index("customer_id")

    directory_name = os.path.dirname(output_path)
    logger.info("Extracting Directory {} from path {}".format(directory_name, output_path))

    output_folder = tempfile.TemporaryDirectory(dir="/tmp")
    filename = os.path.join(output_folder.name, os.path.basename(output_path))

    run_ctx.log("Filename", filename)

    df_final_res.to_csv(filename)

    output_dataset = Dataset.File.upload_directory(src_dir=output_folder.name, target=(datastore, directory_name))

    print(output_dataset)

    return df_final_res
