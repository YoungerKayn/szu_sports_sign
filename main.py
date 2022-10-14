from datetime import datetime, timedelta
from os import path
from random import randint
from time import sleep
from sys import argv

from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

SportInfo = \
    {
        "StudentInfo": ["林漾珈","2021280279"],
        "QQ": "858425673",
        "password": "null",
        "WordUrl": argv[1],
        "picDir": r"D:\Python\test\Pic"
    }


def SummonPic(PicCount: int):
    for i in range(PicCount):
        date = datetime.strftime((datetime.now()-timedelta(days=i)), "%m-%d")
        PicDir = SportInfo["picDir"]
        PicName = datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')
        PicPath = path.join(
            PicDir, "result", f"{PicName}{i}.png")
        step = randint(10000, 23333)
        PicStruct = SummonPicStruct(PicDir=PicDir, step=step, date=date)
        ScreenshotPic = PastePic(PicStruct=PicStruct)
        ScreenshotPic.save(fp=PicPath, format="png")


def SummonPicStruct(PicDir: str, step: int, date: str):
    TemplateDir = path.join(PicDir, "template")
    TemplateDirA = path.join(TemplateDir, "A")
    TemplateDirB = path.join(TemplateDir, "B")
    TemplateDir1 = path.join(TemplateDir, "1")
    TemplateDir2 = path.join(TemplateDir, "2")
    TemplateDir3 = path.join(TemplateDir, "3")
    TemplateDir4 = path.join(TemplateDir, "4")
    TemplateDir5 = path.join(TemplateDir, "5")

    StepPic = SummonSetpPic(step=step, PicDirA=TemplateDirA)
    DatePic = SummonDatePic(PicDirB=TemplateDirB, date=date)
    TimePic = SummonTimePic(TemplateDir1)
    ChargePic = SummonChargePic(TemplateDir2)
    BarPic = SummonBarPic(TemplateDir3)
    LikesPic = SummonLikesPic(TemplateDir4)
    CoverPic = SummonCoverPic(TemplateDir5)

    ScreenshotBlankPicPath = path.join(TemplateDir, "blank.png")
    ScreenshotBlankPic = Image.open(ScreenshotBlankPicPath)

    PicStruct = \
        {
            "ScreenshotBlankPic": ScreenshotBlankPic,
            "StepPic": StepPic,
            "DatePic": DatePic,
            "TimePic": TimePic,
            "ChargePic": ChargePic,
            "BarPic": BarPic,
            "LikesPic": LikesPic,
            "CoverPic": CoverPic
        }
    return PicStruct


def SummonSetpPic(step: int, PicDirA: str):
    assert step > 9999, "Steps out of range"

    step = str(step)
    BlankPicPath = path.join(PicDirA, "blank.png")
    BlankPic = Image.open(BlankPicPath)
    StrPicPath = path.join(PicDirA, "S.png")
    StrPic = Image.open(StrPicPath)

    SizeA = [35, 23, 31, 32, 35, 33, 33, 32, 34, 32]
    SizeStr = 38
    XCursor = 0

    for i in range(len(step)):
        StepVar = step[i]
        ToPastePicPath = path.join(PicDirA, f"{StepVar}.png")
        ToPastePic = Image.open(ToPastePicPath)
        BlankPic.paste(im=ToPastePic, box=(XCursor, 0))
        XCursor += SizeA[int(StepVar)]+4

    XCursor += SizeStr
    BlankPic.paste(im=StrPic, box=(XCursor, 0))

    return BlankPic


def SummonDatePic(PicDirB: str, date: str):
    date = date.split("-")
    month = str(int(date[0]))
    day = str(int(date[1]))

    BlankPicPath = path.join(PicDirB, "blank.png")
    BlankPic = Image.open(BlankPicPath)
    MonthPicPath = path.join(PicDirB, "M.png")
    MonthPic = Image.open(MonthPicPath)
    DayPicPaht = path.join(PicDirB, "D.png")
    DayPic = Image.open(DayPicPaht)

    SizeB = [19, 13, 18, 18, 19, 18, 19, 19, 19, 19]
    SizeStrMonth = 35
    XCursor = 0

    for i in range(len(month)):
        MonthVar = month[i]
        ToPastePicPath = path.join(PicDirB, f"{MonthVar}.png")
        ToPastePic = Image.open(ToPastePicPath)
        BlankPic.paste(im=ToPastePic, box=(XCursor, 0))
        XCursor += SizeB[int(MonthVar)]+3

    BlankPic.paste(im=MonthPic, box=(XCursor, 0))
    XCursor += SizeStrMonth+3

    for i in range(len(day)):
        DayVar = day[i]
        ToPastePicPath = path.join(PicDirB, f"{DayVar}.png")
        ToPastePic = Image.open(ToPastePicPath)
        BlankPic.paste(im=ToPastePic, box=(XCursor, 0))
        XCursor += SizeB[int(DayVar)]+3

    BlankPic.paste(im=DayPic, box=(XCursor, 0))
    return BlankPic


