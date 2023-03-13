int led = 13; //connected led to pin 2
int button = 3; //connected button to pin 3
//  button--->microcontroller---->led
void setup()
{
 // runs once 
 //intialize your input and output
  
 // pin 2 connect led 
 pinMode(led,OUTPUT);
 //pin 3 connect button
 pinMode(button,INPUT);
 
}

void loop() 
{
  // runs continously
  digitalWrite(led,HIGH); //HIGH - on LOW off 
  delay(50); //500ms / half a second
  digitalWrite(led,LOW); //HIGH- on LOW off 
  delay(50); //500ms / half a second

  //digitalRead();
  //analogWrite();
  //analogRead();


}
