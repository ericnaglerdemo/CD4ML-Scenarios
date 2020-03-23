import numpy as np
from cd4ml import pipeline_helpers as ph


def main(*args):
    """
    Run the pipeline
    """
    args = args[0]
    if len(args) > 0:
        variable = args[0]
    else:
        variable = None

    np.random.seed(462748)

    print('variable: %s' % variable)
    ph.download_data()
    ph.split_data()
    ph.train_model()