/*------------------------------------------------------------------
Author: Brindan Adhikari
Pupose: This will be the main arduino loop
Included: 
 1) 2x Ultrasonic 
 2) 1x single beam  
Future Work: 
 1) Motor controller
 2) Linear-mass controller
 3) Encoders
-------------------------------------------------------------------*/
//Define all constants from every mode
const int semi_aut_mod_pin = 12; //Semi-autonomous-mode
    //Define the Single Beam Pins
    const int trigPin_lidar1 = 2;
    const int monitorPin_lidar1 = 3;
    
const int discont_mod_pin = 13; //Discontinuity-mode
    //Define the ultrasonic Sensors pins
    const int trigPin_ultra1 = 9; //ultrasonic#1
    const int echoPin_ultra1 = 10;  
    const int trigPin_ultra2 = 4; //ultrasonic#2  
    const int echoPin_ultra2 = 5;
    long duration;
    float distance;  

//Start all modes at false
int semi_aut_mod = 0; 
int discont_mod =0; 

//Define mode
int MODE;
int lastMODE;

/*-------------------------------------------------------------------
Setup:setup all  the pins as either inputs or outputs &set all 
modes to LOW*/
void setup() 
{   //MODES set to low
    pinMode(semi_aut_mod_pin, INPUT);
    digitalWrite(semi_aut_mod_pin,LOW);
    pinMode(discont_mod_pin, INPUT);
    digitalWrite(discont_mod_pin,LOW);
    
    //Single Beam Setup
    pinMode(trigPin_lidar1,OUTPUT);
    digitalWrite(trigPin_lidar1,LOW);
    pinMode(monitorPin_lidar1,INPUT);
    
    //Ultrasonic Setup
    pinMode(trigPin_ultra1, OUTPUT); // Sets the trigPin as an Output
    pinMode(echoPin_ultra1, INPUT); // Sets the echoPin as an Input
    pinMode(trigPin_ultra2, OUTPUT); // Sets the trigPin as an Output
    pinMode(echoPin_ultra2, INPUT); // Sets the echoPin as an Input

}

/*___________________________________________________________________
---------------------------MAIN LOOP---------------------------------
_____________________________________________________________________*/
void loop() 
{
    //Set all modes to reading the respective pins to verify current mode
    semi_aut_mod = digitalRead(semi_aut_mod_pin);  
    discont_mod = digitalRead(discont_mod_pin);
   
   //Select the mode 
   if (semi_aut_mod == HIGH)
      {
        MODE = 3;
      }
   
   else if (discont_mod == HIGH)
      {
        MODE = 4;
      } 
   else
       {
         Serial.print("No Modes Detected");
       }
         
  //See if MODES have switched
  if(MODE !=lastMODE)
  {

// Enter Swtich cases for the modes

    switch(MODE)
    {
    /*------------------------Discontinuity MODE---------------------*/
      case 0:        
          Serial.begin(9600); //Starts the serial communication
          // Ultrasonics #1
              // Clears the trigPin
              digitalWrite(trigPin_ultra1, LOW);
              delayMicroseconds(2);
              // Sets the trigPin on HIGH state for 10 micro seconds
              digitalWrite(trigPin_ultra1, HIGH);
              delayMicroseconds(10);
              digitalWrite(trigPin_ultra1, LOW);
              // Reads the echoPin, returns the sound wave travel time in microseconds
              duration = pulseIn(echoPin_ultra1, HIGH);
              // Calculating the distance
              distance= duration*0.034/2;
              // Prints the distance on the Serial Monitor
              Serial.print("Distance#1: ");
              Serial.println(distance);
              
              // Ultrasonic #2
              // Clears the trigPin
              digitalWrite(trigPin_ultra2, LOW);
              delayMicroseconds(2);
              // Sets the trigPin on HIGH state for 10 micro seconds
              digitalWrite(trigPin_ultra2, HIGH);
              delayMicroseconds(10);
              digitalWrite(trigPin_ultra2, LOW);
              // Reads the echoPin, returns the sound wave travel time in microseconds
              duration = pulseIn(echoPin_ultra2, HIGH);
              // Calculating the distance
              distance= duration*0.034/2;
              // Prints the distance on the Serial Monitor
              Serial.print("Distance#2: ");
              Serial.println(distance);
              break;
    /*-----------------------Semi-autonomous-Mode--------------------*/
    case 1:
              Serial.begin(115200); //Start Serial communications
              
              //Single-Beam#1
              pulseWidth = pulseIn(monitorPin_lidar1, HIGH); // Count how long the pulse is high in microseconds
            
              if(pulseWidth != 0) //If reading isn't 0
              {
                pulseWidth = pulseWidth / 10; // 10usec = 1 cm of distance
                Serial.println(pulseWidth); // Print the distance
              }
                break;
    }
    lastMODE = MODE;
  }
}

