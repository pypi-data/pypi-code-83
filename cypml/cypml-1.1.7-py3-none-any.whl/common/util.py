import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import normalize
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

import matplotlib.pyplot as plt

from . import globals

if (globals.test_env == 'pkg'):
  SparkT = globals.SparkT
  SparkF = globals.SparkF

# crop name and id mappings
def cropNameToID(crop_id_dict, crop):
  """
  Return id of given crop. Relies on crop_id_dict.
  Return 0 if crop name is not in the dictionary.
  """
  crop_lcase = crop.lower()
  try:
    crop_id = crop_id_dict[crop_lcase]
  except KeyError as e:
    crop_id = 0

  return crop_id

def cropIDToName(crop_name_dict, crop_id):
  """
  Return crop name for given crop ID. Relies on crop_name_dict.
  Return 'NA' if crop id is not found in the dictionary.
  """
  try:
    crop_name = crop_name_dict[crop_id]
  except KeyError as e:
    crop_name = 'NA'

  return crop_name

def getYear(date_str):
  """Extract year from date in yyyyMMdd or dd/MM/yyyy format."""
  return SparkF.when(SparkF.length(date_str) == 8,
                     SparkF.year(SparkF.to_date(date_str, 'yyyyMMdd')))\
                     .otherwise(SparkF.year(SparkF.to_date(date_str, 'dd/MM/yyyy')))

def getMonth(date_str):
  """Extract month from date in yyyyMMdd or dd/MM/yyyy format."""
  return SparkF.when(SparkF.length(date_str) == 8,
                     SparkF.month(SparkF.to_date(date_str, 'yyyyMMdd')))\
                     .otherwise(SparkF.month(SparkF.to_date(date_str, 'dd/MM/yyyy')))

def getDay(date_str):
  """Extract day from date in yyyyMMdd or dd/MM/yyyy format."""
  return SparkF.when(SparkF.length(date_str) == 8,
                     SparkF.dayofmonth(SparkF.to_date(date_str, 'yyyyMMdd')))\
                     .otherwise(SparkF.dayofmonth(SparkF.to_date(date_str, 'dd/MM/yyyy')))

# 1-10: Dekad 1
# 11-20: Dekad 2
# > 20 : Dekad 3
def getDekad(date_str):
  """Extract dekad from date in YYYYMMDD format."""
  month = getMonth(date_str)
  day = getDay(date_str)
  return SparkF.when(day < 30, (month - 1)* 3 +
                     SparkF.ceil(day/10)).otherwise((month - 1) * 3 + 3)

# Machine Learning Utility Functions

# This definition is from the suggested answer to:
# https://stats.stackexchange.com/questions/58391/mean-absolute-percentage-error-mape-in-scikit-learn/294069#294069
def mean_absolute_percentage_error(Y_true, Y_pred):
  """Mean Absolute Percentage Error"""
  Y_true, Y_pred = np.array(Y_true), np.array(Y_pred)
  return np.mean(np.abs((Y_true - Y_pred) / Y_true)) * 100

def printInGroups(items, indices, item_values=None, log_fh=None):
  """Print elements at given indices in groups of 5"""
  num_items = len(indices)
  groups = int(num_items/5) + 1

  items_str = '\n'
  for g in range(groups):
    group_start = g * 5
    group_end = (g + 1) * 5
    if (group_end > num_items):
      group_end = num_items

    group_indices = indices[group_start:group_end]
    for idx in group_indices:
      items_str += str(idx+1) + ': ' + items[idx]
      if (item_values):
        items_str += '=' + item_values[idx]

      if (idx != group_indices[-1]):
          items_str += ', '

    items_str += '\n'

  print(items_str)
  if (log_fh is not None):
    log_fh.write(items_str)

def clusterRegionsUsingYield(pd_yield_df, num_clusters=2, debug_level=0):
  """Cluster regions based on historical yield data"""
  row_idx = 0
  yield_summary = {}
  regions = pd_yield_df['IDREGION'].unique()
  all_years = pd_yield_df['FYEAR'].unique()
  for reg in regions:
    pd_reg_df = pd_yield_df[pd_yield_df['IDREGION'] == reg].sort_values(by=['IDREGION', 'FYEAR'])
    yield_years = pd_reg_df[['FYEAR', 'YIELD']].values
    avg_yield = np.mean(yield_years[:, 1])
    reg_row = np.array([avg_yield for yr in all_years])
    yield_year_idxs = yield_years[:, 0] - all_years[0]
    reg_row[yield_year_idxs.astype('int')] = yield_years[:, 1]
    yield_summary['row' + str(row_idx)] = [reg] + list(reg_row)
    row_idx += 1

  yield_sum_cols = ['IDREGION'] + [str(yr) for yr in all_years]
  pd_yield_clu_df = pd.DataFrame.from_dict(yield_summary, orient='index',
                                           columns=yield_sum_cols)
  pd_yield_clu_df = pd_yield_clu_df.dropna()
  if (debug_level > 1):
    print('\n Tranformed yield data')
    print(pd_yield_clu_df.head(5))

  yield_cols = [str(yr) for yr in pd_yield_df['FYEAR'].unique()]
  X_yield = pd_yield_clu_df[yield_cols]

  # There is linear connection between cosine distance and Euclidean distance for normalized vectors.
  # https://stats.stackexchange.com/questions/299013/cosine-distance-as-similarity-measure-in-kmeans
  yield_normalized = normalize(X_yield)
  yield_norm_kmeans = KMeans(n_clusters=num_clusters)
  yield_norm_kmeans.fit(yield_normalized)
  if (debug_level > 1):
    score_label = 'Cosine kmeans silhouette_score:'
    print('\n', score_label, silhouette_score(yield_normalized,
                                              yield_norm_kmeans.labels_,
                                              metric='cosine'))

  regions_in_clusters = []
  for i in range(num_clusters):
    cluster_i_mask = np.where(yield_norm_kmeans.labels_ == i)
    regions_cluster_i = regions[cluster_i_mask[0]]
    regions_in_clusters.append(regions_cluster_i)

  return regions_in_clusters

