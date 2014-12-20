#include <SoftwareSerial.h>
#include <Pirate4WD.h>

#define E1 5
#define M1 4
#define E2 6
#define M2 7
#define RxD 10
#define TxD 11
#define MinVoltage 125

SoftwareSerial btSerial(RxD, TxD);
Pirate4WD rover(E1, M1, E2, M2);

void setup()
{
  btSerial.flush();
  delay(500);
  btSerial.begin(9600);
  
  Serial.begin(9600);
  Serial.println("Finish Arduino setup.");
}

int getVoltage(char data)
{
  int gear = data - '0';
  int voltage = 0;
  if (gear != 0) voltage = map(gear, 1, 6, MinVoltage, 255);
  Serial.print("Voltage: ");
  Serial.println(voltage);
  return voltage;
}

void loop()
{
  char data;
  if (btSerial.available())
  {
    data = btSerial.read();
    Serial.println(data);
    if (data == 'B')
    {
      data = btSerial.read();
      Serial.println(data);
      if (data == '0') rover.stop();
    }
    if (data == 'V')
    {
      data = btSerial.read();
      Serial.println(data);
      int voltage = getVoltage(data);
      rover.setVoltage(voltage);
    }
    if (data == 'D')
    {
      data = btSerial.read();
      Serial.println(data);
      if (data == '1') rover.moveForward();
      if (data == '3') rover.moveRight();
      if (data == '5') rover.moveBack();
      if (data == '7') rover.moveLeft();
    }
  }
}
