#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: T. Malfatti <malfatti@disroot.org>
@date: 20170612
@license: GNU GPLv3 <https://gitlab.com/malfatti/SciScripts/raw/master/LICENSE>
@homepage: https://gitlab.com/Malfatti/SciScripts
"""

import numpy as np
from itertools import combinations
from rpy2 import robjects as RObj
from rpy2.robjects import packages as RPkg


## Level 0
def AdjustNaNs(Array):
    NaN = RObj.NA_Real

    for I, A in enumerate(Array):
        if A != A: Array[I] = NaN

    return(Array)


def PearsonRP(A,B):
    r = pearsonr(A, B)
    r = list(r)
    r[0] = round(r[0], 3)
    if r[1] < 0.05:
        r[1] = '%.1e' % r[1] + ' *'
    else:
        r[1] = str(round(r[1], 3))

    return(r)


def PToStars(p, Max=3):
    No = 0
    while p < 0.05 and No <= Max:
        p *=10
        No +=1

    return(No)


def RCheckPackage(Packages):
    RPacksToInstall = [Pack for Pack in Packages if not RPkg.isinstalled(Pack)]
    if len(RPacksToInstall) > 0:
        print(str(RPacksToInstall), 'not installed. Install now?')
        Ans = input('[y/N]: ')

        if Ans.lower() in ['y', 'yes']:
            from rpy2.robjects.vectors import StrVector as RStrVector

            RUtils = RPkg.importr('utils')
            RUtils.chooseCRANmirror(ind=1)

            RUtils.install_packages(RStrVector(RPacksToInstall))

        else: print('Aborted.')

    return(None)


## Level 1
def RPCA(Matrix):
    RCheckPackage(['stats']); Rstats = RPkg.importr('stats')

    RMatrix = RObj.Matrix(Matrix)
    PCA = Rstats.princomp(RMatrix)
    return(PCA)


def RAnOVa(Data, Factors, Paired, Id=[]):
    RCheckPackage(['rstatix']); RPkg.importr('rstatix')

    Values = RObj.FloatVector(Data)
    FactorsV = [RObj.FactorVector(_) for _ in Factors]
    Frame = {f'Factor{f+1}': F for f,F in enumerate(FactorsV)}
    Frame['Values'] = Values

    if len(Id):
        Idv = RObj.IntVector(Id)
        RObj.globalenv['Id'] = Idv
        Frame['Id'] = Idv

    Frame = RObj.DataFrame(Frame)

    RObj.globalenv['Frame'] = Frame
    RObj.globalenv['Values'] = Values
    for F,Factor in enumerate(FactorsV): RObj.globalenv[f'Factor{F+1}'] = Factor

    FactorsW = ','.join([f'Factor{_+1}' for _ in range(len(Factors)) if Paired[_]])
    FactorsB = ','.join([f'Factor{_+1}' for _ in range(len(Factors)) if not Paired[_]])
    Model = RObj.r(f'''anova_test(Frame, dv=Values, wid=Id, between=c({FactorsB}), within=c({FactorsW}))''')

    # FactorsS = '*'.join([f'Factor{_+1}' for _ in range(len(Factors))])
    # if RepeatedMeasures:
        # Model = RObj.r(f'''anova_test(Frame, dv=Values, wid=Id, within=c({FactorsS.replace("*",",")}))''')
        # Model = RObj.r(f'''anova_test(Values~{FactorsS} + Error(Id/({FactorsP})), data=Frame)''')
    # else:
        # Model = RObj.r(f'''anova_test(Frame, Values ~ {FactorsS})''')

    return(Model)


def RAnOVaPwr(GroupNo=RObj.NULL, SampleSize=RObj.NULL, Power=RObj.NULL,
           SigLevel=RObj.NULL, EffectSize=RObj.NULL):
    RCheckPackage(['pwr']); Rpwr = RPkg.importr('pwr')

    Results = Rpwr.pwr_anova_test(k=GroupNo, power=Power, sig_level=SigLevel,
                                  f=EffectSize, n=SampleSize)

    print('Running', Results.rx('method')[0][0] + '... ', end='')
    AnOVaResults = {}
    for Key, Value in {'k': 'GroupNo', 'n': 'SampleSize', 'f': 'EffectSize',
                       'power':'Power', 'sig.level': 'SigLevel'}.items():
        AnOVaResults[Value] = Results.rx(Key)[0][0]

    print('Done.')
    return(AnOVaResults)


def RModelToDict(Model):
    Dict = {
        C: np.array(Col.levels)
        if 'Factor' in C and np.array(Col).dtype == np.int32
        else np.array(Col)
        for C,Col in Model.items()
    }

    return(Dict)


def RTTest(DataA, DataB, Paired=True, EqualVar=False, Alt='two.sided', Confidence=0.95):
    RCheckPackage(['rstatix']); RPkg.importr('rstatix')
    Rttest = RObj.r['t.test']
    RCohensD = RObj.r['cohens_d']

    DataA = AdjustNaNs(DataA); DataB = AdjustNaNs(DataB)

    Results = Rttest(RObj.FloatVector(DataA), RObj.FloatVector(DataB),
                     paired=Paired, var_equal=EqualVar, alternative=Alt,
                     conf_level=RObj.FloatVector([Confidence]),
                     na_action=RObj.r['na.omit'])

    TTestResults = {}; Names = list(Results.names)
    for Name in Names:
        TTestResults[Name] = Results.rx(Name)[0][0]

    Values = RObj.FloatVector(np.concatenate((DataA, DataB)))
    Factor = RObj.FactorVector(['A']*len(DataA)+['B']*len(DataB))

    Frame = RObj.DataFrame({
        'Values': Values,
        'Factor': Factor,
    })

    RObj.globalenv["Confidence"] = Confidence
    RObj.globalenv["EqualVar"] = EqualVar
    RObj.globalenv["Factor"] = Factor
    RObj.globalenv["Frame"] = Frame
    RObj.globalenv["Paired"] = Paired
    RObj.globalenv["Values"] = Values
    Model = RObj.r('''cohens_d(Frame, Values ~ Factor, conf.level=Confidence, var.equal=EqualVar, paired=Paired)''')
    TTestResults['CohensD'] = RModelToDict(Model)

    return(TTestResults)


## Level 2
def AnOVa(Data, Factors, Id=[], Paired=[]):
    if not len(Paired): Paired = [False for _ in Factors]
    PairedV = ['TRUE' if _ else 'FALSE' for _ in Paired]

    # Combs = list(combinations(range(len(Factors)),len(Factors)-1))
    # for F,Factor in enumerate(Factors):
        # Others = [F not in _ for _ in Combs].index(True)
        # Others = Combs[Others]

        # OthersCond = []
        # for O in Others:
            # if not len(OthersCond): OthersCond =
        # Paired = [
            # O==ao for ao in np.unique(Others)]
            # for O in Others
        # ]

    # # This works
    # True in [a[((c==af1)*(d==af2)*(e==ai)).astype(bool)].shape[0]>1 for af1 in c for af2 in d for ai in e]
    # # for data a; factors b,c and d; and id e
    # # but how to dynamically iterate through different number of factors?

    ColsAnOVa = ['Effect', 'DFn', 'DFd', 'F', 'p', 'p<.05', 'ges', 'p.adj']
    ColsSph = ['Effect', 'W', 'p', 'p<.05']
    ColsSphCorr = ['Effect', 'GGe', 'DF[GG]', 'p[GG]', 'p[GG]<.05', 'HFe', 'DF[HF]', 'p[HF]']
    ColsPWC = [['Factor', '.y.', 'group1', 'group2', 'n1', 'n2']]*2

    ColsPWC = [
        Cols + ['statistic', 'df', 'p', 'p.adj', 'p.adj.signif']
        if Paired[C] else
        Cols + ['p', 'p.signif', 'p.adj', 'p.adj.signif']
        for C,Cols in enumerate(ColsPWC)
    ]

    Model = RAnOVa(Data, Factors, Paired, Id)

    # if True in Paired:
    FactorsW = [_ for _ in range(len(Factors)) if Paired[_]]
    FPairs = tuple(combinations(range(len(Factors)), 2))

    FXs = {}
    for FPair in FPairs:
        fw = [_ in FactorsW for _ in FPair]

        fs = f'within=Factor{FPair[0]+1}' if fw[0] else f'between=Factor{FPair[0]+1}'
        FXs[f'Factor{FPair[0]+1}'] = RObj.r(
            f'''Frame %>% group_by(Factor{FPair[1]+1}) %>% anova_test(dv=Values, wid=Id, {fs}) %>% get_anova_table() %>% adjust_pvalue(method="bonferroni")'''
        )

        fs = f'within=Factor{FPair[1]+1}' if fw[0] else f'between=Factor{FPair[1]+1}'
        FXs[f'Factor{FPair[1]+1}'] = RObj.r(
            f'''Frame %>% group_by(Factor{FPair[0]+1}) %>% anova_test(dv=Values, wid=Id, {fs}) %>% get_anova_table() %>% adjust_pvalue(method="bonferroni")'''
        )

    PWC = {}
    for FPair in FPairs:
        PWC[f'Factor{FPair[0]+1}'] = RObj.r(
            f'''Frame %>% group_by(Factor{FPair[1]+1}) %>% pairwise_t_test(Values~Factor{FPair[0]+1}, paired={PairedV[FPair[0]]}, p.adjust.method="bonferroni")'''
        )
        PWC[f'Factor{FPair[1]+1}'] = RObj.r(
            f'''Frame %>% group_by(Factor{FPair[0]+1}) %>% pairwise_t_test(Values~Factor{FPair[1]+1}, paired={PairedV[FPair[1]]}, p.adjust.method="bonferroni")'''
        )

    if Model.rclass[1] == 'list':
        Results = {
            'ANOVA': RModelToDict(Model[0]),
            'MauchlySphericity': RModelToDict(Model[1]),
            'SphericityCorrection': RModelToDict(Model[2]),
            'FXFactors': {F: RModelToDict(Fac) for F,Fac in FXs.items()},
            'PWCs': {F: RModelToDict(Fac) for F,Fac in PWC.items()}
        }
    else:
        Results = {
            'ANOVA': RModelToDict(Model),
            'FXFactors': {F: RModelToDict(Fac) for F,Fac in FXs.items()},
            'PWCs': {F: RModelToDict(Fac) for F,Fac in PWC.items()}
        }

    # else:
        # Results = {'ANOVA': RModelToDict(Model)}

    return(Results)

