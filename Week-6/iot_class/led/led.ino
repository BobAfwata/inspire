int led = LED_BUILTIN; //
int button = 2; //button on pin 2

void setup() {
  pinMode(led,OUTPUT); // led as an output
  pinMode(button,INPUT); // led as an output

}

void loop() {

  digitalWrite(led,HIGH); // on
  delay(500); //wait for 500ms 
  digitalWrite(led,LOW); // off
  delay(500); //wait for 500ms 


}
