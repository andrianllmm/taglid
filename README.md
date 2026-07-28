<div align="center">

# TagLID

**A word-level Language Identification (LID) tool for Tagalog-English (Taglish)
text**

</div>

## About

TagLID is a library that labels each word in a Taglish (Tagalog-English mix)
text by language. It gives either a simple tag (`tgl` or `eng`) or detailed
frequency info with flags indicating how the word was identified. It is a
rule-based and opinionated system that mostly uses dictionary lookups. It also
handles cases like skipping numbers, names, and interjections, and includes
logic for dealing with slang, abbreviations, contractions, stemming or
lemmatizing inflected words, intrawords, and correcting misspellings.

## Installation

```sh
pip install git+https://github.com/andrianllmm/taglid.git@main
```

## Usage

TagLID can act as a standalone library that can be imported via `import taglid`
or as a CLI application via `python -m taglid`.

### Library Mode

#### Textual data

Use the `lid` module for textual data.

Use `lang_identify` to identify each word in a text. This takes any string and
returns a list of words and their corresponding English and Tagalog values,
flag, and correction.

```python
from taglid.lid import lang_identify

labeled_text = lang_identify("hello, mundo")
print(labeled_text)
```

Output:

```
[{'Word': 'hello', 'eng': 1.0, 'tgl': 0.0, 'Flag': 'DICT', 'Correction': None}, {'Word': 'mundo', 'eng': 0.0, 'tgl': 1.0, 'Flag': 'DICT', 'Correction': None}]
```

Use [`tabulate`](https://pypi.org/project/tabulate/) to view output in tabular
format.

```python
from tabulate import tabulate

print(tabulate(labeled_text, headers="keys"))
```

Output:

```
word      eng    tgl  flag    correction
------  -----  -----  ------  ------------
hello       1      0  DICT
mundo       0      1  DICT
```

Use `simplify` to only show the words and their language. This takes the return
value of `lang_identify` and returns a list of tuples containing the word and
its language.

```python
from taglid.lid import simplify

simplified_text = simplify(labeled_text)
print(simplified_text)
```

Output:

```
[('hello', 'eng'), ('mundo', 'tgl')]
```

#### Datasets

Use the `lid_dataset` module for datasets.

Use `lang_identify_df` to label each word in each cell in a
[`pandas`](https://pypi.org/project/pandas/) DataFrame. This takes a DataFrame
of multiple rows and columns with each cell containing textual data and returns
a labeled DataFrame where each token is a row labeled by its original row,
original column, and token index.

```python
import pandas as pd
from taglid.lid_dataset import lang_identify_df

data = [['hello po', 'ano?'], ['mag-aask lang po', 'what?']]

df = pd.DataFrame(data)

labeled_df = lang_identify_df(df)
print(labeled_df)
```

Output:

```
     col  token_index      word  eng  tgl  flag correction
row
0      0            1     hello  1.0  0.0  DICT       None
0      0            2        po  0.0  1.0  DICT       None
0      1            1       ano  0.0  1.0  FREQ       None
1      0            1  mag-aask  0.5  0.5  INTW       None
1      0            2      lang  0.0  1.0  FREQ       None
1      0            3        po  0.0  1.0  DICT       None
1      1            1      what  1.0  0.0  DICT       None
```

### CLI Mode

Run TagLID from the terminal.

```sh
python -m taglid.lid
```

Then type a sentence when prompted.

```
text: hello, mundo
```

Output:

```
word      eng    tgl  flag    correction
------  -----  -----  ------  ------------
hello       1      0  DICT
mundo       0      1  DICT
```

Add `--simplify` to only show the words and their language.

```sh
python -m taglid.lid --simplify --text hello, mundo
```

Output:

```
-----  ---
hello  eng
mundo  tgl
-----  ---
```

Use `lid_dataset` with Excel files to directly label spreadsheets.

```sh
python -m taglid.lid_dataset in_path out_path
```

## Accuracy

The accuracy hasn't been tested yet.

## Contributing

Contributions are welcome! To get started:

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a pull request

## Issues

Found a bug or issue? Report it on the
[issues page](https://github.com/andrianllmm/taglid/issues).
