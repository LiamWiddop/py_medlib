from lib.pkl import PickleHandler
from lib.csv import CsvHandler
from lib.html import HTMLRender
from lib.compositor import MergeDataframesByColumns
from lib.medlib import EscapeURN, ColumnMergeWithList

csvData = CsvHandler("./data/SAH_NoPw.csv")
pklData = PickleHandler("./data/SAH_FMC_get.pkl")

# HTMLRender(pklData)

pklData.dataframe = ColumnMergeWithList(pklData.dataframe,[
    'PatientID',
    'PatientName',
    'PatientSex',
    'QueryRetrieveLevel',
    'RetrieveAETitle',
    'SpecificCharacterSet',
    'index'
])
# iterate over rows
EscapeURN(pklData.dataframe,"PatientID")
mergeResult = MergeDataframesByColumns(pklData.dataframe,csvData.dataframe,"PatientName",["SURNAME","FIRSTNAME"])
mergeResult["merged"].to_csv('./output/merged.csv')

HTMLRender(mergeResult["merged"])