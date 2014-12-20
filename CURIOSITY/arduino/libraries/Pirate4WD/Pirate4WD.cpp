/*
 * Pirate4WD.cpp - Library for control the DFROBOT Pirate-4WD Mobile Platform.
 * Created by Manuel Parra Z. on December 20, 2014.
 * Distribute under GNU General Public License version 2.
 */

#include "Pirate4WD.h"

Pirate4WD::Pirate4WD(int E1, int M1, int E2, int M2)
{
	_E1 = E1;
	_M1 = M1;
	_E2 = E2;
	_M2 = M2;
	_voltage = 0;
	_direction = '0';

	pinMode(_M1, OUTPUT);
	pinMode(_E1, OUTPUT);
	pinMode(_M2, OUTPUT);
	pinMode(_E2, OUTPUT);
}

void Pirate4WD::setVoltage(int voltage)
{
	_voltage = voltage;

	switch(_direction) {
	case '1':
		moveForward();
		break;
	case '3':
		moveRight();
		break;
	case '5':
		moveBack();
		break;
	case '7':
		moveLeft();
		break;
	default:
		stop();
		break;
	}
}

void Pirate4WD::moveForward()
{
	digitalWrite(_M1, HIGH);
	digitalWrite(_M2, HIGH);
	analogWrite(_E1, _voltage);
	analogWrite(_E2, _voltage);
	_direction = '1';
}

void Pirate4WD::moveBack()
{
	digitalWrite(_M1, LOW);
	digitalWrite(_M2, LOW);
	analogWrite(_E1, _voltage);
	analogWrite(_E2, _voltage);
	_direction = '5';
}

void Pirate4WD::moveRight()
{
	digitalWrite(_M1, HIGH);
	digitalWrite(_M2, LOW);
	analogWrite(_E1, _voltage);
	analogWrite(_E2, _voltage);
	_direction = '3';
}

void Pirate4WD::moveLeft()
{
	digitalWrite(_M1, LOW);
	digitalWrite(_M2, HIGH);
	analogWrite(_E1, _voltage);
	analogWrite(_E2, _voltage);
	_direction = '7';
}

void Pirate4WD::stop()
{
	digitalWrite(_M1, HIGH);
	digitalWrite(_M2, HIGH);
	analogWrite(_E1, 0);
	analogWrite(_E2, 0);
	_direction = '0';
}
