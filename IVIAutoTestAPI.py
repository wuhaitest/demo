#!/bin/env python
# coding:utf-8
"""
#=============================================================================
#     FileName: IVIAutoTestAPI.py
#         Desc: 用户自定义API
#       Author: Thundersoft
#     HomePage: @_@"
#      History:
#=============================================================================
"""
# 基础工程引用，请勿修改
from _initGI import GI
# 基础API引用，请勿修改
from IVIAutoTest.src.api import API
import datetime,os
# 自定义API类
class IVIAutoTestAPIClass(API):
    """
    自定义API方法, 请参照模版方法在此类中添加自定义方法, 测试工具内置方法通过self即可访问
    """

    # 方法类注册器，用于将方法注册到系统当中
    @GI.common.apilog
    def test(self, test, desc):
        """
        类型:自定义
        说明:
            模版方法
        参数:
            test: 模版参数
            desc: 描述方法操作功能，更具体的展示在测试报告
        返回: -1, 描述： 失败
              0, 描述： 成功
              描述： 成功，并返回描述内容
        """
        # 调用系统内置sleep方法
        self.sleep(sleepTime=10)
        # 返回执行结果成功，并返回描述信息
        return 0, "Sleep 10 seconds success"

        # 返回执行结果失败，并返回描述信息
        # return -1, "Sleep 10 seconds failed"

        # 返回描述信息，并该方法始终为PASS，用于不需要断言的自定义方法
        # return "Sleep 10 seconds"

    @GI.common.apilog
    def clickAPPByName(self, appname, desc=''):
        """
        类型:自定义
        说明:
            模版方法
        参数:
            appname: app name
            desc: 描述方法操作功能，更具体的展示在测试报告
        返回: -1, 描述： 失败
              0, 描述： 成功
              描述： 成功，并返回描述内容
        """
        # 获取App text位置
        Navi=self.GetElementBy_text(text=appname, target="None", timeout="None")
        X=Navi.location.get('x')
        Y=Navi.location.get('y')
        # 点击App icon，进入该App
        self.ClickByPoint(x=X+100,y=Y-100,count="1",target="None")
        self.logInfo(appname+"已进入！")
        # 返回执行结果成功，并返回描述信息
        return 0
   
    @GI.common.apilog
    def clickButtonByOption(self,item):
        """
        类型:自定义
        说明:
            通过选项文本属性点击选项按钮
        参数:
            选项text
        返回: -1, 描述： 失败
              0, 描述： 成功
        """
        button = self.GetElementBy_xpath(xpath="//*[@text='{0}']/../../android.widget.ImageView[2]".format(item),target="None",timeout="None")
        self.ClickElement(button)
        return 0

