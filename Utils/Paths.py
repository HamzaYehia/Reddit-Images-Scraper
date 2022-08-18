import os
import os.path as path


class Paths:

    def CreateFolder(ImagePath: str) -> None:
      FolderDoesntExist: bool = not path.isdir(ImagePath) 

      if FolderDoesntExist:   
          os.makedirs(ImagePath)


    def GetImgPath(DirPath: str) -> str:
        ImagePath: str = path.join(DirPath, "Images/")

        return ImagePath


    def GetIgnorePath(DirPath: str) -> str:
        IgnorePath: str = path.join(DirPath, "IgnoreImages/")

        return IgnorePath
