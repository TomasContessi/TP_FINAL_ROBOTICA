#include <Servo.h>

Servo eje1;  // crea el objeto servo
Servo eje2;  // crea el objeto servo
Servo eje3;  // crea el objeto servo
Servo eje4;  // crea el objeto servo

// eje 1
int pot1 = 15;       // uso la pata A1 para leer la tension del pote      
int pwm1 = 2;        // uso la pata D2 para enviar el PWM
float pos1 = 0;      // posicion del servo
float e1lp=0;
float e1lp2=0;
float e1lp3=0;
float e1lp4=0;

// eje 2
int pot2 = 16;       // uso la pata A2 para leer la tension del pote      
int pwm2 = 3;        // uso la pata D3 para enviar el PWM
float pos2 = 0;      // posicion del servo
float e2lp=0;
float e2lp2=0;
float e2lp3=0;
float e2lp4=0;

// eje 3
int pot3 = 17;       // uso la pata A3 para leer la tension del pote      
int pwm3 = 4;        // uso la pata D4 para enviar el PWM
float pos3 = 0;      // posicion del servo
float e3lp=0;
float e3lp2=0;
float e3lp3=0;
float e3lp4=0;

// eje 4
int pot4 = 18;       // uso la pata A4 para leer la tension del pote      
int pwm4 = 5;        // uso la pata D5 para enviar el PWM
float pos4 = 0;      // posicion del servo
float e4lp=0;
float e4lp2=0;
float e4lp3=0;
float e4lp4=0;

float inicio =0;
float fin = 0;
float r = 0;

void setup() {
   eje1.attach(pwm1);  // vincula los servos
   eje2.attach(pwm2);
   eje3.attach(pwm3);
   eje4.attach(pwm4);
   
   Serial.begin(115200);
}

void loop() {
      inicio=millis();                              // establesco un Ts de 10ms
      fin= inicio+1;

      // leo el pote del eje 1
      pos1 = analogRead(pot1)/5;
      pos1 = (pos1+e1lp+e1lp2+e1lp3+e1lp4)/5;
      e1lp4=e1lp3;
      e1lp3=e1lp2;
      e1lp2=e1lp;
      e1lp=pos1;

      // leo el pote del eje 2
      pos2 = analogRead(pot2)/5;
      pos2 = (pos2+e2lp+e2lp2+e2lp3+e2lp4)/5;
      e2lp4=e2lp3;
      e2lp3=e2lp2;
      e2lp2=e2lp;
      e2lp=pos2;

      // leo el pote del eje 3
      pos3 = analogRead(pot3)/5;
      pos3 = (pos3+e3lp+e3lp2+e3lp3+e3lp4)/5;
      e3lp4=e3lp3;
      e3lp3=e3lp2;
      e3lp2=e3lp;
      e3lp=pos3;

      // leo el pote del eje 4
      pos4 = analogRead(pot4)/5;
      pos4 = (pos4+e4lp+e4lp2+e4lp3+e4lp4)/5;
      e4lp4=e4lp3;
      e4lp3=e4lp2;
      e4lp2=e4lp;
      e4lp=pos4;

      // envio la nformacion de las mediciones por si se quiere ver algo para debuggear
      Serial.println(pos1);
      Serial.println(pos2);
      Serial.println(pos3);
      Serial.println(pos4);
      


      // actualizo los servos
      eje1.write(pos1); 
      eje2.write(pos2); 
      eje3.write(pos3); 
      eje4.write(pos4); 
      
      while (fin > millis())  {}             
}
