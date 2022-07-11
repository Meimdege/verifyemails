# verifyemail

Python在线验证邮箱真实性，支持批量验证，支持全部域名邮箱，支持全部域名邮箱，支持全部域名邮箱，支持全部域名邮箱。

将邮箱放入target.txt，执行python verifyemail.py。

```bash
{'qq.com': ['in.shi@qq.com'], 'chacuo.net': ['312111ssa3@chacuo.net'], '163.com': ['in.shi@163.com'], '52pojie.com': ['in.shi@52pojie.com'], 'sas.com': ['sadada@sas.com']}
2022-07-11 10:09:21,120 - verifyemail.py [line:23] - INFO: 正在查找邮箱服务器
verifyemail.py:24: DeprecationWarning: please use dns.resolver.resolve() instead
  answers = dns.resolver.query(host, 'MX')
2022-07-11 10:09:23,129 - verifyemail.py [line:26] - INFO: 查找结果为：['mx3.qq.com', 'mx1.qq.com', 'mx2.qq.com']
2022-07-11 10:09:23,129 - verifyemail.py [line:57] - INFO: 正在连接服务器...：mx3.qq.com
2022-07-11 10:09:23,317 - verifyemail.py [line:62] - DEBUG: (250, b'newxmmxszb1-11.qq.com-9.138.40.217-29341705\nSIZE 73400320\nOK')
2022-07-11 10:09:23,379 - verifyemail.py [line:65] - DEBUG: (250, b'OK')
2022-07-11 10:09:23,473 - verifyemail.py [line:67] - DEBUG: (250, b'OK')
2022-07-11 10:09:23,473 - verifyemail.py [line:23] - INFO: 正在查找邮箱服务器
2022-07-11 10:09:25,500 - verifyemail.py [line:26] - INFO: 查找结果为：['mx.chacuo.net']
2022-07-11 10:09:25,500 - verifyemail.py [line:57] - INFO: 正在连接服务器...：mx.chacuo.net
2022-07-11 10:09:25,641 - verifyemail.py [line:62] - DEBUG: (250, b'web1905')
2022-07-11 10:09:25,678 - verifyemail.py [line:65] - DEBUG: (250, b'Ok')
2022-07-11 10:09:25,912 - verifyemail.py [line:67] - DEBUG: (250, b'Ok')
2022-07-11 10:09:25,927 - verifyemail.py [line:23] - INFO: 正在查找邮箱服务器
2022-07-11 10:09:27,953 - verifyemail.py [line:26] - INFO: 查找结果为：['163mx00.mxmail.netease.com', '163mx02.mxmail.netease.com', '163mx03.mxmail.netease.com', '163mx01.mxmail.netease.com']
2022-07-11 10:09:27,953 - verifyemail.py [line:57] - INFO: 正在连接服务器...：163mx03.mxmail.netease.com
2022-07-11 10:09:28,156 - verifyemail.py [line:62] - DEBUG: (250, b'OK')
2022-07-11 10:09:29,220 - verifyemail.py [line:65] - DEBUG: (250, b'Mail OK')
2022-07-11 10:09:29,246 - verifyemail.py [line:67] - DEBUG: (250, b'Mail OK')
2022-07-11 10:09:29,246 - verifyemail.py [line:23] - INFO: 正在查找邮箱服务器
2022-07-11 10:09:31,273 - verifyemail.py [line:28] - INFO: 查找邮箱服务器异常
2022-07-11 10:09:31,273 - verifyemail.py [line:76] - INFO: 连接服务器失败：163mx03.mxmail.netease.com
2022-07-11 10:09:31,273 - verifyemail.py [line:23] - INFO: 正在查找邮箱服务器
2022-07-11 10:09:33,289 - verifyemail.py [line:26] - INFO: 查找结果为：['sas-com.mail.protection.outlook.com']
2022-07-11 10:09:33,289 - verifyemail.py [line:57] - INFO: 正在连接服务器...：sas-com.mail.protection.outlook.com
2022-07-11 10:09:33,990 - verifyemail.py [line:62] - DEBUG: (250, b'BN1NAM02FT048.mail.protection.outlook.com Hello [58.34.35.86]')
2022-07-11 10:09:34,209 - verifyemail.py [line:65] - DEBUG: (250, b'2.1.0 Sender OK')
2022-07-11 10:09:34,427 - verifyemail.py [line:67] - DEBUG: (550, b'5.7.606 Access denied, banned sending IP [58.34.35.86]. To request removal from this list please visit https://sender.office.com/ and follow the directions. For more information please go to  http://go.microsoft.com/fwlink/?LinkID=526655 AS(1430) [BN1NAM02FT048.eop-nam02.prod.protection.outlook.com]')
输出结果为：
in.shi@qq.com   存在
312111ssa3@chacuo.net   存在
in.shi@163.com  存在
in.shi@52pojie.com      连接邮箱服务器失败
sadada@sas.com  不存在
```



参考：https://github.com/Tzeross/verifyemail

增加了一些错误处理。