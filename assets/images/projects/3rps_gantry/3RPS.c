#include "simpletools.h"                      // Include simpletools
#include "adcDCpropab.h" 
#include "imu_sensor.h"


#define RPS_LEG1_PIN 12
#define RPS_LEG2_PIN 13
#define RPS_LEG3_PIN 14
#define GANTRY_PIN1 15
#define GANTRY_PIN2 16

float total_duration = 17900; //~ milliseconds (17.9 seconds)
float total_distance = 0.095; //meters
float full_speed = 1700; //pulses per millisecond (1.7 pulses per second)

const float upThresh = 3.0;
const float downThresh = 2.0;


static volatile int forward = 0;
static volatile int backward = 0;
static volatile int up = 0;
static volatile int down = 0;
static volatile int xR = 0;

static volatile  float lrV, udV, xrV;                                   // Voltage variables

//const int RPS_LEG_PINS[] = {12, 13, 14};

void sensor_cog(void *par0);
void rps_cog1(void *par1);
void rps_cog2(void *par2);
void rps_cog3(void *par3);
void gantry_cog1(void *par4); //pending
void gantry_cog2(void *par5); //not written yet
void input_cog(void *par6);

//sensors
int16_t gyro_offsets[3];

//motors
//static volatile int leg1cog, leg2cog, leg3cog;
unsigned int servo1_stack_size[256];                 // Stack vars 
unsigned int servo2_stack_size[256];                 // Stack vars
unsigned int servo3_stack_size[256];                 // Stack vars
unsigned int gantry1_stack_size[256];                 // Stack vars
unsigned int input_cog_stack[256];                 // Stack vars
 
int main()                                    // main function
{ 
   // Initialize IMU
   mpu6050_init(); 
   
   //start cogs (lol)
   cogstart(rps_cog1, NULL, servo1_stack_size, sizeof(servo1_stack_size));
   cogstart(rps_cog2, NULL, servo2_stack_size, sizeof(servo2_stack_size));
   cogstart(rps_cog3, NULL, servo3_stack_size, sizeof(servo3_stack_size));
   
   cogstart(gantry_cog1, NULL, gantry1_stack_size, sizeof(gantry1_stack_size));
   cogstart(input_cog, NULL, input_cog_stack, sizeof(input_cog_stack));
   
   //calibration....
   
   
 while(1){ 
        //print current roll and pitch
          current_pos();
          //print("lrV: %.2f \n",lrV);
          //print("udV: %.2f \n",udV);
          pause(500);
          }
                                                  
}

// Function that can continue on its 
// own if launched into another cog.
  
void rps_cog1(void *par1){
     while(1) {
          while(down == 1){
    pulse_out(RPS_LEG1_PIN, 1600); //up                      
    pause(20); 
  }    
    while(up == 1){
    pulse_out(RPS_LEG1_PIN, 1400); //down                      
    pause(20); 
  } 
  while(xR == 1){
    pulse_out(RPS_LEG1_PIN, 1400); //down                      
    pause(20); 
  } 
  while(xR == -1){
    pulse_out(RPS_LEG1_PIN, 1600); //up                      
    pause(20); 
  } 
    pulse_out(RPS_LEG1_PIN, 1500); //stop                      
    pause(20);     
             }
  }  
  
void rps_cog2(void *par2){
     while(1) {
          while(down == 1){
    pulse_out(RPS_LEG2_PIN, 1600); //up                      
    pause(20); 
  }    
    while(up == 1){
    pulse_out(RPS_LEG2_PIN, 1400); //down                      
    pause(20); 
  } 
  while(xR == 1){
    pulse_out(RPS_LEG2_PIN, 1600); //up                      
    pause(20); 
  } 
  while(xR == -1){
    pulse_out(RPS_LEG2_PIN, 1400); //down                      
    pause(20); 
  } 
    pulse_out(RPS_LEG2_PIN, 1500); //stop                      
    pause(20);  
             }
  }  
  
void rps_cog3(void *par3){
     while(1) {
          while(down == 1){
    pulse_out(RPS_LEG3_PIN, 1600); //up                      
    pause(20); 
  }    
    while(up == 1){
    pulse_out(RPS_LEG3_PIN, 1400); //down                      
    pause(20); 
  } 
  while(xR == 1){
    pulse_out(RPS_LEG3_PIN, 1600); //up                      
    pause(20); 
  } 
  while(xR == -1){
    pulse_out(RPS_LEG3_PIN, 1400); //down                      
    pause(20); 
  } 
    pulse_out(RPS_LEG3_PIN, 1500); //stop                      
    pause(20);  
             }
  }  
 
void gantry_cog1(void *par4){
  while(1){
    while(forward == 1){
    pulse_out(GANTRY_PIN1, 1600); //RIGHT                      
    pause(20); 
  }    
    while(backward == 1){
    pulse_out(GANTRY_PIN1, 1400); //left                      
    pause(20); 
  } 
    pulse_out(GANTRY_PIN1, 1475); //stop                      
    pause(20);       
}
}
  
void input_cog(void *par6){
  pause(1000);                                      // Wait 1 s for Terminal app
  adc_init(21, 20, 19, 18);                         // CS=21, SCL=20, DO=19, DI=18

    while(1)                                          // Loop repeats indefinitely
    {
      udV = adc_volts(1);                             // Check A/D 0                
      lrV = adc_volts(0);                             // Check A/D 1
      xrV = adc_volts(2);                              //Check A/D 2 
      if(lrV > upThresh){
        forward = 1;
        backward = 0;
      } else if(lrV < downThresh){
        backward = 1;
        forward = 0;
      }  else {
        forward = 0;
        backward = 0;
      } 
      
      if(udV > upThresh){
        up = 1;
        down = 0;
      } else if(udV < downThresh){
        down = 1;
        up = 0;
      }  else {
        up = 0;
        down = 0;
      }
      
      if(xrV > upThresh){
        xR = 1;
      } else if(xrV < downThresh){
        xR = -1;
      }  else {
        xR = 0;
      }                      
             
   }     
 }
 