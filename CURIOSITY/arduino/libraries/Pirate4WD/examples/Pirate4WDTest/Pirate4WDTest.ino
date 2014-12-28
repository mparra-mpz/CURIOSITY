/*
 * Pirate4WDTest.ino - Example that test the wheel movement
 * in four different directions.
 * Created by Manuel Parra Z. on December 20, 2014.
 * Distribute under GNU General Public License version 2.
 */

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
  Serial.print("Rover direction: ");
  Serial.println(rover.getDirection());
  delay(5000);
  
  Serial.println("Move Back");
  rover.moveBack();
  Serial.print("Rover direction: ");
  Serial.println(rover.getDirection());
  delay(5000);
  
  Serial.println("Move Right");
  rover.moveRight();
  Serial.print("Rover direction: ");
  Serial.println(rover.getDirection());
  delay(5000);
  
  Serial.println("Move Left");
  rover.moveLeft();
  Serial.print("Rover direction: ");
  Serial.println(rover.getDirection());
  delay(5000);
  
  Serial.println("Stop");
  rover.stop();
  Serial.print("Rover direction: ");
  Serial.println(rover.getDirection());
  delay(5000);
}
