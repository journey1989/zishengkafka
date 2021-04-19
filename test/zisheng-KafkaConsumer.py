import sys,time,json,threading
from kafka import KafkaConsumer

'''
执行步骤：
1、topic话题:"DubmicLog",和bootstrap_servers ip找开发要
2、auto_offset_reset = earliest，就是从 Topic 的头往后读 or latest就是忽略之前的数据，从程序运行以后，新来的数据开始
3、group_id 名称随意写,如果有多少测试消费时，名字不能一样
4、在终端，进入到文件存在目录下，输入： python3 文件名称 udid（自己查）
5、运行
'''


def start_consume(*args):
    consumer = KafkaConsumer(
        "DubmicLog",
        bootstrap_servers=[
            "192.168.115.66:9092",
            "192.168.115.67:9092",
            "192.168.115.68:9092",
            "192.168.115.69:9092",
            "192.168.115.70:9092"
        ],
        auto_offset_reset="latest",
        enable_auto_commit=False,
        group_id='Dub8888',
    )
    for msg in consumer:
        content = json.loads(msg.value.decode())
        #print(content)
        message = content['message']
        p = json.loads(message)

        try:
            if p['h']['appId'] == 30000:
                 continue

            elif p['h']['appId'] == 40000 and p['p']['env'] == 'online':
                timeArray = time.localtime(p['ct'] / 1000)
                cttime = time.strftime("%y-%m-%d %H:%M:%S", timeArray)
                timeArrays = time.localtime(p['st'] / 1000)
                sttime = time.strftime("%y-%m-%d %H:%M:%S", timeArrays)
                print('**************************************************************************************')
                print('事件发生时间：', cttime)
                print('事件写入时间：', sttime)
                if p['h']['_e'] != "40003" and p['h']['_e'] != "40002":
                    print('当前测试设备：', p['p']['os'], '-', p['p']['dm'])
                print('当前测试环境：', p['p']['env'])
                print('当前测试事件ID：', p['h']['_e'])
                print('当前测试事件行为：', p['h']['_a'])
                print('当前测试appID:', p['h']['appId'])
                print('当前测试D参数消息体:', p['d'])
                print('测试结果为h全部参数：', p['h'])
                print('**************************************************************************************', '\n ')
                print('\n')

        except Exception as e:
            print(e)

def run_threading():
    t1 = threading.Thread(target=start_consume, args=("t1",))
    t1.start()


if __name__ == "__main__":
    run_threading()
    start_consume()
