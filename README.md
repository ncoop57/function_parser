# function_parser
> This library contains various utils to parse GitHub repositories into function definition and docstring pairs. It is based on tree-sitter to parse code into ASTs and apply heuristics to parse metadata in more details. Currently, it supports 6 languages: Python, Java, Go, Php, Ruby, and Javascript. It also parses function calls and links them with their definitions for Python.


## Install

`pip install function-parser`

## How to use

In order to use the library you must download and build the language grammars for `tree-sitter` to parser source code with. Included in the library is a handy CLI tool for setting this up.

To download and build grammars: `build_grammars`

This command will download and build the grammars in the same location this python library was installed on your computer after pip installing.

```python
import function_parser
import os

import pandas as pd

from function_parser.language_data import LANGUAGE_METADATA
from function_parser.process import DataProcessor
from tree_sitter import Language

language = "python"
DataProcessor.PARSER.set_language(
    Language(os.path.join(function_parser.__path__[0], "tree-sitter-languages.so"), language)
)
processor = DataProcessor(
    language=language, language_parser=LANGUAGE_METADATA[language]["language_parser"]
)

dependee = "keras-team/keras"
definitions = processor.process_dee(dependee, ext=LANGUAGE_METADATA[language]["ext"])
pd.DataFrame(definitions).head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>nwo</th>
      <th>sha</th>
      <th>path</th>
      <th>language</th>
      <th>identifier</th>
      <th>parameters</th>
      <th>argument_list</th>
      <th>return_statement</th>
      <th>docstring</th>
      <th>docstring_summary</th>
      <th>docstring_tokens</th>
      <th>function</th>
      <th>function_tokens</th>
      <th>url</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>keras-team/keras</td>
      <td>e43af6c89cd6c4adecc21ad5fc05b21e7fa9477b</td>
      <td>keras/backend.py</td>
      <td>python</td>
      <td>backend</td>
      <td>()</td>
      <td></td>
      <td>return 'tensorflow'</td>
      <td>Publicly accessible method for determining the...</td>
      <td>Publicly accessible method for determining the...</td>
      <td>[Publicly, accessible, method, for, determinin...</td>
      <td>def backend():\n  """Publicly accessible metho...</td>
      <td>[def, backend, (, ), :, return, 'tensorflow']</td>
      <td>https://github.com/keras-team/keras/blob/e43af...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>keras-team/keras</td>
      <td>e43af6c89cd6c4adecc21ad5fc05b21e7fa9477b</td>
      <td>keras/backend.py</td>
      <td>python</td>
      <td>cast_to_floatx</td>
      <td>(x)</td>
      <td></td>
      <td>return np.asarray(x, dtype=floatx())</td>
      <td>Cast a Numpy array to the default Keras float ...</td>
      <td>Cast a Numpy array to the default Keras float ...</td>
      <td>[Cast, a, Numpy, array, to, the, default, Kera...</td>
      <td>def cast_to_floatx(x):\n  """Cast a Numpy arra...</td>
      <td>[def, cast_to_floatx, (, x, ), :, if, isinstan...</td>
      <td>https://github.com/keras-team/keras/blob/e43af...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>keras-team/keras</td>
      <td>e43af6c89cd6c4adecc21ad5fc05b21e7fa9477b</td>
      <td>keras/backend.py</td>
      <td>python</td>
      <td>get_uid</td>
      <td>(prefix='')</td>
      <td></td>
      <td>return layer_name_uids[prefix]</td>
      <td>Associates a string prefix with an integer cou...</td>
      <td>Associates a string prefix with an integer cou...</td>
      <td>[Associates, a, string, prefix, with, an, inte...</td>
      <td>def get_uid(prefix=''):\n  """Associates a str...</td>
      <td>[def, get_uid, (, prefix, =, '', ), :, graph, ...</td>
      <td>https://github.com/keras-team/keras/blob/e43af...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>keras-team/keras</td>
      <td>e43af6c89cd6c4adecc21ad5fc05b21e7fa9477b</td>
      <td>keras/backend.py</td>
      <td>python</td>
      <td>reset_uids</td>
      <td>()</td>
      <td></td>
      <td></td>
      <td>Resets graph identifiers.</td>
      <td>Resets graph identifiers.</td>
      <td>[Resets, graph, identifiers, .]</td>
      <td>def reset_uids():\n  """Resets graph identifie...</td>
      <td>[def, reset_uids, (, ), :, PER_GRAPH_OBJECT_NA...</td>
      <td>https://github.com/keras-team/keras/blob/e43af...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>keras-team/keras</td>
      <td>e43af6c89cd6c4adecc21ad5fc05b21e7fa9477b</td>
      <td>keras/backend.py</td>
      <td>python</td>
      <td>clear_session</td>
      <td>()</td>
      <td></td>
      <td></td>
      <td>Resets all state generated by Keras.\n\n  Kera...</td>
      <td>Resets all state generated by Keras.</td>
      <td>[Resets, all, state, generated, by, Keras, .]</td>
      <td>def clear_session():\n  """Resets all state ge...</td>
      <td>[def, clear_session, (, ), :, global, _SESSION...</td>
      <td>https://github.com/keras-team/keras/blob/e43af...</td>
    </tr>
  </tbody>
</table>
</div>