######################################################################
    @GI.common.apilog
    def switchCruiseToNaviBy_point(self):
        """
        类型:自定义
        说明:
            模版方法
        返回: -1, 描述： 失败
              0, 描述： 成功
              描述： 成功，并返回描述内容
        """
        # 进入导航模式-选点
        self.Flick(start_x="1500",start_y="200",end_x="1300",end_y="200",target="None")
        self.ClickElementBy_xpath(xpath="//*[@resource-id='com.autonavi.amapauto:id/sftv_carryout']",target="None",timeout="None")
        self.ClickElementBy_text(text="去这里",target="None",timeout="None")
        self.ClickElementBy_xpath(xpath="//*[@resource-id='com.autonavi.amapauto:id/stv_startnavi_btn']",target="None",timeout="None")
        self.AssertElementBy_xpath(xpath="//*[@resource-id='com.autonavi.amapauto:id/siv_eagle_eye_map']",target="None",timeout="None")
        # 返回执行结果成功
        return 0

    @GI.common.apilog
    def switchNaviToCruiseBy_point(self):
        """
        类型:自定义
        说明:
            模版方法
        返回: -1, 描述： 失败
              0, 描述： 成功
              描述： 成功，并返回描述内容
        """
        #退出导航状态
        self.ClickByPoint(x="1837",y="130",count="1",target="None")
        self.ClickElementBy_text(text="结束导航",target="None",timeout="None")
        self.ClickElementBy_xpath(xpath="//*[@resource-id='com.autonavi.amapauto:id/stv_left']",target="None",timeout="None")
        self.ClickElementBy_text(text="回车位",target="None",timeout="None")
        self.AssertElementBy_xpath(xpath="//*[@resource-id='com.autonavi.amapauto:id/siv_arrow']",target="None",timeout="None")
        # 返回执行结果成功
        return 0

    @GI.common.apilog
    def switchNaviToCruiseBy_Search(self):
        """
        类型:自定义
        说明:
            由搜索目的地进入导航
        返回: -1, 描述： 失败
              0, 描述： 成功
              描述： 成功，并返回描述内容
        """
        #退出导航状态
        self.ClickByPoint(x="1837",y="130",count="1",target="None")
        self.ClickElementBy_text(text="结束导航",target="None",timeout="None")
        self.ClickElementBy_xpath(xpath="//*[@resource-id='com.autonavi.amapauto:id/stv_left']",target="None",timeout="None")
        self.AssertElementBy_xpath(xpath="//*[@resource-id='com.autonavi.amapauto:id/siv_arrow']",target="None",timeout="None")
        # 返回执行结果成功
        return 0

    @GI.common.apilog
    def input_searchDest(self, dest, desc=''):
        """
        类型:自定义
        说明:
        说明:
            模版方法
        参数:
            dest: 目的地
            desc: 描述方法操作功能，更具体的展示在测试报告
        返回: -1, 描述： 失败
              0, 描述： 成功
              描述： 成功，并返回描述内容
        """
        #点击输入框
        self.ClickElementBy_text(text="搜索目的地",target="None",timeout="None")
        #输入目的地
        i_dest=self.GetElementBy_text(text="请输入目的地",target="None",timeout="None")
        i_dest.clear
        self.sleep(sleepTime="1")
        i_dest.set_text(dest)
        #点击<搜索>按钮
        self.sleep(sleepTime="3")
        self.ClickByPoint(x="1825",y="130",count="1",target="None")
        #self.ClickByPoint(x="1760",y="658",count="1",target="None")
        #self.ClickElementBy_xpath(xpath="//*[@resource-id='com.autonavi.amapauto:id/cbt_search_btn']",target="None",timeout="1")
        #self.ClickElementBy_text(text="搜索",target="None",timeout="None")
        # 返回执行结果成功
        return 0
        
	@GI.common.apilog
    def gotoReminderLauncher_wh(self):
        """
        类型:自定义
        说明:快速进入Reminder主界面

        参数:无

        返回: -1, 描述： 失败
              0, 描述： 成功
              描述： 成功，并返回描述内容
        """
        # 调用系统内置sleep方法
        self.StartActivity(app_package="com.patac.hmi.calendar",app_activity="com.patac.hmi.calendar.MainActivity",target="None")
        self.sleep(sleepTime=3)
        return 0
