import os
import os.path as path

def CreateFolder(ImagePath):
    DoesFolderExist = path.isdir(ImagePath)

    if not DoesFolderExist:
      os.makedirs(ImagePath)
