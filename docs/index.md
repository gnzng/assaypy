# assaypy

## table of contents

1. [installation](#installation)
2. [data import](#data-import)
3. [grouping](#grouping)
4. [quick look](#quick-look)
5. [CABP data](#cabp-data)
6. [FAQs](#faqs)

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

## grouping

Grouping is important to combine multiple wells into one unit for analysis and first impression. First attach information if an assay or worksheet is measured in duplicate or triplicate via the following function, a prompt will open and one can type in the right information

```python
dubtrip = attach_dubtrip(dfs)
>>'''final:

{'Assay 3 Shaking': 3, 'Assay 4 Shaking': 3}'''
```

Prompt for changing the attached duplicate or triplicate information via

```python
change_assay_dubtrip(dfs, dubtrip)
```

with that information the grouping can be done for all loaded assays or spreadsheets. Two modes are possible at the moment `'A1-A2'` and `'A1-B1'` for combining the wells.

```python
groups = group_wells(dfs, dubtrip, mode = 'A1-A2')
```

`groups` will be saved as simple `dict`s and can be changed manually by adressing the key value pairs.

## quick look

If you don't want to do a whole procedure but are still interested in a quick look, this functions are now helpful for you:

This section requires update to version 0.0.7:

`analyse_all(dfs1, interval = 200, time0=True, endtime=1000)`

`time0` if `True` starts slope analysis after reaction starts, guessing the start time of the reaction by the long break with no data aquisation. Instead of giving a boolean you can also give a starting time in seconds.

With the exclude parameter one can exclude e.g. 'Assay 1 No Shaking' e.g. or 3 for exluding all triplicate analysis.

Quick look at all the loaded assays:

```python
slopes, errslo = analyse_all(dfs1, interval = 100, time0 = 300, endtime = 2300)

plot_assays_and_slopes(dfs,
                       groups,
                       slopes,
                       errslo,
                       show_average=True,
                       exclude = [],
                       )
```

will result in many plots of all the assays. Showing slopes and derivation with the above defined parameters like that:
![Assay Slopes](img/assay_slopes.png)

Plotting the average slopes of the shown curves above:

```python
plot_slope_values(groups, slopes)
```

![Assay Slope Values](img/assay_slope_values.png)

The grey points in the plot mark the standard deviation of all averaged slope values from the group.

## CABP data

tbd

## FAQs

- 'How do I export the analysis or part of the analysis to Excel sheets?'

```python
export_to_excel(slopes,path='output1.xlsx')
```

from version 0.0.7
