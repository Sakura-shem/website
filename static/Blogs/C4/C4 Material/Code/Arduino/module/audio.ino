const int sound_pin = A0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int value = analogRead(sound_pin);//对模拟值进行数字量化
  value = map(value,0,1023,0,1000);
  delay(100);
  Serial.println(value);//数据给到 python com3串口
}
