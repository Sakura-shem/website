//00--sound_value
//01--pulse_value

//  Variables
const int sound_pin = A0;
int PulseSensorPurplePin = 1;   // Pulse Sensor PURPLE WIRE connected to ANALOG PIN 0
int sound_value;
int pulse_value;
int Threshold = 550;            // Determine which Signal to "count as a beat", and which to ingore.
int i;

void setup() {
  Serial.begin(9600);
}

// The Main Loop Function
void loop() {
  sound_value = analogRead(sound_pin);
  sound_value = map(sound_value,0,1023,0,1000);
  pulse_value = analogRead(PulseSensorPurplePin);
  Serial.println(pulse_value*100000 + sound_value);//数据给到串口【Serial Plotter.】
  if(pulse_value > Threshold){i = i+1;}
  delay(10);//【延时】  
}
