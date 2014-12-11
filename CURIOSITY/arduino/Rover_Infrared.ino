#define E1 4
#define M1 5
#define E2 6
#define M2 7
#define D0 11
#define D1 10

int power = 0;
char movement = '0';
int cal_num = 1000;
float cal_value_A0 = 0.0;
float cal_value_A1 = 0.0;
boolean is_black_A0 = false;
boolean is_black_A1 = false;

void setup()
{ 
  pinMode(M1, OUTPUT);
  pinMode(E1, OUTPUT),
  pinMode(M2, OUTPUT);
  pinMode(E2, OUTPUT);
  pinMode(D0, OUTPUT);
  pinMode(D1, OUTPUT);
  
  digitalWrite(D0, LOW);
  digitalWrite(D1, LOW);
  delay(500);
  
  Serial.begin(9600);
  Serial.println("Start Arduino setup.");
  
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

int setPower(char value)
{
  int gear = value - '0';
  int auxiliar = 0;
  if (gear != 0) {
    //At 130 PWM the rover start to move.
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
  power = setPower('1');
  
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
  
  if (is_black_A0 == false && is_black_A1 == false) {
    if (movement == '1') brake();
    if (movement == '3') right(power);
    if (movement == '7') left(power);
  } else if (is_black_A0 == true && is_black_A1 == true) {
    forward(power);
  } else if (is_black_A0 == true && is_black_A1 == false) {
    right(power);
  } else if (is_black_A0 == false && is_black_A1 == true) {
    left(power);
  }
}
