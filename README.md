# DCEData
大连商品交易所日行情数据爬取工具

[Readme_en](README_en.md)

# 使用exe for Windows10
## 直接使用
- 双击自动爬取当日所有期货交易数据 
## 帮助
```shell script
 ./main.exe -h
```
```shell script
 ./main.exe --help
```
- 内容如下：
```shell script
--variety       -v
        默认：全部
        可选：豆一 豆二 豆粕 豆油 棕榈油 玉米 玉米淀粉 鸡蛋 粳米 纤维板 胶合板 生猪 聚乙烯 聚氯乙烯 聚丙烯 苯乙烯 焦炭 焦煤 铁矿石 乙二醇 液化石油气
--type  -t
        默认：期货
        可选：期货 期权
```
## 指定种类
```shell script
 ./main.exe -v 棕榈油
```
```shell script
 ./main.exe --variety 棕榈油
```
## 指定类别
```shell script
 ./main.exe -t 期权
```
```shell script
 ./main.exe --type 期权
```
## 指定日期
- 默认日期为当天
```shell script
 ./main.exe 20210108
```
## 指定日期范围
```shell script
 ./main.exe 20210104 20210108
```
- 放在同一个excel中
```shell script
 ./main.exe --one 20210104 20210108
```
- ***注意：*** `--one`需要放在日期范围之前
## 综合使用
采集2021年1月4日至2021年1月8日的棕榈油期权交易数据
```shell script
 ./main.exe -v 棕榈油 -t 期权 20210104 20210108
```


# 如何使用
## 帮助
```shell script
python main.py -h
```
```shell script
python main.py --help
```
- 内容如下：
```shell script
--variety       -v
        默认：全部
        可选：豆一 豆二 豆粕 豆油 棕榈油 玉米 玉米淀粉 鸡蛋 粳米 纤维板 胶合板 生猪 聚乙烯 聚氯乙烯 聚丙烯 苯乙烯 焦炭 焦煤 铁矿石 乙二醇 液化石油气
--type  -t
        默认：期货
        可选：期货 期权
```
## 指定种类
```shell script
python main.py -v 棕榈油
```
```shell script
python main.py --variety 棕榈油
```
## 指定类别
```shell script
python main.py -t 期权
```
```shell script
python main.py --type 期权
```
## 指定日期
```shell script
python main.py 20210108
```
## 指定日期范围
```shell script
python main.py 20210104 20210108
```
- 放在同一个excel中
```shell script
python main.py --one 20210104 20210108
```
- ***注意：*** `--one`需要放在日期范围之前
## 综合使用
采集2021年1月4日至2021年1月8日的棕榈油期权交易数据
```shell script
python main.py -v 棕榈油 -t 期权 20210104 20210108
```
