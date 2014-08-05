#include <SoftwareSerial.h>
 
#define M2 4
#define E2 5
#define E1 6
#define M1 7
#define RxD 10
#define TxD 11

SoftwareSerial BTSerial(RxD, TxD);

void setup()
{
  BTSerial.flush();
  delay(500);
  BTSerial.begin(9600);
  
  pinMode(M1, OUTPUT);
  pinMode(E1, OUTPUT),
  pinMode(M2, OUTPUT);
  pinMode(E2, OUTPUT);
  
  Serial.begin(9600);
  Serial.println("Finish Arduino setup.");
}

void forward(int power)
{
  Serial.println("Move FORWARD.");
  digitalWrite(M1, HIGH);   
  digitalWrite(M2, HIGH);       
  analogWrite(E1, power);
  analogWrite(E2, power);
}

void backward(int power)
{
  Serial.println("Move BACKWARD.");
  digitalWrite(M1, LOW);   
  digitalWrite(M2, LOW);       
  analogWrite(E1, power);
  analogWrite(E2, power);
}

void right(int power)
{
  Serial.println("Move RIGHT.");
  digitalWrite(M1, HIGH);   
  digitalWrite(M2, LOW);       
  analogWrite(E1, power);
  analogWrite(E2, power); 
}

void left(int power)
{
  Serial.println("Move LEFT.");
  digitalWrite(M1, LOW);   
  digitalWrite(M2, HIGH);       
  analogWrite(E1, power);
  analogWrite(E2, power);
}

void loop()
{
  int power = 0;
  char data;
  if (BTSerial.available())
  {
    data = BTSerial.read();
    Serial.println(data);
    if (data == 'V')
    {
      int gear = BTSerial.read() - '0';
      Serial.println(gear);
      power = map(gear, 0, 6, 0, 255);
      Serial.print("Power: ");
      Serial.println(power);
    }
    if (data == 'D')
    {
      data = BTSerial.read();
      Serial.println(data);
      if (data == '1')
      {
        forward(power);
      }
      if (data == '2')
      {
        right(power);
        forward(power);
      }
      if (data == '3')
      {
        right(power);
      }
      if (data == '4')
      {
        right(power);
        backward(power);
      }
      if (data == '5')
      {
        backward(power);
      }
      if (data == '6')
      {
        left(power);
        backward(power);
      }
      if (data == '7')
      {
        left(power);
      }
      if (data == '8')
      {
        left(power);
        forward(power);
      }
    }
  }
}
