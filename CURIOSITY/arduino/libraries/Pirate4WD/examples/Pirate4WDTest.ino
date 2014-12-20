#include <Pirate4WD.h>

Pirate4WD rover(5, 4, 6, 7);

void setup()
{
  Serial.begin(9600);
}

void loop() 
{ 
  int voltage = 255;
  Serial.print("Voltage: ");
  Serial.println(voltage);
  rover.setVoltage(voltage);
  
  Serial.println("Move Forward");
  rover.moveForward();
  delay(5000);
  
  Serial.println("Move Back");
  rover.moveBack();
  delay(5000);
  
  Serial.println("Move Right");
  rover.moveRight();
  delay(5000);
  
  Serial.println("Move Left");
  rover.moveLeft();
  delay(5000);
  
  Serial.println("Stop");
  rover.stop();
  delay(5000);
}
