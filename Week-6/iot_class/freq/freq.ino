#include <Keypad.h>

const byte ROWS = 4; //four rows
const byte COLS = 3; //three columns
char keys[ROWS][COLS] = {
{'1','2','3'},
{'4','5','6'},
{'7','8','9'},
{'*','0','#'}
};


//Change the following pins your yours keypad pinout!
byte rowPins[ROWS] = {7, 2, 3, 5}; //connect to the row pinouts of the keypad
byte colPins[COLS] = {6, 8, 4};    //connect to the column pinouts of the keypad

Keypad keypad = Keypad( makeKeymap(keys), rowPins, colPins, ROWS, COLS );

unsigned long loopCount;
unsigned long startTime;
String msg;


void setup() {
    Serial.begin(9600);
    
}
long getKeypadIntegerMulti()
{
  
  long value = 0;                                // the number accumulator
  long keyvalue;                                     // the key pressed at current moment
  int isnum;
  //Serial.println("Enter the digits,press any non-digit to end ");
  //Serial.print("You have typed: ");
  do
  {
    keyvalue = keypad.getKey();                          // input the key
    isnum = (keyvalue >= '0' && keyvalue <= '9');         // is it a digit?
    if (isnum)
    {
      Serial.print(keyvalue - '0');
      value = value * 10 + keyvalue - '0';               // accumulate the input number
    }

  } while (isnum || !keyvalue);                          // until not a digit or while no key pressed
  //
  Serial.println(" "); 
  //Serial.print("Returning from funtion: "); 
  //Serial.println(value);
  return value;

}//getKeypadInteger

void loop() 
{
   int val= getKeypadIntegerMulti(); 
  // Serial.println("Value is");
   Serial.println(val);
   delay(2500);
}  
