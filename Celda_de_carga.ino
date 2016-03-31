#include <LiquidCrystal.h> //Inclui a biblioteca do LCD
#include "HX711.h"
float masa = 0;
int masaML = 0;
int a = 0;
#define DOUT  7
#define CLK  8

String dato;
long int m1=302;
long int m2=65536;
long int b=2;
int n_muestras;
long int i = 0;
String command="";
long int masaEntero;
String inputString = "";         // a string to hold incoming data
boolean stringComplete = false;  // whether the string is complete

//int n_muestras = 10;

HX711 scale(DOUT, CLK);

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

void setup()
{
  Serial.begin(9600);

  lcd.begin(16, 2);
  lcd.setCursor(0, 0);
  lcd.print("Masa:");
  lcd.setCursor(10, 1);
  lcd.print("g");

  // reserve 200 bytes for the inputString:
  //inputString.reserve(200);

  scale.set_scale();
  scale.tare(); //Reset the scale to 0
}

void loop()
{
  //masa = -scale.get_units() / 217+2;
  masa = -scale.get_units() / 219.45;
  //masa = (-scale.get_units()*m1)/m2+b;
  a = (int)(masa);
  dato = "";
  if (a<0){
    dato = "-"+ dato;
    a = -a;}
  else
    dato = " "+ dato;
  if (a > 1000)
    dato = dato+ String(a);
  else if (a < 10)
    dato = dato + "   "+ String(a);
  else if (a < 100)
    dato = dato + "  "+ String(a);
  else if (a < 1000)
    dato = dato + " "+ String(a);
  masaML = -scale.get_units();
  lcd.setCursor(5, 1);
  int sensorValue = analogRead(A0);
  int tiempo = sensorValue * (10000.00 / 1023.00);
  lcd.print(dato);
  //Serial.println(int(m2/m1));
  delay(tiempo);
  if (stringComplete) {
    n_muestras = inputString.toInt();
    if (i < n_muestras) {
      if (i==0)
        delay(300);
      masaEntero = -scale.get_units();
      Serial.println(masaEntero);
      i = i+1;
    } else {
      stringComplete = false;
      i = 0;
      inputString = "";
      Serial.println("");
    }
  }

}

void serialEvent() {
  while (Serial.available() && !stringComplete) {
    // get the new byte:
    char inChar = (char)Serial.read();
    // add it to the inputString:
    inputString += inChar;
    //inChar = 'a';
    // if the incoming character is a newline, set a flag
    // so the main loop can do something about it:
    //lcd.setCursor(0, 0);
    //lcd.print('a');
    //delay(10000);
    if (inChar == '\n') {
      stringComplete = true;
    }
    
    }
}