def SummonCoverPic(PicDir5: str):
    Cover = randint(0, 2)
    CoverPicPath = path.join(PicDir5, f"{Cover}.png")
    CoverPic = Image.open(CoverPicPath)
    return CoverPic


def SummonLikesPic(PicDir4: str):
    Likes = randint(0, 1)
    LikesPicPath = path.join(PicDir4, f"{Likes}.png")
    LikesPic = Image.open(LikesPicPath)
    return LikesPic


def SummonBarPic(PicDir3: str):
    Bar = randint(0, 2)
    BarPicPath = path.join(PicDir3, f"{Bar}.png")
    BarPic = Image.open(BarPicPath)
    return BarPic


def SummonTimePic(PicDir1: str):
    Time = randint(0, 5)
    TimePicPath = path.join(PicDir1, f"{Time}.png")
    TimePic = Image.open(TimePicPath)
    return TimePic


def SummonChargePic(PicDir2: str):
    Charge = randint(0, 1)
    ChargePicPath = path.join(PicDir2, f"{Charge}.png")
    ChargePic = Image.open(ChargePicPath)
    return ChargePic


def PastePic(PicStruct):
    PositionA = (198, 1582)
    PositionB = (821, 1388)
    Position1 = (69, 34)
    Position2 = (953, 30)
    Position3 = (190, 29)
    Position4 = (901, 1603)
    Position5 = (313, 258)
    ScreenshotBlankPic = PicStruct["ScreenshotBlankPic"]
    ScreenshotBlankPic.paste(im=PicStruct["StepPic"], box=PositionA)
    ScreenshotBlankPic.paste(im=PicStruct["DatePic"], box=PositionB)
    ScreenshotBlankPic.paste(im=PicStruct["TimePic"], box=Position1)
    ScreenshotBlankPic.paste(im=PicStruct["ChargePic"], box=Position2)
    ScreenshotBlankPic.paste(im=PicStruct["BarPic"], box=Position3)
    ScreenshotBlankPic.paste(im=PicStruct["LikesPic"], box=Position4)
    ScreenshotBlankPic.paste(im=PicStruct["CoverPic"], box=Position5)
    return ScreenshotBlankPic


def LoginWord(WordUrl):
    account = SportInfo["QQ"]
    password = SportInfo["password"]
    StudentInfo = SportInfo["StudentInfo"]

    # 登录
    driver = webdriver.Chrome(service=Service(
        r"D:\Python\ChromeDriver\chromedriver.exe"))
    driver.get(WordUrl)
    sleep(2)
    driver.find_element(
        by=By.CLASS_NAME, value='login-button').click()
    sleep(2)
    driver.find_element(by=By.ID, value="qq-tabs-title").click()  # 切换QQ登录
    driver.switch_to.frame("login_frame")
    try:
        driver.find_element(
            by=By.ID, value=f"img_out_{account}").click()  # 尝试快捷登录
    except:
        driver.find_element(
            by=By.ID, value="switcher_plogin").click()  # 切换手动登录
        sleep(2)
        driver.find_element(By.ID, value="u").send_keys(account)
        driver.find_element(By.ID, value="p").send_keys(password)
        driver.find_element(By.ID, value="login_button").click()
    sleep(2)

    driver.switch_to.parent_frame()

    # 填写信息
    InputArea = driver.find_elements(
        by=By.CSS_SELECTOR, value="textarea")
    for i in range(len(InputArea)):
        InputArea[i].send_keys(StudentInfo[i])

    SubmitButton = driver.find_element(
        by=By.XPATH, value='//*[@type="button"]')
    print(SubmitButton)

    while (1):
        try:
            driver.find_element(by=By.XPATH, value='//*[@alt="图片"]')
            print("Find Pics, wait for updating...")
            break
        except:
            pass

    sleep(10)
    SubmitButton.click()
    sleep(60)


def main():
    SummonPic(5)
    LoginWord(WordUrl=SportInfo["WordUrl"])


if __name__ == '__main__':
    main()
