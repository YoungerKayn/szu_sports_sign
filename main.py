from datetime import datetime, timedelta
from os import path
from random import randint
from time import sleep
from sys import argv

from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

Wordurl = argv[1] if len(argv) > 1 else 5

SportInfo = \
    {
        "StudentInfo": ["{姓名}", "{学号}"],
        "QQ": "{QQ}",
        "password": "null",
        "WordUrl": Wordurl,
        "picDir": r"D:\Python\test\Pic"
    }

Dir = \
    {
        "PicDir": SportInfo["picDir"],
        "TemplateDir": path.join(SportInfo["picDir"], "template"),
        "TemplateDirA": path.join(SportInfo["picDir"], "template", "A"),
        "TemplateDirB": path.join(SportInfo["picDir"], "template", "B"),
        "TemplateDir1": path.join(SportInfo["picDir"], "template", "1"),
        "TemplateDir2": path.join(SportInfo["picDir"], "template", "2"),
        "TemplateDir3": path.join(SportInfo["picDir"], "template", "3"),
        "TemplateDir4": path.join(SportInfo["picDir"], "template", "4"),
        "TemplateDir5": path.join(SportInfo["picDir"], "template", "5"),
        "TemplateDir8": path.join(SportInfo["picDir"], "template", "8"),
        "ResultDir": r"C:\Users\Administrator\桌面"
    }


def SummonPic(dateOffset: int = 0):
    TemplateDir = Dir["TemplateDir"]
    ScreenshotBlankPic2Path = path.join(TemplateDir, "blank2.png")
    ScreenshotPic2 = Image.open(ScreenshotBlankPic2Path)
    for i in range(5):
        date = datetime.strftime(
            (datetime.now() - timedelta(days=i + dateOffset)), "%m-%d")
        step = randint(10000, 23333)
        PicStruct = SummonPicStruct(step=step, date=date)
        if i == 0:  # 生成当天的主页
            ScreenshotPic1 = PastePic1(PicStruct=PicStruct)
            ResultPath1 = path.join(
                Dir["ResultDir"],
                f"{datetime.strftime(datetime.now()-timedelta(days=dateOffset), '%Y%m%d%H%M%S')}1.png"
            )
            # ScreenshotPic1.show()
            ScreenshotPic1.save(fp=ResultPath1, format="png")
        ScreenshotPic2 = PastePic2(ScreenshotPic2,
                                   PicStruct=PicStruct,
                                   Cursor=i,
                                   dateOffset=dateOffset)

    ResultPath2 = path.join(
        Dir["ResultDir"],
        f"{datetime.strftime(datetime.now()-timedelta(days=dateOffset), '%Y%m%d%H%M%S')}2.png"
    )
    # ScreenshotPic2.show()
    ScreenshotPic2.save(fp=ResultPath2, format="png")
    print(f"Save pics to {Dir['ResultDir']}")


def SummonPicStruct(step: int, date: str) -> dict:
    StepPic = SummonStepPic(PicDirA=Dir["TemplateDirA"], step=step)
    DatePic = SummonDatePic(PicDirB=Dir["TemplateDirB"], date=date)
    TimePic = SummonTimePic(Dir["TemplateDir1"])
    ChargePic = SummonChargePic(Dir["TemplateDir2"])
    MessagePic = SummonMessagePic(Dir["TemplateDir3"])
    LikesPic = SummonLikesPic(Dir["TemplateDir4"])
    CoverPic = SummonCoverPic(Dir["TemplateDir5"])

    ScreenshotBlankPicPath = path.join(Dir["TemplateDir"], "blank.png")
    ScreenshotBlankPic2Path = path.join(Dir["TemplateDir"], "blank2.png")
    ScreenshotBlankPic = Image.open(ScreenshotBlankPicPath)
    ScreenshotBlankPic2 = Image.open(ScreenshotBlankPic2Path)

    PicStruct = \
        {
            "ScreenshotBlankPic": ScreenshotBlankPic,
            "ScreenshotBlankPic2": ScreenshotBlankPic2,
            "StepPic": StepPic,
            "DatePic": DatePic,
            "TimePic": TimePic,
            "ChargePic": ChargePic,
            "MessagePic": MessagePic,
            "LikesPic": LikesPic,
            "CoverPic": CoverPic
        }

    BarPic = SummonBarPic(PicStruct)
    PicStruct["BarPic"] = BarPic
    return PicStruct


