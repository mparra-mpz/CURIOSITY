#include <SoftwareSerial.h>

#define RxD 10
#define TxD 11
#define RST 8
#define LED 7

SoftwareSerial BTSerial(RxD, TxD);

void setup()
{
  pinMode(LED, OUTPUT);
  pinMode(RST, OUTPUT);
  digitalWrite(RST, LOW);
  digitalWrite(LED, LOW);
  digitalWrite(RST, HIGH);
  delay(500);
  BTSerial.flush();
  delay(500);
  BTSerial.begin(9600);
}

void loop()
{
  if (BTSerial.available() > 0)
  {
    String data = "";
    char auxiliar;
    while (BTSerial.available() > 0)
    {
      auxiliar = BTSerial.read();
      data += auxiliar;
    }
    if (data == "D1" or data == "D3") digitalWrite(LED, HIGH);
    else if (data == "D5" or data == "D7") digitalWrite(LED, LOW);
  }
}
