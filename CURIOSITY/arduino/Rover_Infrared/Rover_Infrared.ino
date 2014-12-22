#include <Pirate4WD.h>

#define E1 5
#define M1 4
#define E2 6
#define M2 7
#define D0 13
#define D1 10
#define MinVoltage 150

Pirate4WD rover(E1, M1, E2, M2);
int cal_num = 1000;
float cal_value_A0 = 0.0;
float cal_value_A1 = 0.0;
boolean is_black_A0 = false;
boolean is_black_A1 = false;
char previous = '0';

void setup()
{
  Serial.begin(9600); 
  Serial.println("Start Arduino setup.");
  
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
  Serial.print("Black A0: ");
  Serial.print(cal_value_A0);
  Serial.print(" -- Black A1: ");
  Serial.println(cal_value_A1);
  
  Serial.println("Finish Arduino setup.");
}

void loop()
{
  rover.setVoltage(MinVoltage);
  float value_A0 = analogRead(A0);
  float value_A1 = analogRead(A1);
  Serial.print("A0: ");  
  Serial.print(value_A0);
  Serial.print(" -- A1: ");  
  Serial.println(value_A1);
  
  if (value_A0 < 0.75*cal_value_A0 || value_A0 > 1.25*cal_value_A0) {
    is_black_A0 = false;
    Serial.println("A0 is white");
  } else {
    is_black_A0 = true;
    Serial.println("A0 is black");
  }
  
  if (value_A1 < 0.75*cal_value_A1 || value_A1 > 1.25*cal_value_A1) {
    is_black_A1 = false;
    Serial.println("A1 is white");
  } else {
    is_black_A1 = true;
    Serial.println("A1 is black");
  }
  
  if (is_black_A0 == true && is_black_A1 == true)
  {
    rover.moveForward();
    previous = '1';
  }
  else if (is_black_A0 == true && is_black_A1 == false) 
  {
    rover.moveRight();
    previous = '7';
  }
  else if (is_black_A0 == false && is_black_A1 == true) 
  {
    rover.moveLeft();
    previous = '3';
  }
  else if (is_black_A0 == false && is_black_A1 == false)
  {
    if (previous == '1') rover.stop();
    if (previous == '3') rover.moveLeft();
    if (previous == '7') rover.moveRight();
  }
}