def SummonStepPic(PicDirA: str, step: int):
    assert step > 9999 and step < 100000, "Steps out of range"

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
        XCursor += SizeA[int(StepVar)] + 4

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
        XCursor += SizeB[int(MonthVar)] + 3

    BlankPic.paste(im=MonthPic, box=(XCursor, 0))
    XCursor += SizeStrMonth + 3

    for i in range(len(day)):
        DayVar = day[i]
        ToPastePicPath = path.join(PicDirB, f"{DayVar}.png")
        ToPastePic = Image.open(ToPastePicPath)
        BlankPic.paste(im=ToPastePic, box=(XCursor, 0))
        XCursor += SizeB[int(DayVar)] + 3

    BlankPic.paste(im=DayPic, box=(XCursor, 0))
    return BlankPic


def SummonDatePic2(PicDir8: str, date: str):
    date = date.split("-")
    month = str(int(date[0]))
    day = str(int(date[1]))

    BlankPicPath = path.join(PicDir8, "blank.png")
    BlankPic = Image.open(BlankPicPath)
    MonthPicPath = path.join(PicDir8, "M.png")
    MonthPic = Image.open(MonthPicPath)
    DayPicPaht = path.join(PicDir8, "D.png")
    DayPic = Image.open(DayPicPaht)
    SizeStrMonth = 36
    XCursor = 0

    # 将月份的数字从左到右依次粘贴
    for i in range(len(month)):
        MonthVar = month[i]
        ToPastePicPath = path.join(PicDir8, f"{MonthVar}.png")
        ToPastePic = Image.open(ToPastePicPath)
        BlankPic.paste(im=ToPastePic, box=(XCursor, 3))
        XCursor += 20 + 3

    XCursor += 5
    BlankPic.paste(im=MonthPic, box=(XCursor, 0))
    XCursor += SizeStrMonth + 10

    for i in range(len(day)):
        DayVar = day[i]
        ToPastePicPath = path.join(PicDir8, f"{DayVar}.png")
        ToPastePic = Image.open(ToPastePicPath)
        BlankPic.paste(im=ToPastePic, box=(XCursor, 3))
        XCursor += 20 + 3

    XCursor += 8
    BlankPic.paste(im=DayPic, box=(XCursor, 1))
    return BlankPic


def SummonTimePic(PicDir1: str):
    # 如果现在时间是13：18到18：03，采用0.png
    # 如果现在时间是18：03到20：01，采用1.png
    # 如果现在时间是20：01到22：47，采用2.png
    # 如果现在时间是22：47到23：59，采用3.png
    # 都不满足则采用3.png

    # 当前时间
    Time = datetime.now().strftime("%H:%M")
    # 13：18到18：03
    if Time >= "13:18" and Time <= "18:03":
        Time = 0
    # 18：03到20：01
    elif Time >= "18:03" and Time <= "20:01":
        Time = 1
    # 20：01到22：47
    elif Time >= "20:01" and Time <= "22:47":
        Time = 2
    # 22：47到23：59
    elif Time >= "22:47" and Time <= "23:59":
        Time = 3
    # 其他情况
    else:
        Time = 3
    TimePicPath = path.join(PicDir1, f"{Time}.png")
    TimePic = Image.open(TimePicPath)
    return TimePic


def SummonChargePic(PicDir2: str):
    # Bar
    Charge = randint(0, 1)
    ChargePicPath = path.join(PicDir2, f"{Charge}.png")
    ChargePic = Image.open(ChargePicPath)
    return ChargePic


def SummonMessagePic(PicDir3: str):
    # Bar
    Style = randint(0, 2)
    MessagePicPath = path.join(PicDir3, f"{Style}.png")
    MessagePic = Image.open(MessagePicPath)
    return MessagePic


def SummonLikesPic(PicDir4: str):
    Likes = randint(0, 1)
    LikesPicPath = path.join(PicDir4, f"{Likes}.png")
    LikesPic = Image.open(LikesPicPath)
    return LikesPic


def SummonCoverPic(PicDir5: str):
    Cover = randint(0, 2)
    CoverPicPath = path.join(PicDir5, f"{Cover}.png")
    CoverPic = Image.open(CoverPicPath)
    return CoverPic


def SummonBarPic(PicStruct: dict):
    # 生成一张1080*35的白色图片为Bar
    BarPic = Image.new(mode="RGB", size=(1080, 70), color=(237, 237, 237))
    TimePic = PicStruct["TimePic"]
    ChargePic = PicStruct["ChargePic"]
    MessagePic = PicStruct["MessagePic"]
    TimePosition = (69, 34)
    ChargePosition = (953, 30)
    MessagePosition = (190, 29)
    # 将TimePic、ChargePic、MessagePic粘贴到BarPic上的对应位置
    BarPic.paste(im=TimePic, box=TimePosition)
    BarPic.paste(im=ChargePic, box=ChargePosition)
    BarPic.paste(im=MessagePic, box=MessagePosition)
    # BarPic.show()
    return BarPic


