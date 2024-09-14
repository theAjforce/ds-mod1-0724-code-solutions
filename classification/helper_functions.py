from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import roc_auc_score, roc_curve
from xgboost import XGBClassifier

def grid_train_random_forest(X, y, params, n_folds, eval_metric):
    rfc = RandomForestClassifier()
    grid = GridSearchCV(rfc, params, cv=n_folds, scoring=eval_metric)
    grid.fit(X,y)
    return grid.best_estimator_

    """
    Train Random Forest binary classifier using a grid of hyperparameters. Return
    the best model according to the specified metric.

    Args:
        X: Array-like of shape (n_samples,n_features) - Test feature data.
        y: Array-like of shape (n_samples,) - Test target data.
        params: Dictionary - Parameter grid on which to perform cross validation.
        n_folds: int - Number of folds to use for cross validation.
        eval_metric: str - Metric to use for evaluating model performance in cross validation.

    Returns:
        model: Best Random Forest model according to evaluation metric.

    Examples:
        model = grid_train_random_forest(X, y, params, 4, "accuracy")
    """

def calc_roc_metrics(X, y, model):
    proba = model.predict_proba(X)
    fpr, tpr, thresholds = roc_curve(y, proba[:,1], pos_label='Yes')
    auc = roc_auc_score(y, proba[:,1])
    return fpr, tpr, auc
    
    
    
    """
    Calculate False Positive Rate (FPR), True Positive Rate (TPR), and Area Under ROC Curve (AUC)
    for a given binary classification model and test data.

    Args:
        X: Array-like of shape (n_samples,n_features) - Test feature data.
        y: Array-like of shape (n_samples,) - Test target data.
        model: Scikit-learn style binary classification model.

    Returns:
        fpr: float - False Positive Rate.
        tpr: float - True Positive Rate.
        auc: float - Area Under ROC Curve.

    Examples:
        fpr, tpr, auc = calc_roc_metrics(X, y, model)
    """

def train_xgboost(X_train, y_train, X_test, y_test, params, n_round):
    max_depth = params['max_depth']
    eta = params['eta']
    objective = params['objective']
    n_jobs = params['nthread']
    eval_metric = params['eval_metric']
    y_train = y_train.apply(lambda x: 1 if x=='Yes' else 0)
    y_test = y_test.apply(lambda x: 1 if x=='Yes' else 0)

    xgb = XGBClassifier(max_depth = max_depth,eta = eta,objective = objective,n_jobs = n_jobs,eval_metric = eval_metric,n_estimators = n_round)
    trained_model = xgb.fit(X_train, y_train, eval_set=[(X_test, y_test)])
    return trained_model
    

    """
    Train an XGBoost model with the given parameters and train/test data.

    Args:
        X_train: Array-like of shape (n_train_samples,n_features) - Train feature data.
        y_train: Array-like of shape (n_train_samples,) - Train target data.
        X_test: Array-like of shape (n_test_samples,n_features) - Test feature data.
        y_test: Array-like of shape (n_test_samples,) - Test target data.
        params: Dictionary - Parameters to pass into XGBoost trainer.
        n_round: int - Number of rounds of training.

    Returns:
        model: Trained XGBoost model.

    Examples:
        model = calc_roc_metrics(X_train, y_train, X_test, y_test, params)
    """
