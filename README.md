# Caviar

A command-line tool to remove code sections marked with tags from Python files and Jupyter notebooks.

## Description

Caviar processes Python files (`.py`) and Jupyter notebooks (`.ipynb`) to remove code sections enclosed between configurable start and end tags. This is particularly useful for creating clean exercise templates by removing solution code.

## Installation

```bash
pip install -e .
```

## Usage

### Command Line Interface

```bash
caviar --source <source_dir> --target <target_dir> --starting-tag <start> --ending-tag <end>
```

### Parameters

- `--source`: Source directory containing files to process
- `--target`: Target directory where processed files will be saved
- `--starting-tag`: Tag marking the beginning of content to remove (default: `STRIP_START`)
- `--ending-tag`: Tag marking the end of content to remove (default: `STRIP_END`)

### Environment Variables

You can also set parameters using environment variables:

```bash
export SOURCE=/path/to/source
export TARGET=/path/to/target
export STARTING_TAG=STRIP_START
export ENDING_TAG=STRIP_END
```

### Example

Given a Python file with tagged content:

```python
print("This will be kept")
# STRIP_START
print("This will be removed")
x = 42
# STRIP_END
print("This will also be kept")
```

Running Caviar will produce:

```python
print("This will be kept")
print("This will also be kept")
```

## Features

- ✅ Processes Python files (`.py`)
- ✅ Processes Jupyter notebooks (`.ipynb`)
- ✅ Processes Markdown files (`.md`)
- ✅ Preserves directory structure
- ✅ Handles missing end tags gracefully (no crashes)
- ✅ Configurable start/end tags
- ✅ Environment variable support

## Requirements

- Python ≥ 3.6
- click ≥ 8.1.7
- nbformat == 5.10.4

## License

MIT License - see project metadata for details.