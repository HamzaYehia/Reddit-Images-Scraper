import os
import os.path as path


class Folder:

    def CreateFolder(ImagePath):
      DoesFolderExist = path.isdir(ImagePath) 

      if not DoesFolderExist:   
        os.makedirs(ImagePath)
    

    def GetImgPath(DirPath: str) -> str:
        ImagePath = path.join(DirPath, "Images/")
        IgnorePath = path.join(DirPath, "IgnoreImages/")
        
        return ImagePath