#    @GI.common.apilog
#    def SwipeLeft(self,duration=400,n = ''):
#        """
#        类型:自定义
#        说明:左滑
#
#        参数:无
#
#        返回: -1, 描述： 失败
#              0, 描述： 成功S
#              描述： 成功，并返回描述内容
#        """
#        l = self.get_window_size()
#        x1 = l['width']*0.75
#        y1 = l['height']*0.5
#        X2 = l['height']*0.05
#        for i in range(n):
#            self.Swipe(start_x="",start_y="",end_x="",end_y="",duration="None",target="None")
#            self.sleep(sleepTime="0.4")
#        return 0

    @GI.common.apilog
    def gotoMediaLauncher_wh(self):
        """
        类型:自定义
        说明:快速进入Media主界面

        参数:无

        返回: -1, 描述： 失败
              0, 描述： 成功
              描述： 成功，并返回描述内容
        """
        # 调用系统内置sleep方法
        self.StartActivity(app_package="com.patac.hmi.mymedia",app_activity="com.patac.hmi.mymedia.SourceListActivity",target="None")
        self.sleep(sleepTime=3)
        return 0

    @GI.common.apilog
    def addReminder_wh(self,reminder=""):
        """
        类型:自定义
        说明:添加Reminder

        参数:reminder:添加的提醒

        返回: -1, 描述： 失败
              0, 描述： 成功
              描述： 成功，并返回描述内容
        """
        # 调用系统内置sleep方法
        self.StartActivity(app_package="com.patac.hmi.calendar",app_activity="com.patac.hmi.calendar.MainActivity",target="None")
        self.ClickElementBy_xpath(xpath="//*[@resource-id='com.patac.hmi.calendar:id/reminder_add']",target="None",timeout="None")
        self.sleep(sleepTime="1")
        self.VRSpeek(string=str(reminder),saveFile="")
        self.sleep(sleepTime="5")
        self.LogInfo("添加提醒成功")
        return 0
            
    @GI.common.apilog
    def delAllReminders_wh(self):
        """
        类型:自定义
        说明:删除Reminder

        参数:无

        返回: -1, 描述： 失败
              0, 描述： 成功
              描述： 成功，并返回描述内容
        """
        self.StartActivity(app_package="com.patac.hmi.calendar",app_activity="com.patac.hmi.calendar.MainActivity",target="None")
        self.sleep(sleepTime="1")
        count = 0
        for i in range(3):
            self.Swipe(start_x="1080",start_y="197",end_x="1192",end_y="197",duration="600",target="None")
            self.sleep(sleepTime="1")
            self.ClickElementBy_xpath(xpath="//*[@resource-id='com.patac.hmi.calendar:id/reminder_right_delete_imageview']",target="None",timeout="None")
            self.sleep(sleepTime="1")
            self.ClickElementBy_xpath(xpath="//*[@resource-id='com.patac.hmi.calendar:id/text_alertpop_left_button']",target="None",timeout="None")
            self.sleep(sleepTime="1")
            el = self.GetElementBy_xpath(xpath="//*[@resource-id='com.patac.hmi.calendar:id/mListView']/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]",target="None",timeout="None")
            if el:
                count +=1
            else:
                break
    @GI.common.apilog
    def setAvnDate_wh(self, year_set="",month_set="",day_set=""):
        """
        类型:自定义
        说明:自定义设置车机日期
            
        参数:
            year: 自定义年份
            month:自定义月份
            day:自定义天数
        返回: -1, 描述： 时间设置失败
              0, 描述： 时间设置成功
              描述： 成功，并返回描述内容
        """
        self.year_set = year_set
        self.ReportInfo("自定义年份 ："+str(year_set))
        self.month_set = month_set
        self.ReportInfo("自定义月份 ："+str(month_set))
        self.day_set =day_set
        self.ReportInfo("自定义日份 ："+str(day_set))
        self.ClickByPoint(x="1848",y="34",count="1",target="None")
        self.sleep(sleepTime="0.5")
        
        #获取车机时间
        tm = os.popen("adb shell date")
        avn_time = tm.read()
        self.ReportInfo("车机日期")
        time_list = avn_time.split( )
        year_avn = time_list[5]
        self.ReportInfo("车机年份："+str(year_avn))
        dic={
        'Jan':1,
        'Feb':2,
        'Mar':3,
        'Apr':4,
        'May':5,
        'Jun':6,
        'Jul':7,
        'Aug':8,
        'Sep':9,
        'Oct':10,
        'Nov':11,
        'Dec':12
        }
        month_avn = dic[time_list[1]]
        self.ReportInfo("车机月份："+str(month_avn))
        day_avn = time_list[2]
        self.ReportInfo("车机日份："+str(day_avn))
        year_counts = abs(int(year_set) - int(year_avn))
        self.ReportInfo("年份间隔："+str(year_counts)+"年")
        month_counts = abs(int(month_set) - month_avn)
        self.ReportInfo("月份间隔: "+str(month_counts)+"月")
        day_counts = abs(int(day_set) - int(day_avn))
        self.ReportInfo("日份间隔: "+str(day_counts)+"日")
        
        for i in range(year_counts):
            if year_avn < year_set:
                self.Swipe(start_x="293",start_y="312",end_x="293",end_y="262",duration="400",target="None")
                self.LogInfo("年份上滑"+str(year_counts)+"次")
                self.sleep(sleepTime="0.4")
            else:
                self.Swipe(start_x="293",start_y="262",end_x="293",end_y="312",duration="400",target="None")
                self.LogInfo("年份下滑"+str(year_counts)+"次")
                self.sleep(sleepTime="0.4")
        for i in range(month_counts):
            if int(month_avn) < int(month_set):
                self.Swipe(start_x="460",start_y="312",end_x="460",end_y="262",duration="400",target="None")
                self.LogInfo("月份上滑"+str(month_counts)+"次")
                self.sleep(sleepTime="0.4")
            else:
                self.Swipe(start_x="460",start_y="262",end_x="460",end_y="312",duration="400",target="None")
                self.LogInfo("月份下滑"+str(month_counts)+"次")
                self.sleep(sleepTime="0.4")
        for i in range(day_counts):
            if day_avn < day_set:
                self.Swipe(start_x="586",start_y="312",end_x="586",end_y="262",duration="400",target="None")
                self.LogInfo("日份上滑"+str(day_counts)+"次")
                self.sleep(sleepTime="0.4")
            else:
                self.Swipe(start_x="586",start_y="262",end_x="586",end_y="312",duration="400",target="None")
                self.LogInfo("日份下滑"+str(day_counts)+"次")
                self.sleep(sleepTime="0.4")
        self.ClickElementBy_xpath(xpath="//*[@resource-id='com.patac.hmi.setting:id/common_header_back']",target="None",timeout="None")
        
        return 0,"Date setting success!"

    @GI.common.apilog
    def setCurrentDate_wh(self):
        """
        类型:自定义
        说明:设置车机当前日期等于当前系统日期
            
        参数:无
            
        返回: -1, 描述： 时间设置失败
              0, 描述： 时间设置成功
              描述： 成功，并返回描述内容
        """
        #获取系统当前日期
        today_date=datetime.date.today()
        year_system = today_date.year
        self.LogInfo("获取系统年份： "+str(year_system))
        month_system = today_date.month
        self.LogInfo(string="获取系统月份: "+str(month_system))
        day_system = today_date.day
        self.LogInfo(string="获取系统日份: "+str(day_system))
        self.ClickByPoint(x="1848",y="34",count="1",target="None")
        self.sleep(sleepTime="0.5")
        
        #获取车机日期
        tm = os.popen("adb shell date")
        avn_time = tm.read()
        self.ReportInfo("车机日期")
        time_list = avn_time.split( )
        year_avn = time_list[5]
        self.ReportInfo("车机年份："+str(year_avn))
        dic={
        'Jan':1,
        'Feb':2,
        'Mar':3,
        'Apr':4,
        'May':5,
        'Jun':6,
        'Jul':7,
        'Aug':8,
        'Sep':9,
        'Oct':10,
        'Nov':11,
        'Dec':12
        }
        month_avn = dic[time_list[1]]
        self.ReportInfo("车机月份："+str(month_avn))
        day_avn = time_list[2]
        self.ReportInfo("车机日份："+str(day_avn))
        year_counts = abs(int(year_system) - int(year_avn))
        self.ReportInfo("年份间隔："+str(year_counts)+"年")
        month_counts = abs(int(month_system) - month_avn)
        self.ReportInfo("月份间隔: "+str(month_counts)+"月")
        day_counts = abs(int(day_system) - int(day_avn))
        self.ReportInfo("日份间隔: "+str(day_counts)+"日")
        #设置车机日期等于系统日期
        for i in range(year_counts):
            if int(year_avn) < int(year_system):
                self.Swipe(start_x="293",start_y="312",end_x="293",end_y="262",duration="400",target="None")
                self.LogInfo("年份上滑"+str(year_counts)+"次")
                self.sleep(sleepTime="0.4")
            else:
                self.Swipe(start_x="293",start_y="262",end_x="293",end_y="312",duration="400",target="None")
                self.LogInfo("年份下滑"+str(year_counts)+"次")
                self.sleep(sleepTime="0.4")
        for i in range(month_counts):
            if int(month_avn) < int(month_system):
                self.Swipe(start_x="460",start_y="312",end_x="460",end_y="262",duration="400",target="None")
                self.LogInfo("月份上滑"+str(month_counts)+"次")
                self.sleep(sleepTime="0.4")
            else:
                self.Swipe(start_x="460",start_y="262",end_x="460",end_y="312",duration="400",target="None")
                self.LogInfo("月份下滑"+str(month_counts)+"次")
                self.sleep(sleepTime="0.4")
        for i in range(day_counts):
            if int(day_avn) < int(day_system):
                self.Swipe(start_x="586",start_y="312",end_x="586",end_y="262",duration="400",target="None")
                self.LogInfo("日份上滑"+str(day_counts)+"次")
                self.sleep(sleepTime="0.4")
            else:
                self.Swipe(start_x="586",start_y="262",end_x="586",end_y="312",duration="400",target="None")
                self.LogInfo("日份下滑"+str(day_counts)+"次")
                self.sleep(sleepTime="0.4")
        self.ClickElementBy_xpath(xpath="//*[@resource-id='com.patac.hmi.setting:id/common_header_back']",target="None",timeout="None")
        
        return 0,"Date setting success!"

    @GI.common.apilog
    def getAvnDate_wh(self):
        """
        类型:自定义
        说明:获取车机系统日期
            
        参数:无
            
        返回: -1, 描述：失败
              0, 描述：成功
              描述： 成功，并返回描述内容
        """
        
        #获取车机日期
        tm = os.popen("adb shell date")
        avn_time = tm.read()
