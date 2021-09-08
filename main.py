# -*- coding:utf-8 -*-
from datetime import datetime
from datetime import timedelta

import requests
from lxml import etree
import xlwt
import os
import getopt
import sys
import time

varietyDict = {
    "全部": "all",
    "豆一": "a",
    "豆二": "b",
    "豆粕": "m",
    "豆油": "y",
    "棕榈油": "p",
    "玉米": "c",
    "玉米淀粉": "cs",
    "鸡蛋": "jd",
    "粳米": "rr",
    "纤维板": "fb",
    "胶合板": "bb",
    "生猪": "lh",
    "聚乙烯": "l",
    "聚氯乙烯": "v",
    "聚丙烯": "pp",
    "苯乙烯": "eb",
    "焦炭": "j",
    "焦煤": "jm",
    "铁矿石": "i",
    "乙二醇": "eg",
    "液化石油气": "pg"
}
vVarietyDict = {v: k for k, v in varietyDict.items()}
tradeTypeDict = {
    "期货": 0,
    "期权": 1
}


def get_daily(variety, trade_type, year="", month="", day=""):
    data = {
        "dayQuotes.variety": variety,
        "dayQuotes.trade_type": trade_type,
        "year": year,
        "month": month,
        "day": day
    }
    print("requesting: " + year + "." + month + "." + day + "_" + variety)
    pageRequest = requests.post("http://www.dce.com.cn/publicweb/quotesdata/dayQuotesCh.html", data=data)
    pageRequest.encoding = pageRequest.apparent_encoding

    if pageRequest.status_code != 200:
        print("error while get html (code:" + str(pageRequest.status_code) + ")")
        return

    date = pageRequest.text[pageRequest.text.index("日期") + 3:pageRequest.text.index("日期") + 11]
    # print("查询日期：" + date)
    if "暂无数据" in pageRequest.text:
        print(date + ": 暂无数据")
        return

    html = etree.HTML(pageRequest.text)
    data = html.xpath("//div[@class='dataArea']/table/tr")
    # print("data:  " + str(data))

    name = date + "_" + vVarietyDict[variety] + "_" + str(trade_type)
    print("writing xml:" + name + ".xls")
    workbook = xlwt.Workbook(encoding="utf-8-sig")
    sheet = workbook.add_sheet(name)
    row = 0
    for tr in data:
        col = 0
        head = tr.xpath(".//th/text()")
        data = tr.xpath(".//td/text()")
        if len(head) > 0:
            for th in head:
                sheet.write(row, col, th)
                col = col + 1
                # print(th, end="\t")
        else:
            for td in data:
                sheet.write(row, col, td)
                col = col + 1
                # print(td.strip(), end="\t")
        # print("")
        row = row + 1
    if not os.path.exists("./data"):
        os.makedirs("./data")
    workbook.save("./data/" + name + ".xls")


def get_in_one(variety, trade_type, start, end):
    # 放在一个工作表里
    workbook = xlwt.Workbook(encoding="utf-8-sig")
    sheet = workbook.add_sheet(str(start) + "_" + str(end))
    print("writing xml:" + str(start) + "_" + str(end) + ".xls")
    row = 0
    for d in gen_dates(start, (end - start).days):
        year = str(d.year)
        month = str(d.month - 1)
        day = str(d.day)
        data = {
            "dayQuotes.variety": variety,
            "dayQuotes.trade_type": trade_type,
            "year": year,
            "month": month,
            "day": day
        }
        print("requesting: " + year + "." + month + "." + day + "_" + variety)
        pageRequest = requests.post("http://www.dce.com.cn/publicweb/quotesdata/dayQuotesCh.html", data=data)
        pageRequest.encoding = pageRequest.apparent_encoding

        if pageRequest.status_code != 200:
            print("error while get html (code:" + str(pageRequest.status_code) + ")")
            continue

        date = pageRequest.text[pageRequest.text.index("日期") + 3:pageRequest.text.index("日期") + 11]
        # print("查询日期：" + date)
        if "暂无数据" in pageRequest.text:
            print(date + ": 暂无数据")
            continue

        html = etree.HTML(pageRequest.text)
        data = html.xpath("//div[@class='dataArea']/table/tr")
        # print("data:  " + str(data))

        name = date + "_" + vVarietyDict[variety] + "_" + str(trade_type)
        for tr in data:
            col = 0
            head = tr.xpath(".//th/text()")
            data = tr.xpath(".//td/text()")
            if len(head) > 0:
                for th in head:
                    sheet.write(row, col, th)
                    col = col + 1
                    # print(th, end="\t")
            else:
                for td in data:
                    sheet.write(row, col, td)
                    col = col + 1
                    # print(td.strip(), end="\t")
            # print("")
            row = row + 1
    if not os.path.exists("./data"):
        os.makedirs("./data")
    workbook.save("./data/" + str(start) + "_" + str(end) + ".xls")


def gen_dates(b_date, days):
    day = timedelta(days=1)
    for i in range(days):
        yield b_date + day * i


if __name__ == "__main__":
    inputVariety = "all"
    inputType = 0
    inone = False
    opts, args = getopt.getopt(sys.argv[1:], "hv:t:", ["help", "variety=", "type=", "one"])
    for opts, arg in opts:
        if opts == "-h" or opts == "--help":
            print("--variety\t-v\n"
                  "\t默认：全部\n\t可选：豆一 豆二 豆粕 豆油 棕榈油 玉米 玉米淀粉 鸡蛋 粳米 纤维板 胶合板 生猪 聚乙烯 聚氯乙烯 聚丙烯 苯乙烯 焦炭 焦煤 铁矿石 乙二醇 液化石油气")
            print("--type\t-t\n"
                  "\t默认：期货\n\t可选：期货 期权")
            exit(0)
        elif opts == "-v" or opts == "--variety":
            if arg not in varietyDict.keys():
                print(arg + "不在可选项列表中")
                exit(0)
            inputVariety = varietyDict[arg]
        elif opts == "-t" or opts == "--type":
            if arg not in tradeTypeDict.keys():
                print(arg + "不在可选项列表中")
                exit(0)
            inputType = tradeTypeDict[arg]
        elif opts == "--one":
            inone = True

    if len(args) == 0:
        get_daily(inputVariety, inputType)
    elif len(args) == 1:
        dateTime = None
        try:
            dateTime = datetime.strptime(args[0], "%Y%m%d")
        except:
            print("日期格式出错：" + args[0])
            exit(0)
        get_daily(inputVariety, inputType, str(dateTime.year), str(dateTime.month - 1), str(dateTime.day))
    elif len(args) == 2:
        startTime = datetime.now()
        try:
            startTime = datetime.strptime(args[0], "%Y%m%d")
        except:
            print("日期格式出错：" + args[0])
            exit(0)
        endTime = datetime.now()
        try:
            endTime = datetime.strptime(args[1], "%Y%m%d")
        except:
            print("日期格式出错：" + args[1])
            exit(0)
        if inone:
            get_in_one(inputVariety, inputType, startTime.date(), endTime.date())
        else:
            for d in gen_dates(startTime.date(), (endTime.date() - startTime.date()).days):
                get_daily(inputVariety, inputType, str(d.year), str(d.month - 1), str(d.day))
