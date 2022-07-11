import logging
import random
import smtplib
import re


import dns.resolver

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s [line:%(lineno)d] - %(levelname)s: %(message)s')

logger = logging.getLogger()
email_list = []


def fetch_mx(host):
    '''
    解析服务邮箱
    :param host:
    :return:
    '''
    try:
        logger.info('正在查找邮箱服务器')
        answers = dns.resolver.query(host, 'MX')
        res = [str(rdata.exchange)[:-1] for rdata in answers]
        logger.info('查找结果为：%s' % res)
    except:
        logger.info('查找邮箱服务器异常')
        res = None
    return res



def verify_istrue(email):
    '''
    :param email:
    :return:
    '''
    email_list = []
    email_obj = {}
    final_res = {}
    if isinstance(email, str) or isinstance(email, bytes):
        email_list.append(email)
    else:
        email_list = email

    for em in email_list:
        name, host = em.split('@')
        if email_obj.get(host):
            email_obj[host].append(em)
        else:
            email_obj[host] = [em]
    print(email_obj)
    for key in email_obj.keys():
        try:
            host = random.choice(fetch_mx(key))
            logger.info('正在连接服务器...：%s' % host)
            s = smtplib.SMTP(host, timeout=10)

            for need_verify in email_obj[key]:
                helo = s.docmd('HELO chacuo.net')
                logger.debug(helo)

                send_from = s.docmd('MAIL FROM:<3121113@chacuo.net>')
                logger.debug(send_from)
                send_from = s.docmd('RCPT TO:<%s>' % need_verify)
                logger.debug(send_from)
                if send_from[0] == 250 or send_from[0] == 451:
                    final_res[need_verify] = "存在"  # 存在
                elif send_from[0] == 550:
                    final_res[need_verify] = "不存在"  # 不存在
                else:
                    final_res[need_verify] = "认证失败"  # 未知
            s.close()
        except:
            logger.info('连接服务器失败：%s' % host)
            for m in email_obj[key]:
                final_res[m] = "连接邮箱服务器失败"

    return final_res


if __name__ == '__main__':

    mails = []

    # open file and read the content in a list
    with open('targets.txt', 'r') as filehandle:
        for line in filehandle:
            # remove linebreak which is the last character of the string

            pattern = re.compile(r'\s+')
            currentPlace=re.sub(pattern,'',line)
            pattern_mail = r'^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$'
            if re.match(pattern_mail, currentPlace):
                mails.append(currentPlace)
            else:
                print(currentPlace + '\t邮箱格式异常')


    final_list = verify_istrue(mails)

    print("输出结果为：")

    for key, value in final_list.items():
        print(key + '\t' + value)

