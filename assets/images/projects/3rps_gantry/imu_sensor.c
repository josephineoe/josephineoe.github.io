#include "simpletools.h"
#include "simplei2c.h"
#include "math.h"

#define MPU6050_ADDR 0x68  // Default I2C address (AD0 pin low)
#define SCL_PIN 8          // Use P0 for SCL
#define SDA_PIN 9          // Use P1 for SDA

i2c *imu;  // I2C bus for MPU-60X0

// Register addresses from the datasheet
#define PWR_MGMT_1     0x6B 
#define GYRO_CONFIG    0x1B
#define ACCEL_CONFIG   0x1C
#define ACCEL_XOUT_H   0x3B
#define TEMP_OUT_H     0x41
#define GYRO_XOUT_H    0x43

// Sensor data structure
typedef struct {
    int16_t accel[3];  // X,Y,Z
    int16_t gyro[3];   // X,Y,Z
    int16_t temp;
} imu_data_t;

volatile int samples;
volatile int16_t *offsets;
volatile int16_t gyro_offsets[3];

// Initialize MPU-60X0
void mpu6050_init() {
    // Initialize I2C
    i2c_open(&imu, SCL_PIN, SDA_PIN, 0);
    
    // Wake up MPU-60X0 (disable sleep mode)
    i2c_start(&imu);
    i2c_writeByte(&imu, MPU6050_ADDR << 1);
    i2c_writeByte(&imu, PWR_MGMT_1);
    i2c_writeByte(&imu, 0x00);  // Wake up (clear sleep bit)
    i2c_stop(&imu);
    
    // Configure gyroscope range (±250°/s)
    i2c_start(&imu);
    i2c_writeByte(&imu, MPU6050_ADDR << 1);
    i2c_writeByte(&imu, GYRO_CONFIG);
    i2c_writeByte(&imu, 0x00);  // ±250°/s (FS_SEL=0)
    i2c_stop(&imu);
    
    // Configure accelerometer range (±2g)
    i2c_start(&imu);
    i2c_writeByte(&imu, MPU6050_ADDR << 1);
    i2c_writeByte(&imu, ACCEL_CONFIG);
    i2c_writeByte(&imu, 0x00);  // ±2g (AFS_SEL=0)
    i2c_stop(&imu);
    
    // Optional: Configure DLPF (Digital Low Pass Filter) //NOTE FOR ME ADD A KFILTER HERE 
    // i2c_start(&imu);
    // i2c_writeByte(&imu, MPU6050_ADDR << 1);
    // i2c_writeByte(&imu, 0x1A);  // CONFIG register
    // i2c_writeByte(&imu, 0x03);  // DLPF_CFG=3 (44Hz accel, 42Hz gyro)
    // i2c_stop(&imu);
}

// Read all sensor data from MPU-60X0
void mpu6050_read(imu_data_t *data) {
    uint8_t buf[14];
    
    // Start reading from register 0x3B (ACCEL_XOUT_H)
    i2c_start(&imu);
    i2c_writeByte(&imu, MPU6050_ADDR << 1);
    i2c_writeByte(&imu, ACCEL_XOUT_H);
    
    // Repeated start to begin reading
    i2c_start(&imu);
    i2c_writeByte(&imu, (MPU6050_ADDR << 1) | 1);
    
    // Read 14 bytes (accel, temp, gyro)
    for(int i = 0; i < 13; i++) {
       
        buf[i] = i2c_readByte(&imu, 0);  // ACK all but last byte
  
    }
    buf[13] = i2c_readByte(&imu, 1);     // NAK last byte
    i2c_stop(&imu);
    
    // Format data (registers are big-endian)
    data->accel[0] = (buf[0] << 8) | buf[1];   // X
    data->accel[1] = (buf[2] << 8) | buf[3];   // Y
    data->accel[2] = (buf[4] << 8) | buf[5];   // Z
    data->temp     = (buf[6] << 8) | buf[7];   // Temperature
    data->gyro[0]  = (buf[8] << 8) | buf[9];   // X
    data->gyro[1]  = (buf[10] << 8) | buf[11]; // Y
    data->gyro[2]  = (buf[12] << 8) | buf[13]; // Z
    
}

// Calibrate gyroscope by averaging samples while stationary
void calibrate_gyro(volatile int samples, volatile int16_t *offsets) {
    imu_data_t data;
    int32_t sum[3] = {0};
    
    void calibrate_gyro(volatile int samples, volatile int16_t *offsets); 
    print("Calibrating gyro... keep sensor still!\n");
    
    for(int i = 0; i < samples; i++) {
        mpu6050_read(&data);
        sum[0] += data.gyro[0];
        sum[1] += data.gyro[1];
        sum[2] += data.gyro[2];
        pause(10);
    }
    
    offsets[0] = sum[0] / samples;
    offsets[1] = sum[1] / samples;
    offsets[2] = sum[2] / samples;
    
    print("Offsets: X=%d, Y=%d, Z=%d\n", offsets[0], offsets[1], offsets[2]);
    
}

void current_pos(void) {
    
    // Main loop
        imu_data_t data;
        mpu6050_read(&data);
        
        // Apply gyro calibration
        data.gyro[0] -= gyro_offsets[0];
        data.gyro[1] -= gyro_offsets[1];
        data.gyro[2] -= gyro_offsets[2];
        
        // Convert raw data to human-readable values:
        // Accelerometer: ±2g range (16384 LSB/g)
        float ax = data.accel[0] / 16384.0;
        float ay = data.accel[1] / 16384.0;
        float az = data.accel[2] / 16384.0;
        
        // Gyroscope: ±250°/s range (131 LSB/°/s)
        float gx = data.gyro[0] / 131.0;
        float gy = data.gyro[1] / 131.0;
        float gz = data.gyro[2] / 131.0;
        
        // Temperature: (in °C)
        float temp = data.temp / 340.0 + 36.53;
        
        // Compute roll and pitch using accelerometer data
        float roll = atan2(ay, az) * 180.0 / PI;
        float pitch = atan2(-ax, sqrt(ay * ay + az * az)) * 180.0 / PI;
        
       /* no need to see this
        
        // Print results with fixed-width formatting
        print("%c", HOME);  // Clear terminal
        print("MPU-60X0 IMU Data\n");
        print("-----------------\n");
        print("Accel: X=%7.2fg  Y=%7.2fg  Z=%7.2fg\n", ax, ay, az);
        print("Gyro:  X=%7.2f°/s Y=%7.2f°/s Z=%7.2f°/s\n", gx, gy, gz);
        //print("Temp:  %7.1f°C\n", temp);
        pause(200);
      */

      //read_imu_data(roll, pitch);
        print("Roll: %.2f°, Pitch: %.2f°\n",roll, pitch);
        pause(500);    
}
