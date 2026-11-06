# SACS Global Loading

Version 24.00

[原始 PDF](../../raw/SACS/SACS2024_Global_Loading.pdf)

**Trademark Notice**

Bentley and the "B" Bentley logo are either registered or unregistered trademarks or service marks of Bentley Systems, Incorporated. All other marks are the property of their respective owners.

**Copyright Notice**

Copyright © 2024, Bentley Systems, Incorporated. All Rights Reserved.

## 目录

- [1 INTRODUCTION](#1-introduction)
  - [1.1 OVERVIEW](#11-overview)
  - [1.2 DEFINITIONS](#12-definitions)
  - [1.3 PROGRAM FEATURES](#13-program-features)
  - [1.4 PROGRAM STRUCTURE](#14-program-structure)
- [2 ANALYSIS PROCEDURE](#2-analysis-procedure)
  - [2.1 BASIC OPTIONS](#21-basic-options)
  - [2.2 WAVE RESPONSE MODE](#22-wave-response-mode)
  - [2.3 DIFFRACTION WAVE MODE](#23-diffraction-wave-mode)
- [3 COMMENTARY](#3-commentary)
  - [3.1 LOAD METHOD](#31-load-method)
  - [3.2 STRESS METHOD](#32-stress-method)
- [4 SAMPLE PROBLEMS](#4-sample-problems)
  - [4.1 SAMPLE PROBLEM 1](#41-sample-problem-1)
  - [4.2 SAMPLE PROBLEM 2](#42-sample-problem-2)
  - [4.3 SAMPLE PROBLEM 3](#43-sample-problem-3)
  - [4.4 SAMPLE PROBLEM 4](#44-sample-problem-4)
- [5 INPUT LINES](#5-input-lines)
  - [5.1 INPUT FILE](#51-input-file)

## 1 INTRODUCTION

### 1.1 OVERVIEW

The Global Load Analysis program module can be used to obtain overall structural characteristics from a model file, common solution file or a response file.

The program can be used to calculate quantities such as overall bending moments and shears at defined locations or stations along the structure. For example, the results of a finite element analysis of a ship can be used to calculate quantities such as overall bending moments and shears for stations along the hull. It can also be used on jacket type structures to obtain overall bending moments and shears versus depth or station and to select critical time points of a random wave analysis.

For the case where the structural analysis contains the transfer function information, the short term and long term probability distributions of any of the responses can be calculated provided that the applicable sea state information is available. Section force transfer functions can also be developed.

### 1.2 DEFINITIONS

#### 1.2.1 Short Term Distributions

The probability of exceedance of a variable for a particular sea state can be calculated using a wave spectrum, the variable transfer function, and the Rayleigh distribution of peaks. The probability of exceeding a particular level can be calculated.

#### 1.2.2 Long Term Distributions

The long term distributions are based on a Weibull probability distribution. The parameters of this distribution are calculated using the results of the short term distributions from a scatter diagram base on relative long term observations. The purpose is to predict the extreme response of a variable that may occur in a long term e.g. 100 years.

#### 1.2.3 Long Crested Sea

The long crested sea is a unidirectional sea with no wave spreading.

#### 1.2.4 Short Crested Sea

The short crested sea is characterized as a multi-directional sea and is represented with the use of wave spreading factors.

#### 1.2.5 RAO

RAO is the acronym for response amplitude operator which is another term for a transfer function.

#### 1.2.6 STATION

A location at which structural forces are to be monitored. A station can be a location along a horizontal structure or an elevation along a vertical structure.

### 1.3 PROGRAM FEATURES

The Global Load Analysis program requires a Global Load input file and either a solution file and model file or a response file.

The model file must contain all the load information including those loads calculate by SEASTATE. Some of the main features and capabilities of the program are detailed in the following sections. The response file must contain modal coordinates.

Note: Modal velocities and accelerations are required if load case retrieval is to be performed.

#### 1.3.1 General Capabilities

1. Calculates the section loads (six forces and moments) of cross-sections for all load conditions.\
2. Cross-sections can be defined in any of the three global planes, XY, YZ, or ZX.\
3. Structural or naval architecture nomenclature available.\
4. Cross-section location specified by range or specific position.\
5. Still water plus wave loading available.\
6. Calculates section loading versus spectral wave period.\
7. Allow calculation of section forces based on external load summation or by summation of element internal loads.\
8. Allows inclusion or exclusion of members and plate elements by group names.\
9. Allows scatter diagram input with automatic normalization. Also can repeat previous scatter diagram for different directions with different wave height factors.\
10. Includes wave spreading capability to represent short crested sea states.\
11. Short term response calculations.\
12. Long term response calculations. Includes least squares or last two point fit to Weibull distribution.\
13. Couples with wave diffraction programs WAMIT™ and MORA™.\
14. Allows user to specify selection criteria for critical time point determination.\
15. Select and create time point selection file containing critical time points of a random wave analysis.\
16. Supports multiple seeds in the response file.

#### 1.3.2 Plot Capabilities

The Global Load Analysis program can create the following plots .

1. Section forces versus station for all load cases separately or together.

2. RAO plots of section forces versus frequency or period.\
3. Section forces for still water plus wave versus station.\
4. Section forces versus spectral wave period for constant significant wave height.\
5. Probability of exceedance versus response amplitude using Weibull ordinate.\
6. Maximum moment and shear versus station for each seed shown on one plot.\
7. Average of maximum and minimum moments and shears for multiple seeds versus station.

### 1.4 PROGRAM STRUCTURE

The Global Loading program can be run in three basic modes, general mode, wave response mode or diffraction wave mode.

#### 1.4.1 General Mode

In the general mode, internal forces from a solution file or applied loads from a model file are used to sum shears and moments at the designated locations.

#### 1.4.2 Wave Response Mode

In the wave response mode, modal coordinates from a response file are used to give modal force and moment summations at designated locations. The response file can contain data for numerous wave surface profiles generated from various seeds and numerous response files are supported.

##### 1.4.2.1 Modal Force and Moments

Modal forces and moments are reported and optionally plotted for each station or location specified.

##### 1.4.2.2 Maximum/Minimum Shear and Moment

The maximum and minimum values of shear and moment are reported at each station or location. This information can be plotted and used in conjunction with user specified criteria to select critical time points for load case creation. A time point selection file is created for use by Wave Response when retrieving loads

#### 1.4.3 Diffraction Wave Mode

In the diffraction wave mode, a model file with loading or transfer function data from a diffraction wave analysis can be used to obtain various statistics.

##### 1.4.3.1 Still Water Plus Wave

If the model file or OCI file contains the dead load case as well as the wave load data, then section forces and moments can be calculated for any combination of wave height, wave period, wave direction, and wave phase angle effects added to the still water case. This allows the printing and plotting of hogging and sagging conditions, etc.

##### 1.4.3.2 Section Force Versus Wave Spectrum Periods

Any section force or moment at any station can be plotted versus wave spectrum period for any wave height or direction. The period used in the plots can be either the peak period or the mean period. The wave spectrum types can be either Pierson-Moskowitz or JONSWAP. This is calculated by integrating the section transfer function squared times the wave spectrum at each of the period values.

## 2 ANALYSIS PROCEDURE

### 2.1 BASIC OPTIONS

The Global Load program requires some basic options specified in the Global Load input file regardless of the type of analysis being performed.

#### 2.1.1 Titles

Any number of descriptive titles may be input at the file beginning using columns 2-80 leaving column 1 blank.

#### 2.1.2 Analysis Plane

The global plane in which section forces are to be calculated is entered in columns 14-15 on the GLAOPT line. The axis origins used to calculated moments due to forces normal to the designated plane are input in columns 46-53 and 54-61. Enter the X and Y origins when using the XY plane, Y and Z origins when using the YZ plane and the Z and X origins when using the ZX plane.

The following designates that the structure is to be cut using XY planes. The stress load method is to be used and the X and Y origin coordinates are 0.

![输入示例或输出清单，原文 PDF 第 9 页](SACS2024_Global_Loading/proofread_p9_0.png)

[原文 PDF 第 9 页](../../raw/SACS/SACS2024_Global_Loading.pdf#page=9)

#### 2.1.3 Load Method

The program can use either stresses and internal loads (stress method)or applied loads (load method) to sum shears and moments when using a solution file. The load method sums all loads including reactions on one side of the plane and is the most accurate but does not allow the inclusion or exclusion of specified elements. The ‘stress method’ sums the forces and moments of each element cut by the plane. The accuracy of this method depends on the how well the finite element model represents the stress distribution of the structure. Enter ‘EX’ to use applied load method or ‘SM’ to use the stress method in columns 30-31.

The following designates that the stress load method is to be used.

![输入示例或输出清单，原文 PDF 第 9 页](SACS2024_Global_Loading/proofread_p9_1.png)

[原文 PDF 第 9 页](../../raw/SACS/SACS2024_Global_Loading.pdf#page=9)

Note: The load option is ignored when using a response file as input. A useful byproduct of this analysis is a comparison of the results of the two methods to ascertain the accuracy of the finite element model. The stress method has the advantage of being able to either include or exclude specified elements.

#### 2.1.4 Output Option

The section forces and moments can be identified using either the structural or naval architecture nomenclature. By default, forces are identified by the global axis direction and the moments are identified by the moment vector in the global axis direction, i.e. Fx is the force in the global X axis and Mx is the moment about the global X direction.

Enter ‘NA’ in columns 33-34 of the GLAOPT line if naval architecture nomenclature is to be used for output. The following is a description of the naval architecture nomenclature:

AX Axial force (Perpendicular to the cut plane)

HS Horizontal Shear (Shear in horizontal direction)

VS Vertical Shear (Shear in vertical direction)

TQ Torsion (Moment about normal to cut plane)

VM Vertical Moment (Moment about horizontal axis, associated with the vertical shear.

HM Horizontal Moment (Moment about vertical axis, associated with the horizontal shear.

#### 2.1.5 Cut Locations

The location of the cut planes is specified by the structural coordinate perpendicular to the cut plane. These locations can be specified by sets of a starting position, an ending position, and the number of positions using the RANGE line.

Locations can also be specified by inputting the locations or elevations individually using the LOCATE line.

The following designates that the structure is to cut using XY planes and to be checked at Z elevations 0, -50, -250, -550, -800, -1050, -1200 and -1399.9.

![输入示例或输出清单，原文 PDF 第 10 页](SACS2024_Global_Loading/proofread_p10_0.png)

[原文 PDF 第 10 页](../../raw/SACS/SACS2024_Global_Loading.pdf#page=10)

#### 2.1.6 Plot Options

The section forces and moment can be plotted versus station/location or time using the PLOT line.

The plots can be for individual load cases or all load cases together or for individual wave surface profiles or all surface profiles together when using a response file from wave response. If the SACS input file contains transfer function information, transfer functions (RAO’s) can be plotted versus either period or frequency.

Enter the force type to be plotted in columns 6-7 and the independent variable (ie. station, period, frequency or time in columns 10-12. Enter ‘SL’ in columns 14-15 if each load case or surface profile is to be plotted separately. If plotting versus frequency or period, enter the station or location in columns 53- 50.

The following request that moments about the global Y axis and forces along the global X axis be plotted versus station or location.

![输入示例或输出清单，原文 PDF 第 11 页](SACS2024_Global_Loading/proofread_p11_0.png)

[原文 PDF 第 11 页](../../raw/SACS/SACS2024_Global_Loading.pdf#page=11)

#### 2.1.7 Including/Excluding Member and Plate Groups

Members or plates can be either included or excluded from the analysis using the MGRPSL or the PGRPSL lines. If this feature is used, then the method of calculating section forces and moments must be the ‘stress method’. This feature can be used to isolate a part of the structure to get section forces and moments.

### 2.2 WAVE RESPONSE MODE

The Wave Response mode requires a response file as well as a Global Load input file. This mode allows selection of critical time points by monitoring shear and moments at stations or locations specified by the user. The user can also designate the parameters, ie. maximum moment, minimum moment, maximum shear and minimum shear, to be used to determine critical time points.

The program creates a time selection file containing the critical time points based on the user specified criteria. This file can be used by subsequent Wave Response retrieve load analyses to create loading for the time points designated.

#### 2.2.1 Wave Response Options

Wave response options are designated on the WAVRSP line. The number of response files is designated in columns 7-9. The transient time, or the number of second to be ignored in the beginning of each response is input in columns 21-27.

The program can monitor shear and moments in any direction. Enter the number of directions to be monitored in columns 28-30 along with the beginning direction in columns 31-37 and the ending direction in columns 38-44 defined in the structural coordinate system.

By default, the time points producing maximum moment, minimum moment, maximum shear and minimum shear are flagged for each station or location. The forces and/or moments to be used to determine critical time points can be designated in columns 45-48 by inputting a ‘Y’ or ‘N’ in the appropriate column as follows:

| Column | Description |
| --- | --- |
| 45 | Maximum Moment |
| 46 | Minimum Moment |
| 47 | Maximum Shear |
| 48 | Minimum Shear |

The following stipulates that 1 response file is to be used. Only one direction, 0.0 degree which corresponds to shear along the global X axis and moment about the global Y axis, is to be monitored. Critical time points are those producing maximum moment and maximum shear at the locations specified.

![输入示例或输出清单，原文 PDF 第 12 页](SACS2024_Global_Loading/proofread_p12_0.png)

[原文 PDF 第 12 页](../../raw/SACS/SACS2024_Global_Loading.pdf#page=12)

### 2.3 DIFFRACTION WAVE MODE

If the SACS input file represents the results of a wave diffraction analysis, then wave data must be input.

In particular, if responses due to waves are to be calculated, the SACS input file must have been created by the SACS/WAMITTM converter or the SACS/MORA TM converter. This file contains information about the direction, period, and wave height use to create the load cases.

#### 2.3.1 Still Water Plus Wave

If the model file or OCI file contains the dead load case as well as the wave load data, then section forces and moments can be calculated for any combination of wave height, wave period, wave direction, and wave phase angle effects added to the still water case.

The wave data including height, period, direction and phase angle must be specified on the SWPW line. This allows the printing and plotting of hogging and sagging conditions, etc.

#### 2.3.2 Section Force Versus Wave Spectrum Periods

Any section force or moment at any station can be plotted versus wave spectrum period for any wave height or direction. The period used in the plots can be either the peak period or the mean period. The wave spectrum types can be either Pierson-Moskowitz or JONSWAP. This is calculated by integrating the section transfer function squared times the wave spectrum at each of the period values.

#### 2.3.3 Wave Spectra Specification

There are two ways to enter the wave spectra, using the WSPEC data record for individual wave spectra or to use the scatter diagram input discussed later. The WSPEC data entry is primarily intended for short term wave responses and the scatter diagram for long term although either can be used for both. This entry specifies either a Pierson-Moskowitz, JONSWAP, or user input wave spectrum. If the spectra are to be used for long term distribution calculations, then the fraction of life applicable for this spectrum is also required.

#### 2.3.4 Wave Scatter Diagram

Generally for long term distribution analysis, the environmental conditions are described using a wave scatter diagram. This information describes all the environmental conditions that the location of structure has seen for some period of time. For example, the scatter diagram could represent the number of 3 hour conditions for 35 years. This information is input to the program using the SCDIR, SCATD, SCOFAC, SCWAV, SCPER, and SCEND data records. The SCDIR data specifies the direction of the scatter diagram, fraction of time spent in this direction, and whether the previous scatter diagram is to be repeated.

The SCATD data record specifies the overall wave spectrum parameters such as wave spectrum type (Pierson-Moskowitz, JONSWAP, or Ochi-Hubble) and the associated parameters for each type. It also has an automatic normalization provision where it then makes no difference if the input is in percent of time spent, number of 3 hour storms, etc. The SCOFAC data is optional and is used to specify factors for different wave heights to be applied to the wave scatter data. This is useful where the same scatter diagram is used for multiple direction but the time spent in the particular wave heights varies with direction. The SCWAV data specifies the wave heights in the scatter diagram. The SCPER data specifies the wave period and the wave scatter for each of the wave heights at this period. The SCEND data record is used to terminate the scatter diagram input.

#### 2.3.5 Response Selection Data

The response selection data enables the user to select the response as a section force or moment, deflection, or reaction. Other options include specifying either short term or long term and what wave spreading power is to be used if any. As many response data records as needed can be used to obtain all the desired results.

## 3 COMMENTARY

The Global Load analysis uses two methods to calculate the section forces and moments at a cross-section. The first method is the ‘load method’ which sums up all loads including reactions on one side of the plane. The second method sums up the element internal forces and moments for all elements cut by the plane.

### 3.1 LOAD METHOD

The section forces and moments are calculated by summing the forces and moments on one side of the cut plane. If the cut plane is the YZ plane then the axis is the X-axis. In this case, the force and moment summations can be expressed as:

$$F_{x} = \sum f_{x_{i}}$$

$$F_{y} = \sum f_{y_{i}}$$

$$F_{z} = \sum f_{z_{i}}$$

$$M_{x} = \sum m_{x_{i}} + \sum f_{z_{i}} y_{i} - \sum f_{y_{i}} z_{i}$$

$$M_{y} = \sum m_{y_{i}} + \sum f_{x_{i}} z_{i} - \sum f_{z_{i}} x_{i}$$

$$M_{z} = \sum m_{z_{i}} + \sum f_{y_{i}} x_{i} - \sum f_{x_{i}} y_{i}$$

where ‘f’ and ‘m’ are the applied joint loads and moments respectively. The summation is for joints whose X values are greater than the station X value.

### 3.2 STRESS METHOD

The stress method involve cutting each element at the station plane and summing the cut forces and moments to obtain the overall section loads.

## 4 SAMPLE PROBLEMS

The structure shown in the figure was used in Sample Problems 1, 2 and 3 to illustrate capabilities of the Global Load Analysis program.

1. Sample Problem 1 demonstrates the use of the Global Load Analysis program to:

a. Obtain plots of section forces versus station.\
b. Generate RAO plots\
c. Show use of naval architecture nomenclature\
d. Obtain plots of section force versus wave spectrum period\
e. Generate still water plus wave condition.

2. Sample Problem 2 uses the Global Load Analysis program to demonstrate the short term probability analyses.\
3. Sample Problem 3 demonstrates long term probability capability.\
4. Sample Problem 4 illustrates the ability to select critical time points from a response file, generated by the Wave Response module, containing data for multiple random wave surface profiles.

### 4.1 SAMPLE PROBLEM 1

The following figure is the structure used in Sample Problems 1, 2, and 3.

BARGE MODEL

![](SACS2024_Global_Loading/e1d3c9c177221d6e950b0ab79ab4d7d9ccef91d0573c14d9667945ad2907557a.jpg)\
Figure 1 Barge Model

The input data for Sample Problem 1 is as follows:

![输入示例或输出清单，原文 PDF 第 16 页](SACS2024_Global_Loading/proofread_p16_1.png)

[原文 PDF 第 16 页](../../raw/SACS/SACS2024_Global_Loading.pdf#page=16)

A. The first line is the optional analysis title.\
B. The Global Load Analysis options selecting the input echo, YZ global plane, and English units. The ‘NA’ in columns 33-34 specifies the naval architecture nomenclature is to be used.

C. The RANGE data record specifies that 51 equally spaced points beginning at - 164.0 feet along the X-axis and ending at +164.0 feet.

D. This PLOT data record request that the vertical moment be plotted versus station.\
E. This PLOT data record request that an RAO plot be generated for the vertical moment at station 0.0 be plotted versus period.\
F. The SFVP is the section force versus wave spectrum period at station 0.0 for wave direction t 45 degrees using the peak period varying from 2.5 to 15.0 seconds in 100 steps. The wave spectrum type is Pierson-Moskowitz with a significant wave height of 32.8 feet.

G. This is the still water plus wave condition. This requires that the first load case in the analysis be a still water case which includes the buoyancy and dead loads. For the case in particular, the wave height is 49.2 feet at a period of 3.75 seconds and direction of 45 degrees. The wave phase angle is 90 degrees.

The following are some of the neutral picture plots and a portion of the output listing file created by the Global Load Analysis program module:

![](SACS2024_Global_Loading/d6b2703f8e177d32fe6d7c1c0c31d70bc924b07b60044fff874e1626eaefa23a.jpg)\
Figure 2 Vertical Moment versus Station for Wave Case

![](SACS2024_Global_Loading/3d940632e9a00523f95beb68b64c1de9bbe3b1f9079de733b2ea0078127fc14e.jpg)\
Figure 3 Vertical Moment versus Station for Dead Load Case

![](SACS2024_Global_Loading/3a201e4955c48845f6e846566ca463c75d68e9067b7f0a6f6b2484e6d0082630.jpg)\
Figure 4 Vertical Moment RAO

![](SACS2024_Global_Loading/63a809d439bf4d080b40a938d45b1645122ee398e40f11b34628a6dedad2097a.jpg)\
Figure 5 Vertical Moment versus Wave Spectrum Period

![](SACS2024_Global_Loading/cbed6a075505024729c12cd58ed6cbb751becaf9ae69208029c62529ee3b628a.jpg)\
Global Load Analysis Options

![](SACS2024_Global_Loading/eca0ba2277eb100e61a15a4ec540c0afb1cb37322416fccae697683a4f447dc7.jpg)\
Load Case Description

![输入示例或输出清单，原文 PDF 第 21 页](SACS2024_Global_Loading/proofread_p21_0.png)

[原文 PDF 第 21 页](../../raw/SACS/SACS2024_Global_Loading.pdf#page=21)

![输入示例或输出清单，原文 PDF 第 22 页](SACS2024_Global_Loading/proofread_p22_0.png)

[原文 PDF 第 22 页](../../raw/SACS/SACS2024_Global_Loading.pdf#page=22)

### 4.2 SAMPLE PROBLEM 2

Sample Problem 2 uses the same structural model as Sample Problem 1. The purpose for this sample is to demonstrate the use of the Global Load Analysis program to predict short term responses.

Below is the Global Load Analysis input file used for Sample Problem 2. A detailed description of the input file follows:

![输入示例或输出清单，原文 PDF 第 23 页](SACS2024_Global_Loading/proofread_p23_0.png)

[原文 PDF 第 23 页](../../raw/SACS/SACS2024_Global_Loading.pdf#page=23)

A. The first line is the optional analysis title.\
B. The Global Load Analysis options selecting the input echo, YZ global plane, and English units. The ‘NA’ in columns 33-34 specifies the naval architecture nomenclature is to be used.\
C. The RANGE data record specifies that 11 equally spaced points beginning at -164.0 feet along the X-axis and ending at +164.0 feet.\
D. The WSPEC data records specify the wave direction, type of wave spectrum, peak wave period, and significant wave height.\
E. The RSPSEL data record selects a vertical moment at the 0.0 station. The probability level not to be exceeded is 10 -3.\
F. This RSPSEL is the same as the preceding, except that wave spreading has been included.

A portion of the output print file is as follows:

![输入示例或输出清单，原文 PDF 第 24 页](SACS2024_Global_Loading/proofread_p24_0.png)

[原文 PDF 第 24 页](../../raw/SACS/SACS2024_Global_Loading.pdf#page=24)

### 4.3 SAMPLE PROBLEM 3

Sample Problem 3 uses the same structural model as Sample Problem 1. The purpose for this sample is to demonstrate the use of the Global Load Analysis program to predict long term responses.

Below is the Global Load Analysis input file used for Sample Problem 3. A detailed description of the input file follows:

![输入示例或输出清单，原文 PDF 第 25 页](SACS2024_Global_Loading/proofread_p25_0.png)

[原文 PDF 第 25 页](../../raw/SACS/SACS2024_Global_Loading.pdf#page=25)

A. The Global Load Analysis options selecting the input echo, YZ global plane, and English units. The ‘NA’ in columns 33-34 specifies the naval architecture nomenclature is to be used.\
B. The RANGE data record specifies that 50 equally spaced points beginning at -164.0 feet along the X-axis and ending at +164.0 feet.\
C. The SCDIR data record specifies this scatter diagram is for the wave direction of 0.0 and the fraction of time for this direction is 0.33333.

D. The SCATD data record specifies that the periods in the scatter diagram represent dominant or peak spectral periods. It also specifies that the data in the scatter diagram is to be normalized and that the spectrum type is to be Pierson-Moskowitz.\
E. The SCOFAC is an optional data record and is used to change the amount of time spent in each wave height. If the\
F. The SCWAV data record specifies the wave heights for the scatter diagram. Note that if more than 11 wave heights are entered, the remaining are located on the next data record.\
G. The SCPER data record specifies period and the number of occurrences for that period. The position in the SCPER record corresponds to the wave height position on the SCWAV data record.\
H. The SCEND data record terminates the scatter diagram input.\
I. This SCDIR data record starts the scatter diagram for the 45 degree wave direction.\
J. This SCDIR data record starts the scatter diagram for the 90 degree wave direction.\
K. This RSPSEL data record selects the vertical moment at the 0.0 station as the desired response and request a long term probability using a wave spreading power of 2. The maximum response value is 60000. FT-KIPS and uses 20 divisions for the short term responses. The Weibull fit defaults to the least square fit.\
L. This RSPSEL data record is the same as before except that the Weibull fit is based on the last 2 values of the short term distribution..\
M. This RSPSEL data record is the same as in K except that 40 division are elected.

The following is a portion of the output print file created by the above input:

![输入示例或输出清单，原文 PDF 第 27 页](SACS2024_Global_Loading/proofread_p27_0.png)

[原文 PDF 第 27 页](../../raw/SACS/SACS2024_Global_Loading.pdf#page=27)

![](SACS2024_Global_Loading/42ac91fe9f448e6440ecb8bbd16edf95b8e204d891da023456df027053b20ff4.jpg)\
Sample Problem 3 - Long Term Results

![](SACS2024_Global_Loading/437560feef5d8d38425ffd3d786e692bc404a3db8a7cb86e82803c9fd5acaeb5.jpg)\
Figure 6 Weibull Distribution Using Least Squares Fit

![](SACS2024_Global_Loading/d57049ab1c5eaa9125bd0d477781ff3b91e0b203ecd488903788376091835943.jpg)\
Figure 7 Weibull Distribution Using Last Two Points Fit

![](SACS2024_Global_Loading/dd1a57c0d85f2bc7abdad5bcd0752440950644a78f5d61868ba4bdb6088a877d.jpg)\
Figure 8 Weibull Distribution Using 40 Points

### 4.4 SAMPLE PROBLEM 4

This sample uses a response file generated by Wave Response to determine critical time points.

Elevations 0.0, -50, -150, -250, -550, -800, -1050, -1200 and -1400 will be used to determine the critical positions based on maximum shear and moment. The Global loading input file along with a description follows:

![输入示例或输出清单，原文 PDF 第 32 页](SACS2024_Global_Loading/proofread_p32_0.png)

[原文 PDF 第 32 页](../../raw/SACS/SACS2024_Global_Loading.pdf#page=32)

The following describes the input lines in the Global Loading input file:

A. The GMOPT line specifies that the structure locations are in the XY plane by ‘XY’ in columns 13-14.:\
B. The WAVRSP line is used to input response parameters and indicates the following:.

a. One response file is to be used as input as designated by ‘1’ in columns 7-9.\
b. Only one wave approach direction, namely ‘0.0’ is to be considered.\
c. Critical time points will be determined by checking the elevations designated for maximum shear and maximum moment. Minimum moment and shear will not be considered.

C. Plots will be generated for moment about the Y axis and shear along the X axis versus time.\
D. Plots will be generated for moment about the Y axis and shear along the X axis versus station or elevation.

E. The wave height spectral density is defined using the WSPEC line as follows:

a. Ochi-Hubble spectrum is to be used as stipulated by ‘OH’ in columns 11-12.\
b. The swell period and significant wave height are 16 and 11.8, respectively.\
c. The time duration is to be 60.0 seconds as designated in columns 48-54.

F. The locations to be checked are input on the LOCATE line as 0, -50, -150, -250, -550, -800, - 1050, -1200 and -1399.9.

A portion of the output listing file including the time point selection data follows.

![输入示例或输出清单，原文 PDF 第 33 页](SACS2024_Global_Loading/proofread_p33_0.png)

[原文 PDF 第 33 页](../../raw/SACS/SACS2024_Global_Loading.pdf#page=33)

![](SACS2024_Global_Loading/447f90ad91dd8587f63dd91802571deb24e0eeb479f7f6774375d8e84d03f008.jpg)

From the Global Loading output, only three time points are required to define load cases representing the maximum shear and moment cases at the desired elevations, namely Seed 1 time point 60, seed 2 time point 58 and seed 2 time point 59. A load case consisting of equivalent static loads will be retrieved from the response file for each of the critical cases.

Note: The critical time point information is saved in the time selection file created by the Global Loading program. This file may be specified when creating the retrieve load run file or the time points may be specified by the user.

## 5 INPUT LINES

> 本节按原始 PDF 的书签层级恢复输入记录分组；各记录附原文页码链接。表头中的层级信息已合并到各字段名称中，空白字段、默认值和单位按原文保留。

### 5.1 INPUT FILE

#### 5.1.1 DIFFRACTION WAVE MODE

##### 5.1.1.1 END - END DATA

[原文 PDF 第 36 页](../../raw/SACS/SACS2024_Global_Loading.pdf#page=36)

**GENERAL** THIS LINE IS THE LAST RECORD OF THE GLOBAL LOADING INPUT FILE.

**( 1- 3)** ENTER 'END'.

| LINE LABEL | LEAVE THIS FIELD BLANK |
| --- | --- |
| END |  |
| 1-- 3 | 4--------------------------80 |

##### 5.1.1.2 GLAOPT - GLOBAL LOAD OPTIONS

[原文 PDF 第 37 页](../../raw/SACS/SACS2024_Global_Loading.pdf#page=37)

**GENERAL** THIS DATA IS REQUIRED FOR ANY GLOBAL LOADING EXECUTION. IT SPECIFIES OVERALL ANALYSIS PARAMETERS AND TYPE OF ANALYSIS.

**(11-12)** ENTER 'EC' IF A LISTING OF THE INPUT DATA IS TO BE INCLUDED IN THE OUTPUT LISTING FILE.

**(14-15)** ENTER THE PLANE USED TO CUT THE STRUCTURE AS 'XY','YZ', OR 'ZX'.

**(17-18)** LEAVE BLANK IF THE UNITS ON THE COMMON SOLUTION FILE ARE TO BE USED. OTHERWISE, SELECT FROM THE FOLLOWING UNITS:\
'EN' - ENGLISH.\
'MN' - METRIC (KILONEWTONS).\
'ME' - METRIC (KILOGRAMS).

**(30-31)** ENTER 'EX' TO USE APPLIED LOADS (EXTERNAL LOAD) OR 'SM' FOR STRESS (INTERNAL LOAD) METHOD.

**(33-34)** ENTER 'NA' TO USE NAVAL ARCHITECTURE NOMENCLATURE.

**(46-61)** ENTER THE LOCATION OF THE AXIS ABOUT WHICH MOMENTS DUE TO FORCES NORMAL TO THE DESIGNATED PLANE ARE CALCULATED. ENTER THE X AND Y ORIGINS WHEN USING THE XY PLANE, ENTER THE Y AND Z ORIGINS WHEN USING THE YZ PLANE, AND ENTER THE Z AND X ORIGINS WHEN USING THE ZX PLANE.

| LINE LABEL | INPUT ECHO OPTION | PLANE SELECTION | UNITS OPTION | OUTPUT SELECTIONS / LOAD METHOD | OUTPUT SELECTIONS / NAVAL ARCH | AXIS ORIGIN COORDINATES / Y FOR YZ Z FOR ZX X FOR XY | AXIS ORIGIN COORDINATES / Z FOR YZ X FOR ZX Y FOR XY | LEAVE BLANK |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| GLAOPT |  |  |  |  |  |  |  |  |
| 1-- 6 | 11--12 | 14--15 | 17--18 | 30--31 | 33--34 | 46<--53 | 54<--61 | 62--80 |
| DEFAULT |  | 'YZ' |  |  |  |  |  |  |
| ENGLISH |  |  |  |  |  | FT | FT |  |
| METRIC |  |  |  |  |  | M | M |  |

##### 5.1.1.3 LOCATE - LOCATION SPECIFICATION DATA

[原文 PDF 第 38 页](../../raw/SACS/SACS2024_Global_Loading.pdf#page=38)

**GENERAL** THIS RECORD ALLOWS THE SPECIFICATION OF LOCATIONS WHERE THE CUTS ARE TO OCCUR. FOR EXAMPLE, IF THE DESIGNATED PLANE IS 'YZ', THEN THESE VALUES ARE THE 'X' STRUCTURAL COORDINATES. THIS RECORD CAN BE REPEATED AS DESIRED.

**( 8-15)** ENTER THE FIRST POSITION.

**(16-79)** ENTER THE REMAINING POSITIONS.

| LINE LABEL | SPECIFIC LOCATIONS / 1ST | SPECIFIC LOCATIONS / 2ND | SPECIFIC LOCATIONS / 3RD | SPECIFIC LOCATIONS / 4TH | SPECIFIC LOCATIONS / 5TH | SPECIFIC LOCATIONS / 6TH | SPECIFIC LOCATIONS / 7TH | SPECIFIC LOCATIONS / 8TH | SPECIFIC LOCATIONS / 9TH |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LOCATE |  |  |  |  |  |  |  |  |  |
| 1-- 6 | 8<--15 | 16<--23 | 24<--31 | 32<--39 | 40<--47 | 48<--55 | 65<--63 | 64<--71 | 72<--79 |
| DEFAULT |  |  |  |  |  |  |  |  |  |
| ENGLISH | FT | FT | FT | FT | FT | FT | FT | FT | FT |
| METRIC | M | M | M | M | M | M | M | M | M |

##### 5.1.1.4 MGRPSL - MEMBER GROUP IDENTIFIER SELECTION DATA

[原文 PDF 第 39 页](../../raw/SACS/SACS2024_Global_Loading.pdf#page=39)

**GENERAL** THIS RECORD ALLOWS THE SELECTION OF MEMBER GROUPS TO BE INCLUDED OR EXCLUDED IN THIS ANALYSIS.

**( 8 )** ENTER 'I' TO INCLUDE THESE MEMBER GROUPS OR 'E' TO EXCLUDE. ALL MEMBER GROUP SELECTION SHOULD BE INCLUDES OR EXCLUDES AND NOT MIXED.

**(10-68)** ENTER THE MEMBER GROUP IDENTIFIERS.

| LINE LABEL | SELECTION TYPE | MEMBER GROUP IDENTIFIER SELECTION / 1ST | MEMBER GROUP IDENTIFIER SELECTION / 2ND | MEMBER GROUP IDENTIFIER SELECTION / 3RD | MEMBER GROUP IDENTIFIER SELECTION / 4TH | MEMBER GROUP IDENTIFIER SELECTION / 5TH | MEMBER GROUP IDENTIFIER SELECTION / 6TH | MEMBER GROUP IDENTIFIER SELECTION / 7TH | MEMBER GROUP IDENTIFIER SELECTION / 8TH | MEMBER GROUP IDENTIFIER SELECTION / 9TH | MEMBER GROUP IDENTIFIER SELECTION / 10TH | MEMBER GROUP IDENTIFIER SELECTION / 11TH | MEMBER GROUP IDENTIFIER SELECTION / 12TH | MEMBER GROUP IDENTIFIER SELECTION / 13TH | MEMBER GROUP IDENTIFIER SELECTION / 14TH | MEMBER GROUP IDENTIFIER SELECTION / 15TH | LEAVE BLANK |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MGRPSL |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 1-- 6 | 8 | 10--12 | 14--16 | 18--20 | 22--24 | 26--28 | 30--32 | 34--36 | 38--40 | 42--44 | 46--48 | 50--52 | 54--56 | 58--60 | 62--64 | 66--68 | 69--80 |
| DEFAULT | 'I' |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

##### 5.1.1.5 PGRPSL - PLATE GROUP IDENTIFIER SELECTION DATA

[原文 PDF 第 40 页](../../raw/SACS/SACS2024_Global_Loading.pdf#page=40)

**GENERAL** THIS RECORD ALLOWS THE SELECTION OF PLATE GROUPS TO BE INCLUDED OR EXCLUDED IN THIS ANALYSIS.

**( 8 )** ENTER 'I' TO INCLUDE THESE PLATE GROUPS OR 'E' TO EXCLUDE. ALL PLATE GROUP SELECTIONS SHOULD BE INCLUDES OR EXCLUDES AND NOT MIXED.

**(10-68)** ENTER THE PLATE GROUP IDENTIFIERS.

| LINE LABEL | SELECTION TYPE | PLATE GROUP IDENTIFIER SELECTION / 1ST | PLATE GROUP IDENTIFIER SELECTION / 2ND | PLATE GROUP IDENTIFIER SELECTION / 3RD | PLATE GROUP IDENTIFIER SELECTION / 4TH | PLATE GROUP IDENTIFIER SELECTION / 5TH | PLATE GROUP IDENTIFIER SELECTION / 6TH | PLATE GROUP IDENTIFIER SELECTION / 7TH | PLATE GROUP IDENTIFIER SELECTION / 8TH | PLATE GROUP IDENTIFIER SELECTION / 9TH | PLATE GROUP IDENTIFIER SELECTION / 10TH | PLATE GROUP IDENTIFIER SELECTION / 11TH | PLATE GROUP IDENTIFIER SELECTION / 12TH | PLATE GROUP IDENTIFIER SELECTION / 13TH | PLATE GROUP IDENTIFIER SELECTION / 14TH | PLATE GROUP IDENTIFIER SELECTION / 15TH | LEAVE BLANK |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PGRPSL |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 1-- 6 | 8 | 10--12 | 14--16 | 18--20 | 22--24 | 26--28 | 30--32 | 34--36 | 38--40 | 42--44 | 46--48 | 50--52 | 54--56 | 58--60 | 62--64 | 66--68 | 69--80 |
| DEFAULT | 'I' |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

##### 5.1.1.6 PLOT - PLOT SPECIFICATIONS

[原文 PDF 第 41 页](../../raw/SACS/SACS2024_Global_Loading.pdf#page=41)

**GENERAL** THIS LINE ALLOWS THE SELECTION OF PLOTS TO BE CREATED.

**( 6- 7)** ENTER THE FORCE TYPE TO BE USED AS THE DEPENDENT VARIABLE: \*\*\*\*\*\*\*\* STANDARD \*\*\*\*\*\*\*\* \*\*\* NAVAL ARCHITECTURE \*\*\*\
'FX' - FORCE IN X-DIRECTION\
'AX' - AXIAL FORCE\
'FY' - FORCE IN Y-DIRECTION\
'HS' - HORIZONTAL SHEAR\
'FZ' - FORCE IN Z-DIRECTION\
'VS' - VERTICAL SHEAR\
'MX' - MOMENT ABOUT X-AXIS\
'TQ' - TORSION\
'MY' - MOMENT ABOUT Y-AXIS\
'VM' - VERTICAL MOMENT\
'MZ' - MOMENT ABOUT Z-AXIS\
'HM' - HORIZONTAL MOMENT

**(10-12)** ENTER THE INDEPENDENT VARIABLE IDENTIFIER:\
'STA' - STATION.\
'PER' - PERIOD.\
'FRQ' - FREQUENCY.\
'TIM' - TIME (WAVE RESPONSE ONLY).

**(14-42)** SELECT FROM THE FOLLOWING OPTIONS:\
'SL' - SEPARATE LOAD CASES OR SURFACE PROFILES.

**(43-50)** IF THIS PLOT IS VERSUS PERIOD OR FREQUENCY, ENTER THE STATION THAT THE PLOT IS TO BE CREATED.

| LINE LABEL | FORCE TYPE | INDEPENDENT VARIABLE | PLOT OPTIONS / 1ST | PLOT OPTIONS / 2ND | PLOT OPTIONS / 3RD | PLOT OPTIONS / 4TH | PLOT OPTIONS / 5TH | PLOT OPTIONS / 6TH | PLOT OPTIONS / 7TH | PLOT OPTIONS / 8TH | PLOT OPTIONS / 9TH | PLOT OPTIONS / 10TH | STATION FOR RAO PLOTS | LEAVE BLANK |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PLOT |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 1-- 4 | 6-- 7 | 10--12 | 14--15 | 17--18 | 20--21 | 23--24 | 26--27 | 29--30 | 32--33 | 35--36 | 38--39 | 41--42 | 43<--50 | 51--80 |
| DEFAULT |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ENGLISH |  |  |  |  |  |  |  |  |  |  |  |  | FT |  |
| METRIC |  |  |  |  |  |  |  |  |  |  |  |  | M |  |

##### 5.1.1.7 RANGE - RANGE SPECIFICATION DATA

[原文 PDF 第 42 页](../../raw/SACS/SACS2024_Global_Loading.pdf#page=42)

**GENERAL** THIS RECORD ALLOWS THE SPECIFICATION OF LOCATIONS WHERE THE CUTS ARE TO OCCUR. FOR EXAMPLE, IF THE DESIGNATED PLANE IS 'YZ', THEN THESE VALUES ARE THE 'X' STRUCTURAL COORDINATES. THIS RECORD CAN BE REPEATED AS DESIRED.

**( 8-10)** ENTER THE NUMBER OF POSITIONS. THIS INCLUDES THE STARTING AND ENDING POSITIONS.

**(11-18)** ENTER THE STARTING COORDINATE.

**(19-26)** ENTER THE ENDING COORDINATE.

**(28-46)** ENTER NEXT RANGE IF DESIRED.

**(48-66)** ENTER NEXT RANGE IF DESIRED.

| LINE LABEL | 1ST RANGE / NUMBER OF POSITIONS | 1ST RANGE / STARTING COORDINATE | 1ST RANGE / ENDING COORDINATE | 2ND RANGE / NUMBER OF POSITIONS | 2ND RANGE / STARTING COORDINATE | 2ND RANGE / ENDING COORDINATE | 3RD RANGE / NUMBER OF POSITIONS | 3RD RANGE / STARTING COORDINATE | 3RD RANGE / ENDING COORDINATE | LEAVE BLANK |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RANGE |  |  |  |  |  |  |  |  |  |  |
| 1-- 5 | 8-->10 | 11<--18 | 19<--26 | 28-->30 | 31<--38 | 39<--46 | 48-->50 | 51<--58 | 59<--66 | 67--80 |
| DEFAULT |  |  |  |  |  |  |  |  |  |  |
| ENGLISH |  | FT | FT |  | FT | FT |  | FT | FT |  |
| METRIC |  | M | M |  | M | M |  | M | M |  |

##### 5.1.1.8 RSPSEL - RESPONSE SELECTION DATA

[原文 PDF 第 43 页](../../raw/SACS/SACS2024_Global_Loading.pdf#page=43)

**GENERAL** THIS RECORD ALLOWS THE CALCULATION OF RESPONSES FOR LONG OR SHORT TERM ANALYSES.

**( 8-11)** ENTER THE RESPONSE TYPE:\
'SFRC' - SECTION FORCE.\
'DEFL' - DEFLECTION.\
'REAC' - REACTION FORCE.

**(13-14)** ENTER THE RESPONSE IDENTIFIER: \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* SECTION FORCE \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* \*\*\*\*\*\*\*\* STANDARD \*\*\*\*\*\*\*\* \*\*\* NAVAL ARCHITECTURE \*\*\*\
'FX' - FORCE IN X-DIRECTION\
'AX' - AXIAL FORCE\
'FY' - FORCE IN Y-DIRECTION\
'HS' - HORIZONTAL SHEAR\
'FZ' - FORCE IN Z-DIRECTION\
'VS' - VERTICAL SHEAR\
'MX' - MOMENT ABOUT X-AXIS\
'TQ' - TORSION\
'MY' - MOMENT ABOUT Y-AXIS\
'VM' - VERTICAL MOMENT\
'MZ' - MOMENT ABOUT Z-AXIS\
'HM' - HORIZONTAL MOMENT \*\*\*\*\*\*\*\* REACTION \*\*\*\*\*\*\*\* \*\*\*\*\*\*\* DEFLECTION \*\*\*\*\*\*\*\
'FX' - FORCE IN X-DIRECTION\
'DX' - X-DEFLECTION\
'FY' - FORCE IN Y-DIRECTION\
'DY' - Y-DEFLECTION\
'FZ' - FORCE IN Z-DIRECTION\
'DZ' - Z-DEFLECTION\
'MX' - MOMENT ABOUT X-AXIS\
'RX' - X-ROTATION\
'MY' - MOMENT ABOUT Y-AXIS\
'RY' - Y-ROTATION\
'MZ' - MOMENT ABOUT Z-AXIS\
'RZ' - Z-ROTATION

**(16-19)** ENTER THE JOINT NAME FOR REACTION OR DEFLECTION RESPONSE.

**(20-26)** ENTER THE STATION FOR SECTION FORCE.

**(27-28)** SELECT EITHER SHORT OR LONG TERM RESPONSE.

**(29-30)** IF WAVE SPREADING IS TO BE USED, ENTER THE WAVE SPREADING POWER. (SPREADING FUNCTION IS COSINE TO THIS POWER.)

**(31-41)** ENTER ONLY ONE OF THE FOLLOWING:

**(31-39)** PERCENT PROBABILITY LEVEL OF EXCEEDANCE.

**(40-41)** NEGATIVE OF LOG TO THE BASE 10 OF ONE MINUS THE PROBABILITY OF EXCEEDANCE. EXAMPLE: AN ENTRY OF 3 WOULD CORRESPOND TO 99.9 PERCENT.

**(45-52)** MAXIMUM RESPONSE LEVEL FOR PROBABILITY POINTS: \* TYPE \* \*\* ENGLISH \*\* \*\* METRIC-KN \*\* \*\* METRIC-KG \*\* FORCE KIP KN TONNE MOMENT KIP-FT KN-M TONNE-M DEFLECTION IN CM CM ROTATION RADIANS RADIANS RADIANS

**(53-55)** NUMBER OF PROBABILITY POINTS TO BE CREATED. THE PROGRAM CALCULATES THE PROBABILITY OF EXCEEDANCE OF POINTS UP TO THE MAXIMUM RESPONSE LEVEL.

**(56-57)** SELECT FROM THE FOLLOWING METHODS OF CREATING THE WEIBULL PARAMETERS:\
'LS' - LEAST-SQUARES FIT.\
'L2' - LAST TWO POINTS FIT.

| LINE LABEL | RESPONSE TYPE | RESPONSE ID | JOINT NAME | STATION | LONG OR SHORT TERM OPTION | WAVE SPREAD POWER | SHORT TERM (SELECT ONE) / PROBABILITY LEVEL OF EXCEEDANCE | SHORT TERM (SELECT ONE) / LOG BASE 10 LEVEL OF EXCEEDANCE | LONG TERM PARAMETERS / THRESHOLD VALUE OF RESPONSE | LONG TERM PARAMETERS / NUMBER OF PROBABILITY POINTS | LONG TERM PARAMETERS / WEIBULL FIT SELECTION | LEAVE BLANK |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RSPSEL |  |  |  |  |  |  |  |  |  |  |  |  |
| 1-- 6 | 8--11 | 13--14 | 16-->19 | 20<--26 | 27--28 | 29-->30 | 31<--39 | 40-->41 | 45<--52 | 53-->55 | 56--57 | 58--80 |
| DEFAULT |  |  |  |  | 'ST' |  | 99.9 | 3 |  | 50 | 'LS' |  |
| ENGLISH |  |  |  | FT |  |  | PERCENT |  |  |  |  |  |
| METRIC |  |  |  | M |  |  | PERCENT |  |  |  |  |  |

##### 5.1.1.9 SCATD - SCATTER DIAGRAM HEADER RECORD

[原文 PDF 第 44 页](../../raw/SACS/SACS2024_Global_Loading.pdf#page=44)

**GENERAL** THIS RECORD IS USED IF AND ONLY IF A LONG-TERM RESPONSE ANALYSIS IS BEING DONE. IT IS USED IN CONJUNCTION WITH THE 'SCWAV', 'SCPER', AND 'SCOFAC' RECORDS TO DESIGNATE THE WAVE SPECTRAL ENVIRONMENT.

**( 1- 5)** ENTER 'SCATD'.

**( 7 )** SELECT FROM THE FOLLOWING PERIOD TYPES:\
'D' - DOMINANT OR PEAK.\
'S' - SIGNIFICANT OR ZERO UP-CROSSING.

**( 9-14)** IF THE PERIODS ARE TO FACTORED, ENTER THAT FACTOR HERE. OTHERWISE, LEAVE BLANK.

**(15-20)** IF THE WAVE HEIGHTS ARE TO BE FACTORED, ENTER THAT FACTOR HERE. OTHERWISE, LEAVE BLANK.

**(21-26)** ENTER THE FRACTION LIFE FACTOR. THIS CAN BE USED TO CONVERT THE SCATTER DIAGRAM FROM PERCENTS OR PARTS PER THOUSAND BY ENTERING 0.01 OR 0.001, RESPECTIVELY.

**( 27 )** ENTER 'N' IF THE SCATTER DIAGRAM IS TO BE NORMALIZED. THIS WILL FACTOR ALL FREQUENCY OF OCCURRENCE DATA SO THAT THE SUM WILL BE 1.0.

**(32-33)** SELECT THE TYPE OF WAVE SPECTRUM TO BE GENERATED FROM THE FOLLOWING:\
'PM' - PIERSON-MOSKOWITZ SPECTRUM.\
'JS' - JONSWAP SPECTRUM.\
'OH' - OCHI-HUBBLE SPECTRUM.

**(34-45)** ENTER THE VALUES OF THE PARAMETERS "GAMMA" AND "C" REQUIRED TO FULLY DEFINE THE JONSWAP SPECTRUM IF 'JS' IS IN COLUMNS 32-33.

**(46-65)** ENTER THE VALUES OF THE OCHI-HUBBLE PARAMETERS. THE SWELL WAVE HEIGHTS AND PERIODS ARE ENTERED ON THE 'SCWAV' AND 'SCPER' RECORDS, RESPECTIVELY. THE WIND GENERATED WAVE HEIGHTS AND PERIODS ARE ASSUMED THE SAME FOR ALL SCATTER DIAGRAM ENTRIES.

**( 66 )** IF THE OCHI-HUBBLE WIND WAVE HEIGHT ENTRY IS TO BE USED AS A RATIO OF THE SWELL WAVE HEIGHT, ENTER 'R' HERE.

| LINE LABEL | PERIOD TYPE | PERIOD FACTOR | WAVE HEIGHT FACTOR | FRACTION LIFE FACTOR | NORMALIZATION OPTION | WAVE SPECTRUM TYPE | JONSWAP PARAMETERS / "GAMMA" | JONSWAP PARAMETERS / "C" | OCHI-HUBBLE PARAMETERS / WIND GENERATED PARAMETERS / SIGNIFICANT WAVE HEIGHT OR RATIO | OCHI-HUBBLE PARAMETERS / WIND GENERATED PARAMETERS / PEAK PERIOD | OCHI-HUBBLE PARAMETERS / WIND GENERATED PARAMETERS / LAMBDA | OCHI-HUBBLE PARAMETERS / SWELL LAMBDA | OCHI-HUBBLE PARAMETERS / RATIO OPTION | LEAVE BLANK |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SCATD |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 1-- 5 | 7 | 9<--14 | 15<--20 | 21<--26 | 27 | 32--33 | 34<--39 | 40<--45 | 46<--50 | 51<--55 | 56<--60 | 61<--65 | 66 | 67--80 |
| DEFAULT | 'D' | 1 | 1 | 1 |  | 'PM' | 3.3 | 1.525 |  |  | CALCULATED | 2.72 |  |  |
| ENGLISH |  |  |  |  |  |  |  |  | FT | SEC |  |  |  |  |
| METRIC |  |  |  |  |  |  |  |  | M | SEC |  |  |  |  |

##### 5.1.1.10 SCDIR - SCATTER DIAGRAM DIRECTION DATA

[原文 PDF 第 45 页](../../raw/SACS/SACS2024_Global_Loading.pdf#page=45)

**GENERAL** THIS RECORD IS REQUIRED FOR EACH WAVE DIRECTION FOR THE LONG-TERM RESPONSE ANALYSIS. IT IS IMMEDIATELY FOLLOWED BY THE WAVE SCATTER DIAGRAM DATA.

**( 8- 9)** IF THE PREVIOUS SCATTER DIAGRAM IS TO BE REPEATED FOR THIS DIRECTION, ENTER 'RP'.

**(18-24)** ENTER THE ANGLE FOR THIS DIRECTION. THIS MUST CORRESPOND TO THE TRANSFER FUNCTION DIRECTION.

**(25-31)** ENTER THE DURATION FOR EACH SEASTATE IDENTIFIED IN THE SCATTER DIAGRAM.

**(32-38)** ENTER THE FRACTION OF TIME FOR THIS DIRECTION. IF LEFT BLANK, THE DEFAULT IS EQUAL TIME IN ALL DIRECTIONS.

| LINE LABEL | REPEAT PREVIOUS SCATTER DIAGRAM OPTION | DIRECTION | DURATION OF SEASTATE | FRACTION OF TIME FOR THIS DIRECTION | LEAVE BLANK |
| --- | --- | --- | --- | --- | --- |
| SCDIR |  |  |  |  |  |
| 1-- 5 | 8-- 9 | 18<--24 | 25<--31 | 32<--38 | 39------------80 |
| DEFAULT |  |  | 1 | 1.0/NDIR |  |
| ENGLISH |  | DEG | HOURS |  |  |
| METRIC |  | DEG | HOURS |  |  |

##### 5.1.1.11 SCEND - SCEND DATA

[原文 PDF 第 46 页](../../raw/SACS/SACS2024_Global_Loading.pdf#page=46)

LOCATION THIS RECORD IS THE LAST RECORD FOR THE SCATTER DIAGRAM DATA INPUT.

**GENERAL** THE 'SCEND' RECORD TERMINATES THE SCATTER DIAGRAM DATA INPUT.

| LINE LABEL | LEAVE BLANK |
| --- | --- |
| SCEND |  |
| 1-- 5 | 6--------------------------80 |

##### 5.1.1.12 SCOFAC - SCATTER DIAGRAM FREQUENCY OF OCCURRENCE FACTORS

[原文 PDF 第 47 页](../../raw/SACS/SACS2024_Global_Loading.pdf#page=47)

**GENERAL** THIS DATA IS OPTIONAL AND IS USED TO SPECIFY THE DISTRIBUTION OF THE FREQUENCY OF OCCURRENCE BY WAVE HEIGHTS IN THE SCATTER DIAGRAM.

**( 1- 5)** ENTER 'SCOFAC'.

**(13-78)** ENTER THE FREQUENCY OF OCCURRENCE FACTORS FOR EACH OF THE WAVE HEIGHTS FOR THIS SCATTER DIAGRAM.

| LINE LABEL | WAVE HEIGHT FREQUENCY OF OCCURRENCE FACTORS / 1ST | WAVE HEIGHT FREQUENCY OF OCCURRENCE FACTORS / 2ND | WAVE HEIGHT FREQUENCY OF OCCURRENCE FACTORS / 3RD | WAVE HEIGHT FREQUENCY OF OCCURRENCE FACTORS / 4TH | WAVE HEIGHT FREQUENCY OF OCCURRENCE FACTORS / 5TH | WAVE HEIGHT FREQUENCY OF OCCURRENCE FACTORS / 6TH | WAVE HEIGHT FREQUENCY OF OCCURRENCE FACTORS / 7TH | WAVE HEIGHT FREQUENCY OF OCCURRENCE FACTORS / 8TH | WAVE HEIGHT FREQUENCY OF OCCURRENCE FACTORS / 9TH | WAVE HEIGHT FREQUENCY OF OCCURRENCE FACTORS / 10TH | WAVE HEIGHT FREQUENCY OF OCCURRENCE FACTORS / 11TH |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SCOFAC |  |  |  |  |  |  |  |  |  |  |  |
| 1-- 6 | 13--18 | 19--24 | 25--30 | 31--36 | 37--42 | 43--48 | 49--54 | 55--60 | 61--66 | 67--72 | 73--78 |

##### 5.1.1.13 SCPER - SCATTER DIAGRAM FREQUENCY OF OCCURRENCE

[原文 PDF 第 48 页](../../raw/SACS/SACS2024_Global_Loading.pdf#page=48)

**GENERAL** THIS DATA IS USED TO SPECIFY THE FREQUENCY OF OCCURRENCE OF WAVES DURING A PORTION OF THE LIFE OF THE STRUCTURE. EACH ENTRY REPRESENTS THE FRACTION OF THE TIME THAT THE SEASTATE DEFINED BY THIS WAVE HEIGHT AND PERIOD COMBINATION.

**( 1- 5)** ENTER 'SCPER'.

**( 7-12)** ENTER THE PERIOD FOR THIS ROW OF THE SCATTER DIAGRAM.

**(13-78)** ENTER THE FRACTION OF THE TIME THAT THE SEASTATE DEFINED BY THE PERIOD ENTERED IN COLUMNS 7 TO 12 AND THE WAVE HEIGHTS ENTERED ON THE PRECEDING 'SCWAV' RECORD.

| LINE LABEL | PERIOD | FREQUENCY OF OCCURRENCE (FRACTION) / 1ST | FREQUENCY OF OCCURRENCE (FRACTION) / 2ND | FREQUENCY OF OCCURRENCE (FRACTION) / 3RD | FREQUENCY OF OCCURRENCE (FRACTION) / 4TH | FREQUENCY OF OCCURRENCE (FRACTION) / 5TH | FREQUENCY OF OCCURRENCE (FRACTION) / 6TH | FREQUENCY OF OCCURRENCE (FRACTION) / 7TH | FREQUENCY OF OCCURRENCE (FRACTION) / 8TH | FREQUENCY OF OCCURRENCE (FRACTION) / 9TH | FREQUENCY OF OCCURRENCE (FRACTION) / 10TH | FREQUENCY OF OCCURRENCE (FRACTION) / 11TH |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SCPER |  |  |  |  |  |  |  |  |  |  |  |  |
| 1-- 5 | 7<--12 | 13--18 | 19--24 | 25--30 | 31--36 | 37--42 | 43--48 | 49--54 | 55--60 | 61--66 | 67--72 | 73--78 |
| DEFAULT |  |  |  |  |  |  |  |  |  |  |  |  |
| ENGLISH | SEC |  |  |  |  |  |  |  |  |  |  |  |
| METRIC | SEC |  |  |  |  |  |  |  |  |  |  |  |

##### 5.1.1.14 SCWAV - SCATTER DIAGRAM WAVE HEIGHTS

[原文 PDF 第 49 页](../../raw/SACS/SACS2024_Global_Loading.pdf#page=49)

**GENERAL** THIS DATA IS USED TO SPECIFY THE WAVE HEIGHTS OF A SCATTER DIAGRAM. EACH ENTRY REPRESENTS CENTER WAVE HEIGHT OF A RANGE OF WAVE HEIGHTS.

**( 1- 5)** ENTER 'SCWAV'.

**(13-78)** ENTER THE WAVE HEIGHTS FOR THIS SCATTER DIAGRAM. THESE WAVE HEIGHTS ALONG WITH THE FOLLOWING PERIODS AND FREQUENCY OF OCCURRENCE DATA CONSTITUTE THE SCATTER DIAGRAM.

| LINE LABEL | WAVE HEIGHTS / 1ST | WAVE HEIGHTS / 2ND | WAVE HEIGHTS / 3RD | WAVE HEIGHTS / 4TH | WAVE HEIGHTS / 5TH | WAVE HEIGHTS / 6TH | WAVE HEIGHTS / 7TH | WAVE HEIGHTS / 8TH | WAVE HEIGHTS / 9TH | WAVE HEIGHTS / 10TH | WAVE HEIGHTS / 11TH |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SCWAV |  |  |  |  |  |  |  |  |  |  |  |
| 1-- 5 | 13<--18 | 19<--24 | 25<--30 | 31<--36 | 37<--42 | 43<--48 | 49<--54 | 55<--60 | 61<--66 | 67<--72 | 73<--78 |
| DEFAULT |  |  |  |  |  |  |  |  |  |  |  |
| ENGLISH | FT | FT | FT | FT | FT | FT | FT | FT | FT | FT | FT |
| METRIC | M | M | M | M | M | M | M | M | M | M | M |

##### 5.1.1.15 SFVP - SECTION FORCE VERSUS PERIOD DATA

[原文 PDF 第 50 页](../../raw/SACS/SACS2024_Global_Loading.pdf#page=50)

**GENERAL** THIS RECORD ALLOWS THE CALCULATION OF LOADS VERSUS SPECTRUM WAVE PERIOD AT A PARTICULAR STATION.

**( 6- 7)** ENTER THE IDENTIFIER OF THE SECTION FORCE. \*\*\*\*\*\*\*\* STANDARD \*\*\*\*\*\*\*\* \*\*\* NAVAL ARCHITECTURE \*\*\*\
'FX' - FORCE IN X-DIRECTION\
'AX' - AXIAL FORCE\
'FY' - FORCE IN Y-DIRECTION\
'HS' - HORIZONTAL SHEAR\
'FZ' - FORCE IN Z-DIRECTION\
'VS' - VERTICAL SHEAR\
'MX' - MOMENT ABOUT X-AXIS\
'TQ' - TORSION\
'MY' - MOMENT ABOUT Y-AXIS\
'VM' - VERTICAL MOMENT\
'MZ' - MOMENT ABOUT Z-AXIS\
'HM' - HORIZONTAL MOMENT

**( 8-15)** ENTER THE STATION FOR THIS FORCE.

**(16-23)** ENTER THE WAVE DIRECTION.

**( 24 )** ENTER THE TYPE OF SPECTRUM PERIOD:\
'P' - PEAK.\
'M' - MEAN.

**(25-32)** ENTER THE BEGINNING SPECTRUM PERIOD. THIS WILL BE THE BEGINNING OF THE INDEPENDENT VARIABLE FOR PLOTTING.

**(33-40)** ENTER THE ENDING SPECTRUM PERIOD.

**(41-43)** ENTER THE NUMBER OF PERIOD STEPS.

**(44-45)** ENTER THE SPECTRUM TYPE FROM THE FOLLOWING:\
'PM' - PIERSON-MOSKOWITZ.\
'JS' - JONSWAP.

**(46-53)** ENTER THE SIGNIFICANT WAVE HEIGHT FOR THIS SPECTRUM.

**(54-69)** ENTER THE JONSWAP PARAMETERS.

| LINE LABEL | SECTION FORCE ID | STATION | WAVE DIRECTION | SPECTRUM PERIOD TYPE | BEGINNING PERIOD | ENDING PERIOD | NUMBER OF PERIOD STEPS | WAVE SPECTRUM TYPE | SIGNIFICANT WAVE HEIGHT | JONSWAP PARAMETERS / "GAMMA" | JONSWAP PARAMETERS / "C" | LEAVE BLANK |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SFVP |  |  |  |  |  |  |  |  |  |  |  |  |
| 1-- 4 | 6-- 7 | 8<--15 | 16<--23 | 24 | 25<--32 | 33<--40 | 41-->43 | 44--45 | 46<--53 | 54<--61 | 62<--69 | 70--80 |
| DEFAULT |  |  |  | 'P' |  |  | 40 | 'PM' |  | 3.3 | 1.525 |  |
| ENGLISH |  | FT | DEG |  | SEC | SEC |  |  | FT |  |  |  |
| METRIC |  | M | DEG |  | SEC | SEC |  |  | M |  |  |  |

##### 5.1.1.16 SWPW - STILL WATER PLUS WAVE DATA

[原文 PDF 第 51 页](../../raw/SACS/SACS2024_Global_Loading.pdf#page=51)

**GENERAL** THIS RECORD ALLOWS THE CALCULATION OF LOADS VERSUS STATION TO BE CREATED FOR A SPECIFIC WAVE INCLUDING THE DEAD LOADS FROM THE STILL WATER CONDITION.

**( 8- 9)** ENTER 'PL' IF THIS LOADING IS TO BE PLOTTED VERSUS STATION.

**(15-22)** ENTER THE WAVE HEIGHT. THIS WAVE HEIGHT IS USED TO FACTOR THE LOADINGS FROM THE WAVES REPRESENTED BY THE INPUT LOAD CONDITIONS.

**(23-30)** ENTER THE WAVE PERIOD. THIS PERIOD MUST CORRESPOND TO A WAVE PERIOD CONTAINED IN THE INPUT LOAD CONDITIONS.

**(31-38)** ENTER THE WAVE DIRECTION. THIS DIRECTION MUST CORRESPOND TO A WAVE DIRECTION CONTAINED IN THE INPUT LOAD CONDITIONS.

**(39-46)** ENTER THE PHASE ANGLE TO BE USED TO CALCULATE THE LOADING FROM THE REAL AND IMAGINARY COMPONENTS OF THE INPUT LOADINGS.

| LINE LABEL | PLOT OPTION | WAVE HEIGHT | WAVE PERIOD | WAVE DIRECTION | WAVE PHASE | LEAVE BLANK |
| --- | --- | --- | --- | --- | --- | --- |
| SWPW |  |  |  |  |  |  |
| 1-- 4 | 8-- 9 | 15<--22 | 23<--30 | 31<--38 | 39<--46 | 47--80 |
| DEFAULT |  |  |  |  |  |  |
| ENGLISH |  | FT | SEC | DEG | DEG |  |
| METRIC |  | M | SEC | DEG | DEG |  |

##### 5.1.1.17 GLOBAL MODELING ANALYSIS TITLE

[原文 PDF 第 52 页](../../raw/SACS/SACS2024_Global_Loading.pdf#page=52)

LOCATION IF INPUT, THIS OPTIONAL LINE IS FIRST IN THE GLOBAL LOADING ANALYSIS INPUT FILE.

**GENERAL** THIS LINE IS OPTIONAL AND ALLOWS THE USER TO SPECIFY A TITLE FOR GLOBAL LOADING ANALYSIS OUTPUT OTHER THAN THE TITLE OF THE SACS IV DECK.

**( 2-80)** ENTER ANY ALPHANUMERIC TITLE. THIS TITLE WILL APPEAR ON ALL PAGES OF GLOBAL LOADING ANALYSIS OUTPUT.

| DESCRIPTIVE TITLE |
| --- |
| 2----------------------------80 |

##### 5.1.1.18 WSPEC - WAVE SPECTRAL DENSITY SPECIFICATION DATA

[原文 PDF 第 53 页](../../raw/SACS/SACS2024_Global_Loading.pdf#page=53)

**GENERAL** THIS DATA IS USED IF AND ONLY IF A SHORT TERM SPECTRAL ANALYSIS IS BEING DONE. IT IS USED TO DESIGNATE THE FORM OF THE WAVE HEIGHT SPECTRAL DENSITY FUNCTION.

**( 1- 5)** ENTER 'WSPEC'.

**( 7- 9)** ENTER THE WAVE DIRECTION NUMBER. THIS NUMBER MUST CORRESPOND TO THE TRANSFER FUNCTION DIRECTION NUMBER.

**(11-12)** ENTER THE TYPE OF SPECTRUM TO BE USED FOR THE WAVE HEIGHT SPECTRAL DENSITY FUNCTION. CHOOSE FROM THE FOLLOWING:\
'PM' - PIERSON-MOSKOWITZ SPECTRUM. THIS IS THE DEFAULT.\
'JS' - JONSWAP SPECTRUM.\
'US' - USER-DEFINED SPECTRUM.

**(13-19)** ENTER THE "SIGNIFICANT WAVE HEIGHT" FOR THIS SPECTRUM.

**(20-26)** ENTER THE "DOMINANT PERIOD" FOR THIS SPECTRUM.

**(27-33)** ENTER THE FRACTION OF THE DESIGN LIFE THAT THE STRUCTURE WILL BE SUBJECT TO THIS SPECTRUM.

**(34-47)** ENTER THE VALUES OF THE PARAMETERS "GAMMA" AND "C" REQUIRED TO FULLY DEFINE THE JONSWAP SPECTRUM IF 'JS' IS IN COLUMNS 11-12.

| LINE LABEL | DIRECTION NUMBER | WAVE SPECTRUM TYPE | WAVE SPECTRUM PARAMETERS / SIGNIFICANT WAVE HEIGHT | WAVE SPECTRUM PARAMETERS / DOMINANT (PEAK) PERIOD | FRACTION OF DESIGN LIFE | JONSWAP PARAMETERS / "GAMMA" | JONSWAP PARAMETERS / "C" | LEAVE BLANK |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| WSPEC |  |  |  |  |  |  |  |  |
| 1-- 5 | 7--> 9 | 11--12 | 13<--19 | 20<--26 | 27<--33 | 34<--40 | 41<--47 | 48--80 |
| DEFAULT |  | 'PM' |  |  |  | 3.3 | 1.525 |  |
| ENGLISH |  |  | FT | SEC |  |  |  |  |
| METRIC |  |  | M | SEC |  |  |  |  |

#### 5.1.2 GENERAL MODE INPUT

##### 5.1.2.1 END - END DATA

[原文 PDF 第 54 页](../../raw/SACS/SACS2024_Global_Loading.pdf#page=54)

**GENERAL** THIS LINE IS THE LAST RECORD OF THE GLOBAL LOADING INPUT FILE.

**( 1- 3)** ENTER 'END'.

| LINE LABEL | LEAVE THIS FIELD BLANK |
| --- | --- |
| END |  |
| 1-- 3 | 4--------------------------80 |

##### 5.1.2.2 GLAOPT - GLOBAL LOAD OPTIONS

[原文 PDF 第 55 页](../../raw/SACS/SACS2024_Global_Loading.pdf#page=55)

**GENERAL** THIS DATA IS REQUIRED FOR ANY GLOBAL LOADING EXECUTION. IT SPECIFIES OVERALL ANALYSIS PARAMETERS AND TYPE OF ANALYSIS.

**(11-12)** ENTER 'EC' IF A LISTING OF THE INPUT DATA IS TO BE INCLUDED IN THE OUTPUT LISTING FILE.

**(14-15)** ENTER THE PLANE USED TO CUT THE STRUCTURE AS 'XY','YZ', OR 'ZX'.

**(17-18)** LEAVE BLANK IF THE UNITS ON THE COMMON SOLUTION FILE ARE TO BE USED. OTHERWISE, SELECT FROM THE FOLLOWING UNITS:\
'EN' - ENGLISH.\
'MN' - METRIC (KILONEWTONS).\
'ME' - METRIC (KILOGRAMS).

**(30-31)** ENTER 'EX' TO USE APPLIED LOADS (EXTERNAL LOAD) OR 'SM' FOR STRESS (INTERNAL LOAD) METHOD.

**(33-34)** ENTER 'NA' TO USE NAVAL ARCHITECTURE NOMENCLATURE.

**(46-61)** ENTER THE LOCATION OF THE AXIS ABOUT WHICH MOMENTS DUE TO FORCES NORMAL TO THE DESIGNATED PLANE ARE CALCULATED. ENTER THE X AND Y ORIGINS WHEN USING THE XY PLANE, ENTER THE Y AND Z ORIGINS WHEN USING THE YZ PLANE, AND ENTER THE Z AND X ORIGINS WHEN USING THE ZX PLANE.

| LINE LABEL | INPUT ECHO OPTION | PLANE SELECTION | UNITS OPTION | OUTPUT SELECTIONS / LOAD METHOD | OUTPUT SELECTIONS / NAVAL ARCH | AXIS ORIGIN COORDINATES / Y FOR YZ Z FOR ZX X FOR XY | AXIS ORIGIN COORDINATES / Z FOR YZ X FOR ZX Y FOR XY | LEAVE BLANK |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| GLAOPT |  |  |  |  |  |  |  |  |
| 1-- 6 | 11--12 | 14--15 | 17--18 | 30--31 | 33--34 | 46<--53 | 54<--61 | 62--80 |
| DEFAULT |  | 'YZ' |  |  |  |  |  |  |
| ENGLISH |  |  |  |  |  | FT | FT |  |
| METRIC |  |  |  |  |  | M | M |  |

##### 5.1.2.3 LOCATE - LOCATION SPECIFICATION DATA

[原文 PDF 第 56 页](../../raw/SACS/SACS2024_Global_Loading.pdf#page=56)

**GENERAL** THIS RECORD ALLOWS THE SPECIFICATION OF LOCATIONS WHERE THE CUTS ARE TO OCCUR. FOR EXAMPLE, IF THE DESIGNATED PLANE IS 'YZ', THEN THESE VALUES ARE THE 'X' STRUCTURAL COORDINATES. THIS RECORD CAN BE REPEATED AS DESIRED.

**( 8-15)** ENTER THE FIRST POSITION.

**(16-79)** ENTER THE REMAINING POSITIONS.

| LINE LABEL | SPECIFIC LOCATIONS / 1ST | SPECIFIC LOCATIONS / 2ND | SPECIFIC LOCATIONS / 3RD | SPECIFIC LOCATIONS / 4TH | SPECIFIC LOCATIONS / 5TH | SPECIFIC LOCATIONS / 6TH | SPECIFIC LOCATIONS / 7TH | SPECIFIC LOCATIONS / 8TH | SPECIFIC LOCATIONS / 9TH |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LOCATE |  |  |  |  |  |  |  |  |  |
| 1-- 6 | 8<--15 | 16<--23 | 24<--31 | 32<--39 | 40<--47 | 48<--55 | 65<--63 | 64<--71 | 72<--79 |
| DEFAULT |  |  |  |  |  |  |  |  |  |
| ENGLISH | FT | FT | FT | FT | FT | FT | FT | FT | FT |
| METRIC | M | M | M | M | M | M | M | M | M |

##### 5.1.2.4 MGRPSL - MEMBER GROUP IDENTIFIER SELECTION DATA

[原文 PDF 第 57 页](../../raw/SACS/SACS2024_Global_Loading.pdf#page=57)

**GENERAL** THIS RECORD ALLOWS THE SELECTION OF MEMBER GROUPS TO BE INCLUDED OR EXCLUDED IN THIS ANALYSIS.

**( 8 )** ENTER 'I' TO INCLUDE THESE MEMBER GROUPS OR 'E' TO EXCLUDE. ALL MEMBER GROUP SELECTION SHOULD BE INCLUDES OR EXCLUDES AND NOT MIXED.

**(10-68)** ENTER THE MEMBER GROUP IDENTIFIERS.

| LINE LABEL | SELECTION TYPE | MEMBER GROUP IDENTIFIER SELECTION / 1ST | MEMBER GROUP IDENTIFIER SELECTION / 2ND | MEMBER GROUP IDENTIFIER SELECTION / 3RD | MEMBER GROUP IDENTIFIER SELECTION / 4TH | MEMBER GROUP IDENTIFIER SELECTION / 5TH | MEMBER GROUP IDENTIFIER SELECTION / 6TH | MEMBER GROUP IDENTIFIER SELECTION / 7TH | MEMBER GROUP IDENTIFIER SELECTION / 8TH | MEMBER GROUP IDENTIFIER SELECTION / 9TH | MEMBER GROUP IDENTIFIER SELECTION / 10TH | MEMBER GROUP IDENTIFIER SELECTION / 11TH | MEMBER GROUP IDENTIFIER SELECTION / 12TH | MEMBER GROUP IDENTIFIER SELECTION / 13TH | MEMBER GROUP IDENTIFIER SELECTION / 14TH | MEMBER GROUP IDENTIFIER SELECTION / 15TH | LEAVE BLANK |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MGRPSL |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 1-- 6 | 8 | 10--12 | 14--16 | 18--20 | 22--24 | 26--28 | 30--32 | 34--36 | 38--40 | 42--44 | 46--48 | 50--52 | 54--56 | 58--60 | 62--64 | 66--68 | 69--80 |
| DEFAULT | 'I' |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

##### 5.1.2.5 PGRPSL - PLATE GROUP IDENTIFIER SELECTION DATA

[原文 PDF 第 58 页](../../raw/SACS/SACS2024_Global_Loading.pdf#page=58)

**GENERAL** THIS RECORD ALLOWS THE SELECTION OF PLATE GROUPS TO BE INCLUDED OR EXCLUDED IN THIS ANALYSIS.

**( 8 )** ENTER 'I' TO INCLUDE THESE PLATE GROUPS OR 'E' TO EXCLUDE. ALL PLATE GROUP SELECTIONS SHOULD BE INCLUDES OR EXCLUDES AND NOT MIXED.

**(10-68)** ENTER THE PLATE GROUP IDENTIFIERS.

| LINE LABEL | SELECTION TYPE | PLATE GROUP IDENTIFIER SELECTION / 1ST | PLATE GROUP IDENTIFIER SELECTION / 2ND | PLATE GROUP IDENTIFIER SELECTION / 3RD | PLATE GROUP IDENTIFIER SELECTION / 4TH | PLATE GROUP IDENTIFIER SELECTION / 5TH | PLATE GROUP IDENTIFIER SELECTION / 6TH | PLATE GROUP IDENTIFIER SELECTION / 7TH | PLATE GROUP IDENTIFIER SELECTION / 8TH | PLATE GROUP IDENTIFIER SELECTION / 9TH | PLATE GROUP IDENTIFIER SELECTION / 10TH | PLATE GROUP IDENTIFIER SELECTION / 11TH | PLATE GROUP IDENTIFIER SELECTION / 12TH | PLATE GROUP IDENTIFIER SELECTION / 13TH | PLATE GROUP IDENTIFIER SELECTION / 14TH | PLATE GROUP IDENTIFIER SELECTION / 15TH | LEAVE BLANK |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PGRPSL |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 1-- 6 | 8 | 10--12 | 14--16 | 18--20 | 22--24 | 26--28 | 30--32 | 34--36 | 38--40 | 42--44 | 46--48 | 50--52 | 54--56 | 58--60 | 62--64 | 66--68 | 69--80 |
| DEFAULT | 'I' |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

##### 5.1.2.6 PLOT - PLOT SPECIFICATIONS

[原文 PDF 第 59 页](../../raw/SACS/SACS2024_Global_Loading.pdf#page=59)

**GENERAL** THIS LINE ALLOWS THE SELECTION OF PLOTS TO BE CREATED.

**( 6- 7)** ENTER THE FORCE TYPE TO BE USED AS THE DEPENDENT VARIABLE: \*\*\*\*\*\*\*\* STANDARD \*\*\*\*\*\*\*\* \*\*\* NAVAL ARCHITECTURE \*\*\*\
'FX' - FORCE IN X-DIRECTION\
'AX' - AXIAL FORCE\
'FY' - FORCE IN Y-DIRECTION\
'HS' - HORIZONTAL SHEAR\
'FZ' - FORCE IN Z-DIRECTION\
'VS' - VERTICAL SHEAR\
'MX' - MOMENT ABOUT X-AXIS\
'TQ' - TORSION\
'MY' - MOMENT ABOUT Y-AXIS\
'VM' - VERTICAL MOMENT\
'MZ' - MOMENT ABOUT Z-AXIS\
'HM' - HORIZONTAL MOMENT

**(10-12)** ENTER THE INDEPENDENT VARIABLE IDENTIFIER:\
'STA' - STATION.\
'PER' - PERIOD.\
'FRQ' - FREQUENCY.\
'TIM' - TIME (WAVE RESPONSE ONLY).

**(14-42)** SELECT FROM THE FOLLOWING OPTIONS:\
'SL' - SEPARATE LOAD CASES OR SURFACE PROFILES.

**(43-50)** IF THIS PLOT IS VERSUS PERIOD OR FREQUENCY, ENTER THE STATION THAT THE PLOT IS TO BE CREATED.

| LINE LABEL | FORCE TYPE | INDEPENDENT VARIABLE | PLOT OPTIONS / 1ST | PLOT OPTIONS / 2ND | PLOT OPTIONS / 3RD | PLOT OPTIONS / 4TH | PLOT OPTIONS / 5TH | PLOT OPTIONS / 6TH | PLOT OPTIONS / 7TH | PLOT OPTIONS / 8TH | PLOT OPTIONS / 9TH | PLOT OPTIONS / 10TH | STATION FOR RAO PLOTS | LEAVE BLANK |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PLOT |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 1-- 4 | 6-- 7 | 10--12 | 14--15 | 17--18 | 20--21 | 23--24 | 26--27 | 29--30 | 32--33 | 35--36 | 38--39 | 41--42 | 43<--50 | 51--80 |
| DEFAULT |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ENGLISH |  |  |  |  |  |  |  |  |  |  |  |  | FT |  |
| METRIC |  |  |  |  |  |  |  |  |  |  |  |  | M |  |

##### 5.1.2.7 RANGE - RANGE SPECIFICATION DATA

[原文 PDF 第 60 页](../../raw/SACS/SACS2024_Global_Loading.pdf#page=60)

**GENERAL** THIS RECORD ALLOWS THE SPECIFICATION OF LOCATIONS WHERE THE CUTS ARE TO OCCUR. FOR EXAMPLE, IF THE DESIGNATED PLANE IS 'YZ', THEN THESE VALUES ARE THE 'X' STRUCTURAL COORDINATES. THIS RECORD CAN BE REPEATED AS DESIRED.

**( 8-10)** ENTER THE NUMBER OF POSITIONS. THIS INCLUDES THE STARTING AND ENDING POSITIONS.

**(11-18)** ENTER THE STARTING COORDINATE.

**(19-26)** ENTER THE ENDING COORDINATE.

**(28-46)** ENTER NEXT RANGE IF DESIRED.

**(48-66)** ENTER NEXT RANGE IF DESIRED.

| LINE LABEL | 1ST RANGE / NUMBER OF POSITIONS | 1ST RANGE / STARTING COORDINATE | 1ST RANGE / ENDING COORDINATE | 2ND RANGE / NUMBER OF POSITIONS | 2ND RANGE / STARTING COORDINATE | 2ND RANGE / ENDING COORDINATE | 3RD RANGE / NUMBER OF POSITIONS | 3RD RANGE / STARTING COORDINATE | 3RD RANGE / ENDING COORDINATE | LEAVE BLANK |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RANGE |  |  |  |  |  |  |  |  |  |  |
| 1-- 5 | 8-->10 | 11<--18 | 19<--26 | 28-->30 | 31<--38 | 39<--46 | 48-->50 | 51<--58 | 59<--66 | 67--80 |
| DEFAULT |  |  |  |  |  |  |  |  |  |  |
| ENGLISH |  | FT | FT |  | FT | FT |  | FT | FT |  |
| METRIC |  | M | M |  | M | M |  | M | M |  |

##### 5.1.2.8 GLOBAL MODELING ANALYSIS TITLE

[原文 PDF 第 61 页](../../raw/SACS/SACS2024_Global_Loading.pdf#page=61)

LOCATION IF INPUT, THIS OPTIONAL LINE IS FIRST IN THE GLOBAL LOADING ANALYSIS INPUT FILE.

**GENERAL** THIS LINE IS OPTIONAL AND ALLOWS THE USER TO SPECIFY A TITLE FOR GLOBAL LOADING ANALYSIS OUTPUT OTHER THAN THE TITLE OF THE SACS IV DECK.

**( 2-80)** ENTER ANY ALPHANUMERIC TITLE. THIS TITLE WILL APPEAR ON ALL PAGES OF GLOBAL LOADING ANALYSIS OUTPUT.

| DESCRIPTIVE TITLE |
| --- |
| 2----------------------------80 |

#### 5.1.3 WAVE RESPONSE MODE

##### 5.1.3.1 END - END DATA

[原文 PDF 第 62 页](../../raw/SACS/SACS2024_Global_Loading.pdf#page=62)

**GENERAL** THIS LINE IS THE LAST RECORD OF THE GLOBAL LOADING INPUT FILE.

**( 1- 3)** ENTER 'END'.

| LINE LABEL | LEAVE THIS FIELD BLANK |
| --- | --- |
| END |  |
| 1-- 3 | 4--------------------------80 |

##### 5.1.3.2 GLAOPT - GLOBAL LOAD OPTIONS

[原文 PDF 第 63 页](../../raw/SACS/SACS2024_Global_Loading.pdf#page=63)

**GENERAL** THIS DATA IS REQUIRED FOR ANY GLOBAL LOADING EXECUTION. IT SPECIFIES OVERALL ANALYSIS PARAMETERS AND TYPE OF ANALYSIS.

**(11-12)** ENTER 'EC' IF A LISTING OF THE INPUT DATA IS TO BE INCLUDED IN THE OUTPUT LISTING FILE.

**(14-15)** ENTER THE PLANE USED TO CUT THE STRUCTURE AS 'XY','YZ', OR 'ZX'.

**(17-18)** LEAVE BLANK IF THE UNITS ON THE COMMON SOLUTION FILE ARE TO BE USED. OTHERWISE, SELECT FROM THE FOLLOWING UNITS:\
'EN' - ENGLISH.\
'MN' - METRIC (KILONEWTONS).\
'ME' - METRIC (KILOGRAMS).

**(30-31)** ENTER 'EX' TO USE APPLIED LOADS (EXTERNAL LOAD) OR 'SM' FOR STRESS (INTERNAL LOAD) METHOD.

**(33-34)** ENTER 'NA' TO USE NAVAL ARCHITECTURE NOMENCLATURE.

**(46-61)** ENTER THE LOCATION OF THE AXIS ABOUT WHICH MOMENTS DUE TO FORCES NORMAL TO THE DESIGNATED PLANE ARE CALCULATED. ENTER THE X AND Y ORIGINS WHEN USING THE XY PLANE, ENTER THE Y AND Z ORIGINS WHEN USING THE YZ PLANE, AND ENTER THE Z AND X ORIGINS WHEN USING THE ZX PLANE.

| LINE LABEL | INPUT ECHO OPTION | PLANE SELECTION | UNITS OPTION | OUTPUT SELECTIONS / LOAD METHOD | OUTPUT SELECTIONS / NAVAL ARCH | AXIS ORIGIN COORDINATES / Y FOR YZ Z FOR ZX X FOR XY | AXIS ORIGIN COORDINATES / Z FOR YZ X FOR ZX Y FOR XY | LEAVE BLANK |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| GLAOPT |  |  |  |  |  |  |  |  |
| 1-- 6 | 11--12 | 14--15 | 17--18 | 30--31 | 33--34 | 46<--53 | 54<--61 | 62--80 |
| DEFAULT |  | 'YZ' |  |  |  |  |  |  |
| ENGLISH |  |  |  |  |  | FT | FT |  |
| METRIC |  |  |  |  |  | M | M |  |

##### 5.1.3.3 LOCATE - LOCATION SPECIFICATION DATA

[原文 PDF 第 64 页](../../raw/SACS/SACS2024_Global_Loading.pdf#page=64)

**GENERAL** THIS RECORD ALLOWS THE SPECIFICATION OF LOCATIONS WHERE THE CUTS ARE TO OCCUR. FOR EXAMPLE, IF THE DESIGNATED PLANE IS 'YZ', THEN THESE VALUES ARE THE 'X' STRUCTURAL COORDINATES. THIS RECORD CAN BE REPEATED AS DESIRED.

**( 8-15)** ENTER THE FIRST POSITION.

**(16-79)** ENTER THE REMAINING POSITIONS.

| LINE LABEL | SPECIFIC LOCATIONS / 1ST | SPECIFIC LOCATIONS / 2ND | SPECIFIC LOCATIONS / 3RD | SPECIFIC LOCATIONS / 4TH | SPECIFIC LOCATIONS / 5TH | SPECIFIC LOCATIONS / 6TH | SPECIFIC LOCATIONS / 7TH | SPECIFIC LOCATIONS / 8TH | SPECIFIC LOCATIONS / 9TH |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LOCATE |  |  |  |  |  |  |  |  |  |
| 1-- 6 | 8<--15 | 16<--23 | 24<--31 | 32<--39 | 40<--47 | 48<--55 | 65<--63 | 64<--71 | 72<--79 |
| DEFAULT |  |  |  |  |  |  |  |  |  |
| ENGLISH | FT | FT | FT | FT | FT | FT | FT | FT | FT |
| METRIC | M | M | M | M | M | M | M | M | M |

##### 5.1.3.4 MGRPSL - MEMBER GROUP IDENTIFIER SELECTION DATA

[原文 PDF 第 65 页](../../raw/SACS/SACS2024_Global_Loading.pdf#page=65)

**GENERAL** THIS RECORD ALLOWS THE SELECTION OF MEMBER GROUPS TO BE INCLUDED OR EXCLUDED IN THIS ANALYSIS.

**( 8 )** ENTER 'I' TO INCLUDE THESE MEMBER GROUPS OR 'E' TO EXCLUDE. ALL MEMBER GROUP SELECTION SHOULD BE INCLUDES OR EXCLUDES AND NOT MIXED.

**(10-68)** ENTER THE MEMBER GROUP IDENTIFIERS.

| LINE LABEL | SELECTION TYPE | MEMBER GROUP IDENTIFIER SELECTION / 1ST | MEMBER GROUP IDENTIFIER SELECTION / 2ND | MEMBER GROUP IDENTIFIER SELECTION / 3RD | MEMBER GROUP IDENTIFIER SELECTION / 4TH | MEMBER GROUP IDENTIFIER SELECTION / 5TH | MEMBER GROUP IDENTIFIER SELECTION / 6TH | MEMBER GROUP IDENTIFIER SELECTION / 7TH | MEMBER GROUP IDENTIFIER SELECTION / 8TH | MEMBER GROUP IDENTIFIER SELECTION / 9TH | MEMBER GROUP IDENTIFIER SELECTION / 10TH | MEMBER GROUP IDENTIFIER SELECTION / 11TH | MEMBER GROUP IDENTIFIER SELECTION / 12TH | MEMBER GROUP IDENTIFIER SELECTION / 13TH | MEMBER GROUP IDENTIFIER SELECTION / 14TH | MEMBER GROUP IDENTIFIER SELECTION / 15TH | LEAVE BLANK |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MGRPSL |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 1-- 6 | 8 | 10--12 | 14--16 | 18--20 | 22--24 | 26--28 | 30--32 | 34--36 | 38--40 | 42--44 | 46--48 | 50--52 | 54--56 | 58--60 | 62--64 | 66--68 | 69--80 |
| DEFAULT | 'I' |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

##### 5.1.3.5 PGRPSL - PLATE GROUP IDENTIFIER SELECTION DATA

[原文 PDF 第 66 页](../../raw/SACS/SACS2024_Global_Loading.pdf#page=66)

**GENERAL** THIS RECORD ALLOWS THE SELECTION OF PLATE GROUPS TO BE INCLUDED OR EXCLUDED IN THIS ANALYSIS.

**( 8 )** ENTER 'I' TO INCLUDE THESE PLATE GROUPS OR 'E' TO EXCLUDE. ALL PLATE GROUP SELECTIONS SHOULD BE INCLUDES OR EXCLUDES AND NOT MIXED.

**(10-68)** ENTER THE PLATE GROUP IDENTIFIERS.

| LINE LABEL | SELECTION TYPE | PLATE GROUP IDENTIFIER SELECTION / 1ST | PLATE GROUP IDENTIFIER SELECTION / 2ND | PLATE GROUP IDENTIFIER SELECTION / 3RD | PLATE GROUP IDENTIFIER SELECTION / 4TH | PLATE GROUP IDENTIFIER SELECTION / 5TH | PLATE GROUP IDENTIFIER SELECTION / 6TH | PLATE GROUP IDENTIFIER SELECTION / 7TH | PLATE GROUP IDENTIFIER SELECTION / 8TH | PLATE GROUP IDENTIFIER SELECTION / 9TH | PLATE GROUP IDENTIFIER SELECTION / 10TH | PLATE GROUP IDENTIFIER SELECTION / 11TH | PLATE GROUP IDENTIFIER SELECTION / 12TH | PLATE GROUP IDENTIFIER SELECTION / 13TH | PLATE GROUP IDENTIFIER SELECTION / 14TH | PLATE GROUP IDENTIFIER SELECTION / 15TH | LEAVE BLANK |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PGRPSL |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 1-- 6 | 8 | 10--12 | 14--16 | 18--20 | 22--24 | 26--28 | 30--32 | 34--36 | 38--40 | 42--44 | 46--48 | 50--52 | 54--56 | 58--60 | 62--64 | 66--68 | 69--80 |
| DEFAULT | 'I' |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

##### 5.1.3.6 PLOT - PLOT SPECIFICATIONS

[原文 PDF 第 67 页](../../raw/SACS/SACS2024_Global_Loading.pdf#page=67)

**GENERAL** THIS LINE ALLOWS THE SELECTION OF PLOTS TO BE CREATED.

**( 6- 7)** ENTER THE FORCE TYPE TO BE USED AS THE DEPENDENT VARIABLE: \*\*\*\*\*\*\*\* STANDARD \*\*\*\*\*\*\*\* \*\*\* NAVAL ARCHITECTURE \*\*\*\
'FX' - FORCE IN X-DIRECTION\
'AX' - AXIAL FORCE\
'FY' - FORCE IN Y-DIRECTION\
'HS' - HORIZONTAL SHEAR\
'FZ' - FORCE IN Z-DIRECTION\
'VS' - VERTICAL SHEAR\
'MX' - MOMENT ABOUT X-AXIS\
'TQ' - TORSION\
'MY' - MOMENT ABOUT Y-AXIS\
'VM' - VERTICAL MOMENT\
'MZ' - MOMENT ABOUT Z-AXIS\
'HM' - HORIZONTAL MOMENT

**(10-12)** ENTER THE INDEPENDENT VARIABLE IDENTIFIER:\
'STA' - STATION.\
'PER' - PERIOD.\
'FRQ' - FREQUENCY.\
'TIM' - TIME (WAVE RESPONSE ONLY).

**(14-42)** SELECT FROM THE FOLLOWING OPTIONS:\
'SL' - SEPARATE LOAD CASES OR SURFACE PROFILES.

**(43-50)** IF THIS PLOT IS VERSUS PERIOD OR FREQUENCY, ENTER THE STATION THAT THE PLOT IS TO BE CREATED.

| LINE LABEL | FORCE TYPE | INDEPENDENT VARIABLE | PLOT OPTIONS / 1ST | PLOT OPTIONS / 2ND | PLOT OPTIONS / 3RD | PLOT OPTIONS / 4TH | PLOT OPTIONS / 5TH | PLOT OPTIONS / 6TH | PLOT OPTIONS / 7TH | PLOT OPTIONS / 8TH | PLOT OPTIONS / 9TH | PLOT OPTIONS / 10TH | STATION FOR RAO PLOTS | LEAVE BLANK |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PLOT |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 1-- 4 | 6-- 7 | 10--12 | 14--15 | 17--18 | 20--21 | 23--24 | 26--27 | 29--30 | 32--33 | 35--36 | 38--39 | 41--42 | 43<--50 | 51--80 |
| DEFAULT |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ENGLISH |  |  |  |  |  |  |  |  |  |  |  |  | FT |  |
| METRIC |  |  |  |  |  |  |  |  |  |  |  |  | M |  |

##### 5.1.3.7 RANGE - RANGE SPECIFICATION DATA

[原文 PDF 第 68 页](../../raw/SACS/SACS2024_Global_Loading.pdf#page=68)

**GENERAL** THIS RECORD ALLOWS THE SPECIFICATION OF LOCATIONS WHERE THE CUTS ARE TO OCCUR. FOR EXAMPLE, IF THE DESIGNATED PLANE IS 'YZ', THEN THESE VALUES ARE THE 'X' STRUCTURAL COORDINATES. THIS RECORD CAN BE REPEATED AS DESIRED.

**( 8-10)** ENTER THE NUMBER OF POSITIONS. THIS INCLUDES THE STARTING AND ENDING POSITIONS.

**(11-18)** ENTER THE STARTING COORDINATE.

**(19-26)** ENTER THE ENDING COORDINATE.

**(28-46)** ENTER NEXT RANGE IF DESIRED.

**(48-66)** ENTER NEXT RANGE IF DESIRED.

| LINE LABEL | 1ST RANGE / NUMBER OF POSITIONS | 1ST RANGE / STARTING COORDINATE | 1ST RANGE / ENDING COORDINATE | 2ND RANGE / NUMBER OF POSITIONS | 2ND RANGE / STARTING COORDINATE | 2ND RANGE / ENDING COORDINATE | 3RD RANGE / NUMBER OF POSITIONS | 3RD RANGE / STARTING COORDINATE | 3RD RANGE / ENDING COORDINATE | LEAVE BLANK |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RANGE |  |  |  |  |  |  |  |  |  |  |
| 1-- 5 | 8-->10 | 11<--18 | 19<--26 | 28-->30 | 31<--38 | 39<--46 | 48-->50 | 51<--58 | 59<--66 | 67--80 |
| DEFAULT |  |  |  |  |  |  |  |  |  |  |
| ENGLISH |  | FT | FT |  | FT | FT |  | FT | FT |  |
| METRIC |  | M | M |  | M | M |  | M | M |  |

##### 5.1.3.8 GLOBAL MODELING ANALYSIS TITLE

[原文 PDF 第 69 页](../../raw/SACS/SACS2024_Global_Loading.pdf#page=69)

LOCATION IF INPUT, THIS OPTIONAL LINE IS FIRST IN THE GLOBAL LOADING ANALYSIS INPUT FILE.

**GENERAL** THIS LINE IS OPTIONAL AND ALLOWS THE USER TO SPECIFY A TITLE FOR GLOBAL LOADING ANALYSIS OUTPUT OTHER THAN THE TITLE OF THE SACS IV DECK.

**( 2-80)** ENTER ANY ALPHANUMERIC TITLE. THIS TITLE WILL APPEAR ON ALL PAGES OF GLOBAL LOADING ANALYSIS OUTPUT.

| DESCRIPTIVE TITLE |
| --- |
| 2----------------------------80 |

##### 5.1.3.9 WAVRSP - WAVE RESPONSE OPTIONS

[原文 PDF 第 70 页](../../raw/SACS/SACS2024_Global_Loading.pdf#page=70)

**GENERAL** THIS DATA IS REQUIRED FOR ANALYZING RESPONSES FROM WAVE RESPONSE ANALYSES. THE TIME HISTORY RESULTS FROM RANDOM WAVE ANALYSES IS ANALYZED TO SELECT THE TIME POINTS CORRESPONDING TO MAXIMUM SECTION FORCES.

**( 7- 9)** ENTER THE NUMBER OF WAVE RESPONSE TIME HISTORY FILES TO BE USED. THESE FILES ARE THE RESPONSE FILES CREATED BY THE WAVE RESPONSE PROGRAM. THESE FILES MUST CONTAIN THE MODAL COORDINATES.

**(21-27)** ENTER NUMBER OF SECONDS TO BE IGNORED IN THE BEGINNING OF EACH WAVE RESPONSE ANALYSIS. THIS TO ELIMINATE ANY TRANSIENT EFFECTS FOR TIME HISTORY ANALYSES.

**(28-30)** ENTER THE NUMBER OF DIRECTIONS FOR SHEAR AND MOMENT CALCULATIONS.

**(31-37)** ENTER THE FIRST DIRECTION ANGLE FOR MOMENT AND SHEAR CALCULATIONS. ANGLE IS MEASURED IN THE GLOBAL COORDINATE SYSTEM FROM X TOWARD Y FOR THE X-Y PLANE, Z TOWARD X FOR THE Z-X PLANE, AND Y TOWARD Z FOR THE Y-Z PLANE.

**(38-44)** ENTER THE FINAL DIRECTION ANGLE FOR THE MOMENT AND SHEAR CALCULATIONS.

**(45-48)** SELECT THE SECTION/LOCATION FORCES AND MOMENTS TO BE CONSIDERED FOR SELECTING CRITICAL TIME POINTS. ENTER 'Y' TO BE INCLUDED OR AN 'N' TO BE IGNORED.

| LINE LABEL | NUMBER OF WAVE RESPONSE FILES | TRANSIENT TIME | MONITOR DIRECTIONS / NUMBER OF DIRECTIONS | MONITOR DIRECTIONS / FIRST ANGLE | MONITOR DIRECTIONS / LAST ANGLE | MONITOR FORCES / MAXIMUM MOMENT | MONITOR FORCES / MINIMUM MOMENT | MONITOR FORCES / MAXIMUM SHEAR | MONITOR FORCES / MINIMUM SHEAR | LEAVE BLANK |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| WAVRSP |  |  |  |  |  |  |  |  |  |  |
| 1-- 6 | 7--> 9 | 21<--27 | 28-->30 | 31<--37 | 38<--44 | 45 | 46 | 47 | 48 | 49----80 |
| DEFAULT | 1 |  | 4 | 0 | 135 | 'Y' | 'Y' | 'Y' | 'Y' |  |
| ENGLISH |  | SEC |  | DEG | DEG |  |  |  |  |  |
| METRIC |  | SEC |  | DEG | DEG |  |  |  |  |  |
