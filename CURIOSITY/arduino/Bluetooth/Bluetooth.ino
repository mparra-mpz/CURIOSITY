
#include <SoftwareSerial.h>

#define RxD 10
#define TxD 11
#define RST 9
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
  
  Serial.begin(9600);
  Serial.println("Start debugging");
}

void loop()
{
  char data;
  if (BTSerial.available())
  {
    data = BTSerial.read();
    Serial.println(data);
    if (data == 'D')
    {
      data = BTSerial.read();
      Serial.println(data);
      if (data == '1') digitalWrite(LED, HIGH);
      if (data == '3') digitalWrite(LED, HIGH);
      if (data == '5') digitalWrite(LED, LOW);
      if (data == '7') digitalWrite(LED, LOW);
    } else {
      if (data == 'V')
      {
        int gear = BTSerial.read() - '0';
        Serial.println(gear);
        if (gear > 3) digitalWrite(LED, HIGH);
        if (gear < 3) digitalWrite(LED, LOW);
      }
    }
  }
}