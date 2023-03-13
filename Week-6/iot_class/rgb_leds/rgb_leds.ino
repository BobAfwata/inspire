/* Date 
 * Name : Bob
 * Program to blink 3 leds ; r g b at different intervals
 */
int red_led = 2;   //200
int green_led = 3; // 500
int blue_led = 4;  //1000

void setup() {
  pinMode(red_led,OUTPUT);  // init the leds as output
  pinMode(green_led,OUTPUT);
  pinMode(blue_led,OUTPUT);
}

void loop() {
   digitalWrite(green_led,HIGH);
   delay(200);
   digitalWrite(red_led,HIGH);
   delay(400);
   digitalWrite(blue_led,HIGH);

   digitalWrite(green_led,LOW);
   delay(200);
   digitalWrite(red_led,LOW);
   delay(400);
   digitalWrite(blue_led,LOW);
}
