/*
 * Pirate4WD.h - Library for control the DFROBOT Pirate-4WD Mobile Platform.
 * Created by Manuel Parra Z. on December 20, 2014.
 * Distribute under GNU General Public License version 2.
 */

#ifndef Pirate4WD_h
#define Pirate4WD_h

#include "Arduino.h"

class Pirate4WD
{
	public:
		Pirate4WD(int E1, int M1, int E2, int M2);
		void setVoltage(int voltage);
		void moveForward();
		void moveBack();
		void moveRight();
		void moveLeft();
		void stop();

	private:
		int _E1;
		int _M1;
		int _E2;
		int _M2;
		int _voltage;
		char _direction;
};

#endif
