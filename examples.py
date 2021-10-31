from lib.pkl import PickleHandler
from lib.csv import CsvHandler
from lib.html import HTMLRender
from lib.compositor import MergeDataframesByColumns
from lib.medlib import EscapeURN, ColumnMergeWithList

# specify dataframes
csvData = CsvHandler("./data/SAH_NoPw.csv")
pklData = PickleHandler("./data/SAH_FMC_get.pkl")

# combines all series in dataframe using column name array
pklData.dataframe = ColumnMergeWithList(pklData.dataframe,[
    'PatientID',
    'PatientName',
    'PatientSex',
    'QueryRetrieveLevel',
    'RetrieveAETitle',
    'SpecificCharacterSet',
    'index'
])

# escape out URNS - i.e. remove leading zeros
EscapeURN(pklData.dataframe,"PatientID")

# merge dataframes by column names
# column names can be any number of columns wherein you are trying to find alike substrings to merge
# returns {
#   merged: mergedDF,
#   unmerged: unmergedDF
# }
mergeResult = MergeDataframesByColumns(pklData.dataframe,csvData.dataframe,"PatientName",["SURNAME","FIRSTNAME"])
mergeResult["merged"].to_csv('./output/merged.csv')

# print out merged and unmerged results
HTMLRender(mergeResult["merged"],name="MergedDF")
HTMLRender(mergeResult["unmerged"],name="UNMergedDF")