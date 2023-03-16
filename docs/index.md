# assaypy

# Table of Contents

1. [installation](#installation)
2. [data import](#data-import)
3. [quick look](#quick-look)
4. [CABP data](#cabp-data)
5. [FAQs](#faqs)

## installation

For installation of assaypy use

```python
pip install assaypy
```

One can use cell magic in Jupyter notebook:

```python
%pip install assaypy
```

update to latest version:

```python
pip install -U assaypy
```

install specific version:

```python
pip install assaypy==0.0.2
```

check which versions are installed:

```python
pip freeze | grep assaypy
```

other important modules are: `matplotlib, pprint, pandas, numpy` and `ipywidgets`

## data import

Import data via `path_to_xlsx()` function to locate the excel file, if it can't find the provided excel sheet, the program will open a file browser, where the file can be selected by hand:

```python
assay_run_1 =  path_to_xlsx('tests/testfiles/ 270123 CABP Quant Exp no header.xlsx')
```

Convert the excel sheet into a dictionary of multiple pandas DataFrames for further handling via

```python
dfs = excel_to_pandas(_file: str)-> dict()
```

All metadata and headers are skipped for now. Load all datasheets from the excel file and trim first rows bc of header, can be saved or extracted via another function
trim last 10 rows, to exclude last NaNs.

Now show worksheets of excel sheets and well names:

```python
print_data_structure(dfs)
>> '''data structure with columns found:

Assay 4 Shaking
['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'E1', 'E2', 'E3', 'E4', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12', 'G1', 'G2']
number of columns: 28

Assay 3 Shaking
['A9', 'A10', 'A11', 'A12', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'E10', 'E11', 'E12', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10', 'G11', 'G12']
number of columns: 50

Assay 2 Shaking
['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'C11', 'C12']
number of columns: 30'''
```

### remove worksheets/assay from process

```python
print('tick box to remove Assays:')
checkboxes = [widgets.Checkbox(value=False, description=label) for label in list(dfs)]
display(widgets.VBox(children=checkboxes))
```

-> click boxes of assays to remove and proceed:

```python
remove_assays = []
for i in range(0, len(checkboxes)):
    if checkboxes[i].value == True:
        remove_assays = remove_assays + [checkboxes[i].description]
for n in remove_assays:
     del dfs1[n]
print('removed assays:', remove_assays)
>> '''removed assays: ['Assay 2 Shaking']'''
```

## quick look

If you don't want to do a whole procedure but are still interested in a quick look, this functions are now helpful for you:

## CABP data

## FAQs
