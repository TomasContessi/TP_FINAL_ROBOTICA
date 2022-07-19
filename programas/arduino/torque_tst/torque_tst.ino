#include <Servo.h>

Servo myservo;  // crea el objeto servo

int pot = 20;       // uso la pata A6 para leer la tension del pote      
int pwm = 11;       // uso la pata D11 para enviar el PWM
float pos = 0;      // posicion del servo
float lp=0;
float lp2=0;
float lp3=0;
float lp4=0;
float inicio =0;
float fin = 0;
float r = 0;

void setup() {
   myservo.attach(pwm);  // vincula el servo al pin digital
   Serial.begin(115200);
}

void loop() {
      inicio=millis();                              // establesco un Ts de 10ms
      fin= inicio+10;
      pos = analogRead(pot)/5;
      pos = (pos+lp+lp2+lp3+lp4)/5;
      lp4=lp3;
      lp3=lp2;
      lp2=lp;
      lp=pos;

      Serial.println(pos);
          
      myservo.write(pos); 
      while (fin > millis())  {}             
}
