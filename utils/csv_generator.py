import os.path
import datetime
from pathlib import Path
from typing import Union, List, Dict
import pandas as pd

class NoDirException(Exception):
    """Individual exception for non dir paths"""
    pass

def generate_csv(content: List[Dict[str, str]], path: Union[str|Path]):

    if isinstance(path, str):
        path = Path(path)

    if not path.is_dir():
        raise NoDirException(path, " is not directory. Can not store file to that path. Please provide directory.")

    df = pd.DataFrame(content)

    df.to_csv(os.path.join(f"{path}{os.sep}{datetime.date.today()}_extracted-dsgvo-content.csv"), index=False, encoding="utf-8-sig")
