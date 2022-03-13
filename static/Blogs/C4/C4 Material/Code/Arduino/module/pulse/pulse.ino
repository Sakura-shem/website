//  Variables
int PulseSensorPurplePin = 1;   // Pulse Sensor PURPLE WIRE connected to ANALOG PIN 0
int Signal;                     // holds the incoming raw data. Signal value can range from 0-1024
int Threshold = 550;            // Determine which Signal to "count as a beat", and which to ingore.
int i;
// The SetUp Function:
void setup() {
  Serial.begin(9600);         // Set's up Serial Communication at certain speed.
}

// The Main Loop Function
void loop() {
  Signal = analogRead(PulseSensorPurplePin);  // Read the PulseSensor's value.
  Serial.println(Signal);                     // Send the Signal value to Serial Plotter.
  if(Signal > Threshold){i = i+1;}            // If the signal is above "550", then "turn-on" Arduino's on-Board LED.
  delay(10);
}
