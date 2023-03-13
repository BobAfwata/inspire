/* How to use a Keypad with Arduino uno
   More info: http://www.ardumotive.com/how-to-use-a-keypad-en.html
   Date: 13/7/2015 // www.ardumotive.com  */

#include <Keypad.h>
String inputString;
long inputInt;
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

void setup(){
  Serial.begin(9600); //Init serial communication
}

void loop(){
  char key = keypad.getKey();

  if (key) {
    Serial.println(key);

    
  }
}