def PastePic1(PicStruct: dict):
    PositionA = (198, 1582)
    PositionB = (821, 1388)
    Position1 = (69, 34)
    Position2 = (953, 30)
    Position3 = (190, 29)
    Position4 = (901, 1603)
    Position5 = (313, 258)
    Position6 = (0, 0)
    ScreenshotBlankPic = PicStruct["ScreenshotBlankPic"]
    ScreenshotBlankPic.paste(im=PicStruct["StepPic"], box=PositionA)
    ScreenshotBlankPic.paste(im=PicStruct["DatePic"], box=PositionB)
    # ScreenshotBlankPic.paste(im=PicStruct["TimePic"], box=Position1)
    # ScreenshotBlankPic.paste(im=PicStruct["ChargePic"], box=Position2)
    # ScreenshotBlankPic.paste(im=PicStruct["MessagePic"], box=Position3)
    ScreenshotBlankPic.paste(im=PicStruct["BarPic"], box=Position6)
    ScreenshotBlankPic.paste(im=PicStruct["LikesPic"], box=Position4)
    ScreenshotBlankPic.paste(im=PicStruct["CoverPic"], box=Position5)
    return ScreenshotBlankPic


def PastePic2(ScreenshotPic2, PicStruct: dict, Cursor: int, dateOffset: int):
    Position6 = (0, 0)
    Position7 = (186, 477 + 402 * Cursor)
    Position8 = (66, 1108 + 402 * (Cursor - 2))
    Position9 = (901, 493 + 402 * Cursor)
    if Cursor == 0:
        ScreenshotPic2.paste(im=PicStruct["BarPic"], box=Position6)
    ScreenshotPic2.paste(im=PicStruct["StepPic"], box=Position7)
    if Cursor > 1:
        DatePic2 = SummonDatePic2(
            Dir["TemplateDir8"],
            datetime.strftime(
                (datetime.now() - timedelta(days=Cursor + dateOffset)),
                "%m-%d"))
        ScreenshotPic2.paste(im=DatePic2, box=Position8)
    ScreenshotPic2.paste(im=PicStruct["LikesPic"], box=Position9)
    return ScreenshotPic2


def LoginWord(WordUrl):
    account = SportInfo["QQ"]
    password = SportInfo["password"]
    StudentInfo = SportInfo["StudentInfo"]

    # 登录
    driver = webdriver.Chrome(
        service=Service(r"D:\Python\ChromeDriver\chromedriver.exe"))
    driver.get(WordUrl)
    sleep(2)
    driver.find_element(by=By.CLASS_NAME, value='login-button').click()
    sleep(2)
    driver.find_element(by=By.ID, value="qq-tabs-title").click()  # 切换QQ登录
    driver.switch_to.frame("login_frame")
    try:
        driver.find_element(by=By.ID,
                            value=f"img_out_{account}").click()  # 尝试快捷登录
    except:
        driver.find_element(by=By.ID,
                            value="switcher_plogin").click()  # 切换手动登录
        sleep(2)
        driver.find_element(By.ID, value="u").send_keys(account)
        driver.find_element(By.ID, value="p").send_keys(password)
        driver.find_element(By.ID, value="login_button").click()
    sleep(2)

    driver.switch_to.parent_frame()

    # 填写信息
    InputArea = driver.find_elements(by=By.CSS_SELECTOR, value="textarea")
    for i in range(len(InputArea)):
        InputArea[i].send_keys(StudentInfo[i])

    SubmitButton = driver.find_element(by=By.XPATH,
                                       value='//*[@type="button"]')
    print(SubmitButton)

    while (1):
        try:
            driver.find_element(by=By.XPATH, value='//*[@alt="图片"]')
            print("Find Pics, wait for updating...")
            sleep(10)
            break
        except:
            pass

    SubmitButton.click()
    sleep(60)


def main():
    if len(argv) == 2:
        dateOffset = argv[1]
    elif len(argv) == 3:
        dateOffset = argv[1]
        Dir["ResultDir"] = argv[2]
    else:
        dateOffset = 0
        Dir["ResultDir"] = r"C:\Users\Administrator\桌面"
    dateOffset = int(dateOffset)
    SummonPic(dateOffset=dateOffset)
    # LoginWord(WordUrl=SportInfo["WordUrl"])


if __name__ == '__main__':
    main()
