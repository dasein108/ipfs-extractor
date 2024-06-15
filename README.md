# ipfs-extractor

## Description

- Read text content from a file or IPFS CID 
- Perform text processing on the content
  - Extract keywords using **Named Entity Recognition (NER)**
  - Create summary using **Summarization**

_Only text/markdown formats are supported._

## Installation

#### *python

```
pyenv install 3.10.12
pyenv local 3.10.12
```

#### *virtual environment
```
python3.10 -m venv venv
source venv/bin/activate
```

### Install
```
pip install -r requirements.txt
```

## Usage

```
Perform Named Entity Recognition and Summarization of text content from a file or IPFS CID.

options:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Filename to process
  -c CID, --cid CID     IPFS CID to process
  --ner                 Perform Named Entity Recognition(default: enabled)
  --sum                 Perform Summarization(default: enabled)
```

### Example

```
python ipfs_extractor.py -c QmXkEnWAXjtQVxv3GFg4Y5e6pbXT8Jm2RaQK7DEBtFZTKj --ner --sum
```

---

##### Created by

[dasein](https://github.com/dasein108) (acidpictures@gmail.com)
