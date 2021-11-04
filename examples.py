from lib.pkl import PickleHandler
from lib.csv import CsvHandler

# Creates DataframeHandlers
csvData = CsvHandler("./data/Labels.csv")
pklData = PickleHandler("./data/Meta.pkl")

# escapes patient ID
pklData.EscapeZeros("PatientID")

# Removes all cases where a column value equals something - in this case: 'IssuerOfPatientID' as 'RAH'
pklData.PopWhereNOT("StudyDescription",["CT Brain Without Contrast"])

# combines all series in dataframe using column name array
pklData.ColumnMerge([
    'PatientID',
    'PatientName',
    'PatientSex',
    'QueryRetrieveLevel',
    'RetrieveAETitle',
    'SpecificCharacterSet',
    'index'
])

# Merges DataframeHandler dataframes
pklData.MergeWith(csvData,["PatientName"],["SURNAME","FIRSTNAME"])

# Displays output
pklData.HTMLRender()