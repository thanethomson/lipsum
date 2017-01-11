# lipsum

[![Build Status](https://travis-ci.org/thanethomson/lipsum.svg?branch=master)](https://travis-ci.org/thanethomson/lipsum)
[![PyPI](https://img.shields.io/pypi/v/lipsum.svg)](https://pypi.python.org/pypi/lipsum)
[![PyPI](https://img.shields.io/pypi/pyversions/lipsum.svg)](https://pypi.python.org/pypi/lipsum)

## Overview
`lipsum` for Python is a simple [Lorem Ipsum](https://en.wikipedia.org/wiki/Lorem_ipsum)
generator library which can be used in your Python applications.
Note that this library only generates **randomised** Lorem Ipsum
strings (words, sentences and paragraphs). By default, it takes its
source text from Cicero's
[De finibus bonorum et malorum](https://en.wikipedia.org/wiki/De_finibus_bonorum_et_malorum),
but you can specify your own source text if you want (which must be
greater than 100kB in size).

## Installation
You can install the package from PyPI:

```bash
> pip install lipsum
```

## Usage
Some simple usage examples:

```python
import lipsum

# randomly grab 100 words
lipsum.generate_words(100)

# randomly grab 3 sentences
lipsum.generate_sentences(3)

# randomly grab 2 paragraphs
lipsum.generate_paragraphs(2)

# use your own source text to generate 3 paragraphs
lipsum.generate_paragraphs(2, filename="/path/to/my/source.txt")

# specify the encoding of the source text file
lipsum.generate_paragraphs(2, filename="/path/to/my/source.txt", encoding="utf-8")
```

To see what the output looks like, the following is the result of
randomly generating 2 paragraphs:

```
Heri, inquam, ludis commissis ex urbe profectus veni ad vesperum.
causa autem fuit huc veniendi ut quosdam hinc libros promerem. et
quidem, Cato, hanc totam copiam iam Lucullo nostro notam esse oportebit;
nam his libris eum malo quam reliquo ornatu villae delectari. est enim
mihi magnae curae - quamquam hoc quidem proprium tuum munus est - ut ita
erudiatur, ut et patri et Caepioni nostro et tibi tam propinquo
respondeat. laboro autem non sine causa; nam et avi eius memoria moveor
- nec enim ignoras, quanti fecerim Caepionem, qui, ut opinio mea fert,
in principibus iam esset, si viveret - et Lucullus mihi versatur ante
oculos, vir cum virtutibus omnibus excellens, tum mecum et amicitia et
omni voluntate sententiaque coniunctus.

Praeclare, inquit, facis, cum et eorum memoriam tenes, quorum uterque
tibi testamento liberos suos commendavit, et puerum diligis. quod autem
meum munus dicis non equidem recuso, sed te adiungo socium. addo etiam
illud, multa iam mihi dare signa puerum et pudoris et ingenii, sed
aetatem vides.
```

When generating content, `lipsum` will automatically attempt to append
punctuation to the end of your sentences and capitalise the first letter
of new sentences.

## License
**The MIT License (MIT)**

Copyright (c) 2017 Thane Thomson

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

