# This project is currently in pre-ALPHA stage.
Meaning, it's under development and doesn't really work at all.

## Purpose
To provide a [levenshtein distance](http://en.wikipedia.org/wiki/Levenshtein_distance) for images.  Which will tell you how much one image has to change to become the other image.

This could be useful for comparing screen captures of a website to see how much changed.

## Usage
```bash
python levenshtein.py image1.png image2.png
# levenshtein distance: 1303 error: 0.091632%
```
```python
import image_distance
distance, error_max = image_distance.compare(filename_a, filename_b)
```