#include <SoftwareSerial.h>
#include <Pirate4WD.h>

#define E1 5
#define M1 4
#define E2 6
#define M2 7
#define ENB 8
#define RxD 10
#define TxD 11
#define MinVoltage 150
#define Delay 108

SoftwareSerial btSerial(RxD, TxD);
Pirate4WD rover(E1, M1, E2, M2);

void setup()
{
  pinMode(ENB, OUTPUT);
  digitalWrite(ENB, LOW);
  delay(500);
  digitalWrite(ENB, HIGH);
  btSerial.flush();
  delay(500);
  btSerial.begin(9600);
}

int getVoltage(char data)
{
  int gear = data - '0';
  int voltage = 0;
  if (gear != 0) voltage = map(gear, 1, 6, MinVoltage, 255);
  return voltage;
}

void loop()
{
  char data;
  if (btSerial.available())
  {
    delayMicroseconds(Delay);
    data = btSerial.read();
    if (data == 'B')
    {
      delayMicroseconds(Delay);
      data = btSerial.read();
      if (data == '0') rover.stop();
    }
    if (data == 'V')
    {
      delayMicroseconds(Delay);
      data = btSerial.read();
      int voltage = getVoltage(data);
      rover.setVoltage(voltage);
    }
    if (data == 'D')
    {
      delayMicroseconds(Delay);
      data = btSerial.read();
      if (data == '1') rover.moveForward();
      if (data == '3') rover.moveRight();
      if (data == '5') rover.moveBack();
      if (data == '7') rover.moveLeft();
    }
  }
}
