# 公众号配置
# 公众号appId
app_id = "wx387fd1cc4b27a989"
# 公众号appSecret
app_secret = "fc20353ebb4def3f2912e887cb06d51b"
# 模板消息id
# 每日消息
#template_id1 = "X3cPJP9EI2an40lXlPZuYtk4MmhF9aYfnZ0LV9rM-L8"
template_id1 = "X3cPJP9EI2an40lXlPZuYtk4MmhF9aYfnZ0LV9rM-L8"
template_id1_1 = "U9WYGAuJaBAYnEZT7oIk0zCYJ1T7Tgw78Nej6K9T5Qs"
# 课程消息,上课提醒
template_id2 = "loe1yHWr************************************"
# 晚安心语
template_id3 = "A0FED6ucHRoMboK4I49tWlgUDH6qKTeZhRXqqncKYfw"
# 接收公众号消息的微信号
# 这是openid
user = ["oWX9x5wYWLQSCgdwHpbwiyLSXw8I","oWX9x58k81Me-RlkSSfJEhPhQNEw","oWX9x520AcC7l3YAYqgYVfqOzDRs"]
#user = ["oWX9x5wYWLQSCgdwHpbwiyLSXw8I","oWX9x520AcC7l3YAYqgYVfqOzDRs"]

# 信息配置
# 所在省份
province = "江西"
province2 = "湖北"
# 所在城市
city = "景德镇"
city2 = "武汉"
# 生日，如果月份或者日期小于10，直接用对应的数字即可，例如1997-1-1，---------倒计时
birthday = "2001-7-22"
birthday2 = "2002-10-24"
# 在一起的日子，格式同上------------计时器
love_date = "2021-3-1"
# 天行数据晚安心语 key
good_Night_Key = "ff65b66466d77f098310cdb4a99f05fc"
# -------------------------------------------------------------------------
# 设置学期第一周开始日期
year = 2023
month = 1
day = 20
# 每日推送时间
post_Time = "19:35:00"
# 晚安心语及第二天课程推送时间
good_Night_Time = "14:59:00"

# 模板 1：每日提醒模板
# 本周是开学的第: {{weeks.DATA}} 周
# 今天是: {{date.DATA}}
# 城市： {{city.DATA}}
# 天气： {{weather.DATA}}
# 最低气温: {{min_temperature.DATA}}
# 最高气温: {{max_temperature.DATA}}
# 今天是破壳日的第: {{love_day.DATA}} 天
# 距离开学还有: {{birthday.DATA}} 天
# ----------------今日课程----------------
# 第一讲: {{firstClass.DATA}}
# 第二讲: {{secondClass.DATA}}
# 第三讲: {{thirdClass.DATA}}
# 第四讲: {{fourthClass.DATA}}
# 第五讲: {{fifthClass.DATA}}
# 第六讲: {{sixthClass.DATA}}

# 模板 2 课程单推
# 课程信息: {{classInfo.DATA}}

# 模板 3 晚安心语推送和第二天课程推送
# {{goodNight.DATA}}
# ----------------明日课程----------------
# 明天是: {{week.DATA}}
# 第一讲: {{firstClass.DATA}}
# 第二讲: {{secondClass.DATA}}
# 第三讲: {{thirdClass.DATA}}
# 第四讲: {{fourthClass.DATA}}
# 第五讲: {{fifthClass.DATA}}
# 第六讲: {{sixthClass.DATA}}
