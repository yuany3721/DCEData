# DCEData
大连商品交易所日行情数据爬取工具

# Usage
## Help
```shell script
python main.py -h
```
```shell script
python main.py --help
```
- Here is the help
```shell script
--variety       -v
        默认：全部
        可选：豆一 豆二 豆粕 豆油 棕榈油 玉米 玉米淀粉 鸡蛋 粳米 纤维板 胶合板 生猪 聚乙烯 聚氯乙烯 聚丙烯 苯乙烯 焦炭 焦煤 铁矿石 乙二醇 液化石油气
--type  -t
        默认：期货
        可选：期货 期权
```
## Specify Variety
```shell script
python main.py -v 棕榈油
```
```shell script
python main.py --variety 棕榈油
```
## Specify Type
```shell script
python main.py -t 期权
```
```shell script
python main.py --type 期权
```
## Specify Date
```shell script
python main.py 20210108
```
## Specify Date Range
```shell script
python main.py 20210104 20210108
```
- put in a single excel
```shell script
python main.py --one 20210104 20210108
```
- ***WARNING：*** `--one`should be placed in front of date range
## Multiple use
Collect palm oil option transaction data from January 4, 2021 to January 8, 2021
```shell script
python main.py -v 棕榈油 -t 期权 20210104 20210108
```