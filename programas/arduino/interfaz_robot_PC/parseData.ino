void parseData() {

    // split the data into its parts
    
  char * strtokIndx; // this is used by strtok() as an index
  
  strtokIndx = strtok(inputBuffer,":");      // get the first part - the string
  Q[1] = atoi(strtokIndx);
  
  strtokIndx = strtok(NULL, ":"); // this continues where the previous call left off
  Q[2] = atoi(strtokIndx);     // convert this part to an integer
  
  strtokIndx = strtok(NULL, ":"); 
  Q[3] = atoi(strtokIndx);     // convert this part to a float

  strtokIndx = strtok(NULL, ":"); 
  Q[4] = atoi(strtokIndx);     // convert this part to a float

  strtokIndx = strtok(NULL, ":"); 
  gripper = atoi(strtokIndx);     // convert this part to a float

  strtokIndx = strtok(NULL, ":"); 
  motors = atoi(strtokIndx);     // convert this part to a float

}
