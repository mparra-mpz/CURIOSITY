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

SoftwareSerial btSerial(RxD, TxD);
Pirate4WD rover(E1, M1, E2, M2);

void setup()
{
  pinMode(ENB, OUTPUT);
  digitalWrite(ENB, LOW);
  digitalWrite(ENB, HIGH);
  delay(500);
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
  if (btSerial.available() > 0)
  {
    String data = "";
    char auxiliar;
    while (btSerial.available() > 0)
    {
      auxiliar = btSerial.read();
      data += auxiliar;
    }
    if (data == "D1") rover.moveForward();
    if (data == "D3") rover.moveRight();
    if (data == "D5") rover.moveBack();
    if (data == "D7") rover.moveLeft();
    if (data.charAt(0) == 'V')
    {
      int voltage = getVoltage(data.charAt(1));
      rover.setVoltage(voltage);
    }
  }
}