def customFitPredict(args):
  """
  We need this because scikit-learn does not support
  cross_val_predict for time series splits.
  """
  X_train = args['X_train']
  Y_train = args['Y_train']
  X_test = args['X_test']
  est = args['estimator']
  fit_params = args['fit_params']

  est.fit(X_train, Y_train, **fit_params)
  return est.predict(X_test)

def getPredictionScores(Y_true, Y_predicted, metrics):
  """Get values of metrics for given Y_predicted and Y_true"""
  pred_scores = {}

  for met in metrics:
    score_function = metrics[met]
    met_score = score_function(Y_true, Y_predicted)
    # for RMSE, score_function is mean_squared_error, take square root
    # normalize RMSE
    if (met == 'RMSE'):
      met_score = np.round(100*np.sqrt(met_score)/np.mean(Y_true), 2)
      pred_scores['NRMSE'] = met_score
    # normalize mean absolute errors except MAPE which is already a percentage
    elif ((met == 'MAE') or (met == 'MdAE')):
      met_score = np.round(100*met_score/np.mean(Y_true), 2)
      pred_scores['N' + met] = met_score
    # MAPE, R2, ... : no postprocessing
    else:
      met_score = np.round(met_score, 2)
      pred_scores[met] = met_score

  return pred_scores

def getFilename(crop, country, yield_trend,
                early_season, early_season_end, nuts_level=None):
  """Get filename based on input arguments"""
  suffix = crop.replace(' ', '_')
  suffix += '_' + country

  if (nuts_level is not None):
    suffix += '_' + nuts_level

  if (yield_trend):
    suffix += '_trend'
  else:
    suffix += '_notrend'

  if (early_season):
    suffix += '_early' + str(early_season_end)

  return suffix

def getLogFilename(crop, country, yield_trend,
                   early_season, early_season_end):
  """Get filename for experiment log"""
  log_file = getFilename(crop, country, yield_trend,
                         early_season, early_season_end)
  return log_file + '.log'

def getFeatureFilename(crop, country, yield_trend,
                       early_season, early_season_end):
  """Get unique filename for features"""
  feature_file = 'ft_'
  suffix = getFilename(crop, country, yield_trend, early_season, early_season_end)
  feature_file += suffix
  return feature_file

def getPredictionFilename(crop, country, nuts_level, yield_trend,
                          early_season, early_season_end):
  """Get unique filename for predictions"""
  pred_file = 'pred_'
  suffix = getFilename(crop, country, yield_trend,
                       early_season, early_season_end, nuts_level)
  pred_file += suffix
  return pred_file

def plotTrend(years, actual_values, trend_values, trend_label):
  """Plot a linear trend and scatter plot of actual values"""
  plt.scatter(years, actual_values, color="blue", marker="o")
  plt.plot(years, trend_values, '--')
  plt.xticks(np.arange(years[0], years[-1] + 1, step=len(years)/5))
  ax = plt.axes()
  plt.xlabel("YEAR")
  plt.ylabel(trend_label)
  plt.title(trend_label + ' Trend by YEAR')
  plt.show()

def plotTrueVSPredicted(actual, predicted):
  """Plot actual and predicted values"""
  fig, ax = plt.subplots()
  ax.scatter(np.asarray(actual), predicted)
  ax.plot([actual.min(), actual.max()], [actual.min(), actual.max()], 'k--', lw=4)
  ax.set_xlabel('Actual')
  ax.set_ylabel('Predicted')
  plt.show()

# Based on
# https://stackoverflow.com/questions/39409866/correlation-heatmap
def plotCorrelation(df, sel_cols):
  corr = df[sel_cols].corr()
  mask = np.zeros_like(corr, dtype=np.bool)
  mask[np.triu_indices_from(mask)] = True
  f, ax = plt.subplots(figsize=(20, 18))
  cmap = sns.diverging_palette(220, 10, as_cmap=True)
  sns.heatmap(corr, mask=mask, cmap=cmap, vmax=1.0, center=0,
              square=True, linewidths=.5, cbar_kws={"shrink": .5},
              annot=True, fmt='.1g')
