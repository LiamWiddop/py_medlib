import pandas as pd
from pandas.core.frame import DataFrame
from typing import List
from lib.print import Error
from lib.progress import Bar

def MergeDataframesByColumns(dfONE, dfTWO, colONE, colTWO):

    # dfONE is dataframe one
    # dfTWO is dataframe two

    # colONE and colTWO contain string names for columns of interest to consider for the merge
    # by default, a string should be provided for colONE and colTWO
    # lists can also be provided

    # declare columns of interest into lists if strings
    if not isinstance(colONE, list):
        colONE = [colONE]
    if not isinstance(colTWO, list):
        colTWO = [colTWO]

    columns=dfONE.columns.to_list() + dfTWO.columns.to_list()

    mergedDF = DataFrame()
    unmergedDF = DataFrame()

    for i,one in Bar(dfONE[colONE].values,"Merging dataframes"):
        one = [y.lower() for y in one]
        merged = False
        for j,two in enumerate(dfTWO[colTWO].values):
            two = [y.lower() for y in two]
            shouldMerge = False

            for twoVal in two:
                if all(oneVal in twoVal for oneVal in one):
                    shouldMerge=True
                    break

            for oneVal in one:
                if all(twoVal in oneVal for twoVal in two):
                    shouldMerge=True
                    break
            
            if shouldMerge:
                merged = True
                newSeries = (pd.concat([dfONE.loc[i],dfTWO.loc[j]], axis=0, ignore_index=True,names=columns))
                mergedDF = mergedDF.append(newSeries, ignore_index=True)
                break
        if not merged:
            newSeries = (pd.concat([dfONE.loc[i],dfTWO.loc[j]], axis=0, ignore_index=True,names=columns))
            unmergedDF = unmergedDF.append(newSeries, ignore_index=True)

    mergedDF.columns = columns
    unmergedDF.columns = columns
    
    return {
        "merged":mergedDF,
        "unmerged":unmergedDF
    }

class Compositor:
    def MergeWith(self,Handler,colONE:List[str],colTWO:List[str]):
        if hasattr(Handler, 'dataframe'):
            mergeOutcome = MergeDataframesByColumns(self.dataframe, Handler.dataframe, colONE, colTWO)
            self.dataframe = mergeOutcome["merged"]
            self.unmerged = mergeOutcome["unmerged"]
        else:
            Error("Handler does not contain dataframe")