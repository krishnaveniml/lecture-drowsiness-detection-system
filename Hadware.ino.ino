#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

const int RED_LED = 8;
const int BUZZER = 9;

String currentState = "";

void setup() {

  pinMode(RED_LED, OUTPUT);
  pinMode(BUZZER, OUTPUT);

  digitalWrite(RED_LED, LOW);
  digitalWrite(BUZZER, LOW);

  Serial.begin(9600);

  lcd.init();
  lcd.backlight();

  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("SMART CLASS");

  lcd.setCursor(0, 1);
  lcd.print("SYSTEM READY");

  delay(2000);

  lcd.clear();

  Serial.println("ARDUINO READY");
}


void loop() {

  if (Serial.available() > 0) {

    String command = Serial.readStringUntil('\n');
    command.trim();

    if (command != currentState) {

      currentState = command;


      // NORMAL
      if (command == "NORMAL") {

        digitalWrite(RED_LED, LOW);
        digitalWrite(BUZZER, LOW);

        lcd.clear();

        lcd.setCursor(0, 0);
        lcd.print("CLASS STATUS");

        lcd.setCursor(0, 1);
        lcd.print("NORMAL");
      }


      // DROWSINESS ALARM
      else if (command == "ALARM") {

        digitalWrite(RED_LED, HIGH);
        digitalWrite(BUZZER, HIGH);

        lcd.clear();

        lcd.setCursor(0, 0);
        lcd.print("DROWSINESS");

        lcd.setCursor(0, 1);
        lcd.print("ALERT!");
      }


      // CLASS SUSPENDED
      else if (command == "SUSPEND") {

        digitalWrite(RED_LED, HIGH);
        digitalWrite(BUZZER, HIGH);

        lcd.clear();

        lcd.setCursor(0, 0);
        lcd.print("CLASS");

        lcd.setCursor(0, 1);
        lcd.print("SUSPENDED!");
      }
    }
  }
}