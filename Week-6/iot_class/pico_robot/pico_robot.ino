#define PWM1_Ch1    0     //PWM INIT STUFF -- try NOT to alter this part
#define PWM1_Ch2    1
#define PWM1_Res   8      // Setting speed bounds where 0 is minimum and 255 is maximum
#define PWM1_Freq  5000
// INITIALIZING VARIABLES
int EN1 = 19;     // MOTOR 1 CONNECTIONS 
int IN1A = 20;
int IN1B = 21;


int EN2 = 6;      // MOTOR 2 CONNECTIONS
int IN2A = 7;
int IN2B = 8;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);      // make sure your Serial Monitor is also set at this baud rate.

  Serial.println("ROBOT CAR..\n\n");
  pinMode(EN1, OUTPUT);  // MOTOR 1 AS OUTPUT
  pinMode(IN1A, OUTPUT);
  pinMode(IN1B, OUTPUT);

  pinMode(EN2, OUTPUT);  // MOTOR 2 AS OUTPUT
  pinMode(IN2A, OUTPUT);
  pinMode(IN2B, OUTPUT);

  Serial.println(" SWITCHING ON and setting speed  ");

  


}

void loop() {
  

 
Switch_ON();
delay(500);
Forward();
delay(1000);
Backward();
Left();
delay(500);
Right();
delay(500);
Forward();
  
       
    
}


// ALL CONTROL FUNCTIONS DOWN BELOW 

// TURN ON MOTORS
void Switch_ON()
{
  digitalWrite(EN1, HIGH );
  digitalWrite(EN2, HIGH );
}

// SET SPEED
void Motor_Speed(int dutyCycle)
{
  
}

// TURN OFF MOTORS
void Switch_OFF()
{
  digitalWrite(EN1, LOW );
  digitalWrite(EN2, LOW );
}

// Forward
void Forward()
{
  digitalWrite(IN1A, HIGH); // TURNING MOTOR 1 FORWARD
  digitalWrite(IN1B, LOW);

  digitalWrite(IN2A, HIGH); // TURNING MOTOR 2 FORWARD
  digitalWrite(IN2B, LOW);
}

// BACKWARD
void Backward()
{
  digitalWrite(IN1A, LOW); // TURNING MOTOR 1  BACK
  digitalWrite(IN1B, HIGH);

  digitalWrite(IN2A, LOW); // TURNING MOTOR 2  BACK
  digitalWrite(IN2B, HIGH);
}

// RIGHT
void Right()
{
  digitalWrite(IN1A, HIGH ); // TURNING MOTOR 1  FORWARD
  digitalWrite(IN1B, LOW);

  digitalWrite(IN2A, LOW); // TURNING MOTOR 2  BACKWARD
  digitalWrite(IN2B, HIGH);
}

// TURN ROBOT LEFT
void Left()
{
  digitalWrite(IN1A, LOW); // TURNING MOTOR 1  BACKWARD
  digitalWrite(IN1B, HIGH);

  digitalWrite(IN2A, HIGH); // TURNING MOTOR 2  FORWARD
  digitalWrite(IN2B, LOW);
}

// BRAKE
void Brake()
{
  digitalWrite(IN1A, LOW); // TURNING MOTOR 1 off
  digitalWrite(IN1B, LOW);

  digitalWrite(IN2A, LOW); // TURNING MOTOR 2 off
  digitalWrite(IN2B, LOW);
}
