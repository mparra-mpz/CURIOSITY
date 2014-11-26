#include <SoftwareSerial.h>
 
#define E1 4
#define M1 5
#define E2 6
#define M2 7
#define RxD 10
#define TxD 11

SoftwareSerial BTSerial(RxD, TxD);

int power;
char movement;

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
  movement = '0';
  
  Serial.begin(9600);
  Serial.println("Finish Arduino setup.");
}

int setPower(char value)
{
  int gear = value - '0';
  int auxiliar = 0;
  if (gear != 0) {
    auxiliar = map(gear, 1, 6, 130, 255);
    if (auxiliar < 0 || auxiliar > 255) auxiliar = power;
  } else {
    auxiliar = 0;
  }
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
  movement = '1';
}

void backward(int value)
{
  Serial.println("Move BACKWARD.");
  digitalWrite(M1, LOW);   
  digitalWrite(M2, LOW);       
  analogWrite(E1, value);
  analogWrite(E2, value);
  movement = '5';
}

void right(int value)
{
  Serial.println("Move RIGHT.");
  digitalWrite(M1, HIGH);   
  digitalWrite(M2, LOW);       
  analogWrite(E1, value);
  analogWrite(E2, value);
  movement = '3';
}

void left(int value)
{
  Serial.println("Move LEFT.");
  digitalWrite(M1, LOW);   
  digitalWrite(M2, HIGH);       
  analogWrite(E1, value);
  analogWrite(E2, value);
  movement = '7';
}

void brake()
{
  Serial.println("Brake.");
  digitalWrite(M1, HIGH);   
  digitalWrite(M2, HIGH);       
  analogWrite(E1, 0);
  analogWrite(E2, 0);
  movement = '0';
}

void loop()
{
  char data;
  if (BTSerial.available())
  {
    data = BTSerial.read();
    Serial.println(data);
    if (data == 'B')
    {
      data = BTSerial.read();
      Serial.println(data);
      if (data == '0') brake();
    }
    if (data == 'V')
    {
      data = BTSerial.read();
      Serial.println(data);
      power = setPower(data);
      if (movement == '1') forward(power);
      if (movement == '3') right(power);
      if (movement == '5') backward(power);
      if (movement == '7') left(power);
    }
    if (data == 'D')
    {
      data = BTSerial.read();
      Serial.println(data);
      if (data == '1') forward(power);
      if (data == '3') right(power);
      if (data == '5') backward(power);
      if (data == '7') left(power);
    }
  }
}
