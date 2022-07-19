/*void SerialEvent(){
  int i = 1;
  while(Serial.available()){ //mientras hay algo en el buffer
    Q[i] = Serial.parseInt(); // leo del buffer hasta el primer delimitador
    i++;
    }
  }*/

  
void SerialEvent(){
  int i = 1;
  while(Serial.available()){ //mientras hay algo en el buffer
    getDataFromPC();
    }
  }
