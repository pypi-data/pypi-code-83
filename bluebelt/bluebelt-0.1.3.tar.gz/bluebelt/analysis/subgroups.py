import pandas as pd

def get_subgroups(series, subgroups=None, subgroup_size=None):
    if subgroups:
        pass
    elif subgroup_size:

        if series.size % subgroup_size > 0:
            subgroup_series = series.append(pd.Series((subgroup_size - series.size % subgroup_size) * [np.NaN]), ignore_index=True)

        return pd.DataFrame(subgroup_series.values.reshape(int(subgroup_series.size/subgroup_size), subgroup_size))