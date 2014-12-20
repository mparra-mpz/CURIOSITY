/*
 * VoltageMovementTest.ino - Example that will help you to
 * determine how much voltage do yo need to move the wheels.
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
  int voltage;
  
  for(int i=0; i <= 255; i+=5) {
    Serial.print("Voltage: ");
    Serial.println(i);
    rover.setVoltage(i);
    rover.moveForward();
    delay(5000);
}
