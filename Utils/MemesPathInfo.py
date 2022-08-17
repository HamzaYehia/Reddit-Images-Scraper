from typing import Dict

from Utils.Paths import Paths
from Utils.Tokens import Tokens


class MemesPathInfo:

    # Path to save images
    ImagePath: str = Paths.GetImgPath('')

    Paths.CreateFolder(ImagePath)
