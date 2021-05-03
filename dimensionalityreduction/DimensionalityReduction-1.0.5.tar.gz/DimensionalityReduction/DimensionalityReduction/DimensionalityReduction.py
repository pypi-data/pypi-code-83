#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency

class DimensionalityReduction:
    def __init__(self):
        self.discard = {}
        self.impute = {}
        self.no_impute = {}
    
    def recognize(self, df, target, cat):
        # to let DimensionalityReduction knows what is the dataframe and what is the target 
        self.df = df
        self.target = target
        self.cat = cat
        
    def missingpct(self, plot=False): 
        desc = self.df.describe().T
        desc['missing%'] = 1 - (desc['count']/len(self.df))

        discard_missingpct=[]
        no_impute_missingpct=[]
        impute_missingpct=[]
        for i,j in zip(desc['missing%'].sort_values(ascending=False).index,desc['missing%'].sort_values(ascending=False)):
            if j > 0:
                print(i,str(': '),round(j,3))
            if j >= 0.95:
                discard_missingpct.append(i)
            if j < 0.95 and j > 0.5:
                no_impute_missingpct.append(i)
            if j <= 0.5:
                impute_missingpct.append(i)
                
        if plot==True and desc['missing%'].sum() > 0:
            plt.bar(x=desc.index, height='missing%')
            plt.xticks(rotation=90)
            plt.show()
        else:
            print('No features has missing values.')
        
        self.discard['missingpct'] = discard_missingpct
        self.impute['missingpct'] = impute_missingpct
        self.no_impute['missingpct'] = no_impute_missingpct

    def std(self, threshold=0.85, plot=False):
        def std_filter(df, threshold=threshold, plot=False):    
            df2 = df.drop(self.target, axis=1)
            Standard_Deviation = df2.std(ddof=0)
            std_min=Standard_Deviation.min()
            std_max=Standard_Deviation.max()
            std_scaled=(Standard_Deviation-std_min)/(std_max-std_min)
            
            if plot==True:
                std_res = pd.Series(std_scaled, index=self.df.columns, name='Standard Deviation').sort_values(ascending=False)
                plt.bar(std_res.index, std_res)
                plt.ylabel('Standard Deviation')
                plt.xticks(rotation=90)
                plt.axhline(y=threshold, color='red', linestyle='--')
                plt.show()

            return std_scaled.index[std_scaled < threshold].tolist()
        
        if plot == True:
            std_filter(self.df, plot=True)
            
        elif plot == False:
            std_filter(self.df, plot=False)
            
        MISSING_VALUE_INDICATORS=np.flip(np.arange(0.00001,1,0.1))
        no_features=[]
        for i in MISSING_VALUE_INDICATORS:
            discard_std = std_filter(self.df, threshold=i)
            no_features.append(len(self.df.columns) - len(discard_std))
        
        if plot==True:
            pd.Series(MISSING_VALUE_INDICATORS, index=no_features).plot()
            plt.xlabel('Number of Features Dropped')
            plt.ylabel('Missing Value Indicators')
            plt.show()
        
        self.discard['std'] = std_filter(self.df)
        
    def pearsons_r(self, show=True, plot=True):
        feat_corr = self.df.corr().stack().reset_index(name="correlation")
        feat_corr['abs_correlation']=abs(feat_corr['correlation'])
        feat_corr2=feat_corr[feat_corr.level_0 != feat_corr.level_1].sort_values(by='abs_correlation',ascending=False).iloc[:-2:2]
        discard1=[]
        discard2=[]
        
        if show==True:
            for i,j,k in zip(feat_corr2['level_0'],feat_corr2['level_1'],feat_corr2['abs_correlation']):
                if i!=j:
                    if k >= 0.3 and k <= 0.7:
                        print(i,str('-'),j,str(':'),round(k,3),str('(moderate)'))
                    if k > 0.7:
                        print(i,str('-'),j,str(':'),round(k,3),str('(strong)'))     
                    if k < 0.3 and k !=0:
                        print(i,str('-'),j,str(':'),round(k,3),str('(weak)'))
                    if k ==0:
                        print(i,str('-'),j,str(':'),round(k,3),str('(no relationship)')) 
                    if k >= 0.85:
                        discard1.append(i)
                        discard2.append(j) 
        
        if plot==True:
            sns.set_theme(style="whitegrid")

            # Compute a correlation matrix and convert to long-form
            corr_mat = self.df.corr().stack().reset_index(name="correlation")

            # Draw each cell as a scatter point with varying size and color
            g = sns.relplot(
                data=corr_mat,
                x="level_0", y="level_1", hue="correlation", size="correlation",
                palette="vlag", hue_norm=(-1, 1), edgecolor=".7",
                height=10, sizes=(70, 270), size_norm=(-.2, .8),
            )

            # Tweak the figure to finalize
            g.set(xlabel="", ylabel="", aspect="equal")
            g.despine(left=True, bottom=True)
            g.ax.margins(.02)
            for label in g.ax.get_xticklabels():
                label.set_rotation(90)
            for artist in g.legend.legendHandles:
                artist.set_edgecolor(".7")
                
            plt.show()
            
        discard_Pearsons_R=[]
        for i,j in zip(discard1,discard2):
            if abs(self.df.corr()[[self.target]]).loc[i].values[0] > abs(self.df.corr()[[self.target]]).loc[j].values[0]:
                discard_Pearsons_R.append(j)
            if abs(self.df.corr()[[self.target]]).loc[j].values[0] > abs(self.df.corr()[[self.target]]).loc[i].values[0]:
                discard_Pearsons_R.append(i)

        res = [] 
        for i in discard_Pearsons_R: 
            if i not in res: 
                res.append(i)      
        
        self.discard['pearson_r'] = res
        
    def Cramers_V(self, show=True, plot=True):
        #Corrected Cramers'V function
        def cramers_corrected_stat(contingency_table):
            chi2 = chi2_contingency(contingency_table)[0]
            n = contingency_table.sum().sum()
            phi2 = chi2/n

            r, k = contingency_table.shape
            r_corrected = r - (((r-1)**2)/(n-1))
            k_corrected = k - (((k-1)**2)/(n-1))
            phi2_corrected = max(0, phi2 - ((k-1)*(r-1))/(n-1))

            return (phi2_corrected / min( (k_corrected-1), (r_corrected-1)))**0.5
        
        def categorical_corr_matrix(df):
            if type(df) == pd.Series:
                df = df.to_frame()
                
            cols = df.columns
            n = len(cols)
            corr_matrix = pd.DataFrame(np.zeros(shape=(n, n)), index=cols, columns=cols)

            for col1 in cols:
                for col2 in cols:
                    if col1 == col2:
                        corr_matrix.loc[col1, col2] = 1
                        break
                df_crosstab = pd.crosstab(df[col1], df[col2], dropna=True)
                corr_matrix.loc[col1, col2] = cramers_corrected_stat(df_crosstab)

            # Flip and add to get full correlation matrix
            corr_matrix += np.tril(corr_matrix, k=-1).T
            return corr_matrix
        
        if plot==True:
            fig, ax = plt.subplots(figsize=(10,10))         # Sample figsize in inches
            sns.heatmap((categorical_corr_matrix(self.df[self.cat])), annot=False, cmap='coolwarm', square=True);
            plt.show()
        
        cramersV = categorical_corr_matrix(self.df)
        cmatrix=cramersV.sort_values(by=self.target,ascending=False)

        feat_corr = cmatrix.stack().reset_index(name="correlation")
        feat_corr['abs_correlation']=abs(feat_corr['correlation'])
        feat_corr2=feat_corr[feat_corr.level_0 != feat_corr.level_1].sort_values(by='abs_correlation',ascending=False).iloc[:-2:2]

        discard1=[]
        discard2=[]
        
        if show==True:
            for i,j,k in zip(feat_corr2['level_0'],feat_corr2['level_1'],feat_corr2['abs_correlation']):
                if i!=j:
                    if k >= 0.3 and k <= 0.7:
                        print(i,str('-'),j,str(':'),round(k,3),str('(moderate)'))
                    if k > 0.7:
                        print(i,str('-'),j,str(':'),round(k,3),str('(strong)'))     
                    if k < 0.3 and k !=0:
                        print(i,str('-'),j,str(':'),round(k,3),str('(weak)'))
                    if k ==0:
                        print(i,str('-'),j,str(':'),round(k,3),str('(no relationship)')) 
                    if k >= 0.85:
                        discard1.append(i)
                        discard2.append(j) 

        discard_Cramers_V=[]
        for i,j in zip(discard1,discard2):
            if abs(cmatrix[[self.target]]).loc[i].values[0] > abs(cmatrix[[self.target]]).loc[j].values[0]:
                discard_Cramers_V.append(j)
            if abs(cmatrix[[self.target]]).loc[j].values[0] > abs(cmatrix[[self.target]]).loc[i].values[0]:
                discard_Cramers_V.append(i)

        res = [] 
        for i in discard_Cramers_V: 
            if i not in res: 
                res.append(i)             
        
        self.discard['Cramers_V'] = res
        
    def Multicolinearity(self, plot=False):    
        eig=[]
        for i,j in zip(self.df.isnull().sum().index, self.df.isnull().sum()):
            if j == 0:
                eig.append(i) # Selecting columns that do not contain any NaNs and inf. values

        w, v = np.linalg.eig(self.df[eig].corr()) # eigen values & eigen vectors

        CI=(w.max()/w)**0.5 # Condition Index

        Multicolinearity_matrix=pd.DataFrame(v,columns=[self.df[eig].corr().columns],index=[self.df[eig].corr().columns,CI])
        Multicolinearity_matrix.sort_index(level=1,ascending=False,inplace=True)

        Multicolinearity_matrix=Multicolinearity_matrix[Multicolinearity_matrix.index.get_level_values(1) > 30] # CI that greater than 30
        
        if Multicolinearity_matrix.shape[0] == 0:
            print('No features are dropped due to multicolinearity.')
            
        if plot == True and Multicolinearity_matrix.shape[0] != 0:
            sns.heatmap(Multicolinearity_matrix)
        
        feat_max_weight=[]
        for i in range(0,len(Multicolinearity_matrix.index)):
            feat_max_weight.append(Multicolinearity_matrix.columns[np.argmax(abs(Multicolinearity_matrix).iloc[i,:])][0])

        self.discard['Multicolinearity'] = feat_max_weight
        
    def pearson_with_target(self, show=True):
        Pearsons_R = self.df.corr()
        cmatrix = abs(Pearsons_R).sort_values(by=self.target,ascending=False)
        
        weak_Pearsons_R = []
        if show==True:
            for i,j in zip(cmatrix[self.target].index,cmatrix[self.target]):
                if j >= 0.3 and j <= 0.7:
                    print(str(self.target),str('-'),i,str(':'),round(j,3),str('(moderate)'))
                if j > 0.7:
                    print(str(self.target),str('-'),i,str(':'),round(j,3),str('(strong)'))     
                if j < 0.3 and j !=0:
                    print(str(self.target),str('-'),i,str(':'),round(j,3),str('(weak)'))
                if j == 0:
                    print(str(self.target),str('-'),i,str(':'),round(j,3),str('(no relationship)'))
                if j < 0.05:
                    weak_Pearsons_R.append(i)
                
        self.discard['pearson_with_target'] = weak_Pearsons_R
        
    def cramers_v_with_target(self, show=True):
        #Corrected Cramers'V function
        def cramers_corrected_stat(contingency_table):
            chi2 = chi2_contingency(contingency_table)[0]
            n = contingency_table.sum().sum()
            phi2 = chi2/n

            r, k = contingency_table.shape
            r_corrected = r - (((r-1)**2)/(n-1))
            k_corrected = k - (((k-1)**2)/(n-1))
            phi2_corrected = max(0, phi2 - ((k-1)*(r-1))/(n-1))

            return (phi2_corrected / min( (k_corrected-1), (r_corrected-1)))**0.5
        
        def categorical_corr_matrix(df):
            if type(df) == pd.Series:
                df = df.to_frame()
                
            cols = df.columns
            n = len(cols)
            corr_matrix = pd.DataFrame(np.zeros(shape=(n, n)), index=cols, columns=cols)

            for col1 in cols:
                for col2 in cols:
                    if col1 == col2:
                        corr_matrix.loc[col1, col2] = 1
                        break
                df_crosstab = pd.crosstab(df[col1], df[col2], dropna=True)
                corr_matrix.loc[col1, col2] = cramers_corrected_stat(df_crosstab)

            # Flip and add to get full correlation matrix
            corr_matrix += np.tril(corr_matrix, k=-1).T
            return corr_matrix
        
        cramersV = categorical_corr_matrix(self.df)
        cmatrix = cramersV.sort_values(by=self.target, ascending=False)

        weak_cramers_V=[]
        if show==True:
            for i,j in zip(cmatrix[self.target].index,cmatrix[self.target]):
                if j >= 0.3 and j <= 0.7:
                    print(str(self.target),str('-'),i,str(':'),round(j,3),str('(moderate)'))
                if j > 0.7:
                    print(str(self.target),str('-'),i,str(':'),round(j,3),str('(strong)'))     
                if j < 0.3 and j !=0:
                    print(str(self.target),str('-'),i,str(':'),round(j,3),str('(weak)'))
                if j ==0:
                    print(str(self.target),str('-'),i,str(':'),round(j,3),str('(no relationship)'))
                if j < 0.05:
                    weak_cramers_V.append(i)
                
        self.discard['cramers_v_with_target'] = weak_cramers_V
    
    def reduce(self, show=False, plot=False):
        if show == True:
            print(' ')
            print('1) Missing Percentages')
        self.missingpct(plot)
        
        if show == True:
            print(' ')
            print('2) Amount of Variation')
        self.std(plot=plot) 
        
        if show == True:
            print(' ')
            print("3) Pairwise Correlations - Pearson's R")
        self.pearsons_r(show=show, plot=plot) 
        self.pearson_with_target(show=show)
        
        if show == True:
            print(' ')
            print("4) Pairwise Correlations - Cramers'V") 
        self.Cramers_V(show=show, plot=plot)
        self.cramers_v_with_target(show=show)
        
        if show == True:
            print(' ')
            print('5) Multicolinearity') 
        self.Multicolinearity() 
        
        self.result = list(set().union(self.discard['missingpct'], 
                                       self.discard['std'], 
                                       self.discard['cramers_v_with_target'],
                                       self.discard['pearson_r'],
                                       self.discard['Cramers_V'], 
                                       self.discard['Multicolinearity'], 
                                       self.discard['pearson_with_target'], 
                                       self.discard['cramers_v_with_target']))
