from typing import Dict, Union

from pandas import Series, DataFrame


from hate_speech_detector.utils.models.sklearn import (
    tune_hyperparameters_optuna,
)
from hate_speech_detector.utils.logging_voting import launch_objective

if "transformer" not in globals():
    from mage_ai.data_preparation.decorators import transformer


@transformer
def hyperparameter_tuning(
    training_set: Dict[str, Union[DataFrame, Series]],
    *args,
    **kwargs,
):

    X, y, X_train, y_train, X_test, y_test = training_set["build2"]

    objective = launch_objective(X_train, y_train, X_test, y_test)
    best_model = tune_hyperparameters_optuna(objective)

    return X, y, best_model
