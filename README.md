# gidc

Get Image's Dominant Color

## Usage

```
gidc IMG [IMG ...] [OPTION ...]
```

## Requirements

* Python 3
* Argcomplete
* Argparse
* Numpy

# sidc

Sort Images by their Dominant Color

## Usage
```
sidc IMG [IMG ...] [OPTION ...]
```
or
```
sidc DIR [DIR ...] [OPTION ...]
```

## Example
```
sidc foobar.png
```
Let's say foobar.png is mainly made of white.

`foobar.png` will therefore be moved to a directory called 'white'.

## Configuration

For now, you can configure `sidc` by modifiying the variables at the beginning of the file.

## Requirements

* gidc
* Perl (if you want progress to be displayed)
