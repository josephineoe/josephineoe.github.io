/**
 * @file include/imu_sensor.h
 * @brief Provides IMU 6050 specific functions
 *
 * Copyright (c) 2025 by me (Josephine Odusanya)
 */

#ifndef IMU_SENSOR_H
#define IMU_SENSOR_H

#ifdef __cplusplus
extern "C" 
{
#endif

#include "cog.h"
#include <stdint.h>
#include <string.h>
#include "simpletools.h"
#include "simplei2c.h"
#include "math.h"

i2c *imu;  // I2C bus for MPU-60X0

#define MPU6050_ADDR 0x68  // Default I2C address (AD0 pin low)

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


HUBTEXT void mpu6050_init();

HUBTEXT void mpu6050_read(imu_data_t *data);

HUBTEXT void calibrate_gyro(volatile int samples,volatile int16_t *offsets);

HUBTEXT void current_pos();


#endif  // IMU_SENSOR_H


#ifdef __cplusplus
}
#endif
