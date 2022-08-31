#include "BluetoothSerial.h"

BluetoothSerial SerialBT;

#define GPLed 2
#define B1 15
#define B2 5
#define B3 28
#define B4 19
#define B5 22
#define B6 23

int a=0;
struct Bsig
{
  char sig1=0;
  char sig2=0;
  char sig3=0;
  char sig4=0;
  char sig5=0;
  char sig6=0;
};

void setup()
{
  Serial.begin(115200);
  SerialBT.begin("Boyjo1ho_ESP32");
  Serial.println("Device Setup OK");
  pinMode(GPLed,OUTPUT);
  pinMode(B1,OUTPUT);
  pinMode(B2,OUTPUT);
  pinMode(B3,OUTPUT);
  pinMode(B4,OUTPUT);
  pinMode(B5,OUTPUT);
  pinMode(B6,OUTPUT);
  digitalWrite(B1,LOW);
  digitalWrite(B2,LOW);
  digitalWrite(B3,LOW);
  digitalWrite(B4,LOW);
  digitalWrite(B5,LOW);
  digitalWrite(B6,LOW);
}

void loop()
{
  struct Bsig  Bsig;
  if (SerialBT.available())
  {
    Bsig.sig1=SerialBT.read();
    Bsig.sig2=SerialBT.read();
    Bsig.sig3=SerialBT.read();
    Bsig.sig4=SerialBT.read();
    Bsig.sig5=SerialBT.read();
    Bsig.sig6=SerialBT.read();
    a=1;
  }
  if (a==1)
  {
    digitalWrite(GPLed,HIGH);
    if (Bsig.sig1=='1')
    {
      digitalWrite(B1,HIGH);
    }
    if (Bsig.sig2=='1')
    {
      digitalWrite(B2,HIGH);
    }
    if (Bsig.sig3=='1')
    {
      digitalWrite(B3,HIGH);
    }
    if (Bsig.4=='1')
    {
      digitalWrite(B4,HIGH);
    }
    if (Bsig.5=='1')
    {
      digitalWrite(B5,HIGH);
    }
    if (Bsig.6=='1')
    {
      digitalWrite(B6,HIGH);
    }
    delay(500);
    digitalWrite(GPLed, LOW);
    digitalWrite(B1,LOW);
    digitalWrite(B2,LOW);
    digitalWrite(B3,LOW);
    digitalWrite(B4,LOW);
    digitalWrite(B5,LOW);
    digitalWrite(B6,LOW);
    delay(60);
    a=0;
  }
}
