执行步骤：
1、topic话题:"DubmicLog",和bootstrap_servers ip找开发要

2、auto_offset_reset = earliest，就是从 Topic 的头往后读 or latest就是忽略之前的数据，从程序运行以后，新来的数据开始

3、group_id 名称随意写,如果有多少测试消费时，名字不能一样

4、在终端，进入到文件存在目录下，输入： python3 文件名称

5、运行
