from Utils.Paths import Paths


class ImagesPathInfo:

    # Path to save images
    ImagePath: str = Paths.GetImgPath('')

    Paths.CreateFolder(ImagePath)
