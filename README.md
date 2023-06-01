# Tools by Minho Park

## DictAction

```python
import argparse
from tools_mpark.dictaction import DictAction
parser = argparse.ArgumentParser()
parser.add_argument('--config_add', action=DictAction, nargs='+', default=dict(),
                    help='override some settings in the used config, the key-value pair '
                    'in xxx=yyy format will be merged into config file. If the value to '
                    'be overwritten is a list, it should be like key="[a,b]" or key=a,b '
                    'It also allows nested list/tuple values, e.g. key="[(a,b),(c,d)]" '
                    'Note that the quotation marks are necessary and that no white space '
                    'is allowed.')
```
