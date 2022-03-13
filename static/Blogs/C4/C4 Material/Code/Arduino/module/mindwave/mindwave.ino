/*
 通过UART串口显示信号值、注意力及放松度的值
 */
#define DEBUGOUTPUT 0

//校验相关变量
int   generatedChecksum = 0;
byte  checksum = 0; 

//接收数据长度和数据数组
byte  payloadLength = 0;
byte  payloadData[32] = {0};//总共接收32个自己的数据

//需要读取的信息变量
byte signalquality = 0;//信号质量
byte attention = 0;    //注意力值
byte meditation = 0;   //放松度值

//初始化
void setup() 
{
  Serial.begin(57600); 
}

//从串口读取一个字节数据
byte ReadOneByte() 
{
  int ByteRead;
  while(!Serial.available());
  ByteRead = Serial.read();
  return ByteRead;//返回读到的字节
}

//读取串口数据
void read_serial_data()
{
    //寻找数据包起始同步字节，2个
    if(ReadOneByte() == 0xAA)//先读一个
    {
      if(ReadOneByte() == 0xAA)//读第二个
      {
        payloadLength = ReadOneByte();//读取第三个，数据包字节的长度
        if(payloadLength == 0x20)//如果接收到的是大包数据才继续读取，小包数据则舍弃不读取
        {
          generatedChecksum = 0; //校验变量清0       
          for(int i = 0; i < payloadLength; i++)//连续读取32个字节
          {  
            payloadData[i] = ReadOneByte();//读取指定长度数据包中的数据
            generatedChecksum += payloadData[i];//计算数据累加和
          }         
          checksum = ReadOneByte();//读取校验字节  
          //校验
          generatedChecksum = (~generatedChecksum)&0xff;       
          //比较校验字节
          if(checksum == generatedChecksum)//数据接收正确，继续处理 
          {    
            signalquality = 0;//信号质量变量
            attention = 0;    //注意力值变量
            //赋值数据
            signalquality = payloadData[1];//信号值      
            attention = payloadData[29];//注意力值
            meditation = payloadData[31];//放松度值
            #if !DEBUGOUTPUT         
            //打印信号质量
            Serial.print("SignalQuality: ");
            Serial.print(signalquality, DEC);
            //打印注意力值
            Serial.print("Attation: ");
            Serial.print(attention, DEC);
            //打印放松度值
            Serial.print("Meditation: ");
            Serial.print(meditation, DEC);
            //换行
            Serial.print("\n");       
            #endif              
          } 
        } 
      }
    }
}

//主循环
void loop() 
{
  read_serial_data();//读取串口数据 
}
