int ledPins[] = {8, 9, 10};
int inputPins[] = {2, 3, 4, 5};
int numPins = 4;
int state = 4;
int val[] = {0, 0, 0, 0};

void setup() {
  for (int thisPin = 0; thisPin < numPins; thisPin++) {
    pinMode(ledPins[thisPin], OUTPUT);
    pinMode(inputPins[thisPin], INPUT);
    digitalWrite(inputPins[thisPin], HIGH);
  }
  Serial.begin(9600);
}

void loop(){

  if (Serial.available() == 2) {
    int byteOne = Serial.read();
    int byteTwo = Serial.read();
    if (byteOne == 82 && byteTwo != 87) { // Read is R (ASCII 82)
      Serial.print(state);
    } else if (byteOne == 87) { // Write is W (ASCII 87)
      if (byteTwo < 48 || byteTwo > 52) {
        Serial.print('E');
      } else {
        state = byteTwo - 48; // Converting ASCII to number (ASCII 48 is 0)
        lightState(state);
      }
    } else {
      Serial.print('E');
    }
  } else {  
    for (int thisPin = 0; thisPin < numPins; thisPin++) {
      val[thisPin] = digitalRead(inputPins[thisPin]);
    }
    state = readState();
    lightState(state);
  }

}

int readState() {
  if (val[state]!=LOW) {
    for (int thisPin = 0; thisPin < numPins; thisPin++) {
      if (val[thisPin]==LOW) {
        Serial.print(thisPin);
        return(thisPin);
      }
    }
  }
  return(state);
}

void lightState(int state) {
    for (int thisPin = 0; thisPin < numPins-1; thisPin++) {
      if (ledPins[thisPin]!=state) {
        digitalWrite(ledPins[thisPin], HIGH);
      }
    }
    switch (state) {
      case 0:
        digitalWrite(ledPins[1], LOW);
        break;
      case 1:
        digitalWrite(ledPins[2], LOW);
        break;
      case 2:
        for (int thisPin = 0; thisPin < numPins-1; thisPin++) {
          digitalWrite(ledPins[thisPin], LOW);
        }
        break;
      case 3:
        digitalWrite(ledPins[0], LOW);
        break;
    }
}

