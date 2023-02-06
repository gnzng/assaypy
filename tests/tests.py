import os

from assaypy import path_to_xlsx
from assaypy import excel_to_pandas
from assaypy import print_data_structure
from assaypy import attach_dubtrip, change_assay_dubtrip, group_wells
from assaypy import analyse_all


# import tests:

def test_import():
    path_to_current_file = os.path.realpath(__file__)
    current_directory = os.path.split(path_to_current_file)[0]
    print(current_directory)
    path_to_file = current_directory + '/testfiles/221222 Orange and Lime Run corrected.xlsx'
    assay_run_1 = path_to_xlsx(path_to_file)
    print('using assays xlsx file: ', assay_run_1)


path_to_current_file = os.path.realpath(__file__)
current_directory = os.path.split(path_to_current_file)[0]
path_to_file = current_directory + '/testfiles/221222 Orange and Lime Run corrected.xlsx'
assay_run_1 = path_to_xlsx(path_to_file)


# test pandas dataframe


# save all worksheets as pandas dataframes:
dfs1 = excel_to_pandas(assay_run_1)


def test_dict():
    assert isinstance(dfs1, dict)


def test_pd():
    import pandas as pd
    for worksheet in list(dfs1):
        assert isinstance(dfs1[worksheet], pd.DataFrame)


def test_print_data_structure():
    print_data_structure(dfs1)


# test attach_dubtrip data:


def test_attach_dubtrip_and_groups():
    dubtrip = attach_dubtrip(dfs1)
    change_assay_dubtrip(dfs1, dubtrip)
    # groups =
    group_wells(dfs1, dubtrip)


test_attach_dubtrip_and_groups()


def test_analyse_all():
    return analyse_all(dfs1, interval=300, time0=True)
    # slopes = analyse[0]
    # errslo = analyse[1]


test_analyse_all()
