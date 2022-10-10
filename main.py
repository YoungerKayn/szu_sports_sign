from os import path

from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

SportInfo = \
    {
        "name": "Test",
        "number": "2021123456",
        "class": "13",
        "type": "2",
        "picDir": r"D:\Python\test\Pic"
    }


def SummonPic(picDir):
    templateDir = path.join(picDir, 'template')
    assert path.isdir(templateDir), f"{templateDir} is not a dir"
    return templateDir


def SubmitInfo(SubmitUrl, SportInfo):
    pass


def main():
    templateDir = SummonPic(picDir=SportInfo["picDir"])
    print(templateDir)
    return 0


if __name__ == '__main__':
    main()