#        self.ReportInfo("车机日期")
        time_list = avn_time.split( )
        year_avn = time_list[5]
#        self.ReportInfo("车机年份："+str(year_avn))
        dic={
        'Jan':1,
        'Feb':2,
        'Mar':3,
        'Apr':4,
        'May':5,
        'Jun':6,
        'Jul':7,
        'Aug':8,
        'Sep':9,
        'Oct':10,
        'Nov':11,
        'Dec':12
        }
        month_avn = dic[time_list[1]]
#        self.ReportInfo("车机月份："+str(month_avn))
        day_avn = time_list[2]
#        self.ReportInfo("车机日份："+str(day_avn))
#        avn_date = str(year_avn) + "年" + str(month_avn) + "月" + str(day_avn) + "日"
        avn_date = '{0}年{1}月{2}日'.format(year_avn,month_avn,day_avn)
        return avn_date
        
    @GI.common.apilog
    def getSystemYearMonth_wh(self):
        """
        类型:自定义
        说明:获取车机系统年月
            
        参数:无
            
        返回: -1, 描述：失败
              0, 描述：成功
              描述： 成功，并返回描述内容
        """
        
        #获取车机日期
        tm = os.popen("adb shell date")
        avn_time = tm.read()
#        self.ReportInfo("车机日期")
        time_list = avn_time.split( )
        year_avn = time_list[5]
#        self.ReportInfo("车机年份："+str(year_avn))
        dic={
        'Jan':1,
        'Feb':2,
        'Mar':3,
        'Apr':4,
        'May':5,
        'Jun':6,
        'Jul':7,
        'Aug':8,
        'Sep':9,
        'Oct':10,
        'Nov':11,
        'Dec':12
        }
        month_avn = dic[time_list[1]]
#        self.ReportInfo("车机月份："+str(month_avn))
        day_avn = time_list[2]
#        self.ReportInfo("车机日份："+str(day_avn))
#        avn_date = str(year_avn) + "年" + str(month_avn) + "月" + str(day_avn) + "日"
        avn_yearmonth = '{} 年 {} 月'.format(year_avn,month_avn)
        return avn_yearmonth       

