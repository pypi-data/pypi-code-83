def clusters():
    cl = Clusters(self.__pc_df.loc[self.training_ids]) 
    accuracies = [self.__create_models(n_models, data = self.__pc_df.loc[self.training_ids])]
    pbar.update(1)

    for x in range(2, 6):
        clusters = cl.get_cluster_labels(x)
        for i in np.unique(clusters):
            data = self.__pc_df.loc[self.training_ids].iloc[np.where(clusters == i)]
            accuracies.append(self.__create_models(n_models, data))
        pbar.update(1)
    self.__models = self.__models[np.argmax(accuracies)]

    return self.__predict()

def __get_extensive_cluster_df(self) -> pd.DataFrame:
        groups = []
        columns = len(self.__pc_df.columns) * 2
        for group in ["Labels", "Artists", "Companies"]:
            ids = self.__df[group].str.split(";")
            exploded = ids.explode()    
            occurrences = exploded.value_counts()        
            tqdm.pandas(desc = "Finding cluster centers", total = len(exploded.unique()))
            cluster_data = np.concatenate(exploded.to_frame().groupby(group).progress_apply(self.__lookup).values).ravel()
            cluster_data = pd.DataFrame(cluster_data.reshape(int(len(cluster_data) / columns), columns), index = exploded.unique()).fillna(0).apply(pd.to_numeric, downcast="float").round(3)
            cluster_data = cluster_data.multiply(occurrences, axis = 0)

            tqdm.pandas(desc = "Apply cluster centers to releases", total = len(ids.index))
            a = ids.groupby(level=0).progress_apply(lambda x: cluster_data.loc[x.values[0]].sum() / occurrences[x.values[0]].sum()).unstack() # weighted average
            groups.append(a)

        return pd.concat(groups, axis = 1)

   def __lookup(self, x):
        return [self.__pc_df.loc[x.index].mean()]


def calculate_most_similar_group(self, group: str) -> pd.Series:
        groups = {"Release": 0, "Artists": 1, "Labels": 2, "Companies": 3}
        group_size = len(self.__pc_df.columns) / 4
        start = groups[group] * group_size
        end = start + group_size
        mean_group = self.__pc_df.loc[self.__training_ids,start:end].mean()

        group_data = self.__df[group].drop_duplicates().to_frame()
        group_data.columns = ["IDs"]
        group_data["%s Similarity" % group] = 1 / np.array([np.linalg.norm(mean_group - self.__pc_df.loc[i,start:end]) for i in self.__df[group].drop_duplicates().index])
        return group_data.sort_values("%s Similarity" % group, ascending = False)



    def probability_per_release(self, release_id: int) -> pd.Series:
        return self.__predictions.loc[release_id]