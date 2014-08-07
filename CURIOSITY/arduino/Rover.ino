#include <SoftwareSerial.h>
 
#define M2 4
#define E2 5
#define E1 6
#define M1 7
#define RxD 10
#define TxD 11

SoftwareSerial BTSerial(RxD, TxD);

int power;

void setup()
{
  BTSerial.flush();
  delay(500);
  BTSerial.begin(9600);
  
  pinMode(M1, OUTPUT);
  pinMode(E1, OUTPUT),
  pinMode(M2, OUTPUT);
  pinMode(E2, OUTPUT);
  
  power = 0;
  
  Serial.begin(9600);
  Serial.println("Finish Arduino setup.");
}

int setPower(char value)
{
  int gear = value - '0';
  int auxiliar = map(gear, 0, 6, 0, 255);
  if (auxiliar < 0 || auxiliar > 255) auxiliar = power;
  Serial.print("Power: ");
  Serial.println(auxiliar);
  return auxiliar;
}

void forward(int value)
{
  Serial.println("Move FORWARD.");
  digitalWrite(M1, HIGH);   
  digitalWrite(M2, HIGH);       
  analogWrite(E1, value);
  analogWrite(E2, value);
}

void backward(int value)
{
  Serial.println("Move BACKWARD.");
  digitalWrite(M1, LOW);   
  digitalWrite(M2, LOW);       
  analogWrite(E1, value);
  analogWrite(E2, value);
}

void right(int value)
{
  Serial.println("Move RIGHT.");
  digitalWrite(M1, HIGH);   
  digitalWrite(M2, LOW);       
  analogWrite(E1, value);
  analogWrite(E2, value); 
}

void left(int value)
{
  Serial.println("Move LEFT.");
  digitalWrite(M1, LOW);   
  digitalWrite(M2, HIGH);       
  analogWrite(E1, value);
  analogWrite(E2, value);
}

void loop()
{
  char data;
  if (BTSerial.available())
  {
    data = BTSerial.read();
    Serial.println(data);
    if (data == 'V')
    {
      data = BTSerial.read();
      Serial.println(data);
      power = setPower(data);
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
