#include <Arduino.h>

char buffer[2];
int byteReads=0;

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);                  // init on-board LED
  Serial.begin(115200);                          // init serial comm
}

void loop() {
  if (Serial.available()){
    byteReads = Serial.readBytes(buffer, 2);     // check if data has been sent from the computer
  
    if (byteReads == 2 && buffer[0] == 'D'){     // parse data
      if((buffer[1] - '0') == 1){                // command 'D1'
          digitalWrite(LED_BUILTIN, HIGH);
      }
      else{                                      // command 'D0'
          digitalWrite(LED_BUILTIN, LOW);
      }
    }
  }
}
