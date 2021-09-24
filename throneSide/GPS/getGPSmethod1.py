import serial #导入serial模块

ser = serial.Serial("/dev/ttyUSB0",9600)#打开串口，存放到ser中，/dev/ttyUSB0是端口名，9600是波特率

while True:
    line = str(str(ser.readline())[2:])  # readline()是用于读取整行
    # print(line)
    # 这里如果从头取的话，就会出现b‘，所以要从第三个字符进行读取
    if line.startswith('$GPGGA'):
    #我这里用的GPGGA，有的是GNGGA
        #print('接收的数据：' + str(line))
        line = str(line).split(',')  # 将line以“，”为分隔符
        jing = float(line[4][:3]) + float(line[4][3:])/60
        # 读取第5个字符串信息，从0-2为经度，即经度为116，再加上后面的一串除60将分转化为度
        wei = float(line[2][:2]) + float(line[2][2:])/60
        # 纬度同理
        print("经度:",jing)
        print("维度:",wei)