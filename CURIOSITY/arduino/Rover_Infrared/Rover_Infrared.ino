#include <Pirate4WD.h>

#define E1 5
#define M1 4
#define E2 6
#define M2 7
#define D0 11
#define D1 10
#define MinVoltage 150

Pirate4WD rover(E1, M1, E2, M2);
int cal_num = 1000;
float cal_value_A0 = 0.0;
float cal_value_A1 = 0.0;

void setup()
{ 
  pinMode(D0, OUTPUT);
  pinMode(D1, OUTPUT);
  digitalWrite(D0, LOW);
  digitalWrite(D1, LOW);
  delay(500);
  digitalWrite(D0, HIGH);
  digitalWrite(D1, HIGH);
  
  for (int i = 0; i < cal_num; i++) {
    cal_value_A0 = cal_value_A0 + analogRead(A0);
    cal_value_A1 = cal_value_A1 + analogRead(A1);
  }
  cal_value_A0 = cal_value_A0 / cal_num;
  cal_value_A1 = cal_value_A1 / cal_num;
  
  rover.setVoltage(MinVoltage);
}

void loop()
{
  boolean is_black_A0 = false;
  boolean is_black_A1 = false;
  float value_A0 = analogRead(A0);
  float value_A1 = analogRead(A1);
  
  if (value_A0 >= 0.75*cal_value_A0 || value_A0 <= 1.25*cal_value_A0) is_black_A0 = true;
  if (value_A1 >= 0.75*cal_value_A1 || value_A1 <= 1.25*cal_value_A1) is_black_A1 = true;
  
  if (is_black_A0 == true && is_black_A1 == true) rover.moveForward();
  else if (is_black_A0 == true && is_black_A1 == false) rover.moveRight();
  else if (is_black_A0 == false && is_black_A1 == true) rover.moveLeft();
  else if (is_black_A0 == false && is_black_A1 == false && rover.getDirection() == 1) rover.stop();
}
