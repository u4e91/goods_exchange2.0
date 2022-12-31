#导入模块
import pymssql
#建立连接
#db = pymssql.connect('dinghy\SQLEXPRESS', 'sa', '1234', 'master')

list = {"面包": ["夹心草莓味面包", "学校", "136"],  "123": ["食品", "123", 123, "123", "123"], "包": ["夹心草莓包", "学校", "136"], "面": ["夹包", "学校", "136"]}
a = []
for i in list:
    a.append(i)
print(a)