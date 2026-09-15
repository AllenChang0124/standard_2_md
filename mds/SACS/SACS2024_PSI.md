SACS

Pile-Structure Interaction

Version 24.00

Trademark Notice

Bentley and the "B" Bentley logo are either registered or unregistered trademarks or service marks of Bentley Systems, Incorporated. All other marks are the property of their respective owners.

Copyright Notice

Copyright © 2024, Bentley Systems, Incorporated. All Rights Reserved.

TABLE OF CONTENTS

1 INTRODUCTION .. . 6

## 1.1 OVERVIEW.. . 6
## 1.2 PROGRAM FEATURES.. . 6

2 CREATING PSI INPUT . ... 8

## 2.1 DEFINING ANALYSIS OPTIONS... . 8

2.1.1 General Options .... . 8   
2.1.2 Analysis Options.... . 8   
2.1.3 Convergence and Tolerance Criteria.. . 8   
2.1.4 API-RP2A Edition .. . 8   
2.1.5 Pile Options ... . 8   
2.1.6 Output Options . 9

2.1.6.1 Creating a Pile Solution File... 9   
2.1.7 Designating Load Cases for Pile Capacity and Code Check.. . 9

## 2.2 DEFINING PLOT OPTIONS.. 9

2.2.1 Plot Data.... . 9   
2.2.2 Designating Piles to Plot.. .. 10   
2.2.3 Designating Load Cases to Plot .. .10   
2.2.4 Overriding Plot Size .. .. 10

## 2.3 DEFINING THE PILE.. .. 10

2.3.1 Pile Section Properties .... 10   
2.3.2 Pile Group Properties..... 11

2.3.2.1 Pile Group End Bearing Area. .11   
2.3.2.2 Segmented Pile Groups.... .11   
2.3.2.3 Pile Group Surface Dimension Overrides.. .11

2.3.3 Defining Pile Elements .... 12

2.3.3.1 Pile Batter.... . 12   
2.3.3.2 Pile Local Coordinate System ..... . 12

2.3.4 Pile Clusters... .. 14

## 2.4 MODELING SOIL PROPERTIES.. .. 14

2.4.1 Overview ..... .14   
2.4.2 Specifying Elevations for Soil Resistance Curves .... .. 14   
2.4.3 Soil Axial Resistance .. 15

2.4.3.1 Linear Axial Spring... . 15   
2.4.3.2 Generating Adhesion & Bearing Capacity per API-RP2A . . 15   
2.4.3.3 User Defined Adhesion and Bearing Capacity Data. .. 16   
2.4.3.4 Generating T-Z Curves & Bearing Capacity per API-RP2A.. .. 16   
2.4.3.5 Generating T-Z Curves Using CPT-Based Methods . .17   
2.4.3.6 Applying API General Scour Recommendations ..... .. 18   
2.4.3.7 User Defined T-Z Curves..... .. 18   
2.4.3.8 User Defined Bearing Capacity Curves.... . 19

2.4.4 Soil Torsional Resistance... 19

2.4.4.1 Linear Torsional Spring..... .19

2.4.4.2 Soil Torsion Adhesion... .. 19   
2.4.4.3 User Defined ?? − ?? Curves .... ... 20

2.4.5 Soil Lateral Resistance.... . 21

2.4.5.1 Generating P-Y Curves per API-RP2A .. .. 21   
2.4.5.2 User Defined P-Y Curves .... .. 22   
2.4.5.3 Base Shear and Base Moment Effects .... .. 23   
2.4.5.4 User Defined Base Shear and Base Moment Curves .. .. 27   
2.4.5.5 Distributed Moment Effect .. .. 29

2.4.6 Soil Bending Resistance.... .29   
2.4.6.1 User Defined ?? − ?? Curves .... .. 29   
2.4.7 Soil Liquefaction Potential . . 30

## 2.5 CREATING FOUNDATION SUPERELEMENTS. ... 31
2.5.1 Foundation Super Element Options... . 31

## 2.6 SIMULATING MUDSLIDES.. .. 32
## 2.7 INPUTTING PILE HEAD STIFFNESS TABLES .. ... 33

2.7.1 Optional User Defined Pilehead Stiffness Tables.. .. 33

2.7.1.1 Guidelines for Axial Ranges.... .. 33   
2.7.1.2 Guidelines for Lateral Ranges ..... .. 34   
2.7.1.3 Guidelines for Torsional Ranges... .. 35

3 CREATING PILE INPUT... .. 36

## 3.1 OVERVIEW... ... 36
## 3.2 DEFINING ANALYSIS OPTIONS... ... 36

## 3.3 SPECIFYING PLOT OPTIONS.. .. 37

3.3.1 Plot Data.... . 37   
3.3.2 Designating Load Cases to Plot ... . 37   
3.3.3 Overriding Plot Size. . 37   
3.3.4 Plotting Soil Data from PSI Input.. . 38

## 3.4 DEFINING THE PILE.. ... 38

3.4.1 Pile Section Properties .. .. 38   
3.4.2 Pile Group Properties... . 38   
3.4.3 Defining Pile Elements . . 38

3.4.3.1 Pile Batter.... .. 38

3.4.4 Pile Local Coordinate System.. . 39   
3.4.5 Pilehead Spring .. .39

## 3.5 MODELING SOIL PROPERTIES.. ... 40

3.5.1 Overview .... .. 40   
3.5.2 Soil Axial Resistance .... .40

3.5.2.1 Inputting Axial Load Distribution ... .. 40

3.5.3 Soil Torsional Resistance.. .. 40   
3.5.4 Soil Lateral Resistance... .40   
3.5.5 Soil Liquefaction Potential . .. 40

## 3.6 INPUTTING PILEHEAD STIFFNESS TABLES . ... 40
## 3.7 SPECIFYING LOADING FOR ISOLATED PILE ANALYSIS . ... 40
3.7.1 3D Pile Head Load ... .. 41

3.7.2 Specifying Pile Load at Depth.. ... 41   
## 3.8 CREATING A PILE FATIGUE SOLUTION FILE.. ... 42
## 3.9 CREATING A PILE STUB.... .... 43
3.9.1 Pile Stub Loading.. . 43   
## 3.10 CREATING A LOAD/DEFLECTION CURVE FOR SOILS... .... 43

4 COMMENTARY . .45

## 4.1 INTRODUCTION.. .... 45
## 4.2 DERIVATION OF INTERACTION EQUATIONS ... .... 46
## 4.3 ALIGNING TUBULAR PILE LOCAL COORDINATES.. ... 50
## 4.4 API-RP2A PILE RESISTANCE .. .. 50

4.4.1 Axial Resistance... . 51

4.4.1.1 Ultimate Pile Capacity ... . 51   
4.4.1.2 Skin Friction and End Bearing . .51   
4.4.1.3 Soil Axial Load Transfer Curves .... . 52   
4.4.1.4 Tip Load - Displacement Curves.. . 53

4.4.2 Lateral Resistance for Soft Clays .... . 54   
4.4.3 Lateral Resistance for Sand.. . 55

## 4.5 EQUIVALENT PILE STUB.. .. 56

4.5.1 Rules for Modeling a Pile Stub . . 58

## 4.6 PILE CAPACITY CALCULATION .. ... 60
## 4.7 SOIL LIQUEFACTION .. .... 62

5 PISA Method.. .. 65

## 5.1 Background . ... 65
## 5.2 Plaxis Monopile Designer and Pile3D Interoperability ....... ... 65
## 5.3 PISA Method Verification..... .... 66

5.3.1 Soil Data . 66   
5.3.2 Pile Geometries... .. 67

5.3.3 SACS Pile3D Comparison with Monopile Designer 1D FE Analysis .. .. 68

5.3.3.1 Pile3D Input... .. 68   
5.3.3.2 Special Considerations for PISA Sand.. .. 69   
5.3.3.3 Results’ Comparison... . 69

5.3.3.3.1 Cowden Clay Models.. . 69   
5.3.3.3.2 Dunkirk Sand Models . .. 76

## 5.4 Extended Winkler Foundation .82

6 TROUBLESHOOTING COMMON PROBLEMS.. .. 83  
7 SAMPLE PROBLEMS.. .. 85

## 7.1 PILE SOIL INTERACTION ANALYSIS .. ... 86
## 7.2 SINGLE PILE ANALYSIS... .. 96
## 7.3 MUDSLIDE ANALYSIS.. .102

8 REFERENCES . .112   
9 INPUT LINES... ..113

1 INTRODUCTION

## 1.1 OVERVIEW

PSI, Pile Structure Interaction, analyzes the behavior of a pile supported structure subject to one or more static load conditions. Finite deflection of the piles ("P-delta" effect) and nonlinear soil behavior both along and transverse to the pile axis are accounted for. The program uses a finite difference solution to solve the pile model which is represented by a beam column on a nonlinear elastic foundation. The structure resting on the piles is represented as a linear elastic model.

PSI first obtains the pile axial solution, then uses the resulting internal axial forces to obtain the lateral solution of the piles. In general, soils exhibit nonlinear behavior for both axial and transverse loads, therefore an iterative procedure is used to find the pile influence on the deflection of the structure.

## 1.2 PROGRAM FEATURES

PSI is designed to use pile and soil data, specified in an input file, in conjunction with linear structural data produced by the SACS IV program. Among the features of PSI are the following:

1. Tubular and H pile cross sections supported.   
2. Pile may have varying properties along its length.   
3. Soil axial behavior may be represented by adhesion data, nonlinear T-Z data, or as a linear spring.   
4. End bearing effects may be accounted for.   
5. Soil lateral behavior represented by nonlinear P-Y curves.   
6. Basic soil properties may be used to generate the soil axial properties in the form of T-Z curves or adhesion data, end bearing T-Z data and/or lateral soil properties in the form of P-Y curves, based on API-RP2A recommendations.   
7. Soil stratification may be modeled.   
8. Mudslide condition simulation capabilities.   
9. Complete soil property plot capabilities, including P-Y, T-Z and adhesion data.   
10. Analysis results plot capabilities, including deflections, rotations, loads, reactions (soil and pile), and unity check ratios plotted along the pile length.   
11. Creates up to two equivalent linearized foundation super-elements to be used by dynamic analyses in lieu of pile stubs.   
12. Implementation of API RP-2A 21st (Supplement 2 and 3), 22nd editions of soil adhesion, T-Z and P-Y data generation based on basic soil properties.   
13. Creates foundation solution file containing pile stresses to be used for fatigue analysis.

14. Allows the user to designate load cases to be used for pile capacity and code check calculations.

The Pile and Pile3D programs, which are sub-programs of PSI, may be executed alone to calculate the behavior of a single pile. In addition to the features outlined above, the Pile program has the following features:

1. Determines an equivalent pile stub that yields the same deflections and rotations as the soil/pile system.   
2. Allows the application of forces and moments obtained from SACS analyses to create a postfile to be used for a subsequent fatigue analysis.   
3. Calculates the Pile capacity using three different methods.

2 CREATING PSI INPUT

The nonlinear foundation model, including the pile and the soil properties, is specified separately from the model information in a PSI input file.

The interface joints between the linear structure and the nonlinear foundation must be designated in the SACS model by specifying the support condition ‘PILEHD’ on the appropriate JOINT input line. The analysis option ‘PI’ must be specified either on the model OPTIONS line or designated in the Executive.

## 2.1 DEFINING ANALYSIS OPTIONS

Pile/Soil interaction options are input on the PSIOPT line.

2.1.1 General Options

General options such as the upward vertical axis and the units are specified in columns 8-9 and 10-12, respectively. ‘CE’ may be specified in columns 17-18 to have the program continue the analysis regardless of errors encountered in the iteration procedure.

2.1.2 Analysis Options

The final pile stress analysis option is designated in columns 23-24. The pile/structure coupled interaction analysis may be skipped by specifying ‘SK’ in columns 19-20. Likewise, the solution fine tuning procedure may be skipped by entering ‘NA’ in columns 21-22.

2.1.3 Convergence and Tolerance Criteria

The displacement, rotation and force convergence tolerances are designated in columns 25-32, 33-40 and 67-72, respectively. The maximum number of iterations for a pilehead, if other than 20, may be specified in columns 41-43. Solution iteration continues until each degree of freedom at the pilehead has converged to within the specified tolerances or until the maximum number of iterations has been exceeded. Enter 'N' in column 15 if equilibrium relaxation is not to be used. Equilibrium relaxation improves the chances of convergence.

2.1.4 API-RP2A Edition

PSI program can generate soil resistance curves (T-Z, Q-Z, and P-Y) based on different editions of API recommendations. The API edition is selected in columns 59-60. The user may input S2 (for API-RP2A 21stEdition with Supplement 2), S3 (for API-RP2A 21st Edition with Supplement 3) or 22 to use API-RP2A WSD 22nd Edition – leaving this part BLANK results in the default API-RP2A 21st Edition with Supplement 3.

2.1.5 Pile Options

The pile unit weight may be designated in columns 73-80 if the effect of the pile weight is to be included in the analysis. The number of increments that the pile is divided into may be overridden in columns 62- 64.

2.1.6 Output Options

The pile stiffness tables, reduced stiffness matrix of the linear structure and the reduced force vector may be printed by specifying ‘PT’ in columns 44-45, 46-47 or 48-49, respectively. Intermediate iteration results and input data may be printed by specifying ‘PT’ in columns 50-51 and 52-53, respectively.

A sample of the PSIOPT line specifying English units and a density of 490 follows:

```txt
1 2 3 4 5 6 7 8 123456789012345678901234567890123456789012345678901234567890 1 PSIOPT +ZENG 490.0 0 
```

2.1.6.1 Creating a Pile Solution File

A solution file containing pile internal loads and stresses at each increment along the pile may be created. Entered ‘PP’ in columns 54-55 on the OPTIONS line to create a solution file to be read by the Fatigue program. The in-line SCF option used to factor stresses may be specified in columns 56-58 on the OPTIONS line.

Note: The ‘FTG’ option should be specified in columns 56-58 if stresses are to be unfactored so that one of the in-line SCF options available in Fatigue may be used. The final pile analysis option should not be skipped (‘SK’) in columns 19-20.

The following PSIOPT line indicates that a fatigue solution file is to be used. The stresses are not to be factored because they will be factored by the in-line SCF designated in the Fatigue input file.

```txt
1 2 3 4 5 6 7 8 1234567890123456789012345678901234567890123456789012345678901234567890 1 PSIOPT +ZENG Y PPFTG 490.0 
```

An auxiliary detail pile file may be generated by entering ‘PF’ in columns 54-55.

2.1.7 Designating Load Cases for Pile Capacity and Code Check

By default, all load cases solved in the PSI execution are used to code check and calculate pile capacity safety factors. The user may designate which load cases are to be included or excluded for pile check and capacity using the LCSEL line.

Designate whether the load cases listed are to be included or excluded by entering ‘IN’ or ‘EX’, respectively. For example, the following specifies that load cases ‘OP08’, ‘OP09’ and ‘EQ01’ are to be excluded.

```txt
1 2 3 4 5 6 7 8 123456789012345678901234567890123456789012345678901234567890 1 LCSEL EX OP08 OP09 EQ01 
```

## 2.2 DEFINING PLOT OPTIONS

Plot options are designated on the PLTRQ, PLTPL, PLTLC and PLTSZ input lines.

2.2.1 Plot Data

Data to be plotted is designated on the PLTRQ input line. Soil input data, axial deflection, axial load, axial soil reactions, required pile thickness and unity check ratio may be plotted versus pile penetration. A

maximum of 150 soil strata may be plotted. Lateral deflection, lateral rotation, bending moment, shear load and lateral soil reaction along or about the pile local Y and local Z axes may be plotted versus penetration in addition to the resultant. Also, torsional rotation and torsion moments for the case of “User Defined ?? − ?? Curve” may be plotted versus pile penetration.

By default, for any of the result plot options, for each load case a separate plot is generated for each pile. Piles to be plotted may be designated on the PLTPL line while load cases to plot may be designated on the PLTLC line. Alternatively, a plot envelope showing the critical value for all load cases selected may be plotted instead by specifying an ‘E’ (for envelope) after the desired option. Plot appearance options such as grid lines and cross hatching may be designated also.

The following requests soil data plots along with lateral and axial displacement, pile unity check and pile redesign plots:

```txt
1 2 3 4 5 6 7 8 1 23456789012345678901234567890123456789012345678901234567890 PLTRQ SD UC PR 
```

2.2.2 Designating Piles to Plot

By default, plots are generated for each pile defined in the PSI input file. Piles to be plotted may be designated on the PLTPL line be specifying the pilehead joint names of the piles to be included for plotting. The following designates that only piles defined by pilehead joints 4 and 8 are to be included in plots.

```txt
1 2 3 4 5 6 7 8 1 23456789012345678901234567890123456789012345678901234567890 1 PLTPL 4 8 
```

2.2.3 Designating Load Cases to Plot

By default, all load cases are included for plot generation. If load cases are specified on the PLTLC input line, then only load cases specified will be included for plotting purposes. The following designates that only load cases ‘OP00’ and ‘ST90’ are to be plotted.

```txt
1 2 3 4 5 6 7 8 123456789012345678901234567890123456789012345678901234567890PLTLC OP00 ST90 
```

2.2.4 Overriding Plot Size

The default plot paper size, character size, cross hatching spacing and number of colors may be overridden using the PLTSZ line.

## 2.3 DEFINING THE PILE

The geometry and characteristics of piles and conductors below the pileheads, including section and material properties, pile batter, pile chord angle, weight per unit length and several dimension overrides are included in the PSI input file.

2.3.1 Pile Section Properties

Section properties for tubular sections can be calculated directly from the outside diameter and wall thickness input on the PLGRUP line or can be defined on the PLSECT line. Non-tubular sections and/or tubular sections with user defined stiffness properties are defined using PLSECT lines.

When a section label is specified on the PLGRUP line, the properties are determined from the input on the corresponding PLSECT line. For tubular sections, the section label field should be left blank when section properties are to be determined from the outside diameter and wall thickness specified on the PLGRUP line.

When defining section properties using a PLSECT line, the unique cross section label referenced by a subsequent PLGRUP line and the cross-section type are required in columns 8-14 and 16-18, respectively. The cross-section dimensions must be specified in columns 51-74.

The PSI program calculates the cross-section stiffness properties based on the cross-section dimensions input. The calculated stiffness properties may be overridden in columns 19-48. Likewise, the unit weight specified on the PSIOPT may be overridden in columns 75-80.

The following defines the pile section named H47 as an H section:

```txt
1 2 3 4 5 6 7 8 1 234567890123456789012345678901234567890123456789012345678901234567890 PLSECT H47 H 12.0 24.0 8.0 6.0 
```

2.3.2 Pile Group Properties

Pile group properties such as modulus of elasticity, shear modulus, and yield stress are specified on the appropriate PLGRUP line. The group to which a pile is assigned is designated on the PILE line.

2.3.2.1 Pile Group End Bearing Area

The effective end bearing area is specified on the PLGRUP line in columns 75-80. The user may specify end bearing area for each pile segment to model a stepped pile. Normally only the PLGRUP line corresponding to the bottom segment of the pile will have end bearing area specified.

2.3.2.2 Segmented Pile Groups

A series of PLGRUP lines with the same group label is used to define the property group of a segmented pile. Each input line corresponds to one of the segments of that pile group. Material properties of the segment in addition to the segment length are required.

For example, the following defines a 200-foot tubular pile group named ‘PL1’ consisting of two segments. The first segment has a wall thickness of 1.5 and a yield strength of 50.0, while the second has a wall thickness of 0.75 and a yield of 36.0. The length of the first segment is 50 feet while the second is 150 feet long. End bearing area is defined for the second segment only.

```typescript
1 2 3 4 5 6 7 8 12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567891 6.5 PLGRUPPL1 60.0 1.5 29.0 11.6 5.0 50.0 50.0 2 PLGRUPPL1 60.0 0.75 29.0 11.6 5.0 36.0 150.0 
```

Note: The length of each segment must be specified. Also, although the local X axis of the pile is up from the pilehead joint toward the reference joint, segment properties are assigned from the pilehead joint down along the pile. In the above example, the first 50 feet from the pilehead down is defined as 60x1.5.

2.3.2.3 Pile Group Surface Dimension Overrides

By default, the actual dimensions of the pile are used to calculate soil resistance. The surface dimension of a pile group, used for soil resistance calculations, may be overridden on the PLGRUP line in columns

58-69. For tubular piles, the OD and wall thickness are required, while the effective width and depth are input for H sections.

2.3.3 Defining Pile Elements

Pile elements are specified on PILE lines following the PILE header input line. The pile element is named by the pilehead joint in the model to which it is attached. The pilehead joint to which the pile is attached is specified in columns 7-10. The pile group to which the pile is assigned is specified in columns 16-18.

Note: Pilehead joints must be designated as such in the SACS model file by ‘PILEHD’ in columns 55-60 on the corresponding JOINT line.

The soil ID defining pile/soil interaction properties in the local X-Z plane is designated in columns 69-72. If the soil table for local X-Y plane interaction is different from that of the X-Z plane, the applicable soil ID must be specified in columns 74-77.

The following defines a pile connected to pilehead joint 2. The pile is assigned to pile group ‘PL1’ and uses soil table ‘SOL1’.

```txt
1 2 3 4 5 6 7 8 1234567890123456789012345678901234567890123456789012345678901234567890  
1 PILE
2 PILE 2 201 PL1
```

2.3.3.1 Pile Batter

The pile batter is defined by either a batter definition joint specified in columns 11-14 or batter definition coordinates specified in columns 21-50 on the PILE line. The batter of the pile designated below is defined using the pilehead joint and joint 201.

```txt
1 2 3 4 5 6 7 8  
123456789012345678901234567890123456789012345678901234567890  
1 PILE
2 PILE 2 201 PL1
```

Note: When specifying a batter definition joint, the batter definition joint must be above the pilehead joint. The pile will be oriented such that the pile axis lies on the line through the batter definition joint and the pilehead joint.

Batter definition coordinates are used to determine the pile batter if no batter definition joint is specified. The global X, Y and Z distances from the pilehead to any point above it lying on the pile axis should be input in columns 21-30, 31-40 and 41-50, respectively. For example, to define a pile battered 1:8 in the global X-Z plane and vertical in the global Y-Z plane, batter coordinate values of X=1.0, Y=0.0 and Z=8.0 should be entered.

2.3.3.2 Pile Local Coordinate System

The pile default local coordinate system is defined with the local X axis pointing upward from the pilehead joint along the pile axis defined by the pile batter joint or batter coordinates.

![](SACS2024_PSI/chunk0_deb419666d768509f06136134ecf306cd4380cb4f4dcbdd8b2a55d0e7574e242.jpg)

By default, the local Y and Z axis orientations are load case dependent. For each load case, the local Y axis is automatically oriented such that it coincides with the direction of maximum pilehead deflection. The figure on the right illustrates the default local coordinate system of the pile.

The orientation of the local Y and Z axes may be overridden by the user by specifying the rotation angle about the local X axis in columns 51-56 on the PILE line. In this case, the local Y axis will not be aligned in the direction of maximum pilehead deflection but will be defined by the rotation angle as shown in the figure below.

![](SACS2024_PSI/chunk0_38eddf16e105d0cd8f67e5e1e3312c4f1104bc1e02bc93a64f6b22bed2e9afd8.jpg)

Note: The pile analysis is done in the local XZ and XY planes. For mudslide cases, a pile rotation angle should be used to orient either the pile local XZ or XY plane in the direction of the mudslide.

2.3.4 Pile Clusters

Piles driven near other piles can have a different capacity from a single pile acting independently.

Figure 1a. shows a pair of piles near each other. There is a tendency for piles to act as a unit in the direction of the line joining the centers of the two piles. Therefore, the combined resistance for the two piles in this direction, is less than double the resistance of a single pile. In the other direction, however, there is no such interaction and the two piles behave independently.

Figure 1b. shows a cluster of four piles. In this case all four piles will have reduced resistance in both directions. The behavior of such clusters can be modeled by reducing the P-Y curves input for the directions where the piles act as a system rather than independent piles.

![](SACS2024_PSI/chunk0_3924ff9f2e58c294538500c671de4192628f2e05534addb2395796e9468ae2d0.jpg)  
1a

![](SACS2024_PSI/chunk0_947e035a51b38f864792a5b36a774d5f59367498ba3146ada8772c4df467222d.jpg)

![](SACS2024_PSI/chunk0_779e19f07aff8da21b2018788deede3ba0f21173d9b29cc22f2093057606bf1f.jpg)  
1b

## 2.4 MODELING SOIL PROPERTIES

2.4.1 Overview

PSI allows the user to specify the pile/soil response to axial, lateral, and torsional loads applied at the pilehead through nonlinear load deflection curves (P-Y and T-Z curves). Axial resistance can also be specified in terms of linear spring rates and soil adhesion values. In addition, axial bearing capacity may be specified at the pile tip and at arbitrary points along the pile, when modeling piles with varying diameter. In lieu of pile capacity curves or adhesion data, the characteristics of the soil may also be specified in terms of basic soil properties (unit weight, shear strength, etc.), that the program can use to develop the pile/soil response based on API-RP2A recommendations.

The PSI program requires that the soil properties be defined in a specific order, namely axial resistance, bearing capacity, torsional resistance followed by lateral capacity. For axial, bearing and lateral capacity, the soil capacity or properties may be defined at various elevations or soil stratum.

Note: When multiple soils are to be defined, all properties of the first soil must be defined before any properties of the next soil may be specified.

2.4.2 Specifying Elevations for Soil Resistance Curves

Within a soil stratum, the PSI program connects the input P-Y or T-Z points with straight lines to fully define the pile/soil interaction curve for arbitrary displacements in that stratum. At depths between specified soil strata, PSI can linearly interpolate between curves or to use a constant T-Z curve.

When the soil properties are to be assumed constant throughout the depth of a soil stratum, the distances from the pilehead to the top and bottom of the stratum should both be specified. The curve generated is used for the entire depth of the stratum. When soil properties specified apply only to a specific elevation, only the distance to the top of the stratum should be specified. The soil curve generated applies only the specific elevation designated.

Note: If only the distance to the bottom of the stratum is specified, the stiffness is assumed to be constant throughout the depth of the soil stratum.

Soil properties at elevations without resistance curves defined are obtained by interpolating between the curves defined immediately above and below. For example, the first SOIL API AXL line in the sample below, specifies that axial soil properties from elevation 0.0 to 30.0 are constant. The second SOIL API AXL line stipulates that the T-Z curves generated defines soil properties at elevation 60.0. Therefore, axial soil properties at elevations between 30 and 60 will be determined through linear interpolation between the two curves.



|  | 1 | 1 | 2 | 2 | 3 | 3 | 4 | 4 | 5 | 5 | 6 | 6 | 7 | 7 | 8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | 123456789012345678901234567890123456789012345678901234567890 | 123456789012345678901234567890123456789012345678901234567890 | 123456789012345678901234567890123456789012345678901234567890 | 123456789012345678901234567890123456789012345678901234567890 | 123456789012345678901234567890123456789012345678901234567890 | 123456789012345678901234567890123456789012345678901234567890 | 123456789012345678901234567890123456789012345678901234567890 | 123456789012345678901234567890123456789012345678901234567890 | 123456789012345678901234567890123456789012345678901234567890 | 123456789012345678901234567890123456789012345678901234567890 | 123456789012345678901234567890123456789012345678901234567890 | 123456789012345678901234567890123456789012345678901234567890 | 123456789012345678901234567890123456789012345678901234567890 | 123456789012345678901234567890123456789012345678901234567890 | 123456789012345678901234567890123456789012345678901234567890 |
| 1 | SOIL | TZAPI | HEAD | 2 |  |  |  |  | SOL1 |  |  |  |  |  |  |
| 2 | SOIL | API | AXL | SLOC | 0.0 | 30.0 | SAND | 0.8 |  | 93.0 | 30.0 | 500. |  |  |  |
| 3 | SOIL | API | AXL | SLOC | 60.0 |  | SAND | 0.8 |  | 93.0 | 30.0 | 500. |  |  |  |



2.4.3 Soil Axial Resistance

For any soil, the first property that must be defined is the axial resistance or capacity. Axial loads are resisted by distributed longitudinal surface shear forces along the length of the pile and by end bearing forces at the end and at intermediate points where the pile’s outer diameter changes. Axial resistance for a soil may be specified in terms of either a linear axial spring, adhesion (skin friction), or axial load deflection curves (T-Z curves).

2.4.3.1 Linear Axial Spring

Pilehead axial behavior made be modeled as a linear axial spring at the pilehead using the SOIL AXIAL HEAD input line. The soil ID and the linear stiffness of the spring must be specified in columns 41-44 and 31-40, respectively. When using a pilehead axial spring, the axial force in the pile is assumed to linearly dissipate from the pilehead axial force to zero at the end of the pile. No other axial capacity data or bearing capacity data may be specified when assigning an axial spring to a pilehead.

2.4.3.2 Generating Adhesion & Bearing Capacity per API-RP2A

PSI can automatically generate the pile axial adhesion or skin friction and bearing capacity based on API guidelines from basic soil characteristics input by the user.

The SOIL AXIAL HEAD line is required to generate skin friction and bearing capacities from basic soil characteristics. The number of soil strata to be defined and the soil ID or name must be specified in columns 18-20 and 41-44, respectively.

The properties of each stratum making up the soil are specified immediately following the header line using either the sand, clay or rock soil axial stratum line designated by “SOIL API AXL” in columns 1-12. The API 10th Edition is input in column 13 and the stratum location label “SLOC” in columns 14-17 is required. The vertical distance from the pilehead to the top and bottom of the stratum are specified in

columns 19-24 and 25-30, respectively. The soil type and the soil characteristics are input in columns 32- 77.



|  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | 123456789012345678901234567890123456789012345678901234567890 | 123456789012345678901234567890123456789012345678901234567890 | 123456789012345678901234567890123456789012345678901234567890 | 123456789012345678901234567890123456789012345678901234567890 | 123456789012345678901234567890123456789012345678901234567890 | 123456789012345678901234567890123456789012345678901234567890 | 123456789012345678901234567890123456789012345678901234567890 | 123456789012345678901234567890123456789012345678901234567890 |
| 1 | SOIL TZAPI | HEAD | 2 | 250.0 | SOL2 | SOL2 | SOL2 | SOL2 |
| 2 | SOIL API AXL SLOC | SOIL API AXL SLOC | 0.0 | 136.0 | SAND | 0.8 | 93.0 |  |
| 3 | SOIL API AXL SLOC | SOIL API AXL SLOC | 136.0 | 215. | SAND | 0.7 |  |  |
|  | 105.0 |  |  |  |  |  |  |  |



Note: Either a sand, clay or rock soil axial stratum line is required for each soil stratum to be defined.

Axial adhesion capacity is calculated for each soil stratum input. Beginning at the top stratum, the length over which the adhesion must act to dissipate the axial load is computed. If this length is less than the stratum thickness, the axial load is completely dissipated in the current stratum. If the required length is greater than the stratum thickness, the excess pile load into the next stratum below. The procedure is repeated until all the pile load is dissipated or until all stratum have reached capacity. If the total pile load has not been dissipated, the excess load is transferred by end bearing until the end bearing capacity is reached. If the total axial load has not been dissipated, the pile fails.

Note: Because end bearing data is automatically generated, no end bearing data should be specified when generating axial capacity automatically.

2.4.3.3 User Defined Adhesion and Bearing Capacity Data

Adhesion and bearing capacity data may directly input by the user using the Soil Axial Adhesion header line (named SOIL AXIAL HEAD) and specifying the number of soil stratum, the end bearing capacity and the soil ID/name in columns 18-10, 21-30 and 41-44, respectively.

The distance between the pilehead and the top and bottom of each of the soil stratum must be specified on the SOIL SLOC line(s) immediately following the header line. The soil adhesion data for each stratum is defined on the following Soil Axial Adhesion Capacity line(s).



|  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | 12345678901 | 12345678901 | 12345678901 | 12345678901 | 12345678901 | 12345678901 | 12345678901 | 1234567890 |
| 1 | SOIL AXIAL | HEAD | 45.0 |  | SOL1 |  |  |  |
| 2 | SOIL ADHT | SLOC | 30.0 | 30.0 | 50.0 |  |  |  |
| 3 | SOIL ADHA | EXT | 0.1 | 0.1 | 0.16 | 0.16 |  |  |



2.4.3.4 Generating T-Z Curves & Bearing Capacity per API-RP2A

PSI can automatically generate axial load deflection curves (T-Z curves) and bearing load deflection curves (Q-Z curves) based on API guidelines from basic soil characteristics input by the user.

The SOIL TZAPI HEAD line is required to generate T-Z and Q-Z curves from basic soil characteristics. The number of soil strata to be defined and the soil ID or name must be specified in columns 18-20 and 41- 44, respectively.

The properties of each stratum making up the soil are specified immediately following the header line using either the sand, clay or rock soil axial stratum line designated by “SOIL API AXL” in columns 1-12. The API version is input in column 13 and the stratum location label “SLOC” in columns 14-17 is required. The vertical distance from the pilehead to the top of the stratum is specified in columns 19-24. The distance from the pilehead to the bottom of the stratum may be optionally input in columns 25-30. The soil type and the soil characteristics are required in columns 32-77. API RP-2A 22nd Edition

recommends the skin friction is fully mobilized at $Z_{ \mathsf{ p e a k } }$ . The user-defined $Z_{ p e a k }$ ratio to pile diameter may be inputted in columns 78-80. Leaving the field blank results in the default value of 1%. API-RP2A $22^{ \mathsf{ n d } }$ Edition recommends that the $Z_{ \mathsf{ p e a k } }$ ratio to pile diameter may vary from 0.25 % to 2.0 %.

```txt
1 2 3 4 5 6 7 8  
123456789012345678901234567890123456789012345678901234567890  
1 SOIL TZAPI HEAD 2 SOL1  
2 SOIL API AXL SLOC 0.0 30.0 SAND 0.8 93.0 30.0 500.  
3 SOIL API AXL SLOC 60.0 SAND 0.8 93.0 30.0 500. 
```

Note: Because end bearing data is also automatically generated, no end bearing data should be specified when generating axial capacity automatically.

2.4.3.5 Generating T-Z Curves Using CPT-Based Methods

PSI can automatically generate T-Z and Q-Z curves based on one of the four API-recommended CPTbased methods, namely; Simplified ICP-05, Offshore UWA-05, Fugro-05 and NGI-05. The chosen method is invoked by specifying one of ‘ICP’, ‘UWA’, ‘FUG’ and ‘NGI’ in Columns 62-64 of the SOIL TZAPI HEAD line. A CPT tool diameter should also be specified in Columns 66-72. The subsequent strata are defined using the SOIL API AXL lines with ‘CPT’ entered in Columns 32-34. In addition to the data required for the definition of the stratum location and type, the following soil properties are defined for each CPT stratum; (i) the cone-tip resistance in Columns 42-47, (ii) the constant volume interface friction angle in Columns 54-59 and (iii) the submerged mass density in Columns 48-53. The coefficient of lateral earth pressure may be specified optionally for usage with the Simplified-ICP method to calculate the sand relative density using the Ticino Sand relationship. If the coefficient of lateral earth pressure is not specified, the sand relative density is calculated using the Lunne and Christofferson formula.

It should be noted that the unit skin-frictions that are generated using CPT-based methods are dependent on pile geometry. Furthermore, the unit skin frictions generally differ in tension and compression. In accordance with $\mathsf{ A P l } 21^{ \mathsf{ s t } }$ Edition recommendation, the unit end bearing is assumed to be fully mobilized at $z / \mathsf{ D } = 0 . 1$ . The unit skin friction is also assumed to be mobilized at 0.1 inches, consistent with previous API recommendations for cohesionless strata. A z-factor may be specified for usage with CPT-based methods using Columns 34-40 of the SOIL TZAPI HEAD line. API $22^{ \mathsf{ n d } }$ Edition revises this recommendation; the unit friction is now assumed to be mobilized at $Z_{ \mathsf{ p e a k } }$ which is defined as a ratio to pile diameter – similar to adhesive soils in API 21st Edition. The user-defined $Z_{ \mathsf{ p e a k } }$ ratio to pile diameter may be input in columns 78-80. Leaving the field blank results in the default value of 1%. API-RP2A $22^{ \mathsf{ n d } }$ Edition recommends that the $Z_{ \mathsf{ p e a k } }$ ratio to pile diameter may vary from 0.25 % to 2.0 %.

The following (metric) example illustrates two CPT strata, the latter of which has defined a cone tip resistance of 5.0 MPa and a constant volume interface friction angle of 28 degrees. The CPT tool diameter is 3.56 cm and the axial resistance curves are to be constructed using the Simplified ICP-05 method.

```txt
1 2 3 4 5 6 7 8  
123456789012345678901234567890123456789012345678901234567890  
1 SOIL TZAPI HEAD 2 SOL1 ICP 3.56  
2 SOIL API AXL SLOC 0.0 CPT 1.580 28.0  
3 SOIL API AXL SLOC 1.0 CPT 5.0 1.580  
## 28.0
```

2.4.3.6 Applying API General Scour Recommendations

The API guidelines define ‘general scour’ as seabed erosion due to wave and current action. General scour can affect both the axial and lateral soil resistance, due to decreases in cone tip resistance and vertical effective stress.

API recommendations present two methods for taking general scour into account when calculating axial resistance. Two methods are presented, henceforth referred to as the ‘NNI’ and ‘Fugro’ methods. Both methods involve the determination of a ‘scour reduction factor’, χ, which factors the original cone tip resistance to give a final cone tip resistance: $q_{ c , f } = \chi q_{ c , 0 }$

The NNI method, specifies that the scour reduction factor is the ratio of the final vertical effective stress to the original vertical effective stress. The Fugro method provides a more complicated formula for χ, and is recommended for high general scour depths and normally consolidated sands.

There are also API recommendations for taking general scour into account when calculating lateral resistance. The scour brings about a reduction in lateral support due to (i) a decreased vertical effective stress and (ii) a decreased initial modulus of subgrade reaction (ES).

The SCOUR line provides a means to specify a depth for ‘general scour’. The general scour depth is applied to all piles in the model and is specified in Columns 9-14 of the SCOUR line. The axial soil resistance is reduced by general scour only for soils that have been defined using CPT data. By default, the NNI method is used, although the Fugro method may be used by specifying an ‘F’ in Column 7 of the SCOUR line. The lateral soil resistance is reduced for all curves generated using API recommendations. Scour recommendations should only be applied to cohesionless strata. For this reason, the general scour depth is limited by the top depth of the first clay stratum of the relevant lateral soil table.

Note: User-generated T-Z, Q-Z and P-Y curves are unaffected by the general scour specification.

2.4.3.7 User Defined T-Z Curves

T-Z curves defining the soil axial resistance may be input directly by the user. The SOIL TZAXIAL header line designates the number of soil stratum, the maximum number of points on any curve and the soil ID or name must initiate the T-Z curve input.

For each soil stratum, the stratum location line and the T-Z curve data follow. The stratum top and optionally the bottom elevation are input in columns 25-30 and 31-36 of the SOIL SLOC line. The number of points defining the curve and the “T” factor used to scale the force value of all points specified are designated in columns 22-23 and 39-44, respectively. If the curve has the same shape whether the pile is in tension or compression, enter ‘SM’ in columns 18-19.

The T and Z data for each point on the curve are entered on the SOIL T-Z line immediately following the soil stratum location line. The number of data points entered must correspond to the value specified on the stratum location line.

Note: When using the symmetric option, only positive values for T and Z may be input and the origin, T=0 and P=0 must be the first data point.

$$\begin{array}{c c c c c c c c} \hline 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 \\ 1234567890123456789012345678901234567890123456789012345678990 \end{array}$$



| 1 | SOIL | TZAXIAL | HEAD | 2 |  |  |  | SOL2 |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | SOIL | T-Z | SLOCSM | 6 | 0.0 | 30.0 | 1.0 |  |  |  |  |  |  |  |
| 3 | SOIL |  | T-Z | 0.0 | 0.0 | 1.3 | 0.3 | 2.5 | 0.8 | 2.9 | 1.6 | 3.0 | 4.0 |  |
| 4 | SOIL |  | T-Z | 3.5 | 10.0 |  |  |  |  |  |  |  |  |  |
| 5 | SOIL | T-Z | SLOCSM | 5 | 30.0 |  |  |  |  |  |  |  |  |  |
| 6 | SOIL |  | T-Z | 0.0 | 0.0 | 1.3 | 0.5 | 2.5 | 0.9 | 2.9 | 1.9 | 3.0 | 10.0 |  |



2.4.3.8 User Defined Bearing Capacity Curves

T-Z or Q-Z curves defining the pile end bearing capacity may be input directly by the user. The SOIL BEARING header line designates the number of stratum at which capacity curves will be defined, the maximum number of points on any curve and the soil ID or name must initiate the end bearing curve input.

For each stratum, that bearing capacity is to be defined, the stratum location line and the T-Z/Q-Z curve data follow. The stratum top and optionally the bottom elevation are input in columns 25-30 and 31-36 of the SOIL SLOC line. The number of points defining the curve and the “T” factor used to scale the force value of all points specified are designated in columns 22-23 and 39-44, respectively.

The T and Z data for each point on the curve are entered on the SOIL T-Z line immediately following the soil stratum location line. The number of data points entered must correspond to the value specified on the stratum location line.

Note: Both positive (end bearing) and negative (suction) values may be entered. User defined end bearing data should not be defined if soil axial resistance data is generated automatically.



|  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | 123456789012345678901234567890123456789012345678901234567890 | 123456789012345678901234567890123456789012345678901234567890 | 123456789012345678901234567890123456789012345678901234567890 | 123456789012345678901234567890123456789012345678901234567890 | 123456789012345678901234567890123456789012345678901234567890 | 123456789012345678901234567890123456789012345678901234567890 | 123456789012345678901234567890123456789012345678901234567890 | 123456789012345678901234567890123456789012345678901234567890 |
| 1 | SOIL BEARING | HEAD | 1 | SOL2 | SOL2 | SOL2 | SOL2 | SOL2 |
| 2 | SOIL BEAR | SLOCSM | 3 | 0.0 | 30.0 | 30.0 | 30.0 | 30.0 |
| 3 | SOIL | T-Z | 0.0 | 0.0 | 1.0 | 0.5 | 2.0 | 1.5 |



2.4.4 Soil Torsional Resistance

Torsional loads are resisted by adhesion values (skin friction) along the length of the pile or by a linear spring value. The resulting shears act in the circumferential direction around the perimeter of the pile. Torsional resistance must be specified following soil bearing properties. If the soil torsional resistance is not specified, the torsional stiffness defaults to a value equal to GJ/L, where L is the length of the pile, G is the modulus of rigidity of the pile at the pile head and J is the torsion constant of the pile cross section at the pile head. In addition, a warning message is issued.

2.4.4.1 Linear Torsional Spring

The torsional resistance may be represented by a linear torsional spring at the pilehead. The torsional spring stiffness is specified in columns 31-40 of the SOIL TORSION HEAD line. The soil ID or name is specified in columns 41-44.

Note: When specifying a torsional spring stiffness, torsional adhesion data may not be specified.

2.4.4.2 Soil Torsion Adhesion

The pile soil torsional adhesion resistance data may be input directly by the user. The SOIL TORSION HEAD line with the number of stratum and the soil ID or name designated in columns 18-20 and 41-44, respectively, must be specified.

The distance from the pilehead to the top and the bottom of each soil stratum is specified on the SOIL SLOC line(s) immediately following the header. The torsion adhesion capacity at the top and the bottom of each stratum defined, is specified on the SOIL line immediately following the stratum location line.

```c
1 2 3 4 5 6 7 8  
123456789012345678901234567890123456789012345678901234567890  
1 SOIL TORSION HEAD 2 SOL1  
2 SOIL ADHT SLOC 0.0 30.0 30.0 50.0  
3 SOIL ADHT 0.1 0.1 0.16 0.16 
```

2.4.4.3 User Defined ?? − ?? Curves

The torsional resistance may be represented by attached springs at all segments of the pile using T – Z Curves. Therefore, this option uses previously input T-Z curves (in Axial resistance) for each pile to generate an appropriate ?? − ?? curve and considers the nonlinear behavior of the soil in the torsion analysis. The application of distributed torsion analysis is specified in column 61 of the SOIL TORSION HEAD line. Converting T-Z curves to ?? − ?? curves to determine the torsional spring (??/??) values to calculate internal forces which should be later balanced with external forces (applied torsion) is explained in following sections. The only assumption that has been made is that the unit soil adhesion value from axial T-Z curve applies with the same value in the perpendicular direction on the pile surface. This is shown schematically in the following figure. A representative disk with thickness ???? and unit reaction shear ?? is shown in the left side. A representative element from the thin disk assuming that the shear is the same along ?? direction is shown in the right side:

![](SACS2024_PSI/chunk0_1ea5c77e58f34baa798599eef2dccf714a1c87b564a73af26b96632eafccad71.jpg)

![](SACS2024_PSI/chunk0_f2561ff91be65fa1bbb4774451cf5ee2d31ea9550dee4b1db4491dd3343066ba.jpg)

Force produced by the adhesion on the area can be calculated as:

$$d F = T (d A) = T (r d \theta) (d z) = T r (d z) (d \theta)$$

Torsion produced by the element reads:

$$d M = r (d F) = T r^{2} (d z) (d \theta)$$

Total torsion along the pile can be calculated as:

$$M = \int d M = \int_{0}^{L} \int_{0}^{2 \pi} T r^{2} (d z) (d \theta) = 2 \pi T r^{2} L$$

With the same argument, considering torsion in one segment of the pile with the length $\Delta L = L_{ 2 } - L_{ 1 }$ (between two nonlinear springs representing the soil behavior), torsion can be calculated as:

$$\Delta M = \int_{L_{1}}^{L_{2}} d M = \int_{L_{1}}^{L_{2}} \int_{0}^{2 \pi} T r^{2} (d z) (d \theta) = 2 \pi T r^{2} \Delta L$$

The angle is calculated using values from axial T-Z curve (?? value):

$$\theta = \frac{z}{r}$$

Therefore, ?? − ?? curve can be obtained from T- Z curve using previous equations by dividing the Z axis values by pile radius and multiplying the T axis values by $2 \pi r^{ 2 } ( \Delta L )$ . Generating $M - \theta$ curves based on T-Z curves results in determining the equivalent stiffness of the spring that models the effect of soil on pile. Generally, and like T-Z curves, $M - \theta$ curve would be a nonlinear curve which corresponds to the relation $M = K_{ s } \theta$ . Substituting previous equations into equilibrium equations, reduces the problem to the following single equation:

$$- \frac{d}{d z} \bigg (G J \frac{d \theta}{d z} \bigg) + K_{s} \theta = 0$$

The nonlinear nature of equation (9) comes from the fact that the term $K_{ s } \theta$ is a nonlinear function of ?? and is equal to the value that can be read from the previously generated $M - \theta$ curve. PSI program solves aforementioned differential equation to fully analyze torsional behavior of the pile.

Note: When specifying torsion analysis using T-Z curves, program changes the value given for torsional spring stiffness to zero, and instead, computes the stiffness using the nonlinear behavior of soil.

2.4.5 Soil Lateral Resistance

Pilehead lateral loads are resisted by distributed normal forces transverse to the pile axis along its length. These resistances may be specified in terms of the relationship between lateral load and deflection represented by P-Y curves. P-Y curves can be generated automatically from basic soil properties or specified by the user.

2.4.5.1 Generating P-Y Curves per API-RP2A

PSI can automatically generate lateral load deflection curves (P-Y curves) based on API (21st Edition with Supplement 2 and 3, and $22^{ \mathsf{ n d } }$ Edition) guidelines from basic soil characteristics input by the user.

The SOIL LATERAL HEAD line is required to generate P-Y curves from basic soil characteristics. The number of soil strata to be defined and the soil ID or name must be specified in columns 18-20 and 41- $^{ 44 , }$ respectively. The reference pile diameter for which the curves are generated should be entered in columns 28-33 if the P values of the curves are to be multiplied by the ratio of the pile diameter to the

reference diameter. Both the P and Y values may be scaled by the ratio of the pile diameter to the reference diameter by specifying “YEXP” in columns 24-27.

The properties of each stratum making up the soil are specified immediately following the header line using either the sand or clay or soil lateral stratum line designated by “SOIL API LAT” in columns 1-12. The stratum location label “SLOC” in columns 14-17 is required. The vertical distance from the pilehead to the top of the stratum is specified in columns 25-30. The distance from the pilehead to the bottom of the stratum may be optionally input in columns 31-36. The soil type and the soil characteristics are required in columns 19-22 and 45-68, respectively.

For each stratum, P-Y data may be designated as either static or cyclic by specifying “S” or “C” in column 23. For sand strata, the relative location of the water table is designated in column 24. The P values for a stratum may be factored by the number input in columns 37-40. Additionally, the P-Y curve may be shifted by designating the amount to be added to generated Y values in columns 41-44. A high precision "P" factor for this P-Y curve can be specified in columns 70-76.



|  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | 123456789012345678901234567890123456789012345678901234567890 | 123456789012345678901234567890123456789012345678901234567890 | 123456789012345678901234567890123456789012345678901234567890 | 123456789012345678901234567890123456789012345678901234567890 | 123456789012345678901234567890123456789012345678901234567890 | 123456789012345678901234567890123456789012345678901234567890 | 123456789012345678901234567890123456789012345678901234567890 | 123456789012345678901234567890123456789012345678901234567890 |
| 1 | SOIL LATERAL HEAD | 2 | 36.0 | SOL1 |  |  |  |  |
| 2 | SOIL API LAT SLOC SANDSA | 0.0 | 30.01.25 |  | 120. |  | 35.0 |  |
| 3 | SOIL API LAT SLOC SANDSB | 30.0 | 60.01.25 |  | 112.3 |  | 37.5 |  |



2.4.5.2 User Defined P-Y Curves

P-Y curves defining the soil lateral resistance for as many soil strata as desired may be input directly by the user as discrete P-Y pairs at each soil stratum. The only restriction when specifying points on the curve is that the lateral force P, must be a single value function of the displacement Y. Shifted, flat and humped P-Y curves are permitted.

The SOIL LATERAL header line designates the number of soil stratum, the maximum number of points on any curve and the soil ID or name must initiate the P-Y curve input.

The reference pile diameter for which the curve data applies should be entered in columns 28-33. The P values of the curves are multiplied by the ratio of the pile diameter to the reference diameter. Both the P and Y values may be scaled by the ratio of the pile diameter to the reference diameter by specifying “YEXP” in columns 24-27. A “Y” factor to be applied to all Y values input may be specified in columns 34- 40.

Note: Although the P-Y curves may be factored by the ratio of the pile diameter to the reference diameter, only the original input curve is reported in the listing file.

For each soil stratum, the stratum location line and the P-Y curve data follow. The stratum top and optionally the bottom elevation are input in columns 25-30 and 31-36 of the SOIL SLOC line. The number of points defining the curve and the “P” factor used to scale the force value of all points specified are designated in columns 22-23 and 37-40, respectively. The P-Y curve may be shifted along the deflection axis by specifying a “Y” shift value in columns 41-44. If the curve has the same shape whether the pile is

![](SACS2024_PSI/chunk0_bc9b3cc5fc7ac05ef3de438b727ded612aa0325a3435bf1728f4c74a6d1a7267.jpg)

in tension or compression, enter ‘SM’ in columns 18-19. A high precision "P" factor for this P-Y curve can be specified in columns 70-76.

The P and Y data for each point on the curve are entered on the SOIL P-Y line immediately following the soil stratum location line. The number of data points entered must correspond to the value specified on the stratum location line.

Note: When using the symmetric option, only positive values for P and Y may be input and the origin, P=0 and Y=0 must be the first data point.

```txt
1 2 3 4 5 6 7 8  
1234567890123456789012345678901234567890123456789012345678901234567890  
1 SOIL LATERAL HEAD 2 36.0 SOL2  
2 SOIL P-Y SLOCSM 6 0.0 30.00.01  
3 SOIL P-Y 0.0 0.0 1.3 0.3 2.5 0.8 2.9 1.6 3.0 4.0  
4 SOIL P-Y 3.5 10.0  
5 SOIL SLOCSM 5 30.0 0.01  
6 SOIL P-Y 0.0 0.0 1.3 0.5 2.5 0.9 2.9 1.9 3.0 10.0 
```

Note: Within a soil stratum, the PSI program connects the input P-Y points with straight lines to fully define the pile/soil interaction curve for arbitrary displacements in that stratum. At depths between specified soil strata, PSI can linearly interpolate between P-Y curves or to use a constant P-Y curve.

2.4.5.3 Base Shear and Base Moment Effects

Base shear is the result of skin friction of the pile tip cross section and base moment is the result of the soil compression on one side of the pile due to rotation of the pile tip. Base shear effect is significant especially for rigid piles. This effect is significant for gravity type with large diameter pile and may increase its lateral stiffness. PSI program calculates base shear using displacement of the pile tip and t-z curve. It also calculates the Base Moment using the rotation of the pile tip and p-y curve and considers both effects in calculation and pile analysis.

As mentioned before, base shear and base moment are important for rigid piles, where they have significant displacement or rotation in pile tip. This is crucial for rigid piles which is the case for gravity base piles with large diameter. Pile rigidity is defined as following:

$$K_{R} = \frac{(E I)_{p}}{G_{0} L^{4}}$$

Where $G_{ 0 }$ is the soil modules, ?? is the length of the pile, ?? modules of elasticity of the pile and ?? is the moment of inertia of the pile section. Piles with $K_{ R } > 0 . 1$ are considered rigid piles while piles with $K_{ R } < 10^{ - 5 }$ are considered flexible piles. PSI program will apply base shear and base moment to all piles regardless of their rigidity. A single pile with exaggerated displacement at pile tip and applied loads on pile head is shown in the following figure schematically.

The soil under the pile tip will resist this sliding utilizing its friction. Therefore, an extra spring can show the effect of base shear created by soil at the pile tip. Since this effect comes from friction, T-Z curve associated with the strata that include the pile tip can be used to calculate stiffness （$K_{ s } )$ and base shear. Displacement ?? will result in a ?? value (from the T-Z curve) and Base shear reads:

$$V_{b} = T A$$

![](SACS2024_PSI/chunk0_f5ab59273f5e6a901ff9b38256e8149359e1e0fa61da98042e940419bababf6a.jpg)

![](SACS2024_PSI/chunk0_16e30d6896d8a96a5aa8a36200a6d9ca124fdead66bf4d4e98d337e0b2ac0e3b.jpg)

Area (??) will be the area in contact with soil in pile tip. Therefore, for the case of unplugged piles, area will be just the cross-section area of the pile tip and for the case of plugged piles, the area will be the summation of the pile cross section and soil inside the pile. Base shear will be applied to the pile tip in each iteration to solve the bending of the pile, which will help the design and analysis process. Since the T-Z curve (related to axial deformation of pile) is used for this analysis for lateral behavior of pile, the application of base shear is specified in column 61 of the AXIAL HEAD line. To explain the application and effect of the base moment, an exaggerated rotation of pile tip is shown in the following figure. As it can be seen in the previous figure, rotation of the center of pile tip, will push down half of the pile area and the other half will work in tension. The latter area will be ignored in the calculation, since it is assumed that the soil tension resistance is small comparing to the compression resistance. To calculate base moment, it is proposed to divide the half area of pile tip to pieces. The number of these pieces are limited to 20 and can be changed by the user.

For the case of driven plugged piles, half pile area is divided as shown in the following figure. The area and the distance between the segment ?? and the center of pile （$x_{ i } )$ are shown as well. It should be mentioned that in this case, widths of all segments are equal.

![](SACS2024_PSI/chunk0_b9d008298154224230c35b4d86ae539b4a421aa6e589603a7e3fb1d7e4c0e21d.jpg)

For the case of driven unplugged pile, half pile area is divided as shown in the following figure. The area and the distance between the segment ?? center and the center of pile （$x_{ i } )$ are shown as well. It should be mentioned that, in this case the angle of all segments is equal.

![](SACS2024_PSI/chunk0_cf05f96613fe6f6309913595a1582781b7ad9b3e7614121e97fd74f2a8f3a330.jpg)

With the rotation angle of pile tip at each iteration (??), the displacement downward can be calculated as:

$$y_{i} = x_{i} \theta$$

Therefore, using P-Y curve at the pile tip, applied spring forces （$P_{ i } )$ on each area （$A_{ i } )$ can be obtained. Summation of moments generated by these forces around the center line will give the base moment value (??), which will be applied to the pile tip in the analysis in each iteration as:

$$M = \sum P_{i} A_{i} y_{i}$$

The application of base moment is specified in column 61 of the LATERAL HEAD line. The number of segments that the half pile tip area will be divided to is specified in columns 63-64 of the LATERAL HEAD line. As mentioned before, this number cannot be greater than 20 and the default value of the PSI program is set to 10.

2.4.5.4 User Defined Base Shear and Base Moment Curves

Base shear and Base Moment effects explained in the previous section can alternatively be considered by defining two curves representing the pile tip lateral and bending resistance. Base Shear and Base Moment curves defining the soil resistance surrounding the pile tip may be input directly by the user as discrete ??ℎ?????? − ????????. and ???????? ?? − ?? pairs at the pile tip soil stratum. The only restriction when specifying points on the curves, is that the base shear must be a single value function of the pile tip displacement and base moment must be a single value function of the pile tip rotation ??. The definition of each curve is as follows:

The SOIL BASESHR header line designating the maximum number of points on base shear curve, reference pile diameter and the soil ID or name must initiate the base shear curve input. Additional factors for base shear factor and displacement factor values are available on this line as well.

The reference pile diameter for which the curve data applies, should be entered in columns 45-51. The shear values of the curves are multiplied by the ratio of the pile diameter to the reference pile diameter and then divided by the pile diameter.

Note: Although the Base Shear curve may be factored by the ratio of the pile diameter to the reference diameter, only the original input curve is reported in the listing file.

It’s assumed that the base shear curve contains the data for the soil stratum where the pile tip is located. The number of points is input in columns 22-23 of the SOIL SLOC line. If the curve has the same shape whether the pile is in tension or compression, enter ‘SM’ in columns 18-19. The Shear and displacement data for each point on the curve are entered on the SOIL BH-V line immediately following the soil stratum location line. The number of data points entered must correspond to the value specified on the stratum location line.

Note: When using the symmetric option, only positive values for Shear and Displacement may be input and the origin, Shear=0 and Disp=0 must be the first data point.

The SOIL BASEMOM header line designates the maximum number of points on base moment curve, reference pile diameter and the soil ID or name must initiate the base moment curve input immediately after the base shear curve. Additional factors for base moment factor and base rotation ?? factor values are available on this line as well. The reference pile diameter for which the curve data applies, should be entered in columns 45-51. The base moment values of the curve are multiplied by the ratio of the pile diameter to the reference pile diameter and then divided by the pile diameter squared.

Note: Although the Base Moment curve may be factored by the ratio of the pile diameter to the reference diameter, only the original input curve is reported in the listing file.

It’s assumed that the base moment curve contains the data for the soil stratum where the pile tip is located. The number of points is input in columns 22-23 of the SOIL SLOC line. If the curve has the same shape whether the pile is in tension or compression, enter ‘SM’ in columns 18-19. The Base ?? and base rotation ?? data for each point on the curve are entered on the SOIL BM-T line immediately following the soil stratum location line. The number of data points entered must correspond to the value specified on the stratum location line. A sample input is shown in the figure.

Note: When using the symmetric option, only positive values for Base Moment and base rotation ?? may be input and the origin, M=0 and ??=0 must be the first data point.

Here is an example of a soil profile with definitions of both base shear and base moment soil reaction curves:

```txt
1 2 3 4 5 6 7 8 12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567891 1.0SOL1 1.0SOL1  
2 SOIL BH-V SLOCSM 4  
3 SOIL BH-V 0.0 0.0 1.1E4 1.047 1.4E4 1.57 1.5E4 1.97  
4 SOIL BASEMOM HEAD 20 1.0 1.0SOL1  
5 SOIL BM-T SLOCSM 12  
6 SOIL BM-T 0.0 0.0 6.3E4 6.E-3 8.0E4 0.013 9.5E4 0.025 1.0E5 0.038  
7 SOIL BM-T 1.1E5 0.05 1.2E5 0.069 1.3E5 0.0891.32E5 0.113 1.4E5 0.15  
8 SOIL BM-T1.42E5 0.163 1.5E5 0.192 
```

2.4.5.5 Distributed Moment Effect

Distributed moment along the pile is the result of the soil resistance on each node of the pile due to rotation of pile and it is a significant effect for gravity type large diameter rigid pile analysis/design and may increase its lateral capacity. Pile 3D program calculates distributed moment along the pile using the set of $M - \theta$ curves. Applying this effect to the pile can be chosen by the user using the option given in column 67 of SOIL LATERAL Header line. If this option is chosen, then program reads set of ?? − ?? curves right after definition of P-Y curves.

2.4.6 Soil Bending Resistance

Part of the Pilehead lateral loads are resisted by distributed moment in the plane of the pile along its length. This effect is crucial for large diameter rigid pile analysis and design. These resistances may be specified in terms of the relationship between bending moment and in-plane rotation represented by ?? − ?? curves. ?? − ?? curves can only be specified by the user, as there are no general ?? − ?? tables currently available. This option is available in Pile 3D for monopile design and is available in PSI as a technical preview.

2.4.6.1 User Defined ?? − ?? Curves

?? − ?? curves defining the soil bending resistance for as many soil strata as desired may be input directly by the user as discrete ?? − ?? pairs at each soil stratum. The only restriction when specifying points on the curve, is that the bending moment ??, must be a single value function of the rotation ??.

The SOIL BENDING header line designates the number of soil stratum, the maximum number of points on any curve and the soil ID or name must initiate the ?? − ?? curve input. Additional factors for ?? and ?? values are available on this line as well.

The reference pile diameter for which the curve data applies should be entered in columns 45-51. The ?? values of the curves are multiplied by the ratio of the pile diameter to the reference diameter if the soil type is sand and the pile diameter squared to the reference pile diameter squared if the soil type is clay (Soil type defined in the soil stratum lines).

Note: Although the ?? − ?? curves may be factored by the ratio of the pile diameter to the reference diameter, only the original input curve is reported in the listing file.

For each soil stratum, the stratum location line and the ?? − ?? curve data follow. The stratum top and, optionally the bottom elevation are input in columns 25-30 and 31-36 of the SOIL SLOC line. The number of points defining the curve and the “??” factor used to scale the force value of all points specified are designated in columns 22-23 and 39-44, respectively. If the curve has the same shape whether the pile is in tension or compression, enter ‘SM’ in columns 18-19. The ?? and ?? data for each point on the curve are entered on the SOIL M-T line immediately following the soil stratum location line. The number of data points entered must correspond to the value specified on the stratum location line.

Note: Only positive values for M and ?? may be input and the origin, M=0 and ??=0 must be the first data point.

2 3 4 5 6 7 8 34567890123456789012345678901234567890123456789012345678901234567890

```txt
1 SOIL BENDING HEAD 21 20 1.0 1.0SOL1 1000.0   
2 SOIL M-T SLOCSM 4 50.00051.000 1.0 S   
3 SOIL M-T 0.0 0.08.06515.7E-733.5631.5E-634.5561.9E-6   
4 SOIL M-T SLOCSM 6 51.00052.000 1.0 S   
5 SOIL M-T 0.0 0.06.92133.9E-723.3758.3E-795.5362.2E-697.6682.5E-6   
6 SOIL M-T 98.2212.7E-6 
```

Note: When using a “displacement control” type using the LTDFL input line in Pile3D, in order to apply moment on the pile head, it is recommended to define a soil layer with “ZERO” properties to define a pile extension. For “load control” types with Pile3D or PSI, the loading is not incrementally applied which can cause convergence issues when compared with “displacement control” cases.

2.4.7 Soil Liquefaction Potential

SACS can calculate the liquefaction potential of a soil layer for a given earthquake loading and change the soil stiffness properties accordingly before conducting the pile-soil-interaction analysis. This functionality is available in Collapse, Pile, and PSI programs in SACS.

For each soil defined in a PSI or Pile input file, the user can specify the soil liquefaction data. One ‘SOIL LIQUEFY HEAD’ line followed by a number of ‘SOIL LIQUFY SLOC’ lines, one for each stratum, is required to completely describe the liquefaction data for the soil.

SOIL LIQUEFY HEAD line description: The number of soil strata to be defined and the soil ID or name must be specified in columns 18-20 and 41-44, respectively. Seismic loading must be specified by providing the values of the earthquake magnitude and the peak ground acceleration (as a ratio of gravity) in columns 34-36 and 37-40, respectively. There is also an option to make the estimation of liquefaction potential more (or less) conservative by changing the values of “% horizontal shift in CRR curve” and “% vertical shift in CRR curve” in columns 21-26 and 27-32, respectively. Also, the effect of liquefaction on soil stiffness properties can be modulated by changing the liquefaction multiplier factor in columns 45-50.

SOIL LIQUEFY SLOC line description: Liquefaction stratum lines should follow the liquefaction header line. The location of the stratum with respect to the water table should be specified in column 18. The vertical distances from the pilehead to the top and the bottom of the stratum are specified in columns 19-24 and 25-30, respectively. The cone tip resistance value and the sleeve friction value obtained from the CPT tests are specified in columns 45-50 and 51-56, respectively. The submerged unit weight of the soil is specified in columns 57-62. If liquefaction effects are to be ignored for a stratum, the calculation method in columns 31-33 should be specified as ‘N’. If soil type is known, it can be specified in columns 34-37.

If the soil type for a layer is described as ‘CLAY’ or if the soil type is not specified and SACS determines (based on the CPT data) that the soil type is likely to be clay, or if the calculation method is specified as ‘N’, then it is assumed that this layer is not prone to liquefaction and stiffness values for this layer are not changed. In all other cases, SACS calculates the factor of safety for liquefaction due to the seismic loading specified by the user. If the factor of safety is calculated to be greater than or equal to 1.0, then there is no change in the soil stiffness. If the factor of safety is calculated to be less than 1.0, then the layer is considered as liquefied, and a factor called liquefaction multiplier is calculated. If the calculated value of the liquefaction multiplier is less than 1.0, then soil skin friction resistance (T-z), bearing resistance (Q-z), and lateral resistance (P-y) are multiplied by the liquefaction multiplier to calculate the stiffness of the liquefied soil layer.

Note 1: Liquefaction related calculations are conducted at the mid depth of each liquefaction stratum specified by the user. Therefore, it is advisable to use several soil liquefaction strata through the pile depth for a better estimation of the liquefaction potential.

Note 2: liquefaction effect on the axial behavior is ignored if soil axial resistance is defined as adhesion or linear axial spring at the pilehead.

Note 3: Both "from" and "to" information for each liquefaction stratum is required. The strata should be continuous and should cover at least the entire length of the pile.

```txt
1 2 3 4 5 6 7 8  
1234567890123456789012345678901234567890123456789012345678901234567890  
1 SOIL LIQUEFY HEAD 4 8.50.80SOL2  
2 SOIL LIQUEFY SLOCB 0.0 3.00CPT 7.00 0.25 1.019  
3 SOIL LIQUEFY SLOCB 3.0 8.00CPT 15.00 0.80 1.019  
4 SOIL LIQUEFY SLOCB 8.0 20.00CPT 20.00 0.50 1.019  
5 SOIL LIQUEFY SLOCB 20.0 30.00CPT 40.00 1.50 1.019 
```

## 2.5 CREATING FOUNDATION SUPERELEMENTS

Up to two linearized foundation stiffness matrices may be generated at each pilehead to be used by the SACS dynamics modules in lieu of a pile stub, pile spring etc. The program creates a coupled threedimensional stiffness matrix for a pile group that has lateral stiffness properties in both lateral directions along with axial stiffness properties. The stiffness properties are derived from either the average displacement of all piles of the pile group or the maximum pile displacements for the load cases designated by the user.

Note: A super element is created for each pile group. The super element is applied to each pilehead connected to a pile assigned to the pile group in question.

2.5.1 Foundation Super Element Options

Linearized foundation super elements or stiffness matrices are created at each pilehead automatically by the PSI program if the PILSUP input line is specified.

The method used to calculate the pile stiffness, ‘AVG’ or ‘MAX’, for a pile group is specified in columns 8- 10. Up to four load conditions, specified in columns 21-24, 29-32, 37-40 and 45-48, may be chosen to calculate the pile stiffness in the global X direction. If different load cases are to be used to calculate stiffness in the global Y direction, they may be specified in columns 25-28, 33-36, 41-44 and 49-52, respectively.

A second foundation superelement may be generated by specifying a second PILSUP line. In the sample below, the first superelement is to be used for Fatigue analysis and is created using load cases 8 and 9, while the second superelement is to be used for earthquake analysis and is created using load cases ‘DEDX’ and ‘DEDY’.

Note: Stiffness is calculated independently in the X and Y directions.

```txt
1 2 3 4 5 6 7 8 1234567890123456789012345678901234567890123456789012345678901234567890  
1 PILSUP AVG 8 9  
2 PILSUP AVG DEDXDEDY 
```

## 2.6 SIMULATING MUDSLIDES

Mudslides against the jacket above the pilehead can be modeled in Seastate. Mudslides against the piles are modeled in PSI or Pile using flat and/or shifted P-Y curves. In PSI, one of the pile local coordinate directions is oriented to correspond to the direction of the mudslide by specifying a pile rotation angle on the PILE line. Separate soil tables (axial, bearing, torsion, lateral) are defined for the local XY and XZ planes of the pile.

Note: Normally the axial, bearing and torsion lines will be the same for the two directions with only the lateral lines being different.

In the direction of the mudslide, the P-Y data can be the same as in the other direction except that a “shift” is specified in columns 41-44 on the SOIL SLOC line. Conversely, a “flat” P-Y curve that has a constant value of P for all Y values, may be specified for the mudslide direction. In either case, force is exerted by the soil against the pile even when there is no displacement. This corresponds to active soil exerting a thrust on the pile as opposed to the usual problem of passive soil resisting a thrust exerted by the pile.

If an initially symmetrical P-Y curve is given a positive Y shift, as shown in the figure below, then for any pile displacement less than the shift amount, a negative force is exerted on the soil (P-Y data is for the soil, not the pile). This in turn results in a force on the pile in a positive direction. Thus, to model a mudslide in the positive Y direction (pile coordinates) a positive shift should be used. In the same manner if a flat P-Y curve is used to model a mudslide in the positive Y direction then the constant value for P must be negative.

![](SACS2024_PSI/chunk0_4498ce0ad62c8e1fa78417cbdf649f1b997bf1314ea81d7ddb198eea7ccdd879.jpg)

The figure above also shows that for values of Y beyond the limits of the input data, the program extends the curve as flat. For this figure to be valid, the user must input the direction for the pile local coordinates so that the pile local Y or Z axis is aligned with the mudslide. This is done on the PILE line in columns 50 to 56.

The following illustrates shifted P-Y data for soil table ‘SOL2’. The curves for each stratum are symmetric and are shifted 7.0 and 4.25, respectively.



|  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | 123456789012 | 3456789012345678901 | 2345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890 | 36.0 | SOL2 |  |  |  |  |
| 1 | SOIL LATERAL | HEAD 2 |  |  |  |  |  |  |  |
| 2 | SOIL P-Y | SLOCSM | 6 | 0.0 | 30.00.01 | 7.0 |  |  |  |
| 3 | SOIL | P-Y | 0.0 | 0.0 | 1.3 | 0.3 | 2.5 | 0.8 | 2.9 |
| 4 | SOIL | P-Y | 3.5 | 10.0 |  |  |  |  |  |
| 5 | SOIL P-Y | SLOCSM | 6 | 30.0 | 0.014.25 |  |  |  |  |
| 6 | SOIL | P-Y | 0.0 | 0.0 | 1.3 | 0.5 | 2.5 | 0.9 | 2.9 |



Note: Since the pile local coordinates are defined by the direction of the mudslide, if any significant lateral loads (such as waves, current or wind) are acting on the jacket in a direction different from that of the mudslide, the user should check the final pilehead loads in the “Pilehead Comparison” report to make sure that proper convergence has been achieved.

## 2.7 INPUTTING PILE HEAD STIFFNESS TABLES

Because the pile/soil foundation exhibits nonlinear behavior, the pile head stiffness matrix varies for each iteration of each pile for each load case. Normally this would require the reformulation of the pile stiffness matrix at each iteration, thus requiring a great deal of computation time. PSI eliminates this requirement by initially forming a table of pile head stiffness coefficients for a range of values expected in the solution. The pile head stiffness used for any iteration is found by linearly interpolating between table coefficient values. Iterations are continued until an approximate solution (within 5 percent) is found. PSI then proceeds using a “fine tune” procedure which recalculates the individual pile stiffness for each iteration.

2.7.1 Optional User Defined Pilehead Stiffness Tables

In general, normal convergence for pilehead loads is 0.5 percent. For some situations however, the pilehead stiffness tables generated automatically by PSI may not be adequate to obtain this convergence or sufficient program accuracy. In these cases, a user specified pilehead stiffness table may be required.

As discussed above, before the iterative solution to the lateral deformation problems begins, PSI first does a number of pile solutions for all combinations of user input of axial load or displacement, pilehead lateral displacement, and pilehead rotation. The iterative solution will produce values for pilehead axial load, or displacement, lateral displacement, and rotation. These values should be within the ranges spanned by the user specified input values. This is particularly important if the final values are in a highly nonlinear region of the corresponding load-deformation surface.

Note: Table ranges for all degrees of freedom must be specified if any are included in the input file.

2.7.1.1 Guidelines for Axial Ranges

The user should select the input TABR values based on prior experience with similar structures and soil conditions as well as PSI analyses. The following is offered as a guide.

First, the capacity of the pile in compression and tension should be found. If the axial soil data is in terms of T-Z data, the capacity can be found using the Pile program with a large input value of pilehead axial displacement, large enough so that the “Z” value of any point on the pile is on the flat part of the T-Z curve. Ten or twenty inches is usually sufficient. If the actual soil data is expressed in terms of adhesion data or if the API soil option is selected, the pile capacity can be found by running Pile with a value of axial load much larger than the pile capacity, in which case the output will include a report to the effect

that the applied load exceeds the capacity and the capacity will be reported. A value of 100,000 kips should be sufficient in most cases.

After the axial capacities in tension and compression are found, they are divided by a factor of safety to get the maximum working values for axial load. Then the interval between these two values is subdivided into approximately equal subdivisions, these two points are then used as the values on the axial TABR lines, the point “0.0” should be among the input values. Usually no more than a total of seven values will be required.

Note: If the soil exhibits highly nonlinear properties (such as humped T-Z curves) and if the pile will be operating under conditions that place the deflections along the length of the pile in the highly nonlinear region (e.g. past the hump), then the pilehead force displacement curves will also be highly nonlinear and the above guidelines may not be adequate. More TABR values may be needed and it may be necessary to make spacing between values much closer together for points where the slope of the curve is changing rapidly than for the regions where the slope is changing less rapidly so that the shapes of the pilehead load vs.

2.7.1.2 Guidelines for Lateral Ranges

Normally P-Y soil properties are symmetrical, the principal exception being for shifted P-Y curves. TABR values should be entered for several values from zero to about 1.5 times the largest expected lateral deflection. Normally six or seven values will be sufficient. If the P-Y data is not symmetrical then several values from about 1.5 times the maximum expected negative defection to 1.5 times the maximum expected positive deflection should be entered. The zero-deflection point should be one of the entries

Note: If the maximum pilehead lateral deflection is small enough such that the pilehead lateral load vs. deflection curve is approximately linear for all values of displacement up to the maximum then many fewer than seven points may be used.

The maximum expected lateral deflection can be estimated as follows: Normally Seastate will have been run to produce the loads on the structure. The resulting base shear can be distributed equally to the piles, these pilehead shears will then be multiplied by a factor of about 1.5 to get working pilehead shears. The Pile program can be run with this pilehead shear acting in conjunction with the working pilehead axial load (described above). A pilehead rotational spring having stiffness approximating that of the structure at the pilehead joint can be used to account for the restraining influence of the structure on the pile. The pilehead displacement and rotation can then be used as the maximum TABR values. TABR values for pilehead displacement should be entered in radians from the maximum negative to the maximum positive values. It is important that both positive and negative values be entered even if the soil has symmetrical P-Y data because the significance of the sign of the pilehead rotation is that the rotation either augments (positive) the deflection caused by the pilehead shear or diminishes it (negative). Again, normally seven approximately equally spaced values will suffice. In many cases the following set of TABR values for pilehead rotation will be adequate.

```batch
1 2 3 4 5 6 7 8 1 23456789012345678901234567890123456789012345678901234567890 1 TABR ROTATION -0.01 -.007 -.003 0.0 .003 .007 0.01
```

Note: If the soil exhibits highly nonlinear properties (such as humped P-Y curves) and if the pile will be operating under conditions that place the deflections along the length of the pile in the highly nonlinear

region (e.g. past the hump), then the pilehead force displacement curves will also be highly nonlinear and the above guidelines may not be adequate. More TABR values may be needed and it may be necessary to make the spacing between values much closer together for points where the slope of the curve is changing rapidly than for the regions where the slope is changing less rapidly so that the shapes of the pilehead load vs. displacement curves are adequately approximated by the piecewise linear curves that are used to represent them.

2.7.1.3 Guidelines for Torsional Ranges

While torsional loads on the pileheads are almost never very large, a torsion TABR line is always required. There is no interaction of torsion with any of the other loads (axial, lateral, and bending). In most cases, two points (e.g., 0.0 and 100.0) will be sufficient.

3 CREATING PILE INPUT

## 3.1 OVERVIEW

Pile and Pile3D are sub-programs of PSI that can run in stand-alone mode for the analysis of a pile subject to known pilehead forces or displacements. They are mainly used to perform single or isolated pile analyses and utilize the same input file as the PSI program with minor modifications (see sections 3.2 to 3.5 for details). Pile and Pile3D can be used to plot soil data prior to executing a PSI analysis. They can also create a post file for use by the Fatigue program to evaluate the pile fatigue life.

In general, the PSI input lines may be used in the Pile or Pile3D input file to describe the pile and soil model, except where noted in the following sections. The following applies to the execution of single pile analysis or 3D single pile analysis, generating equivalent linearized foundation and pile fatigue using Pile or Pile3D. When using Pile or Pile3D to generate plots of soil data, the PSI input file may be used without modification.

The difference between Pile and Pile3D is noted in subsequent sections. Basically, the difference lies in two- and three-dimensional pile analysis. Pile3D offers an extended set of options for single pile analysis over that which is supported by Pile. Options supported only by Pile3D are marked as such in the text.

## 3.2 DEFINING ANALYSIS OPTIONS

The Pile program requires the use of the PLOPT line to designate analysis options.

The input and output units are specified in columns 7-8 and 11-12, respectively. The number of pile increments, the maximum number of iterations and the lateral deflection convergence tolerance are designated in columns 13-15, 18-20 and 21-30, respectively. The pile unit weight may be designated in columns 31-40.

The soil data plots and/or soil reactions may be output by specifying ‘PT’ in columns 43-44 and 61-62, respectively.

The API edition is selected in columns 59-60. The user may input S2 (for API-RP2A 21st Edition with Supplement 2), S3 (for API-RP2A 21st Edition with Supplement 3) or 22 (for API-RP2A 22nd Edition). If this field is left blank, Pile program uses default API-RP2A 21st Edition with Supplement 3

The following shows a PLOPT line designates English units, the latest API code and 490. material weight.

```txt
1 2 3 4 5 6 7 8 123456789012345678901234567890123456789012345678901234567890 PLOPT ENUC 490. 
```

The coupling of axial and torsional loading on a pile may be achieved using the current ‘PLOPT’ line with the Pile3D program. The option is input as ‘TTZ’ in columns 45-47 of the ‘PLOPT’ line. With this option chosen any torsional soil data will be removed from the input data file. This data will be computed internally. This option with the Pile3D loading features is particularly useful for caisson-like structures with foundations which are torsion sensitive.

A specification of axial and torsional load coupling is shown. The example specifies API RP-2A 20th Edition unity checks with English input and output units. Ten pile length increments are used for the

finite difference solution. Pile self-weight is included in the analysis with pile density of 490.0 lb/ft³. An input echo is to be printed, all T-Z plots will be produced on one plot, and axial and torsional loads are to be coupled, with soil reactions reported along each station of the pile.

```txt
1 2 3 4 5 6 7 8 1 23456789012345678901234567890123456789012345678901234567890 PLOPT ENUC 10 490.0PTPTTTZ PT 
```

Pile program is capable of computing pile capacity using three different methods

1. SACS method based on nonlinear interaction between pile and soil.   
2. Ultimate based on maximum skin friction (non-conservative)   
3. Residual based on residual skin friction (non-conservative)

This option can be selected by inputting S (SACS), U (Ultimate), and R (Residual) in column 66 of PLOPT option line. The details of these methods are discussed in section 4.6.

## 3.3 SPECIFYING PLOT OPTIONS

As in PSI, plot options are designated on the PLTRQ, PLTLC and PLTSZ input lines. In addition, since the Pile program only allows one pile to be defined, the PLTPL input line that allows specification of which piles to plot, is not applicable.

3.3.1 Plot Data

Data to be plotted is designated on the PLTRQ input line. Soil input data, axial deflection, axial load, axial soil reactions, required pile thickness and unity check ratio may be plotted versus pile penetration. Lateral deflection, lateral rotation, bending moment, shear load and lateral soil reaction along or about the pile local Y and local Z axes may be plotted versus penetration in addition to the resultant.

By default, for any of the result plot options, load cases to plot may be designated on the PLTLC line. Plot appearance options such as grid lines and cross hatching may be designated also.

The following requests soil data plots, lateral and axial displacement along with unity check plots:

```txt
1 2 3 4 5 6 7 8 1 23456789012345678901234567890123456789012345678901234567890 1 PLTRQ SD DA DT UC 
```

Note: Envelope options on the PLTRQ line are not available in the Pile program

3.3.2 Designating Load Cases to Plot

By default, all load cases are included for plot generation. If load cases are specified on the PLTLC input line, then only load cases specified will be included for plotting purposes.

3.3.3 Overriding Plot Size

The default plot paper size, character size, cross hatching spacing and number of colors may be overridden using the PLTSZ line.

3.3.4 Plotting Soil Data from PSI Input

The Pile program may be used to plot soil data so that it may be checked prior to PSI execution. When using the Pile program to generate plots of the soil data, the PSI input file may be used without modification. A maximum of 150 soil strata may be plotted with either program.

## 3.4 DEFINING THE PILE

In general, the pile is defined using the same input as required by the PSI program. Exceptions are noted in the following sections.

3.4.1 Pile Section Properties

Section properties are defined using the PLSECT and PLGRUP lines used in the PSI input file.

3.4.2 Pile Group Properties

Pile group properties such as modulus of elasticity, shear modulus, and yield stress are specified on the appropriate PLGRUP line as in PSI.

3.4.3 Defining Pile Elements

Pile elements are specified on PILE lines following the PILE header input line. The pile element is named by the optional pilehead joint name specified in columns 7-10. The pile group to which the pile is assigned is specified in columns 16-18.

The soil ID defining pile/soil interaction properties in the local XZ plane is designated in columns 69-72.

Note: Because the Pile is a two-dimensional analysis, only a soil table for the XZ plane is required.

The following defines a pile assigned to pile group ‘PL1’ and uses soil table ‘SOL1’. A pilehead joint was designated for reference purposes.



|  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789 | PILE |  |  |  |  |  |  |
| 2 | PILE | 2 | PL1 | 1.0 | 1.0 | 8.0 | SOL1 |  |



3.4.3.1 Pile Batter

The pile batter must be defined by batter definition coordinates specified on the PILE line. The global X, Y and Z distances from the pilehead to any point above it lying on the pile axis should be input in columns 21-30, 31-40 and 41-50, respectively. For example, the following defines a pile battered 1:8 in the global XZ plane and vertical in the global YZ plane.



|  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789 | PILE |  |  |  |  |  |  |
| 2 | PILE | 2 | PL1 | 1.0 | 0.0 | 8.0 | SOL1 |  |



Note: Pile batter coordinates may be specified regardless of whether the rise value of the batter is the same for both planes. For example, a pile battered 1:8 in the global XZ plane as 1:10 in the global XY plane may be defined using the X, Y and Z batter coordinates of 10.0, 8.0 and 80.0.

3.4.4 Pile Local Coordinate System

The pile local coordinate system used in the Pile program is defined as follows:

The pile local X-axis extends from the pilehead down the pile along the pile centerline. The local Z-axis is perpendicular to the pile local X-axis and is assumed to be directed to the right of the pile. Using the right-hand rule, the local Y-axis is normal to the pile and points into the page.

Positive axial deflection is assumed to be deflection down along the pile axis while positive lateral deflection is along the positive Z axis. Positive rotation is assumed about the Y-axis and is into the paper using the right-hand rule.

![](SACS2024_PSI/chunk0_ffe22ef634d54e1a453527a66c36f1d5d3042ec0d90cfe60de3c735bcfb76a74.jpg)

The Pile program reports pile internal loading such that positive internal axial load is tension and a positive internal Z shear load acts along the local Z axis. A positive internal Y moment acts about the local Y-axis and results in a compressive stress on the right side of the pile. Internal stresses are reported such that a positive axial stress is tensile and positive shear stress results from a positive shear load. Positive bending stress corresponds to a positive moment about the local Y axis.

3.4.5 Pilehead Spring

Unlike PSI, the Pile program does not include the effects of the stiffness of the structure connected above the pilehead. By default, the top of the pile is assumed to be free to rotate and translate.

However, the stiffness effects of a structure connected at the top of the pile may be incorporated by specifying elastic boundary conditions at the top of the pile using the PLSPRG line. A lateral and/or rotational (bending) spring may be defined by specifying the spring type and the spring constant. The following defines a lateral and a rotational spring:



|  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789 | PLSPRG |  |  |  |  |  |  |
| 2 | PLSPRG | LATERAL | 1200.0ROTATION | 20.0E6 |  |  |  |  |



## 3.5 MODELING SOIL PROPERTIES

3.5.1 Overview

In general, soil resistance is described using the lines available for use in PSI input except where noted in the following sections.

3.5.2 Soil Axial Resistance

The axial capacity of the soil may be described using the same input lines available in the PSI program.

3.5.2.1 Inputting Axial Load Distribution

If axial soil data in unavailable, the user may input the axial load distribution in the pile using the AXLOAD line, thus allowing Pile to bypass the axial solution.

The number of points along the pile that axial load will be specified is designated in columns 14-16. For each of these points, the axial force and the distance from the pilehead must be specified. Pile uses these input values in performing the lateral solution. The following defines the axial load in the pile at eight points:



|  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | 123456789012345678901234567890123456789012345678901234567890 | 123456789012345678901234567890123456789012345678901234567890 | 123456789012345678901234567890123456789012345678901234567890 | 123456789012345678901234567890123456789012345678901234567890 | 123456789012345678901234567890123456789012345678901234567890 | 123456789012345678901234567890123456789012345678901234567890 | 123456789012345678901234567890123456789012345678901234567890 | 123456789012345678901234567890123456789012345678901234567890 |
| 1 | AXLOAD |  |  |  |  |  |  |  |
| 2 | AXLOAD | 8 | 900. | 0.0 | 800.0 | 10.0 | 700.0 | 20.0 |
| 3 | AXLOAD |  | 200. | 70.0 | 100.0 | 90.0 | 50.0 | 100.0 |



Note: Compressive force should be entered as positive values. The first value entered should be the axial load at the pilehead (0.0 in columns 24-29). This value is used as the axial load in the pile. Any additional axial load specified using PLLOAD lines is ignored.

3.5.3 Soil Torsional Resistance

Torsional resistance of the soil is not considered by the Pile program. Any SOIL TORSION input lines are ignored.

3.5.4 Soil Lateral Resistance

Soil lateral capacity is modeled using the same techniques as the PSI program module.

3.5.5 Soil Liquefaction Potential

Soil liquefaction potential is calculated using the same techniques as the PSI program module.

## 3.6 INPUTTING PILEHEAD STIFFNESS TABLES

Pilehead stiffness table data is not required. Any pilehead stiffness data input is ignored by the Pile program.

## 3.7 SPECIFYING LOADING FOR ISOLATED PILE ANALYSIS

The loading at the top of the pile must be described when executing an isolated pile analysis. If code check is to be performed, the code must be designated in columns 9-10 on the PLOPT line.

The loading or displacements for which to analyze the pile are designated on the PLLOAD line(s). The lateral force or displacement is input in columns 21-30, while moment or rotation is input in columns 31- 40. Either axial force or axial displacement but not both, must be specified in columns 41-50 or 51-60, respectively.

Note: Enter positive axial load for compression or positive axial displacement for displacement down along the pile.

The allowable stress modifier or material factor may be specified in columns 71-75.

As many PLLOAD lines as desired may be input. By default, each PLLOAD line is considered to be a separate load condition unless the ‘Start from previous solution’ flag is set. If this flag is set, the loading specified prior to the present PLLOAD line is assumed to be the initial position for the present analysis to begin. The following designates pile loading with the second line continuing from the previous solution:



|  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789 | PLLOAD | FM | 150.0 | 100000.0 | 700.0 |  |  |
| 2 | 1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789 | PLLOAD | FM | 250.0 | 150000.0 | 1000.0 | PREV | PREV |
| 3 | 1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789 | PLLOAD | FM |  |  |  |  |  |



Note: When the Pile program is run using a PSI input file (with the PSIOPT line replaced by a PLOPT line), a pile analysis will be performed on each pile for each pile load case, even if all piles are identical and are installed in the same soil. To avoid this duplication, it is suggested that redundant PILE lines be removed from the Pile input file.

3.7.1 3D Pile Head Load

The first step in creating three-dimensional pile head loading in Pile3D is specifying the pile head height on the ‘PILE’ line. After specifying the pile head height, loading is applied to the pile via the ‘PLOD3D’ line. Three-dimensional loads (forces and moments) or three-dimensional displacements (translation and rotation) may be applied to the pile at the height specified in the previous ‘PILE’ line. Forces ‘F’ or displacements ‘D’ are specified in columns 11-34; moments ‘M’ or rotations ‘R’ are specified in columns 35-58. All quantities specified on the ‘PLOD3D’ line are specified in the pile local coordinate system.

The following sample specifies pile forces of 100.0 in the axial direction, 8.0 in the local Y direction and a torsional moment of 10.0. The pile itself has a batter of 1:10 in the global XZ plane and a pile head height of 10.0. All forces/moments are applied at this height above the mud line.



|  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789 | PILE |  |  |  |  |  |  |
| 2 | PILE | PL1 | 1.0 | 0.0 | 10.0 |  | SOL1 |  |
| 3 | PLOD3D | F 100.0F | 8.0F 0.0M | 10.0M 0.0M | 0.0M 0.0 |  |  |  |



3.7.2 Specifying Pile Load at Depth

A new feature of three-dimensional single pile analysis is the ability to specify pile loading at places along the pile other than the pile head. This feature is contained in the line DEPLOD. Loads (forces and moments) are specified at a given vertical depth relative to the mud line. Vertical depth is specified in columns 8-14. Forces are specified in columns 16-36 with moments specified in columns 37-57. Each DEPLOD line creates a single pile analysis. All quantities specified on the ‘DEPLOD’ line are specified in

the global coordinate system. As such, to effectively use the ‘DEPLOD’ line the model must have the positive global Z axis in the vertical upward direction.

The following sample specifies global pile forces of 8.0 in the global X direction, 0.0 in the global Y direction, and -100.0 in the global Z direction. Global pile moments of 0.0 about the global X, 0.0 about the global Y, and 10.0 about the global Z are specified. The pile loading is specified at 10.0 units below the mud line.



|  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 12345678901234567890123456789012345678901234567890123456789012345678901234567890 | 12345678901234567890123456789012345678901234567890123456789012345678901234567890 | 12345678901234567890123456789012345678901234567890123456789012345678901234567890 | 12345678901234567890123456789012345678901234567890123456789012345678901234567890 | 12345678901234567890123456789012345678901234567890123456789012345678901234567890 | 12345678901234567890123456789012345678901234567890123456789012345678901234567890 | 12345678901234567890123456789012345678901234567890123456789012345678901234567890 | 12345678901234567890123456789012345678901234567890123456789012345678901234567890 |
| DEPLODG | 10.0 | 8.0 | 0.0 | -100.0 | 0.0 | 0.0 | 10.0 |  |



## 3.8 CREATING A PILE FATIGUE SOLUTION FILE

The Pile program can be used to create a pile solution file for use by subsequent fatigue analysis by entering ‘PP’ in columns 57-58 on the PLOPT line. The SCF option should be specified in columns 63-65.

The forces and moments to be applied to the pile are designated on the LOAD input line. The forces along X, Y and Z axes are entered in columns 17-23, 24-30 and 31-37, respectively along with the moments about the X, Y and Z axes specified in columns 38-44, 46-52 and 53-59, respectively.

By default, the loads specified are assumed to be in the pile local coordinate system (shown on right). If on the other hand, the pile loads were taken directly from a member internal loads report or are specified using the Timoshenko sign convention, ‘MEMB’ and ‘INTL’ must be specified in columns 61-64 and 66-69, respectively.

![](SACS2024_PSI/chunk0_78b42ebf421559d7c809d6f1c15d98141decb62fa574a1d197c216a29f0d7f64.jpg)  
Global Cartesian and Pile Local Coordinate System

![](SACS2024_PSI/chunk0_8f2dfc953c9d1b52c72176bfc742a5551707ff9ae9d74ef8553748082c12075c.jpg)  
Internal Load Report and Timoshenko Convention

As many LOAD lines as required may be specified. A load condition, with results, will be created in the solution for each LOAD line specified.

## 3.9 CREATING A PILE STUB

It is often desirable or necessary to replace the nonlinear pile-soil system with an approximately equivalent linear pile stub beam element. Static analysis of the linearized system for instance, may be sufficiently accurate for preliminary design purposes. For dynamic analysis, it is necessary to linearize the foundation. The Pile program offers an automated equivalent pile stub design facility in which the program calculates an equivalent pile stub and outputs input lines containing the pile stub properties including member length, member offsets and prismatic section properties.

3.9.1 Pile Stub Loading

The loading or displacements used to calculate the equivalent linearized foundation element are specified on the PLSTUB line. The lateral and bending stiffness may be determined using forces and moments or displacement and rotation by entering ‘F’ or ‘D’ in column 10, respectively. If deflections are designated, the lateral deflection and rotation are entered in columns 21-30 and 31-40. Otherwise, lateral shear force and moment should be entered. Either an axial load or axial displacement, but not both, may be specified in columns 41-50 or 51-60.

```txt
1 2 3 4 5 6 7 8 1234567890123456789012345678901234567890123456789012345678901234567890 1 PLSTUB D 9020 2.28 0.013 625.0 
```

Note: The loads specified at the pilehead should be specified in the pile local coordinate system. For a more detailed discussion on the theory and derivation of the equivalent pile stub procedure used by Pile, see the Commentary. Sample problem 2 illustrates the procedure in detail.

## 3.10 CREATING A LOAD/DEFLECTION CURVE FOR SOILS

The Pile program can be used to create the load versus deflection curves for a given pilehead. This is useful for the visualization of specific static load/deflection characteristics in the specified pilehead. Pilehead capacity may often be easily determined by examining the peak of the pilehead load/deflection curve.

The creation of a load/deflection curve is accomplished by means of the LODFL line. This line is used to calculate the axial compression and tension pilehead versus deflection. The number of deflection increments is entered in columns 7-10. The maximum axial deflection is entered in columns 11-20. The deflection range from zero to the maximum axial deflection is divided evenly by the number of deflection increments. A pilehead load is calculated for each axial deflection. If the units specified were SI, the following line defines a load/deflection curve with fifty points and a maximum axial deflection of 15.0 centimeters.

```txt
1 2 3 4 5 6 7 8 1 234567890123456789012345678901234567890123456789012345678901234567890 1 LODFL 50 15.0 
```

Note: the LODFL line is only used in single pile analysis.

Using the above load deflection line, the pile program will produce a neutral picture file with the load/deflection curve plotted with the given number of points and maximum axial deflection. An example of the output produced is shown. The LODFL options used to create the figure were those shown above in the example line.

![](SACS2024_PSI/chunk0_43ca49d534d12588e89babfbdf34bd2fe853489671cfa26ab83911885fc4369d.jpg)

# 4 COMMENTARY

## 4.1 INTRODUCTION

PSI, (Pile Structure Interaction), analyzes the behavior of a pile supported structure subject to one or more static load conditions. Finite deflection of the pile is accounted for (the “P-delta” effect) and the soil may exhibit nonlinear force-deformation behavior both along and transverse to the pile axis.

Because of the nonlinear behavior of the pile-soil system, the overall stiffness of the structurefoundation system is a function of displacement. In a linear analysis, the structural stiffness matrix is formed based on the undeformed structure and does not change as the structure deforms. When there is significant nonlinearity, however, the stiffness matrix for the deformed shape cannot be determined until the deformed shape is obtained. The deformed shape, in turn, cannot be found until the stiffness matrix is found.

Iterative methods have proven to be useful for solving problems of this type. One starts with an initial assumption for the displacements and solves for the stiffness matrix. New displacements are found using this stiffness matrix, then an updated stiffness matrix is formed. The process is repeated until the calculated displacements for an iteration are within a specified tolerance of those from the previous iteration.

The technique described above is not practical for structures with many degrees of freedom without first introducing the notion of “condensation” of the structural stiffness matrix.

The structure is divided into two parts, with the interface at the “pilehead joints” at or near the mudline, as shown in Figure 1 below.

![](SACS2024_PSI/chunk0_5638c34c0226ae05b1cd54578185910e1138c6f073f1474374b9b82583444cdf.jpg)

The piles below the pilehead joints are nonlinear elements while the structure above the pilehead joints is linear. The structure above the pilehead joints serves the following roles:

1. Connect the piles to each other with a medium having certain well defined linear stiffness properties.   
2. Introduce loads to the pileheads.

The process of condensation involves reducing the linear structure above the pilehead joints and loads to an equivalent linear stiffness matrix involving only the pilehead degrees of freedom and a set of forces applied to those degrees of freedom. For example, a four-pile jacket may have several hundred degrees of freedom but the nonlinear part of the stiffness matrix will only have 24 degrees of freedom (i.e. 4 pilehead joints with 6 degrees of freedom per pile).

## 4.2 DERIVATION OF INTERACTION EQUATIONS

To derive the interaction equation, first consider a single pile as illustrated in the figure below.

Assume that the deflected shape of the pile is very nearly in a plane containing the axis of the pile. This assumption is valid if:

1. The pilehead torque does not influence the lateral deflection.   
2. The resultant pilehead bending moment is about an axis perpendicular to the direction of the resultant pilehead lateral force.

Note: The reasons for this assumption will be addressed later in the discussion.

![](SACS2024_PSI/chunk0_582da9d521def89497a8f5a39f54bea500cf203988399b6e54683b1f4e2dfaa9.jpg)

The first of these conditions may be accepted based on the usual small displacement restriction of structural analysis. The usual conditions under which offshore structures (and indeed most other structures) operate produce resultant pilehead bending moments and lateral forces that nearly satisfy

condition 2. Note that it is not assumed that all the piles deform in the same plane, but only that each pile deforms in a plane. That plane, however, may be different from pile to pile.

Plots can be developed relating any pilehead force (or moment) component to any pilehead displacement (or rotation) component for fixed values of axial load and the other displacement or rotation components. A typical plot may have the general appearance of Figure 3. The slope of the curve at a point such as $^{ \prime \prime } { \sf A }^{ \prime \prime } ,$ , is defined as the stiffness coefficient relating the force or moment to the displacement or rotation at that point $" \mathsf{ A }^{ \prime \prime }$ . It is a function of displacement, rotation, or axial load.

![](SACS2024_PSI/chunk0_827d09bda610e3f2be3b92693a4efa685c54eaa45b0c542ac4cdc8333aa2d88a.jpg)

The equation of the F vs. δ curve may be written in the form:

$$F = K \delta + F_{O} \tag{1}$$

where K and $F_{ O }$ are functions of $\delta , \vartheta ,$ and P.

These considerations are generalized to 6 pilehead degrees of freedom and the results written in matrix form:

$$\{F \} = [ K ] \{\delta \} + \left\{F_{O} \right\} \tag{2}$$

where $\{ F \} , \{ \delta \} .$ , and $\{ F o \}$ are ${ \sf 6 } \times{ \sf 1 }$ matrices (column vectors) and [K] is a $6 \times 6$ matrix. In addition, [K] and $\{ F o \}$ are functions of $\delta , \vartheta ,$ and P.

![](SACS2024_PSI/chunk0_60bfdedcc63fa0595c6af7e450ad2554a90d038e816bc2981b4b4777750550ee.jpg)  
Figure 4 is a schematic sketch of a jacket supported by piles. The nonlinear piles are symbolically represented by the spring-like elements at the pilehead joints. External forces are applied over the jacket including, perhaps, at the pilehead joints. The jacket consists of the pile interface degrees of freedom (designated by subscript I) and the “free” degrees of freedom (designated by the subscript F). The Force-Displacement relationship for the jacket-pile combination can be written in partitioned matrix notation as:

$$\left\{\frac{F_{F}}{F_{I}} \right\} = \left[ \begin{array}{c c} K_{F F} & K_{F I} \\ \hline K_{I F} & K_{I I} + K_{P} \end{array} \right] \left\{\frac{D_{F}}{D_{I}} \right\} + \left\{\frac{0}{F_{O}} \right\} \tag{3}$$

In equation 3, the terms FF and FI are the external force vectors applied to the structure at the “free” and interface degrees of freedom respectively and $\mathsf{ D }_{ \mathsf{ F } }$ and $\mathsf{ D }_{ \mathsf{ I } }$ are the corresponding displacement vectors. $\mathsf{ K }_{ \mathsf{ P } }$ is the assembled nonlinear stiffness matrix of the piles at the interface degrees of freedom, and $\mathsf{ F }_{ 0 }$ is the column vector of the pile “intercept” forces. As discussed previously, both $\mathsf{ K }_{ \mathsf{ P } }$ and $\mathsf{ F }_{ 0 }$ depend on the interface displacement vector $\mathsf{ D }_{ \mathsf{ I } } .$ All other stiffness coefficients are independent of the displacements and can be evaluated once at the start of the problem.

Figure 5 (above) shows the free bodies of the jacket and piles. The forces acting in these bodies include the equal and opposite interface force vector, $F_{ I } .$ The force-displacement relationships for the piles and jacket respectively are:

$$\bar{F}_{I} = K_{P} D_{I} + F_{O}, \tag{4}$$

and

$$\left\{ \begin{array}{c} F_{F} \\ F_{I} - \bar{F}_{I} \end{array} \right\} = \left[ \begin{array}{l l} K_{F F} & K_{F I} \\ K_{I F} & K_{I I} \end{array} \right] \left\{ \begin{array}{l} D_{F} \\ D_{I} \end{array} \right\} \tag{5}$$

Equations 4 and 5 are simply a breakdown of equation 3 into the contribution from the nonlinear pile and linear structure respectively. Combining these two equations yields equation 3.

Equation 5 can be expanded, resulting in:

$$F_{F} = K_{F F} D_{F} + K_{I F} D_{I} \tag{6}$$

and

$$F_{I} - \bar{F}_{I} = K_{F I} D_{F} + K_{I I} D_{I} \tag{7}$$

Equation 6 is solved for DF and the result is substituted into equation 7, which is then rearranged to give:

$$- \bar{F}_{I} = K_{I F} K_{F F}^{-1} \left(F_{F} - K_{F I} D_{I}\right) + K_{I I} D_{I} - F_{I} \tag{8}$$

Equation 8 is a matrix equation whose order is equal to the number of interface degrees of freedom of equation 4. Adding these two equations eliminates the internal interface vector FI.

$$\left(K_{I I} - K_{I F} K_{F F}^{-1} K_{F I} + K_{P}\right) D_{I} + K_{I F} K_{F F}^{-1} F_{F} - F_{I} + F_{O} = 0 \tag{9}$$

The terms in this equation can be grouped into those that depend on DI and those that do not. The like terms are collected and the equation are rearranged resulting in:

$$D_{I} = - \left(\bar{K}_{I I} + K_{P}\right)^{-1} \left(\bar{\bar{F}}_{I I} + F_{O}\right) \tag{10}$$

where:

$$\overline{{\bar{F}}}_{I I} = K_{I F} K_{F F}^{-1} F_{F}$$

$$\bar{K}_{I I} = K_{I I} - K_{I F} K_{F F}^{-1} K_{F I} \tag{11}$$

Equations 4 and 10 are the basis for the iterative solution. One can do an analysis of each pile using the current pilehead displacement vector as its boundary condition. The pilehead force and moment are calculated, then a second pile analysis is done with an increment added to the displacements, resulting in new forces and moments. The stiffness coefficients then are the ratios of each of the pilehead force (or moment) increments to each of the displacement (or rotation) increments. The pilehead intercept force (or moment) components are then calculated using equation 4.

This process can be repeated for each iteration at each pilehead and for each load case. This approach, although theoretically sound, can require a large number of pile analyses.

The PSI program uses a more efficient approach. Instead of doing pile analyses at each pile for each iteration of each load case, a number of pile analyses are done at the outset to produce a set of pilehead force vs. displacement curves similar to Figure 3. Values for pilehead axial load (or deflection), lateral deflection, and rotation that span the range of values expected in the final solution are used. The program performs a pile analysis for each combination of these loads and rotations and stores the results. For each iteration, the pilehead displacements are used to determine the resulting pilehead stiffness coefficient and intercept forces from the curves. This procedure is continued until a preliminary convergence is met. Upon converging, PSI continues iterating but now performs a complete pile stiffness analysis for each iteration. This fine-tuning procedure continues until the force tolerance or maximum number of iterations is met.

## 4.3 ALIGNING TUBULAR PILE LOCAL COORDINATES

The P-Y data for the type of problems commonly encountered in the offshore applications can be highly nonlinear for a range of displacements over which the pile may have to function. This results in pilehead lateral force-displacement curves that are likewise nonlinear. Because of this, to get more accurate results, PSI performs its iterations in the plane of the resultant pilehead lateral displacement for tubular piles.

In actuality, the final results may have a small component of displacement out of the analysis plane. This is because, for each pile, the plane is found in the first iteration and that plane is used for all further iterations. The chord angle used in the first iteration is reported in the Initial Deflections report for each load case under the header ‘Beta’.

![](SACS2024_PSI/chunk0_bab3d7b8502f60944f5f09678dc942ba7c2b9177ddee65cc612b88328381bab8.jpg)  
(a)

![](SACS2024_PSI/chunk0_df3bec2d9c4ed1290fb7a167c78c1028a4a5ae0268f049df228e5bf5be19d5a0.jpg)  
(b)

To illustrate the necessity for the approach taken, consider a pile having the pilehead forcedisplacement curve shown in figure 8(b). Furthermore, the pile is loaded in a direction making an angle of 45 degrees with the coordinates used for analysis. The true resultant force on the pilehead is F, the corresponding true resulting displacement is δ. The true X and Y components of the pilehead force are each 0.707(F). If the pile were analyzed in these component directions the displacements would be equal and have the value 0.707δ, as shown in figure 8(b). The vector sum of these displacements would be δ which is far less than the true displacement δ. Thus, in order to insure an accurate result it is seen that the iterative analysis should be done in the plane of the pile deformation.

Therefore, accuracy is lost if a large component of pilehead bending moment exists in the direction of the resultant pilehead lateral load. On the other hand, if this component of moment is small then only a negligible error is made by combining the analyses in the two planes.

## 4.4 API-RP2A PILE RESISTANCE

PSI allows the user to specify the pile/soil response to axial, lateral, and torsional loads applied at the pilehead. In lieu of this information, the user may specify general soil properties with which the Pile program will use to develop the pile/soil response based on API-RP2A recommendations.

4.4.1 Axial Resistance

4.4.1.1 Ultimate Pile Capacity

Section 6.4 of the $20^{ \mathrm{ t h } }$ edition of API-RP2A suggest that the pile capacity, $Q_{ d } ,$ may be determined from (equation 6.41.1-1 in API-RP2A):

$$Q_{d} = f A_{s} + q A_{p} \tag{12}$$

where f = unit skin friction capacity, $A_{ s } =$ side surface area of pile, q = unit end bearing capacity and $A_{ p } =$ gross end area of pile.

4.4.1.2 Skin Friction and End Bearing

For pipe piles in cohesive soils, the unit skin friction, $f ,$ at any point along the pile, can be calculated from the following:

$$f = \alpha c \tag{13}$$

where c is the undrained shear strength and α is a dimensionless factor that may be taken as:

$$\alpha = \left\{ \begin{array}{l l} 1. 0 & \text{i f} \quad \psi <   0. 25 \\ 0. 5 \psi^{- 0. 5} & \text{i f} 0. 25 \leq \psi \leq 1. 0 \\ 0. 5 \psi^{- 0. 25} & \text{i f} 1. 0 <   \psi \end{array} \right. \tag{14}$$

where $\psi = c / p_{ o }^{ \prime }$ and ${ p_{ o } }^{ \prime }$ is the effective overburden pressure. The unit end bearing q for piles in cohesive soils is taken as 9c.

For pipe piles in cohesionless soil, the unit skin friction and unit end bearing are calculated from (equations 6.4.3-1 and 6.4.3-2 in API-RP2A):

$$F = K p_{o} \tan (\delta) \tag{15}$$

and

$$q = p_{o} N_{q} \tag{16}$$

where K = coefficient of lateral earth pressure, $p_{ o } =$ effective overburden pressure, δ = angle of soil friction on pile wall and $N_{ q } =$ bearing capacity factor.

Note: Unit skin friction and unit end bearing for cohesionless soils do not increase linearly with the overburden pressure indefinitely. The values are limited to the maximum values listed in the table below.

The user may enter values for these parameters or use program defaults. The coefficient for lateral earth pressure, $K ,$ may be between 0.5 and 1.0 as suggested by $\mathsf{ A P l } ,$ and has a default value of 1.0. At any depth, the program uses the weight of the soil above the level as the effective overburden pressure, $p_{ o } .$ This weight is calculated using the submerged unit weight of the soil, which the user must input. The default values for friction angle, δ, and bearing capacity factor, $\mathsf{ N }_{ \mathsf{ q } } ,$ depend on the soil type and are listed along with $f_{ \mathrm{ m a x } }$ and $q_{ \mathrm{ m a x } }$ below:



| API 21stEd. Suppl.2Soil Type | API 21stEd. Suppl.3API 22ndEd.Soil Type | SACS Soil Type | δ | Nq | fmax | qmax |
| --- | --- | --- | --- | --- | --- | --- |
| Dense GravelVery Dense Sand | Very Dense Sand | Gravel | 35° | 50 | 2.4 | 250 |
| Dense Sand | Dense Sand |  |  |  |  |  |
| Very Dense Sand-Silt | Very Dense Sand-Silt | Clean Sand | 30° | 40 | 2.0 | 200 |
| Medium Sand | Medium Sand | Silty Sand | 25° | 20 | 1.7 | 100 |
| Dense Sand-Silt | Dense Sand-Silt |  |  |  |  |  |
| Loose Sand* |  |  |  |  |  |  |
| Medium Sand-Silt | Medium Sand-Silt | Sandy Silt | 20° | 12 | 1.4 | 60 |
| Dense Silt* |  |  |  |  |  |  |
| Very Loose Sand* | Very Loose Sand* |  |  |  |  |  |
| Loose Sand* | Loose Sand* |  |  |  |  |  |
| Loose Sand-Silt* | Loose Sand-Silt* | Silt | 15° | 8 | 1.0 | 40 |
| Medium Silt* | Medium Silt* |  |  |  |  |  |
|  | Dense Silt* |  |  |  |  |  |



* API RP-2A 21st Edition supplement 3 and API RP-2A 22nd edition recommend the use of CPT-based methods to determine properties these soil types.   
Note: For rock, the user must input values for the skin friction capacity, f, and the unit bearing capacity, q.

4.4.1.3 Soil Axial Load Transfer Curves

Axial load transfer and pile displacement curves, T-Z curves, are constructed based on API RP2A recommendations. The T-Z curves are generated based on the following tables where z is the local pile deflection, D is the pile diameter, t is the mobilized soil adhesion and $t_{ \mathsf{ m a x } }$ is the maximum soil pile adhesion or unit skin friction.

$\mathsf{ A P l ~ R P - 2 A 21^{ s t } \mathsf{ E d i t i o n } }$   



| Clay | Clay | Sand | Sand |
| --- | --- | --- | --- |
| z/D | t/tmax | z (in) | t/tmax |
| 0.00 | 0.00 | 0.00 | 0.00 |
| 0.0016 | 0.30 | 0.10 | 1.00 |
| 0.0031 | 0.50 | ∞ | 1.00 |
| 0.0057 | 0.75 |  |  |





| 0.0080 | 0.90 |
| --- | --- |
| 0.0100 | 1.0 |
| 0.0200 | 0.70-0.90 |
| ∞ | 0.70-0.90 |



API RP-2A 22nd Edition   



| Clay | Clay | Sand | Sand |
| --- | --- | --- | --- |
| z/zpeak | t/tmax | z/zpeak | t/tmax |
| 0.00 | 0.00 | 0.00 | 0.00 |
| 0.16 | 0.30 | 0.16 | 0.30 |
| 0.31 | 0.50 | 0.31 | 0.50 |
| 0.57 | 0.75 | 0.57 | 0.75 |
| 0.80 | 0.90 | 0.80 | 0.90 |
| 1.00 | 1.0 | 1.00 | 1.0 |
| 2.00 | 0.70-0.90 | 2.00 | 1.0 |
| ∞ | 0.70-0.90 | ∞ | 1.0 |



Note: API RP-2A $22^{ n d }$ Edition recommends the skin friction is fully mobilized at $Z_{ p e a k }$ (a user-defined parameter). API-RP2A 22nd Edition recommends that the $Z_{ p e a k }$ ratio to pile diameter may vary from 0.25 % to 2.0 % (with the default value of 1%).

4.4.1.4 Tip Load - Displacement Curves

The end bearing or tip load capacity can be generated in the form of end bearing T-Z (or Q-Z) curves based on API RP2A recommendations as follows:



| z/D | t/tp |
| --- | --- |
| 0.002 | 0.25 |
| 0.013 | 0.50 |
| 0.042 | 0.75 |
| 0.073 | 0.90 |
| 0.100 | 1.00 |



where z is the axial tip deflection, D is the pile diameter, t is the mobilized end bearing capacity and $t_{ p }$ is the total end bearing.

4.4.2 Lateral Resistance for Soft Clays

P-Y curves for lateral resistance are generated based on the suggestions in section 6.8 of the $20^{ \mathrm{ t h } }$ edition of API RP2A. For soft clays the ultimate resisting pressure, $p_{ u } ,$ is given by:

For $X < X_{ \mathsf{ R } }$ (equation 6.8.2-1 in API RP2A)

$$p_{u} = 3 c + \gamma X + J \frac{X c}{D} \tag{17}$$

and for $X > X_{ R }$ (equation 6.8.2-2 in API RP2A)

$$p_{u} = 9 c \tag{18}$$

where c = undrained shear strength of undisturbed clay simple, D = pile diameter γ = effective unit weight of the soil, J = dimensionless constant between 0.25 and 0.5, X = depth below soil surface, and XR= depth to bottom of the zone of reduced resistance.

Note: $X_{ R }$ is the value of X for which equations 6.8.2-1 and 6.8.2-2 produce equal values for $p_{ u } .$

Once the ultimate resistance is known the P-Y curve is constructed as a series of straight lines. Two cases arise: static and cyclic load conditions. For the static case, the following points define the P-Y curve:

Clay P-Y curves for static loading   



| API 21st Edition Supple. 2 | API 21st Edition Supple. 2 | API 21st Edition Supple. 3 | API 21st Edition Supple. 3 |
| --- | --- | --- | --- |
|  |  | API 22nd Edition | API 22nd Edition |
| p/pu | y/yc | p/pu | y/yc |
| 0.00 | 0.0 | 0.00 | 0.0 |
| 0.50 | 1.0 | 0.23 | 0.1 |
| 0.72 | 3.0 | 0.33 | 0.3 |
| 1.00 | 8.0 | 0.50 | 1.0 |
| 1.00 | ∞ | 0.72 | 3.0 |
|  |  | 1.00 | 8.0 |
|  |  | 1.00 | ∞ |



where p = lateral resistance, y = lateral deflection, $y_{ c } = 2 . 5 e_{ c } D$ and $e_{ c } = \mathsf{ s t r a i n }$ at one half the maximum stress for undrained compression test for undisturbed samples.

Note: When $e_{ c }$ is left blank, yc is assumed to be 1.0.

For cyclic loading, the points defining the P-Y curves are:

Clay P-Y curves for cyclic loading $X > X_{ R }$   



| API 21st Edition Supple. 2 | API 21st Edition Supple. 2 | API 21st Edition Supple. 3 | API 21st Edition Supple. 3 |
| --- | --- | --- | --- |
|  |  | API 22nd Edition | API 22nd Edition |
| p/pu | y/yc | p/pu | y/yc |
| 0.00 | 0.0 | 0.0 | 0.0 |
| 0.50 | 1.0 | 0.23 | 0.1 |
| 0.72 | 3.0 | 0.33 | 0.3 |
| 0.72 | ∞ | 0.50 | 1.0 |
|  |  | 0.72 | 3.0 |
|  |  | 0.72 | ∞ |



Clay P-Y curves for cyclic loading $X < X_{ R }$   



| API 21st Edition Supple. 2 | API 21st Edition Supple. 2 | API 21st Edition Supple. 3 | API 21st Edition Supple. 3 |
| --- | --- | --- | --- |
| API 21st Edition Supple. 2 | API 21st Edition Supple. 2 | API 22nd Edition | API 22nd Edition |
| p/pu | y/yc | p/pu | y/yc |
| 0.00 | 0.0 | 0.0 | 0.0 |
| 0.50 | 1.0 | 0.23 | 0.1 |
| 0.72 | 3.0 | 0.33 | 0.3 |
| 0.72X/XR | 15.0 | 0.50 | 1.0 |
| 0.72X/XR | ∞ | 0.72 | 3.0 |
|  |  | 0.72X/XR | 15.0 |
|  |  | 0.72X/XR | ∞ |



4.4.3 Lateral Resistance for Sand

RP2A gives the ultimate bearing capacity for sand as the smaller value of:

$$p_{u s} = \left(C_{1} H + C_{2} D\right) \gamma H$$

$$p_{u d} = C_{3} D \gamma H \tag{19}$$

where $p_{ u } =$ ultimate resistance (subscript s for shallow, d for deep), γ = effective unit weight of soil, $H =$ depth, D = pile diameter and $C_{ 1 } , C_{ 2 } , C_{ 3 } =$ coefficients from figure 6.8.6-1 in API RP2A (using $\phi^{ \prime } = \mathsf{ a n g l e }$ of internal friction for sand).

The load-deflection (P-Y) curves are nonlinear and are approximated by the following expression:

$$P = A p_{u} \tanh  \left[ \frac{k H y}{A p_{u}} \right] \tag{20}$$

where $p_{ u } = \mathsf{ u l t i m a t e }$ bearing capacity at depth H, k = initial modulus of subgrade reaction, y = lateral deflection, $A = 0 . 9$ for cyclic loading or $3 . 0 - 0 . 8 H / D \geq 0 . 9$ for static loading.

## 4.5 EQUIVALENT PILE STUB

The following is the derivation of the method used to linearize the soil/pile system into an equivalent pile stub.

Throughout this discussion, the following definitions apply:

L =length of elastic stub model

$L_{ o }$ =length of rigid link offset

$M_{ o } , P_{ o }$ = forces at pilehead joint

M,P = forces on end of elastic stub at offset end

$\delta , \delta_{ o }$ = deflection of elastic stub at offset end and pilehead joint

$\theta , \theta_{ o }$ = rotation of elastic stub at offset end and pilehead joint

![](SACS2024_PSI/chunk0_7ff7c8a7564b005ffa4855869d4cdee2414a9df48dccb75d6b1ae541cbf6d962.jpg)  
PILEHEAD JOINT RIGID OFFSET   
ELASTIC STUB

Rigid link relationships are defined by

$$P_{o} = P$$

$$M_{o} = M - P L_{o}$$

$$\delta_{o} = \delta + L_{o} \theta$$

$$\theta_{o} = \theta \tag{21}$$

and governing equation and matrix notation are given as follow.

We may formulate Elastic Stub as

$$\left\{ \begin{array}{l} P \\ M \end{array} \right\} = \left[ \begin{array}{l l} K_{\delta \delta} & K_{\delta \theta} \\ K_{\theta \delta} & K_{\theta \theta} \end{array} \right] \left\{ \begin{array}{l} \delta \\ \theta \end{array} \right\} \tag{22}$$

and the rigid link is given by

$$\left\{ \begin{array}{l} P_{o} \\ M_{o} \end{array} \right\} = \left[ \begin{array}{c c} 1 & 0 \\ - L_{o} & 1 \end{array} \right] \left\{ \begin{array}{l} P \\ M \end{array} \right\} \tag{23}$$

and

$$\left\{ \begin{array}{l} \delta_{o} \\ \theta_{o} \end{array} \right\} = \left[ \begin{array}{c c} 1 & L_{o} \\ 0 & 1 \end{array} \right] \left\{ \begin{array}{l} \delta \\ \theta \end{array} \right\} \tag{24}$$

or

$$\left\{ \begin{array}{l} \delta \\ \theta \end{array} \right\} = \left[ \begin{array}{c c} 1 & 0 \\ - L_{o} & 1 \end{array} \right] \left\{ \begin{array}{l} \delta_{o} \\ \theta_{o} \end{array} \right\} \tag{25}$$

Substituting 23 into 24 then into 25 the following equation, we get

$$\left\{ \begin{array}{l} P_{0} \\ M_{0} \end{array} \right\} = \left[ \begin{array}{l l} 1 & 0 \\ - L_{0} & 1 \end{array} \right] \left[ \begin{array}{l l} K_{\delta \delta} & K_{\delta \theta} \\ K_{\theta \delta} & K_{\theta \theta} \end{array} \right] \left[ \begin{array}{l l} 1 & - L_{0} \\ 0 & 1 \end{array} \right] \left\{ \begin{array}{l} \delta_{0} \\ \theta_{0} \end{array} \right\} \tag{26}$$

then

$$\left\{ \begin{array}{l} P_{0} \\ M_{0} \end{array} \right\} = \left[ \begin{array}{c c} K_{\delta \delta} & K_{\delta \theta} \\ K_{\theta \delta} - L_{0} K_{\delta \delta} & K_{\theta \theta} - L_{0} K_{\delta \theta} \end{array} \right] \left[ \begin{array}{c c} 1 & - L_{0} \\ 0 & 0 \end{array} \right] \left\{ \begin{array}{l} \delta_{0} \\ \theta_{0} \end{array} \right\} \tag{27}$$

and finally

$$\left\{ \begin{array}{l} P_{0} \\ M_{0} \end{array} \right\} = \left[ \begin{array}{c c} K_{\delta \delta} & K_{\delta \theta} - L_{0} K_{\delta \delta} \\ K_{\theta \delta} - L_{0} K_{\delta \delta} & L_{0}^{2} K_{\delta \delta} - 2 L_{0} K_{\theta \delta} + K_{\theta \theta} \end{array} \right] \left\{ \begin{array}{l} \delta_{0} \\ \theta_{0} \end{array} \right\} \tag{28}$$

The elastic stub stiffness matrix can be rewritten as follows from beam theory.

$$\left[ \begin{array}{l l} K_{\delta \delta} & K_{\delta \theta} \\ K_{\theta \delta} & K_{\theta \theta} \end{array} \right]^{-1} = \left[ \begin{array}{c c} \frac{L^{3}}{3 E I} & \frac{L^{2}}{2 E I} \\ \frac{L^{2}}{2 E I} & \frac{L}{E I} \end{array} \right] \tag{29}$$

Inverting the matrix yields:

$$\left[ \begin{array}{l l} K_{\delta \delta} & K_{\delta \theta} \\ K_{\theta \delta} & K_{\theta \theta} \end{array} \right] = \left[ \begin{array}{c c} \frac{12 E I}{L^{3}} & - \frac{6 E I}{L^{2}} \\ - \frac{6 E I}{L^{2}} & \frac{4 E I}{L} \end{array} \right] \tag{30}$$

therefore, for the elastic stub:

$$K_{\delta \delta} = \frac{12 E I}{L^{3}} \tag{31}$$

$$K_{\delta \theta} = K_{\theta \delta} = - \frac{6 E I}{L^{2}} \tag{32}$$

and

$$K_{\theta \theta} = \frac{4 E I}{L} \tag{33}$$

Substitute these values into equation 28 to determine combined stiffness terms.

$$K_{\delta \delta}^{\prime} = K_{\delta \delta} = \frac{12 E I}{L^{3}} \tag{34}$$

$$K_{\delta \theta}^{\prime} = K_{\theta \delta}^{\prime} = K_{\delta \theta} - L_{o} K_{\delta \delta} = - \frac{6 E I}{L^{2}} - \frac{12 E I L_{o}}{L^{3}} \tag{35}$$

$$K_{\theta \theta}^{\prime} = L_{o}^{2} K_{\delta \delta} - L_{o} K_{\delta \theta} - K_{\theta \delta} L_{o} + K_{\theta \theta} = \frac{12 E I L_{o}^{2}}{L^{3}} + \frac{12 E I L_{o}}{L^{2}} + \frac{4 E I}{L} \tag{36}$$

Solving for $I , L_{ o }$ and L yields:

$$I = \frac{K_{\delta \delta}^{\prime} L^{3}}{12 E} \tag{37}$$

$$L_{o} = - \frac{K_{\delta \theta}^{\prime}}{K_{\delta \delta}^{\prime}} - \frac{L}{2} \tag{38}$$

$$L = \sqrt{12 \left(\frac{K_{\theta \theta}^{\prime}}{K_{\delta \delta}^{\prime}} - \left(\frac{K_{\delta \theta}^{\prime}}{L_{\delta \delta}^{\prime}}\right)^{2}\right)} \tag{39}$$

In addition, the axial stiffness of the pile is modeled by giving the pile a cross sectional area such that:

$$K_{\text{a x i a l}}^{\prime} = \frac{A E}{L} \tag{40}$$

Or

$$A = \frac{L}{E} K_{\text{a x i a l}}^{\prime} \tag{41}$$

where the length, L, is from equation 39.

4.5.1 Rules for Modeling a Pile Stub

Pile stubs may be modeled such that the stub runs down from the pilehead to the pile stub tip or from the pile stub tip up to the pilehead joint. In either case, the distance from the pilehead to the pile tip is represented by $L + L_{ o } ,$ where L is the actual length of the pile stub element and Lo is either a positive or negative offset.

The Pile program reports the pile stub properties assuming that the pile stub is modeled from the pilehead down to the pile stub tip. Therefore, positive offsets reported by the program refer to an offset down from the pilehead joint that shortens the stub member (see Figure A). Conversely, offsets reported as negative numbers elongate the pile stub above the pilehead joint (see Figure B).

![](SACS2024_PSI/chunk0_8187d315882ff4995a26b949c50219c7dce653ac1edeec5ca2ce82c15fdf7a61.jpg)

When adding pile stubs to a model, the following rules should be adhered to:

1. Use Prismatic cross section “PRI” for the elastic stub model. Use shear areas ten times larger than the axial area to eliminate shear deflection.   
2. Use local member offsets.   
3. Fix the tip of the pile stub to the ground.

## 4.6 PILE CAPACITY CALCULATION

Pile program computes the pile capacity using three different methods:

1. SACS Capacity method based on nonlinear interaction between pile and soil.

In this method, SACS applies an axial displacement at the pilehead and gradually increases the displacement – either pulling the pile for tensile capacity or pushing it for compressive capacity. The pile capacity is maximum or peak of the force-displacement curve. This method results in the most accurate value for pile capacity. See following figure for more details.

![](SACS2024_PSI/chunk0_1f0ae365457e583089420e30c54ec1a7758e037eaffc91b9ef384820443a2152.jpg)

2. Ultimate Capacity method based on maximum skin friction:

This method assumes the soil is fully mobilized along the entire length of the pile – skin friction reaches the maximum value in T-Z curve for the entire pile length. When the skin friction is determined, the pile capacity is skin friction multiplied by the pile's outer area. It many pile simulations (specifically long piles), the soil is not necessarily fully mobilized at all points along the pile length. Therefore, this method may overestimate the pile capacity.

3. The residual Capacity method based on residual skin friction:

This method is similar to Ultimate Capacity Method, but it uses residual skin friction (instead of maximum skin friction) to determine pile capacity. This method may also result in overestimating the pile capacity. The following graph shows the difference between maximum skin friction and residual skin friction for a sample T-Z curve.

![](SACS2024_PSI/chunk0_edd092db789934e2d3373511ab3327b6fee0820d2a63afa9619dcee9362edec2.jpg)  
T-Z Curve

## 4.7 SOIL LIQUEFACTION

When the user specifies soil liquefaction layers, PSI will reduce the p-y, t-z, and q-z curves by a calculated soil liquefaction reduction factor $\mathrm{ m }_{ \mathrm{ p } } . [ 1 ]$

The soil behavior is first classified using the soil behavior index $\left( \mathrm{ I }_{ \mathrm{ c } } \right) \left[ 2 \right]$ :

$$\mathrm{I_{c}} = \sqrt{(3 . 47 - \log (\mathrm{Q}))^{2} + (1 . 22 + \log (\mathrm{F}))^{2}}$$

Q and F are the normalized tip and sleeve friction ratios:

$$Q = \frac{\left(q_{c} - \sigma_{v o}\right) \left(P_{a} / \sigma_{v o}^{\prime}\right)^{n}}{\sigma_{v o}^{\prime}}$$

$$F = \frac{f_{s}}{q_{c} - \sigma_{v o}}\times 100\%$$

Where $\mathrm{ f }_{ s }$ is the sleeve friction, ${ \mathsf{ q } }_{ \mathsf{ c } }$ is the cone tip resistance, $\sigma_{ v o }$ is the overburden pressure, $\sigma_{ v o }^{ ' }$ is the effective overburden pressure, $P_{ a }$ is the atmospheric pressure, and n is the soil type exponent.

The soil type exponent varies between 0.5 in sands and 1.0 in clays. In SACS, the following values are used:



| Soil Type | n |
| --- | --- |
| CLAY | 1.0 |
| SILT | 0.7 |
| SAND | 0.5 |



If the soil type is not specified, SACS will determine ?? based on the relationship between $I_{ c }$ and ??.

The normalized dimensionless core penetration resistance can then be calculated:

$$\mathrm{q}_{\mathrm{c} 1 \mathrm{N}} = \frac{\mathrm{C}_{\mathrm{Q}} * \mathrm{q}_{\mathrm{c}}}{\mathrm{P}_{\mathrm{a}}}$$

Where $C_{ Q }$ is the overburden stress correction factor:

$$C_{Q} = \frac{P_{a}}{\sigma_{v o}^{\prime}} \leq 1. 7$$

The clean sand normalized core penetration resistance is then calculated:

$$\left(\mathrm{q}_{\mathrm{c 1 N}}\right)_{\mathrm{c s}} = \mathrm{q}_{\mathrm{c 1 N}} \mathrm{K}_{\mathrm{c}}$$

Where $K_{ c }$ is the clean sand normalization factor:

$$\mathrm{K}_{\mathrm{c}} = \left\{ \begin{array}{r l r} & 1. 0, & I_{c} \leq 1. 64 \\ - 0. 403 I_{c}^{4} + 5. 581 I_{c}^{3} - 21. 63 I_{c}^{2} + 33. 75 I_{c} - 17. 88, & I_{c} > 1. 64 \end{array} \right.$$

The cyclic resistance ratio, $\mathrm{ C R R }_{ 7 . 5 } ,$ can then be calculated:

$$C R R_{7. 5} = \left(1 + \frac{\alpha_{\mathrm{v}}}{100}\right) \left\{ \begin{array}{l l} 0. 833 \left[ \frac{(q_{c 1 N})_{c s}}{1000} \Big (1 + \frac{\alpha_{h}}{100} \Big) \right] + 0. 05, & (q_{c 1 N})_{c s} \leq 50 \\ 93 \left[ \frac{(q_{c 1 N})_{c s}}{1000} \Big (1 + \frac{\alpha_{h}}{100} \Big) \right]^{3} + 0. 08, & 160 > (q_{c 1 N})_{c s} \leq 50 \end{array} \right.$$

Where $\alpha_{ v }$ is a user-defined vertical shift of the ?????? curve and $\alpha_{ h }$ is a user-defined horizontal shift of the ?????? curve.

The cyclic stress ratio can be calculated as:

$$\mathrm{C S R} = 0. 65 \frac{\mathsf{a}_{\mathrm{m a x}}}{\mathsf{g}} \frac{\sigma_{\mathrm{v o}}}{\sigma_{v o}^{\prime}} \mathsf{r}_{\mathrm{d}}$$

Where $\mathtt{ a }_{ \mathrm{ m a x } }$ is the peak ground acceleration, g is the acceleration of gravity and $\boldsymbol{ \mathrm{ r_{ d } } }$ is a stress reduction factor calculated as:

$$r_{d} = \left\{ \begin{array}{l l} 1. 0 - 0. 00233 z, & z <   30 f t \\ 1. 174 - 0. 00813 z, & 75 f t \geq z > 30 f t \end{array} \right.$$

The factor of safety can then be calculated:

$$\mathrm{F S} = \frac{C R R_{7 . 5}}{C S R} M S F$$

Where ?????? is the magnitude scaling factor, expressed as:

$$\mathrm{M S F} = \frac{10^{2 . 24}}{\mathrm{M}_{\mathrm{w}}^{2 . 56}}$$

Where $\mathrm{ M }_{ \mathrm{ w } }$ is earthquake magnitude.

If the factor of safety is less than 1, then soil liquefaction occurs in the soil layer and the following modifications are applied to the p-y, t-z, and q-z curves.

The corrected standard penetration resistance is calculated using the following equation [3]:

$$(\mathrm{N}_{1})_{\mathrm{60 c s}} = \left[ 3. 242 (\mathrm{q}_{\mathrm{c 1 N}})_{\mathrm{c s}}^{0. 264} - 7. 209 \right]^{2}$$

And the soil liquefaction reduction factor $\mathrm{ m }_{ \mathrm{ p } }$ is then determined using the Average Brandenburg curve [4]:

$$\mathrm{m_{p}} = 4 \mathrm{x} 10^{-4} (\mathrm{N_{1}})_{60 \mathrm{c s}}^{2} + 1 \mathrm{x} 10^{-3} (\mathrm{N_{1}})_{60 \mathrm{c s}} + 5 \mathrm{x} 10^{-2}$$

$\mathbf{ m_{ p } m a y }$ be modified with the liquefaction multiplier factor $\alpha_{ \mathrm{ { m }_{ \mathrm{ { p } } } } }$ :

$$\mathrm{m_{p} = \alpha_{m_{p}} m_{p}}$$

The p-y, t-z, and q-z curves are then modified by the $\mathrm{ m_{ p } }$ factor:

$$P^{\prime} = P m_{p}$$

$$\mathrm{T}^{\prime} = \mathrm{T m}_{\mathrm{p}}$$

$$Q^{\prime} = Q m_{p}$$

5 PISA Method

## 5.1 Background

The PISA project was a research study to determine the behavior of monopiles for wind turbines [5-6]. These monopiles are relatively large in diameter compared to their length and do not behave the same as long slender piles, which are traditionally used for offshore structures. These monopiles tend to behave rigidly, remaining relatively straight when deflecting instead of bending.

Additional soil reactions have been introduced to represent this new behavior:

• P, the distributed lateral load   
${ \mathsf{ m } } ,$ the distributed moment   
$\mathsf{ H }_{ \mathsf{ B } } ,$ the horizontal base shear   
$M_{ \mathsf{ B } } ,$ the base moment

![](SACS2024_PSI/chunk0_aca70b78b0e716292600bbfb6f2f539cd5322791f3cfa9d0217fb713b5728050.jpg)  
Figure 1 - PISA Pile FE Model

## 5.2 Plaxis Monopile Designer and Pile3D Interoperability

Plaxis Monopile Designer can generate multiple 3D FE analysis geometries, which can be solved to generate soil reaction curves. The 3D FE models utilize a volumetric mesh of the soil geometry with advanced soil constitutive models, a mesh of the pile geometry, and interfaces defining the interaction between the pile and soil. The calculated soil reaction curves can then be used to calibrate a 1D FE model with the previously described soil reactions. This 1D FE model can then be used to quickly analyze and design the monopile geometry utilizing Timoshenko beam theory. However, Plaxis Monopile Designer is primarily a foundation analysis and design tool and is not intended to be used as a design

tool for the overall structure. The PISA method (distributed moment, base shear, and base moment soil reactions) has been implemented in Pile3D to be used for rigid monopile analysis in SACS. In the following sections, a series of analyses will be compared between Pile3D and 1D Plaxis Monopile Designer results.

## 5.3 PISA Method Verification

5.3.1 Soil Data

The soils from the original PISA research project were used in the comparison analysis models. One set of sand models and one set of clay models were included to capture the effects of soil type on the additional soil reactions. Additionally, there is a different normalization parameter for clay or soil which will be in the discussion of the Pile3D input data. The soil input data used to Generate the 3D FE Monopile Designer models is provided below.

Table 1 - Sand Model Properties   



| Soil | Top (m) | Bottom (m) | Submerged Unit Weight (kN/m3) | Small Strain Shear Stiffness Modulus (kN/m2) | Friction Angle (Deg) | Angle of Dilatancy (Deg) | Lateral Earth Pressure Coeff. at Rest |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Dunkirk Sand | 0.00 | -75.00 | 10.09 | 239.5E3 | 42.00 | 12.50 | 0.40 |





| Soil | Top (m) | Bottom (m) | Submerged Unit Weight (kN/m^3) | Undrained Shear Strength at Top (kN/m^2) | Undrained Shear Strength at Bottom (kN/m^2) | Sand Friction Angle (deg) |
| --- | --- | --- | --- | --- | --- | --- |
| Cowden Clay | 0.00 | -1.00 | 11.19 | 200.0 | 200.0 | 1.5 |
| Cowden Clay | -1.00 | -2.00 | 11.19 | 200.0 | 200.0 | 1.5 |
| Cowden Clay | -2.00 | -3.50 | 11.19 | 200.0 | 125.0 | 1.5 |
| Cowden Clay | -3.50 | -4.00 | 11.19 | 125.0 | 118.0 | 1.5 |
| Cowden Clay | -4.00 | -5.00 | 11.19 | 118.0 | 104.0 | 1.4 |
| Cowden Clay | -5.00 | -6.50 | 11.19 | 104.0 | 110.0 | 1.3 |
| Cowden Clay | -6.50 | -8.00 | 11.19 | 110.0 | 116.0 | 1.1 |
| Cowden Clay | -8.00 | -11.00 | 11.19 | 116.0 | 128.0 | 1.0 |
| Cowden Clay | -11.00 | -14.00 | 11.19 | 128.0 | 140.0 | 1.0 |
| Cowden Clay | -14.00 | -17.00 | 11.19 | 140.0 | 150.5 | 1.0 |
| Cowden Clay | -17.00 | -24.50 | 11.19 | 150.5 | 176.0 | 0.9 |



Table 2 - Clay Model Properties   



| Cowden Clay | -24.50 | -32.00 | 11.19 | 176.0 | 201.5 | 0.81 |
| --- | --- | --- | --- | --- | --- | --- |
| Cowden Clay | -32.00 | -40.00 | 11.19 | 201.5 | 227.5 | 0.77 |
| Cowden Clay | -40.00 | -55.00 | 11.19 | 227.5 | 277.0 | 0.71 |
| Cowden Clay | -55.00 | -75.00 | 11.19 | 277.0 | 343.0 | 0.64 |



Additional information about the soil parameters and how they are considered in the Monopile Designer analysis can be found in the Plaxis Monopile Designer documentation.

5.3.2 Pile Geometries

A wide variety of geometries were used with both soil types to generate the 3D FE models in Monopile Designer. Six of these geometries were also used in the Pile3D analyses for comparisons. Two flexible piles were included to measure the effects of the PISA method on those models even though the PISA method is primarily intended for rigid piles.

![](SACS2024_PSI/chunk0_fc1339da414105afef11d2e894d69b730b96cc681395d8859ecf2c132a7c825d.jpg)  
Figure 2 - Pile Geometry Definition

Table 3 - Clay Soil Model Geometries   



| Pile ID | Soil type | Pile Extension, h (m) | Pile Length, L (m) | Diameter, D (m) | Thickness (m) | L/D |
| --- | --- | --- | --- | --- | --- | --- |
| P01 | Cowden Clay | 50 | 20 | 10 | 0.09 | 2 |
| P02 | Cowden Clay | 50 | 20 | 10 | 0.125 | 2 |
| P03 | Cowden Clay | 50 | 60 | 10 | 0.09 | 6 |
| P04 | Dunkirk Sand | 50 | 20 | 10 | 0.09 | 2 |
| P05 | Dunkirk Sand | 50 | 20 | 10 | 0.125 | 2 |
| P06 | Dunkirk Sand | 50 | 60 | 10 | 0.09 | 6 |



Table 4 - Sand Soil Model Geometries

5.3.3 SACS Pile3D Comparison with Monopile Designer 1D FE Analysis

5.3.3.1 Pile3D Input

The Plaxis Monopile Designer 1D FE solution was compared against the SACS Pile3D solution by taking the depth variation functions reported by Monopile Designer, converting them into SACS Pile3D input, and analyzing the same pile geometry in both Pile3D and Monopile Designer. The resulting displacements form the two analyses were then compared along the length of the piles.

The soil reaction curves are reported as normalized values in Monopile Designer; hence the curves were converted to the specific geometry using the following normalization parameters, these parameters are discussed in detail in the Monopile Designer documentation:

Figure 3 - PISA Normalization Parameters   



| Component | Clay normalisation | Sand normalisation |
| --- | --- | --- |
| Distributed load, p̅ | p̅ = p/(su/D) | p̅ = p/(σ'ν0D) |
| Lateral displacement, v̅ | v̅ = vI_R/D | v̅ = (vI_R/D) · √(pa/σ'ν0) = νG0/(σ'ν0D) |
| Distributed moment, m̅ | m̅ = m/(suD2) | m̅ = m/(pD) |
| Pile cross section rotation, ψ̅ | ψ̅ = ψIR | ψ̅ = ψIs · √(pa/σ'ν0) = ψG0/σ'ν0 |
| Base horizontal force, H_B | H_B = H_B/(suD²) | H_B = H_B/(σ'ν0D²) |
| Base moment, M_B | M_B = M_B/(suD³) | M_B = M_B/(σ'ν0D³) |



The Pile3D input was generated automatically by Monopile Designer. To account for pile extension (h), a zero-stiffness layer was added so that the imposed displacement at the top of the pile would result in the same rotations and displacements of the pile at the mudline. The pile length was updated as the sum of the pile length and extension and the soil layers were then shifted down (by extension length) to their corresponding depth. A displacement-controlled analysis (using LTDFL card) was used in Pile3D to improve convergence, especially for highly non-linear cases which may include unloading. This method is not intended for load-controlled analyses as the load input supports both forces and moments at the mudline.

5.3.3.2 Special Considerations for PISA Sand

One of the main findings of the PISA project for Dunkirk Sand was that the distributed moment in Sand is highly nonlinear and depends on the lateral soil forces (p)[6]. Therefore, unlike for Clay, the distributed moment in Sand is a function of both lateral rotation and displacement of the pile, $i . e . , m =$ $m ( \theta , v )$ . This is also why in Figure $_{ 3 ; }$ the normalized distributed moment of Sand depends on the distributed lateral load (p). This, however, makes exporting the Sand distributed moments to Pile3d as only a function of pile rotation impossible. Therefore, for Sand, Pile3d and Plaxis Monopile Designer assume that the distributed moment was sampled linearly using lateral displacements of the corresponding, lateral distributed load curve, i.e., at each point where the distributed moment $m ( \theta_{ i } , v_{ i } )$ . is sampled, we assume:

$$\frac{v_{i}}{v_{\mathrm{m a x}}} = \frac{\theta_{i}}{\theta_{\mathrm{m a x}}}$$

During the solution, for each Sand layer (designated by entering $' 5^{ \prime }$ on column 63 of SOIL M-T SLOC line), Pile3d reconstructs the normalized distributed moment ??̅ and uses both lateral displacement and rotation to calculate the distributed moment value as $m = p D \overline{ { m } }$ .

5.3.3.3 Results’ Comparison

Pile tip displacement and pile head force reported in Pile3D were directly compared against the Monopile Designer. These values are chosen here because, due to the nature of the analysis, the largest errors for displacement and load occur for each model at the pile tip and pile head, respectively. Additionally, we plot comparisons of pile lateral displacement, internal forces, and moments against depth and pile head lateral force versus displacement.

Note: All verification problems presented in this section are available under Sample 27 in SACS samples.

5.3.3.3.1 Cowden Clay Models

The clay models' largest numerical differences in pile tip displacement and pile head force were 1.18% and 1.55% for P01.

Table 5 - Clay Soil Results’ Comparison   



| Pile | Soil type | L/D | Depth (m) | Pile Tip Displacement (cm) | Pile Tip Displacement (cm) | Pile Tip Displacement (cm) | Pile Head Force (kN) | Pile Head Force (kN) | Pile Head Force (kN) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | Pile3d | Plaxis | Difference | Pile3d | Plaxis | Difference |
| P01 | Cowden Clay | 2 | 70 | -51.03 | -51.64 | 0.61 | 13420 | 13632 | 212 |
| P02 | Cowden Clay | 2 | 70 | -52.42 | -52.02 | 0.4 | 13447 | 13651 | 204 |
| P03 | Cowden Clay | 6 | 110 | -17.53 | -17.40 | 0.13 | 85126 | 85849 | 343 |



![](SACS2024_PSI/chunk0_663bef72864b676f1aada9d23659cdeb063e6318c6534254899208311db4dd29.jpg)  
Figure 4. P01, lateral displacement vs. depth

![](SACS2024_PSI/chunk0_62437ae526f8ee6436cacf76225930d1ff7e8f0a99b74ccafc18105c8c390a41.jpg)  
Figure 5. P01, pile head force vs. displacement

![](SACS2024_PSI/chunk0_c5d3b555e2cfb31a62932cf2fbd18540bb237e7c5ec216e8065bc881b9a4ea23.jpg)

![](SACS2024_PSI/chunk0_0e945bd4a28711d45fc324540a9c7a74d5ecb63f6e3a290220b953bcb287b166.jpg)  
Figure 6. P01, internal force (shear) vs. depth   
Figure 7. P01, internal (bending) moment vs. depth

![](SACS2024_PSI/chunk0_d0b5ce50f44718b0969a7abf1d468949ea4d1e03cf9daf66a7e78c7cc9117fbe.jpg)  
Figure 8. P02, lateral displacement vs. depth

![](SACS2024_PSI/chunk0_30bfabff2c12b50bffea9864303f6fe7f5c23c566bb884f4fb1430af2f6ac647.jpg)  
Figure 9. P02, pile head force vs. displacement

![](SACS2024_PSI/chunk0_e2832ae672a9ef81d1dc1167fece9ae95aafa1a3d65eaf87c59e5032fb079b1c.jpg)

![](SACS2024_PSI/chunk0_bd8101df2a9a6fd3a186f5300c5881d67ba3c8d290da89152e55ebbcf411259c.jpg)  
Figure 10. P02, internal force (shear) vs. depth   
Figure 11. P02, internal (bending) moment vs. depth

![](SACS2024_PSI/chunk0_989d24aa5cd7b7e527dc0b7ad1255296d1a705ff1112a3fc91bf718708dbce61.jpg)  
Figure 12. P03, lateral displacement vs. depth

![](SACS2024_PSI/chunk0_d1d0bcb3ff5b5ba3c68a31790ad920822005cafc79927dd957d402a345ff84c3.jpg)  
Figure 13. P03, pile head force vs. displacement

![](SACS2024_PSI/chunk0_f3b79f91734d4ec9a8d9d023491fb1c6e4fb63ca4085c773d0f112068d920c5f.jpg)

![](SACS2024_PSI/chunk0_e29347ce0512da3d564a7924117d95fd56bed68cbc3b18e0d030bcda629fa8ea.jpg)  
Figure 14. P03, internal force (shear) vs. depth   
Figure 15. P03, internal (bending) moment vs. depth

5.3.3.3.2 Dunkirk Sand Models

The clay models' largest numerical differences in pile tip displacement and pile head force were 0.001% and 0.88% for P04.

Table 6 - Sand Pile Tip Displacement Comparison   



| Pile | Soil type | L/D | Depth (m) | Pile Tip Displacement (cm) | Pile Tip Displacement (cm) | Pile Tip Displacement (cm) | Pile Head Force (kN) | Pile Head Force (kN) | Pile Head Force (kN) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | Pile3d | Plaxis | Difference | Pile3d | Plaxis | Difference |
| P04 | Dunkirk Sand | 2 | 70 | -64.393 | -64.392 | 0.001 | 25220 | 25000 | 220 |
| P05 | Dunkirk Sand | 2 | 70 | -64.405 | -64.410 | 0.005 | 25216 | 25000 | 216 |
| P06 | Dunkirk Sand | 6 | 110 | -1.988 | -1.354 | 0.634 | 119900 | 120000 | 100 |



![](SACS2024_PSI/chunk0_1586fe855281c1fe47a02f672d50d28d4e038c0194d04f90d96aa2bfc5bb1ef8.jpg)  
Figure 16. P04, vertical displacement vs. depth

![](SACS2024_PSI/chunk0_ce4c6051932b22e73a3e92ba62aba373cf90d670fcd27befaaa138dde54f98c2.jpg)  
Figure 17.

![](SACS2024_PSI/chunk0_da479ca0384ead84bda38897794018e910b5ee1506308d5171a8979d3a12fb2b.jpg)  
Figure 18. P04, pile head load vs. displacement   
Figure 19. P04, internal load (shear) vs. depth

![](SACS2024_PSI/chunk0_c8eb42dfccd07a6fb1c4a10ecad5d352beb1596d28aca48403236d45d6913c7b.jpg)

![](SACS2024_PSI/chunk0_bdc87f481388512b9a0bc8cecefa827bf8b21788b314f347b20780ae32364a4f.jpg)  
Figure 20. P04, internal (bending) moment vs. depth   
Figure 21. P05, vertical displacement vs. depth

![](SACS2024_PSI/chunk0_65f968bad0689f64cb78c9277c2db0750a669d0c162fdc694cca44ab99b71515.jpg)

![](SACS2024_PSI/chunk0_ceb8144692d15b50c67cb82bb18041e5acfa71670beaf40a5fb85b6f868e7131.jpg)  
Figure 22. P05, pile head load vs. displacement   
Figure 23. P05, internal load (shear) vs. depth

![](SACS2024_PSI/chunk0_225b1fe91cbcdbe695c9d484e7a1f3a3c41bff241624174b046f06b45d9f6929.jpg)

![](SACS2024_PSI/chunk0_70b79eefb8a28e79f5e3a1500cec3d073488f062858b577ad5a42bc932c01af4.jpg)  
Figure 24. P05, internal (bending) moment vs. depth   
Figure 25. P06, lateral displacement vs. depth

![](SACS2024_PSI/chunk1_5b2b3df99e8e2836ffb5186d2f389c91b7d39c14945c1cfe89113ecf0e0f78e6.jpg)

![](SACS2024_PSI/chunk1_21629bfd784ba050c1d2cc9c9846ff23a354312bb88c19e1b4e8c4160b14b9e0.jpg)  
Figure 26. P06, pile head force vs. displacement   
Figure 27. P06, internal force (shear) vs. depth

![](SACS2024_PSI/chunk1_ca650f01344900c01e48ed9312fd24a00516dea025cefa37249939a28388fcc2.jpg)  
Figure 28. P06, internal (bending) moment vs. depth

## 5.4 Extended Winkler Foundation

The extended Winkler foundation is a method developed at SACS that aims to approximate the distributed moment, base shear, and moment curves of the PISA method using the readily available soil lateral (P-Y) and axial (T-Z) reaction curves. Pile3d approximates the distributed moment and base shear using the T-Z curve and the base moment using the P-Y curve. Users can enable these options through SOIL LATERAL HEAD card columns 61, 62, and 67. The resulting curves can be viewed in the neutral chart file by including the PLTRQ card in the pile input.

6 TROUBLESHOOTING COMMON PROBLEMS

PSI is an iterative solution approach to a highly complicated problem and as such requires a certain degree of care on the part of the user. The following section discusses means of avoiding and correcting problems that may arise during the execution of PSI.

1. When a pile cannot completely dissipate the axial load, it may experience “soil punch through”. Usually piles exhibiting this problem must be redesigned with increased pile penetration, thus providing more pile length available to dissipate the load

This problem may also occur if user-specified TABR values exceed the pile’s axial capacity. If the final axial loads are much smaller than the user input values, the values should be decreased so that the axial behavior is adequately defined in the range of the solution value and the user-specified loads do not cause “punch through.” Alternatively, the user can specify axial deflection values instead of load values.

2. The iterative pile solution (either axial or lateral) may fail to converge. The program will produce a message to the effect that the solution did not converge for the set of conditions involved.

This usually occurs for the axial solution when the T-Z curves have a sharp slope discontinuity for the same value of displacement over the length of the pile. If the axial load is such that the pile displaces by this amount, the iteration procedure may cycle back and forth from one portion of the T-Z curve to another without converging. The problem can be corrected by either replacing the T-Z curves by ones with a more gradual transition from one portion to another or by changing the TABR value (if specified) by a small amount (perhaps 5 or 10 percent) so that the pile solution will be removed from the point of slope discontinuity. Similar behavior may occur for the lateral solution but is less common since for lateral loads the entire pile does not displace by approximately the same amount as is the case for axial loads. Lack of convergence for lateral loads may be similarly corrected by modifying the P-Y curves to smooth out the slope discontinuities or by changing the optional lateral TABR deflection values.

3. The number of iterations allowed per load case may be exceeded if:

a. Too few iterations are requested (columns 41-43 of the PSI options line).   
b. The convergence tolerances are too small (columns 25-40 of the PSI options line).   
c. Unusual soil conditions, such as a very stiff stratum (rock) sandwiched between two very soft strata, are present.

The problem can usually be resolved by increasing the number of iterations.

4. The combined reduced structural stiffness matrix and pilehead stiffness matrix is non-positive definite. The combined structural and pile stiffness matrix may be singular. This is usually the result of a joint in the structure being improperly constrained. One very common instance of

this is when a conductor is released for all three rotations at all of its nodes, including the top one. This causes the conductor to have no torsional stiffness, which results in the singular stiffness matrix. The correction is to remove the release for rotation about the local “X” axis at any node or nodes.

7 SAMPLE PROBLEMS

The structure shown in the figure was used to illustrate the various capabilities of the PSI program. Three separate runs are illustrated:

1. The first problem is a typical PSI analysis where axial and lateral soil properties are described by T-Z and P-Y curves respectively. In addition, numerous plots were generated including the soil data, axial and lateral deflections, and pile unity check. The pilehead stiffness tables were generated automatically in PSI.   
2. Sample Problem 2 is a single pile analysis used to determine the equivalent pile stub of the soil/pile foundation. In lieu of curves to define the soil load displacement relationships, general soil properties were input. Pile used this information to form the soil load displacement relationship per API-RP2A recommendations.   
3. Sample Problem 3 illustrates a mudslide case in the global X direction. User defined pilehead stiffness tables were used.

![](SACS2024_PSI/chunk1_3472b260de1815b6408802150667ddd4289f68ccb633c96555d39e196645cadc.jpg)

## 7.1 PILE SOIL INTERACTION ANALYSIS

The following is an example of a typical PSI analysis where T-Z and P-Y curves are used to define the load displacement relationship of the soil/pile foundation in the axial and lateral directions respectively.

The structure shown in the figure stands in 261.0 ft. of water. The model contains a load condition (AREA) which represents an area dead load on the deck, a load condition (EQPT) with equipment skid loading, a load condition (MISC) representing miscellaneous dead loads, and a load condition (LIVE) which represents area live loading on the deck. Load conditions FSEX and FSEY represent a combination of the element dead load and operational wave loading used in pile linearization for dynamic fatigue analyses. GRVX, GRVY, and GRVZ load conditions represent unit accelerations along each global axis direction used in pile linearization for dynamic seismic analyses. Load conditions P000, P045, and P090 represent operational environmental loading, while S000, S045, and S090 represent storm condition environmental loading. Wind area, marine growth, coefficient of drag and mass overrides, and member and group overrides are specified. Load combinations ESEX and EXEY are used in pile linearization for dynamic seismic analyses, OPR1, OPR2, and OPR3 are used for operating conditions and STM1, STM2, and STM3 are used for storm conditions.

The following is a portion of the SACS input file containing the input lines. For clarity, some model data not specific to PSI has been omitted.

```txt
1 2 3 4 5 6 7 8  
1234567890123456789012345678901234567890123456789012345678901234567890  
1 SAMPLE 03 ENGLISH UNITS MODEL  
2 OPTIONS EN SDUC 2 1 PTPT PT  
3 SECT
4 SECT CONE CON 36.0000.75026.000  
5 GRUP
6 GRUP LG1 42.000 1.375 29.0011.6050.00 1 1.001.00 0.500N490.005.00  
7 GRUP LG1 41.250 1.000 29.0011.6036.00 1 1.001.00 0.500N490.00  
8 GRUP LG1 42.000 1.375 29.0011.6050.00 1 1.001.00 0.500N490.005.00  
9**********ADDITIONAL GRUP LINES**********  
10 GRUP W.B 36.433 1.000 29.0111.2035.97 1 1.001.00 0.500 489.99  
11 GRUP W01 W24X162 29.0111.2035.97 1 1.001.00 0.500 489.99  
12 GRUP W02 W24X131 29.0111.2035.97 1 1.001.00 0.500 489.99  
13 MEMBER
14 MEMBER 101 201 LG1  
15 MEMBER 103 203 LG1  
16**********ADDITIONAL MEMBER LINES**********  
17 MEMBER 838 842 W02  
18MEMBER 839 844 W02  
19 PGRP
20 PGRP P01 0.375O129.000 0.25O36.ooo 49O.OOOO  
21PLATE
22PLATE AAAC 8O1 834 8O5 837 P01 O  
23PLATE AAAD 834 835 837 838 P01 O  
24JOINT
25JOINT 1O1 -24.-5O-26I-3.OOO  
26JOINT 1O2 -24.-5O-26I-3.OOOPILEHD  
27JOINT 1O3 5I.-5O-26I-4.OOO-3.OOO  
28JOINT 1O4 5I.-5O-26I-4.OOO-3.OOOPILEHD  
29JOINT 1O5 -24.-5O-26I-3.OOO  
3OJOINT 1O6 -24.-5O-26I-3.OOOPILEHD  
3IJOINT 1O7 5I.-5O-26I-4.OOO3.OOOPILEHD  
32JOINT 1O8 5I.-5O-26I-4.OOO3.OOOPILEHD 
```

The model input file specifies the following:

Lines 26-32. Joints 102, 104, 106 and 108 are specified as pilehead joints by PILEHD in columns 55-60 on the JOINT line.

The following is the PSI input file used in Sample Problem 1, followed by a detailed discussion of the input lines.



|  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | 1234567890123456789012345678901234567890123456789012345678901234567890 | 1234567890123456789012345678901234567890123456789012345678901234567890 | 1234567890123456789012345678901234567890123456789012345678901234567890 | 1234567890123456789012345678901234567890123456789012345678901234567890 | 1234567890123456789012345678901234567890123456789012345678901234567890 | 1234567890123456789012345678901234567890123456789012345678901234567890 | 1234567890123456789012345678901234567890123456789012345678901234567890 | 1234567890123456789012345678901234567890123456789012345678901234567890 |
| 1 | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS |
| 2 | PSIOPT +ZENG | SM | SM | SM | SM | 100 | 0.5 | 490. |
| 3 | * EXCLUDE FOUNDATION SE LOAD CASES FROM PILE CHECK | * EXCLUDE FOUNDATION SE LOAD CASES FROM PILE CHECK | * EXCLUDE FOUNDATION SE LOAD CASES FROM PILE CHECK | * EXCLUDE FOUNDATION SE LOAD CASES FROM PILE CHECK | * EXCLUDE FOUNDATION SE LOAD CASES FROM PILE CHECK | * EXCLUDE FOUNDATION SE LOAD CASES FROM PILE CHECK | * EXCLUDE FOUNDATION SE LOAD CASES FROM PILE CHECK | * EXCLUDE FOUNDATION SE LOAD CASES FROM PILE CHECK |
| 4 | LCSEL EX | FSEX FSEY ESEX ESEY | FSEX FSEY ESEX ESEY | FSEX FSEY ESEX ESEY | FSEX FSEY ESEX ESEY | FSEX FSEY ESEX ESEY | FSEX FSEY ESEX ESEY | FSEX FSEY ESEX ESEY |
| 5 | * FOUNDATION SUPERELEMENT FOR FATIGUE | * FOUNDATION SUPERELEMENT FOR FATIGUE | * FOUNDATION SUPERELEMENT FOR FATIGUE | * FOUNDATION SUPERELEMENT FOR FATIGUE | * FOUNDATION SUPERELEMENT FOR FATIGUE | * FOUNDATION SUPERELEMENT FOR FATIGUE | * FOUNDATION SUPERELEMENT FOR FATIGUE | * FOUNDATION SUPERELEMENT FOR FATIGUE |
| 6 | PILSUP AVG | FSEXFSEY | FSEXFSEY | FSEXFSEY | FSEXFSEY | FSEXFSEY | FSEXFSEY | FSEXFSEY |
| 7 | * FOUNDATION SUPERELEMENT FOR EARTHQUAKE | * FOUNDATION SUPERELEMENT FOR EARTHQUAKE | * FOUNDATION SUPERELEMENT FOR EARTHQUAKE | * FOUNDATION SUPERELEMENT FOR EARTHQUAKE | * FOUNDATION SUPERELEMENT FOR EARTHQUAKE | * FOUNDATION SUPERELEMENT FOR EARTHQUAKE | * FOUNDATION SUPERELEMENT FOR EARTHQUAKE | * FOUNDATION SUPERELEMENT FOR EARTHQUAKE |
| 8 | PILSUP AVG | ESEXESEY | ESEXESEY | ESEXESEY | ESEXESEY | ESEXESEY | ESEXESEY | ESEXESEY |
| 9 | PLTRQ SD DL | LS DA | LS DA | LS DA | LS DA | UC | UC | UC |
| 10 | PLGRP |  |  |  |  |  |  |  |
| 11 | PLGRP PL1 | 36.00 | 1.000 | 29.00 | 11.60 | 50.00 | 35.00 |  |
| 12 | PLGRP PL1 | 36.00 | 0.625 | 29.00 | 11.60 | 36.00 | 95.0 | 7.07 |
| 13 | PLGRP PL2 | 36.00 | 1.000 | 29.00 | 11.60 | 50.00 | 35.00 |  |
| 14 | PLGRP PL2 | 36.00 | 0.625 | 29.00 | 11.60 | 36.00 | 95.0 | 7.07 |
| 15 | PILE |  |  |  |  |  |  |  |
| 16 | PILE 102 202 PL1 |  |  |  |  |  | SOL1 |  |
| 17 | PILE 104 204 PL2 |  |  |  |  |  | SOL1 |  |
| 18 | PILE 106 206 PL1 |  |  |  |  |  | SOL1 |  |
| 19 | PILE 108 208 PL2 |  |  |  |  |  | SOL1 |  |
| 20 | SOIL |  |  |  |  |  |  |  |
| 21 | SOIL TZAXIAL HEAD 7 5 SOL1 | SOIL TZAXIAL HEAD 7 5 SOL1 | SOIL TZAXIAL HEAD 7 5 SOL1 | SOIL TZAXIAL HEAD 7 5 SOL1 | SOIL TZAXIAL HEAD 7 5 SOL1 | SOIL TZAXIAL HEAD 7 5 SOL1 | SOIL TZAXIAL HEAD 7 5 SOL1 | SOIL TZAXIAL HEAD 7 5 SOL1 |
| 22 | SOIL SLOCSM 5 0.00 17.88 0.0909 | SOIL SLOCSM 5 0.00 17.88 0.0909 | SOIL SLOCSM 5 0.00 17.88 0.0909 | SOIL SLOCSM 5 0.00 17.88 0.0909 | SOIL SLOCSM 5 0.00 17.88 0.0909 | SOIL SLOCSM 5 0.00 17.88 0.0909 | SOIL SLOCSM 5 0.00 17.88 0.0909 | SOIL SLOCSM 5 0.00 17.88 0.0909 |
| 23 | SOIL T-Z 0.00.00000.20200.1181 .4040.2362 .6730.3937 .6730.5906 | SOIL T-Z 0.00.00000.20200.1181 .4040.2362 .6730.3937 .6730.5906 | SOIL T-Z 0.00.00000.20200.1181 .4040.2362 .6730.3937 .6730.5906 | SOIL T-Z 0.00.00000.20200.1181 .4040.2362 .6730.3937 .6730.5906 | SOIL T-Z 0.00.00000.20200.1181 .4040.2362 .6730.3937 .6730.5906 | SOIL T-Z 0.00.00000.20200.1181 .4040.2362 .6730.3937 .6730.5906 | SOIL T-Z 0.00.00000.20200.1181 .4040.2362 .6730.3937 .6730.5906 | SOIL T-Z 0.00.00000.20200.1181 .4040.2362 .6730.3937 .6730.5906 |
| 24 | SOIL SLOCSM 5 17.88 36.25 0.0909 | SOIL SLOCSM 5 17.88 36.25 0.0909 | SOIL SLOCSM 5 17.88 36.25 0.0909 | SOIL SLOCSM 5 17.88 36.25 0.0909 | SOIL SLOCSM 5 17.88 36.25 0.0909 | SOIL SLOCSM 5 17.88 36.25 0.0909 | SOIL SLOCSM 5 17.88 36.25 0.0909 | SOIL SLOCSM 5 17.88 36.25 0.0909 |
| 25 | SOIL T-Z 0.00.00000.26800.1181 .5360.2362 .8940.3937 .8940.5906 | SOIL T-Z 0.00.00000.26800.1181 .5360.2362 .8940.3937 .8940.5906 | SOIL T-Z 0.00.00000.26800.1181 .5360.2362 .8940.3937 .8940.5906 | SOIL T-Z 0.00.00000.26800.1181 .5360.2362 .8940.3937 .8940.5906 | SOIL T-Z 0.00.00000.26800.1181 .5360.2362 .8940.3937 .8940.5906 | SOIL T-Z 0.00.00000.26800.1181 .5360.2362 .8940.3937 .8940.5906 | SOIL T-Z 0.00.00000.26800.1181 .5360.2362 .8940.3937 .8940.5906 | SOIL T-Z 0.00.00000.26800.1181 .5360.2362 .8940.3937 .8940.5906 |
| 26 | SOIL SLOCSM 5 36.25 54.13 0.0909 | SOIL SLOCSM 5 36.25 54.13 0.0909 | SOIL SLOCSM 5 36.25 54.13 0.0909 | SOIL SLOCSM 5 36.25 54.13 0.0909 | SOIL SLOCSM 5 36.25 54.13 0.0909 | SOIL SLOCSM 5 36.25 54.13 0.0909 | SOIL SLOCSM 5 36.25 54.13 0.0909 | SOIL SLOCSM 5 36.25 54.13 0.0909 |
| 27 | SOIL T-Z 0.00.00000.22500.1181 .4500.2362 .7500.3937 .7500.5906 | SOIL T-Z 0.00.00000.22500.1181 .4500.2362 .7500.3937 .7500.5906 | SOIL T-Z 0.00.00000.22500.1181 .4500.2362 .7500.3937 .7500.5906 | SOIL T-Z 0.00.00000.22500.1181 .4500.2362 .7500.3937 .7500.5906 | SOIL T-Z 0.00.00000.22500.1181 .4500.2362 .7500.3937 .7500.5906 | SOIL T-Z 0.00.00000.22500.1181 .4500.2362 .7500.3937 .7500.5906 | SOIL T-Z 0.00.00000.22500.1181 .4500.2362 .7500.3937 .7500.5906 | SOIL T-Z 0.00.00000.22500.1181 .4500.2362 .7500.3937 .7500.5906 |
| 28 | SOIL SLOCSM 5 54.13 59.71 0.0909 | SOIL SLOCSM 5 54.13 59.71 0.0909 | SOIL SLOCSM 5 54.13 59.71 0.0909 | SOIL SLOCSM 5 54.13 59.71 0.0909 | SOIL SLOCSM 5 54.13 59.71 0.0909 | SOIL SLOCSM 5 54.13 59.71 0.0909 | SOIL SLOCSM 5 54.13 59.71 0.0909 | SOIL SLOCSM 5 54.13 59.71 0.0909 |
| 29 | SOIL T-Z 0.00.00000.20200.1181 .4040.2362 .6730.3937 .6730.5906 | SOIL T-Z 0.00.00000.20200.1181 .4040.2362 .6730.3937 .6730.5906 | SOIL T-Z 0.00.00000.20200.1181 .4040.2362 .6730.3937 .6730.5906 | SOIL T-Z 0.00.00000.20200.1181 .4040.2362 .6730.3937 .6730.5906 | SOIL T-Z 0.00.00000.20200.1181 .4040.2362 .6730.3937 .6730.5906 | SOIL T-Z 0.00.00000.20200.1181 .4040.2362 .6730.3937 .6730.5906 | SOIL T-Z 0.00.00000.20200.1181 .4040.2362 .6730.3937 .6730.5906 | SOIL T-Z 0.00.00000.20200.1181 .4040.2362 .6730.3937 .6730.5906 |
| 30 | SOIL SLOCSM 5 59.71 72.01 0.0909 | SOIL SLOCSM 5 59.71 72.01 0.0909 | SOIL SLOCSM 5 59.71 72.01 0.0909 | SOIL SLOCSM 5 59.71 72.01 0.0909 | SOIL SLOCSM 5 59.71 72.01 0.0909 | SOIL SLOCSM 5 59.71 72.01 0.0909 | SOIL SLOCSM 5 59.71 72.01 0.0909 | SOIL SLOCSM 5 59.71 72.01 0.0909 |
| 31 | SOIL T-Z 0.00.00000.35900.1181 .7180.2362 1.1970.3937 1.1970.5906 | SOIL T-Z 0.00.00000.35900.1181 .7180.2362 1.1970.3937 1.1970.5906 | SOIL T-Z 0.00.00000.35900.1181 .7180.2362 1.1970.3937 1.1970.5906 | SOIL T-Z 0.00.00000.35900.1181 .7180.2362 1.1970.3937 1.1970.5906 | SOIL T-Z 0.00.00000.35900.1181 .7180.2362 1.1970.3937 1.1970.5906 | SOIL T-Z 0.00.00000.35900.1181 .7180.2362 1.1970.3937 1.1970.5906 | SOIL T-Z 0.00.00000.35900.1181 .7180.2362 1.1970.3937 1.1970.5906 | SOIL T-Z 0.00.00000.35900.1181 .7180.2362 1.1970.3937 1.1970.5906 |
| 32 | SOIL SLOCSM 5 72.01 73.49 0.0909 | SOIL SLOCSM 5 72.01 73.49 0.0909 | SOIL SLOCSM 5 72.01 73.49 0.0909 | SOIL SLOCSM 5 72.01 73.49 0.0909 | SOIL SLOCSM 5 72.01 73.49 0.0909 | SOIL SLOCSM 5 72.01 73.49 0.0909 | SOIL SLOCSM 5 72.01 73.49 0.0909 | SOIL SLOCSM 5 72.01 73.49 0.0909 |
| 33 | SOIL T-Z 0.00.00000.07200.1181 .1440.2362 .2390.3937 .2390.5906 | SOIL T-Z 0.00.00000.07200.1181 .1440.2362 .2390.3937 .2390.5906 | SOIL T-Z 0.00.00000.07200.1181 .1440.2362 .2390.3937 .2390.5906 | SOIL T-Z 0.00.00000.07200.1181 .1440.2362 .2390.3937 .2390.5906 | SOIL T-Z 0.00.00000.07200.1181 .1440.2362 .2390.3937 .2390.5906 | SOIL T-Z 0.00.00000.07200.1181 .1440.2362 .2390.3937 .2390.5906 | SOIL T-Z 0.00.00000.07200.1181 .1440.2362 .2390.3937 .2390.5906 | SOIL T-Z 0.00.00000.07200.1181 .1440.2362 .2390.3937 .2390.5906 |
| 34 | SOIL SLOCSM 5 73.49 160.0 0.0909 | SOIL SLOCSM 5 73.49 160.0 0.0909 | SOIL SLOCSM 5 73.49 160.0 0.0909 | SOIL SLOCSM 5 73.49 160.0 0.0909 | SOIL SLOCSM 5 73.49 160.0 0.0909 | SOIL SLOCSM 5 73.49 160.0 0.0909 | SOIL SLOCSM 5 73.49 160.0 0.0909 | SOIL SLOCSM 5 73.49 160.0 0.0909 |
| 35 | SOIL T-Z 0.00.00000.20200.1181 .4040.2362 .6730.3937 .6730.5906 | SOIL T-Z 0.00.00000.20200.1181 .4040.2362 .6730.3937 .6730.5906 | SOIL T-Z 0.00.00000.20200.1181 .4040.2362 .6730.3937 .6730.5906 | SOIL T-Z 0.00.00000.20200.1181 .4040.2362 .6730.3937 .6730.5906 | SOIL T-Z 0.00.00000.20200.1181 .4040.2362 .6730.3937 .6730.5906 | SOIL T-Z 0.00.00000.20200.1181 .4040.2362 .6730.3937 .6730.5906 | SOIL T-Z 0.00.00000.20200.1181 .4040.2362 .6730.3937 .6730.5906 | SOIL T-Z 0.00.00000.20200.1181 .4040.2362 .6730.3937 .6730.5906 |
| 36 | SOIL BEARING HEAD 1 2 SOL1 | SOIL BEARING HEAD 1 2 SOL1 | SOIL BEARING HEAD 1 2 SOL1 | SOIL BEARING HEAD 1 2 SOL1 | SOIL BEARING HEAD 1 2 SOL1 | SOIL BEARING HEAD 1 2 SOL1 | SOIL BEARING HEAD 1 2 SOL1 | SOIL BEARING HEAD 1 2 SOL1 |
| 37 | SOIL SLOCSM 2 0.00 160.0 .00015 | SOIL SLOCSM 2 0.00 160.0 .00015 | SOIL SLOCSM 2 0.00 160.0 .00015 | SOIL SLOCSM 2 0.00 160.0 .00015 | SOIL SLOCSM 2 0.00 160.0 .00015 | SOIL SLOCSM 2 0.00 160.0 .00015 | SOIL SLOCSM 2 0.00 160.0 .00015 | SOIL SLOCSM 2 0.00 160.0 .00015 |
| 38 | SOIL T-Z 0.00.0000 1.00 39.37 | SOIL T-Z 0.00.0000 1.00 39.37 | SOIL T-Z 0.00.0000 1.00 39.37 | SOIL T-Z 0.00.0000 1.00 39.37 | SOIL T-Z 0.00.0000 1.00 39.37 | SOIL T-Z 0.00.0000 1.00 39.37 | SOIL T-Z 0.00.0000 1.00 39.37 | SOIL T-Z 0.00.0000 1.00 39.37 |
| 39 | SOIL TORSION HEAD 1000.0SOL1 | SOIL TORSION HEAD 1000.0SOL1 | SOIL TORSION HEAD 1000.0SOL1 | SOIL TORSION HEAD 1000.0SOL1 | SOIL TORSION HEAD 1000.0SOL1 | SOIL TORSION HEAD 1000.0SOL1 | SOIL TORSION HEAD 1000.0SOL1 | SOIL TORSION HEAD 1000.0SOL1 |
| 40 | SOIL LATERAL HEAD 10 YEXP 20.0 SOL1 | SOIL LATERAL HEAD 10 YEXP 20.0 SOL1 | SOIL LATERAL HEAD 10 YEXP 20.0 SOL1 | SOIL LATERAL HEAD 10 YEXP 20.0 SOL1 | SOIL LATERAL HEAD 10 YEXP 20.0 SOL1 | SOIL LATERAL HEAD 10 YEXP 20.0 SOL1 | SOIL LATERAL HEAD 10 YEXP 20.0 SOL1 | SOIL LATERAL HEAD 10 YEXP 20.0 SOL1 |
| 41 | SOIL SLOCSM 4 0.0 .010 0.0 | SOIL SLOCSM 4 0.0 .010 0.0 | SOIL SLOCSM 4 0.0 .010 0.0 | SOIL SLOCSM 4 0.0 .010 0.0 | SOIL SLOCSM 4 0.0 .010 0.0 | SOIL SLOCSM 4 0.0 .010 0.0 | SOIL SLOCSM 4 0.0 .010 0.0 | SOIL SLOCSM 4 0.0 .010 0.0 |
| 42 | SOIL P-Y 0.00 0.00 0.82 0.134 1.02 0.201 1.02 0.240 | SOIL P-Y 0.00 0.00 0.82 0.134 1.02 0.201 1.02 0.240 | SOIL P-Y 0.00 0.00 0.82 0.134 1.02 0.201 1.02 0.240 | SOIL P-Y 0.00 0.00 0.82 0.134 1.02 0.201 1.02 0.240 | SOIL P-Y 0.00 0.00 0.82 0.134 1.02 0.201 1.02 0.240 | SOIL P-Y 0.00 0.00 0.82 0.134 1.02 0.201 1.02 0.240 | SOIL P-Y 0.00 0.00 0.82 0.134 1.02 0.201 1.02 0.240 | SOIL P-Y 0.00 0.00 0.82 0.134 1.02 0.201 1.02 0.240 |
| 43 | SOIL SLOCSM 5 18.04 .010 0.0 | SOIL SLOCSM 5 18.04 .010 0.0 | SOIL SLOCSM 5 18.04 .010 0.0 | SOIL SLOCSM 5 18.04 .010 0.0 | SOIL SLOCSM 5 18.04 .010 0.0 | SOIL SLOCSM 5 18.04 .010 0.0 | SOIL SLOCSM 5 18.04 .010 0.0 | SOIL SLOCSM 5 18.04 .010 0.0 |
| 44 | SOIL P-Y 0.00 0.00 1.76 0.331 2.26 0.496 2.54 0.594 2.54 0.709 | SOIL P-Y 0.00 0.00 1.76 0.331 2.26 0.496 2.54 0.594 2.54 0.709 | SOIL P-Y 0.00 0.00 1.76 0.331 2.26 0.496 2.54 0.594 2.54 0.709 | SOIL P-Y 0.00 0.00 1.76 0.331 2.26 0.496 2.54 0.594 2.54 0.709 | SOIL P-Y 0.00 0.00 1.76 0.331 2.26 0.496 2.54 0.594 2.54 0.709 | SOIL P-Y 0.00 0.00 1.76 0.331 2.26 0.496 2.54 0.594 2.54 0.709 | SOIL P-Y 0.00 0.00 1.76 0.331 2.26 0.496 2.54 0.594 2.54 0.709 | SOIL P-Y 0.00 0.00 1.76 0.331 2.26 0.496 2.54 0.594 2.54 0.709 |
| 45 | SOIL SLOCSM 6 30.42 .010 0.0 | SOIL SLOCSM 6 30.42 .010 0.0 | SOIL SLOCSM 6 30.42 .010 0.0 | SOIL SLOCSM 6 30.42 .010 0.0 | SOIL SLOCSM 6 30.42 .010 0.0 | SOIL SLOCSM 6 30.42 .010 0.0 | SOIL SLOCSM 6 30.42 .010 0.0 | SOIL SLOCSM 6 30.42 .010 0.0 |
| 46 | SOIL P-Y 0.00 0.00 16.76 0.331 17.0 0.496 17.33 0.594 17.57 0.709 | SOIL P-Y 0.00 0.00 16.76 0.331 17.0 0.496 17.33 0.594 17.57 0.709 | SOIL P-Y 0.00 0.00 16.76 0.331 17.0 0.496 17.33 0.594 17.57 0.709 | SOIL P-Y 0.00 0.00 16.76 0.331 17.0 0.496 17.33 0.594 17.57 0.709 | SOIL P-Y 0.00 0.00 16.76 0.331 17.0 0.496 17.33 0.594 17.57 0.709 | SOIL P-Y 0.00 0.00 16.76 0.331 17.0 0.496 17.33 0.594 17.57 0.709 | SOIL P-Y 0.00 0.00 16.76 0.331 17.0 0.496 17.33 0.594 17.57 0.709 | SOIL P-Y 0.00 0.00 16.76 0.331 17.0 0.496 17.33 0.594 17.57 0.709 |
| 47 | SOIL P-Y 17.57 2.16 | SOIL P-Y 17.57 2.16 | SOIL P-Y 17.57 2.16 | SOIL P-Y 17.57 2.16 | SOIL P-Y 17.57 2.16 | SOIL P-Y 17.57 2.16 | SOIL P-Y 17.57 2.16 | SOIL P-Y 17.57 2.16 |
| 48 | SOIL SLOCSM 6 36.42 .010 0.0 | SOIL SLOCSM 6 36.42 .010 0.0 | SOIL SLOCSM 6 36.42 .010 0.0 | SOIL SLOCSM 6 36.42 .010 0.0 | SOIL SLOCSM 6 36.42 .010 0.0 | SOIL SLOCSM 6 36.42 .010 0.0 | SOIL SLOCSM 6 36.42 .010 0.0 | SOIL SLOCSM 6 36.42 .010 0.0 |
| 49 | SOIL P-Y 0.00 0.00 12.57 0.331 12.57 0.496 12.57 0.594 12.57 0.709 | SOIL P-Y 0.00 0.00 12.57 0.331 12.57 0.496 12.57 0.594 12.57 0.709 | SOIL P-Y 0.00 0.00 12.57 0.331 12.57 0.496 12.57 0.594 12.57 0.709 | SOIL P-Y 0.00 0.00 12.57 0.331 12.57 0.496 12.57 0.594 12.57 0.709 | SOIL P-Y 0.00 0.00 12.57 0.331 12.57 0.496 12.57 0.594 12.57 0.709 | SOIL P-Y 0.00 0.00 12.57 0.331 12.57 0.496 12.57 0.594 12.57 0.709 | SOIL P-Y 0.00 0.00 12.57 0.331 12.57 0.496 12.57 0.594 12.57 0.709 | SOIL P-Y 0.00 0.00 12.57 0.331 12.57 0.496 12.57 0.594 12.57 0.709 |
| 50 | SOIL P-Y 12.67 2.16 | SOIL P-Y 12.67 2.16 | SOIL P-Y 12.67 2.16 | SOIL P-Y 12.67 2.16 | SOIL P-Y 12.67 2.16 | SOIL P-Y 12.67 2.16 | SOIL P-Y 12.67 2.16 | SOIL P-Y 12.67 2.16 |
| 51 | SOIL SLOCSM 6 54.13 .010 0.0 | SOIL SLOCSM 6 54.13 .010 0.0 | SOIL SLOCSM 6 54.13 .010 0.0 | SOIL SLOCSM 6 54.13 .010 0.0 | SOIL SLOCSM 6 54.13 .010 0.0 | SOIL SLOCSM 6 54.13 .010 0.0 | SOIL SLOCSM 6 54.13 .010 0.0 | SOIL SLOCSM 6 54.13 .010 0.0 |
| 52 | SOIL P-Y 0.00 0.00 12.57 0.331 12.57 0.496 18.41 0.594 18.76 0.709 | SOIL P-Y 0.00 0.00 12.57 0.331 12.57 0.496 18.41 0.594 18.76 0.709 | SOIL P-Y 0.00 0.00 12.57 0.331 12.57 0.496 18.41 0.594 18.76 0.709 | SOIL P-Y 0.00 0.00 12.57 0.331 12.57 0.496 18.41 0.594 18.76 0.709 | SOIL P-Y 0.00 0.00 12.57 0.331 12.57 0.496 18.41 0.594 18.76 0.709 | SOIL P-Y 0.00 0.00 12.57 0.331 12.57 0.496 18.41 0.594 18.76 0.709 | SOIL P-Y 0.00 0.00 12.57 0.331 12.57 0.496 18.41 0.594 18.76 0.709 | SOIL P-Y 0.00 0.00 12.57 0.331 12.57 0.496 18.41 0.594 18.76 0.709 |
| 53 | SOIL P-Y 18.92 2.16 | SOIL P-Y 18.92 2.16 | SOIL P-Y 18.92 2.16 | SOIL P-Y 18.92 2.16 | SOIL P-Y 18.92 2.16 | SOIL P-Y 18.92 2.16 | SOIL P-Y 18.92 2.16 | SOIL P-Y 18.92 2.16 |
| 54 | SOIL SLOCSM 6 54.13 .010 0.0 | SOIL SLOCSM 6 54.13 .010 0.0 | SOIL SLOCSM 6 54.13 .010 0.0 | SOIL SLOCSM 6 54.13 .010 0.0 | SOIL SLOCSM 6 54.13 .010 0.0 | SOIL SLOCSM 6 54.13 .010 0.0 | SOIL SLOCSM 6 54.13 .010 0.0 | SOIL SLOCSM 6 54.13 .010 0.0 |
| 55 | SOIL P-Y 0.00 0.00 10.27 0.323 10.27 0.484 18.38 0.583 18.76 0.709 | SOIL P-Y 0.00 0.00 10.27 0.323 10.27 0.484 18.38 0.583 18.76 0.709 | SOIL P-Y 0.00 0.00 10.27 0.323 10.27 0.484 18.38 0.583 18.76 0.709 | SOIL P-Y 0.00 0.00 10.27 0.323 10.27 0.484 18.38 0.583 18.76 0.709 | SOIL P-Y 0.00 0.00 10.27 0.323 10.27 0.484 18.38 0.583 18.76 0.709 | SOIL P-Y 0.00 0.00 10.27 0.323 10.27 0.484 18.38 0.583 18.76 0.709 | SOIL P-Y 0.00 0.00 10.27 0.323 10.27 0.484 18.38 0.583 18.76 0.709 | SOIL P-Y 0.00 0.00 10.27 0.323 10.27 0.484 18.38 0.583 18.76 0.709 |
| 56 | SOIL P-Y 18.92 2.16 | SOIL P-Y 18.92 2.16 | SOIL P-Y 18.92 2.16 | SOIL P-Y 18.92 2.16 | SOIL P-Y 18.92 2.16 | SOIL P-Y 18.92 2.16 | SOIL P-Y 18.92 2.16 | SOIL P-Y 18.92 2.16 |
| 57 | SOIL SLOCSM 5 59.71 .010 0.0 | SOIL SLOCSM 5 59.71 .010 0.0 | SOIL SLOCSM 5 59.71 .010 0.0 | SOIL SLOCSM 5 59.71 .010 0.0 | SOIL SLOCSM 5 59.71 .010 0.0 | SOIL SLOCSM 5 59.71 .010 0.0 | SOIL SLOCSM 5 59.71 .010 0.0 | SOIL SLOCSM 5 59.71 .010 0.0 |
| 58 | SOIL P-Y 0.00 0.00 10.27 0.323 20.26 0.583 20.70 0.709 20.86 2.16 | SOIL P-Y 0.00 0.00 10.27 0.323 20.26 0.583 20.70 0.709 20.86 2.16 | SOIL P-Y 0.00 0.00 10.27 0.323 20.26 0.583 20.70 0.709 20.86 2.16 | SOIL P-Y 0.00 0.00 10.27 0.323 20.26 0.583 20.70 0.709 20.86 2.16 | SOIL P-Y 0.00 0.00 10.27 0.323 20.26 0.583 20.70 0.709 20.86 2.16 | SOIL P-Y 0.00 0.00 10.27 0.323 20.26 0.583 20.70 0.709 20.86 2.16 | SOIL P-Y 0.00 0.00 10.27 0.323 20.26 0.583 20.70 0.709 20.86 2.16 | SOIL P-Y 0.00 0.00 10.27 0.323 20.26 0.583 20.70 0.709 20.86 2.16 |
| 59 | SOIL SLOCSM 4 72.18 .010 0.0 | SOIL SLOCSM 4 72.18 .010 0.0 | SOIL SLOCSM 4 72.18 .010 0.0 | SOIL SLOCSM 4 72.18 .010 0.0 | SOIL SLOCSM 4 72.18 .010 0.0 | SOIL SLOCSM 4 72.18 .010 0.0 | SOIL SLOCSM 4 72.18 .010 0.0 | SOIL SLOCSM 4 72.18 .010 0.0 |
| 60 | SOIL P-Y 0.00 0.00 25.15 0.331 25.15 0.496 25.16 0.594 | SOIL P-Y 0.00 0.00 25.15 0.331 25.15 0.496 25.16 0.594 | SOIL P-Y 0.00 0.00 25.15 0.331 25.15 0.496 25.16 0.594 | SOIL P-Y 0.00 0.00 25.15 0.331 25.15 0.496 25.16 0.594 | SOIL P-Y 0.00 0.00 25.15 0.331 25.15 0.496 25.16 0.594 | SOIL P-Y 0.00 0.00 25.15 0.331 25.15 0.496 25.16 0.594 | SOIL P-Y 0.00 0.00 25.15 0.331 25.15 0.496 25.16 0.594 | SOIL P-Y 0.00 0.00 25.15 0.331 25.15 0.496 25.16 0.594 |





| 61 | SOIL | SLOCSM 8 | 72.18 | .010 | 0.0 |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 62 | SOIL | P-Y 0.00 | 0.00 | 7.36 | 0.122 | 13.58 | 0.248 | 19.27 | 0.413 | 22.89 | 0.618 |
| 63 | SOIL | P-Y 24.38 | 2.09 | 24.96 | 2.62 | 25.16 | 3.14 |  |  |  |  |
| 64 | SOIL | SLOCSM 5 | 73.49 | 160. | .010 | 0.0 |  |  |  |  |  |
| 65 | SOIL | P-Y 0.00 | 0.00 | 10.27 | 0.673 | 10.27 | 1.012 | 25.68 | 1.213 | 28.56 | 1.3 |
| 66 | END |  |  |  |  |  |  |  |  |  |  |
| 67 |  |  |  |  |  |  |  |  |  |  |  |



Line 2. The PSIOPT line specifies English units (col. 10-12) and that a final pile analysis is to be executed with summarized output reports. 100 pile increments are to be used, with a force convergence tolerance of 0.5% and a pile material density of 490 lb/ft3.

Line 4. Load cases FSEX, FSEY, ESEX, and ESEY will be excluded from the pile capacity and load checks as those will be used for pile linearization.

Line 6. One pile superelement will be created using the average loads and deflections from load cases FSEX and FSEY for dynamic fatigue analyses.

Line 8. Another pile superelement will be created using the average loads and deflections from load cases ESEX and ESEY for dynamic seismic analyses.

Line 9. The PLTRQ line request that soil data, lateral deflection, axial deflection, lateral soil reaction and unity check plots be generated.

Lines 11-14. The PLGRUP lines designate pile group PL1 as a 36 inch diameter segmented member with a 1.0 inch wall and 50 ksi yield stress for the first 35 feet and a 0.625 inch wall and 36 ksi yield stress for the remaining 95 feet. An available end bearing area of 7.07 square feet is also specified. Pile group PL2 is identical to pile group PL1 in this example.

Lines 16-19. Pilehead joints 102, 104, 106 and 108 are assigned reference joints 202, 204, 206 and 208 respectively. All piles have member properties defined by group PL1 or PL2 and use soil properties defined by soil group SOL1.

Line 21. The SOIL TZAXIAL HEAD line indicates that seven soil layers will be defined by T-Z curves for soil group SOL1.

Line 22. The elevation of the soil layer, the number of points defining the curve for that layer and the factor to which multiply T by, are designated on the SOIL SLOC line.

Line 23. The T-Z curve for the soil layer specified, is defined by the points specified on the SOIL T-Z line.

Line 36. The SOIL BEARING HEAD line indicates that one soil stratum will be defined with a maximum of two points defined on the T-Z line.

Line 37. The elevation of the soil layer, the number of points defining the curve for that layer and the factor to which multiply T by, are designated on the SOIL SLOC line.

Line 38. The T-Z curve for the soil layer specified, is defined by the points specified on the SOIL T-Z line.

Line 39. A torsional spring with stiffness value of 1000.0 in-lb/radian for soil group SOL1 is designated on the SOIL TORSION HEAD line.

Line 40. The SOIL LATERAL HEAD line specifies that ten soil strata will be used to define the lateral load deflection relationship of the soil/pile system. The reference diameter is 20.0 inches.

Line 42. The P-Y curve for the soil layer at the elevation specified on the previous SLOC line, is defined by the points specified on the SOIL P-Y line.

The following are the PSI output plots and a portion of the listing file for Sample Problem 1.

LATERAL P-Y DATA

|SOIL ID SOL1 REF. OD 20.00 IN

AXIAL DEFLECTION   
![](SACS2024_PSI/chunk1_c004b0f0c543bdb874f112216dc7d5a5ae0059e11389d959453abb5275fb9e21.jpg)  
|PILE JOINT 102 LOAD CASE OPR1

![](SACS2024_PSI/chunk1_7651a615b667fa60eb8b1492fe82079750b688696e836ae015610c75194c57af.jpg)

![](SACS2024_PSI/chunk1_05d1a3c2cdc016d87bafa788c1da9f028aaa9fdf4d27a0e9a0a5f3a6a9a2c8f5.jpg)

![](SACS2024_PSI/chunk1_42b0f86527027021a8b3e2818e0769719c120fcf69e6ecc4dcc947546edbbf35.jpg)

![](SACS2024_PSI/chunk1_83b59c12dcea7c0067d9628ee8659006976d8364bcc81fc60cef1c0c683d1e30.jpg)  
PSI SAMPLE ANALYSIS

* * O P T I O N S * *

ANALYSIS

UNITS ENGLISH

VERTICAL COORDINATE . . +Z

CONVERGENCE

-DISPLACEMENT . . . . 0.00100 IN   
-ROTATION . . . . . . 0.00010 RAD   
-FORCE . . 0.50000 PERCENT

ITERATIONS 20 MAX

PILE INCREMENTS . . 100

PILE MATERIAL DENSITY 490.000 LB/FT3

EXECUTE

LINEAR STRUCTURE STIFFNESS REDUCTION

LINEAR STRUCTURE FORCE REDUCTION

PILEHEAD STIFFNESS TABLE GENERATION

PILE-TO-STRUCTURE FOUNDATION ANALYSIS

LINEAR STRUCTURE ANALYSIS

PILE ANALYSIS

SAVE

LINEAR STRUCTURE STIFFNESS REDUCTION

RECOVER

PRINT

PILE SUMMARY ONLY

CREATE 2 PILE SUPERELEMENT FILE(S) FOR DYNAMIC ANALYSIS

AMERICAN PETROLEUM INSTITUTE 21ST EDITION CODE SELECTED

* PLOT OPTIONS REQUESTED *

AXIAL DEFLECTION

LATERAL DISPLACEMENTS (Y AND Z)

LATERAL SOIL REACTIONS (Y AND Z)

UNITY CHECK RATIO

PLOTS SHOWN WITHOUT GRID LINES

PLOTS GENERATED FOR ALL PILES

PLOTS GENERATED FOR ALL LOAD CASES

SACS CONNECT Edition V(14.3) - CLPSI SAMPLE ANALYSIS

Company: Bentley Sytems DATE 02-SEP-2020 TIME 17:40:23 PSI PAGE 3

* * P I L E G R O U P D E S C R I P T I O N * *



| LABELS GROUP SECTION | TUBE O.D. | SECTION TW | MATERIAL PROPERTIES | MATERIAL PROPERTIES | MATERIAL PROPERTIES | SEGMENT LENGTH FT | SURFACE AS IN | DIMENSIONS BS IN | T FACTOR | BEARING AREA FT**2 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LABELS GROUP SECTION | IN | IN | E*10-3 KSI | G*10-3 KSI | FY KSI | SEGMENT LENGTH FT | SURFACE AS IN | DIMENSIONS BS IN | T FACTOR | BEARING AREA FT**2 |
| PL1 | 36.00 | 1.000 | 29.00 | 11.60 | 50.00 | 35.00 | 36.00 | 1.00 | 1.00 | 0.00 |
| PL1 | 36.00 | 0.625 | 29.00 | 11.60 | 36.00 | 95.00 | 36.00 | 0.62 | 1.00 | 7.07 |
| PL2 | 36.00 | 1.000 | 29.00 | 11.60 | 50.00 | 35.00 | 36.00 | 1.00 | 1.00 | 0.00 |
| PL2 | 36.00 | 0.625 | 29.00 | 11.60 | 36.00 | 95.00 | 36.00 | 0.62 | 1.00 | 7.07 |



SACS CONNECT Edition V(14.3) - CLPSI SAMPLE ANALYSIS

Company: Bentley Sytems DATE 02-SEP-2020 TIME 17:40:23 PSI PAGE 4



|  | * * PILE DESCRIPTION * * | * * PILE DESCRIPTION * * | * * PILE DESCRIPTION * * | * * PILE DESCRIPTION * * | * * PILE DESCRIPTION * * | * * PILE DESCRIPTION * * | * * PILE DESCRIPTION * * | * * PILE DESCRIPTION * * |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| * PILE JOINTS * GROUP * BATTER INCREMENTS * CHORD SOIL TABLES | * PILE JOINTS * GROUP * BATTER INCREMENTS * CHORD SOIL TABLES | * PILE JOINTS * GROUP * BATTER INCREMENTS * CHORD SOIL TABLES | * PILE JOINTS * GROUP * BATTER INCREMENTS * CHORD SOIL TABLES | * PILE JOINTS * GROUP * BATTER INCREMENTS * CHORD SOIL TABLES | * PILE JOINTS * GROUP * BATTER INCREMENTS * CHORD SOIL TABLES | * PILE JOINTS * GROUP * BATTER INCREMENTS * CHORD SOIL TABLES | * PILE JOINTS * GROUP * BATTER INCREMENTS * CHORD SOIL TABLES | * PILE JOINTS * GROUP * BATTER INCREMENTS * CHORD SOIL TABLES |
| HEAD | BATTER | LABEL | X | Y | Z | ANGLE | XYZ | XY |
|  |  |  | FT | FT | FT | DEG |  |  |
| 102 | 202 | PL1 |  |  |  | 0.00 | SOL1 |  |
| 104 | 204 | PL2 |  |  |  | 0.00 | SOL1 |  |
| 106 | 206 | PL1 |  |  |  | 0.00 | SOL1 |  |
| 108 | 208 | PL2 |  |  |  | 0.00 | SOL1 |  |



PSI SAMPLE ANALYSIS

DATE 02-SEP-2020 TIME 17:40:23 PSI PAGE

5

* * AXIAL SOIL STIFFNESS TABLE * *



| SOIL TABLE ID | SOIL TABLE ID | SOL1 |
| --- | --- | --- |
| NUMBER OF SOIL STRATA = | NUMBER OF SOIL STRATA = | 7 |
| NUMBER OF POINTS/CURVE = | NUMBER OF POINTS/CURVE = | 5 |





| STRATA | DESCRIPTION | APPLIED FACTOR | FROM DEPTH FT | TO DEPTH FT | T Z | T Z | T Z | T Z | T Z | T Z | T Z | T Z | T Z | T Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| STRATA | DESCRIPTION | APPLIED FACTOR | FROM DEPTH FT | TO DEPTH FT | KSI | IN | KSI | IN | KSI | IN | KSI | IN | KSI | IN |
| 1 |  | 0.90900E-01 | 0.00 | 17.88 | 0.0000 | 0.000 | 0.0184 | 0.118 | 0.0367 | 0.236 | 0.0612 | 0.394 | 0.0612 | 0.591 |
| 2 |  | 0.90900E-01 | 17.88 | 36.25 | 0.0000 | 0.000 | 0.0244 | 0.118 | 0.0487 | 0.236 | 0.0813 | 0.394 | 0.0813 | 0.591 |
| 3 |  | 0.90900E-01 | 36.25 | 54.13 | 0.0000 | 0.000 | 0.0205 | 0.118 | 0.0409 | 0.236 | 0.0682 | 0.394 | 0.0682 | 0.591 |
| 4 |  | 0.90900E-01 | 54.13 | 59.71 | 0.0000 | 0.000 | 0.0184 | 0.118 | 0.0367 | 0.236 | 0.0612 | 0.394 | 0.0612 | 0.591 |
| 5 |  | 0.90900E-01 | 59.71 | 72.01 | 0.0000 | 0.000 | 0.0326 | 0.118 | 0.0653 | 0.236 | 0.1088 | 0.394 | 0.1088 | 0.591 |
| 6 |  | 0.90900E-01 | 72.01 | 73.49 | 0.0000 | 0.000 | 0.0065 | 0.118 | 0.0131 | 0.236 | 0.0217 | 0.394 | 0.0217 | 0.591 |
| 7 |  | 0.90900E-01 | 73.49 | 160.00 | 0.0000 | 0.000 | 0.0184 | 0.118 | 0.0367 | 0.236 | 0.0612 | 0.394 | 0.0612 | 0.591 |



SACS CONNECT Edition V(14.3) - CLPSI SAMPLE ANALYSIS

Company: Bentley Sytems DATE 02-SEP-2020 TIME 17:40:23 PSI PAGE 6

* * TORSIONAL SOIL ADHESION TABLE * *



| SOIL TABLE ID | SOL1 |
| --- | --- |
| NUMBER OF SOIL STRATA = | 0 |
| LINEAR STIFFNESS VALUE = | 1000.00 INKP/RAD |



SACS CONNECT Edition V(14.3) - CLPSI SAMPLE ANALYSIS

Company: Bentley Sytems DATE 02-SEP-2020 TIME 17:40:23 PSI PAGE 7

* * END-BEARING SOIL STIFFNESS TABLE * *

SOIL TABLE ID SOL1



| NUMBER OF SOIL STRATA = 1 NUMBER OF POINTS/CURVE = 2 | NUMBER OF SOIL STRATA = 1 NUMBER OF POINTS/CURVE = 2 | NUMBER OF SOIL STRATA = 1 NUMBER OF POINTS/CURVE = 2 | NUMBER OF SOIL STRATA = 1 NUMBER OF POINTS/CURVE = 2 | NUMBER OF SOIL STRATA = 1 NUMBER OF POINTS/CURVE = 2 | NUMBER OF SOIL STRATA = 1 NUMBER OF POINTS/CURVE = 2 | NUMBER OF SOIL STRATA = 1 NUMBER OF POINTS/CURVE = 2 | NUMBER OF SOIL STRATA = 1 NUMBER OF POINTS/CURVE = 2 | NUMBER OF SOIL STRATA = 1 NUMBER OF POINTS/CURVE = 2 | NUMBER OF SOIL STRATA = 1 NUMBER OF POINTS/CURVE = 2 | NUMBER OF SOIL STRATA = 1 NUMBER OF POINTS/CURVE = 2 | NUMBER OF SOIL STRATA = 1 NUMBER OF POINTS/CURVE = 2 | NUMBER OF SOIL STRATA = 1 NUMBER OF POINTS/CURVE = 2 |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| STRATA DESCRIPTION | APPLIED FACTOR | FROM DEPTH FT | TO DEPTH FT | T KSI | Z IN | T KSI | Z IN | T KSI | Z IN | T KSI | Z IN | T KSI | Z IN |
| 1 | 0.15000E-03 | 0.00 | 160.00 | 0.0000 | 0.000 | 0.0001 | 39.370 |  |  |  |  |  |  |
| SACS CONNECT Edition V(14.3) - CL PSI SAMPLE ANALYSIS | SACS CONNECT Edition V(14.3) - CL PSI SAMPLE ANALYSIS | SACS CONNECT Edition V(14.3) - CL PSI SAMPLE ANALYSIS | SACS CONNECT Edition V(14.3) - CL PSI SAMPLE ANALYSIS | SACS CONNECT Edition V(14.3) - CL PSI SAMPLE ANALYSIS | SACS CONNECT Edition V(14.3) - CL PSI SAMPLE ANALYSIS | SACS CONNECT Edition V(14.3) - CL PSI SAMPLE ANALYSIS | SACS CONNECT Edition V(14.3) - CL PSI SAMPLE ANALYSIS | Company: Bentley Sytems DATE 02-SEP-2020 | TIME 17:40:23 | PSI | PAGE | 8 |  |
| * * LATERAL SOIL STIFFNESS TABLE * * | * * LATERAL SOIL STIFFNESS TABLE * * | * * LATERAL SOIL STIFFNESS TABLE * * | * * LATERAL SOIL STIFFNESS TABLE * * | * * LATERAL SOIL STIFFNESS TABLE * * | * * LATERAL SOIL STIFFNESS TABLE * * | * * LATERAL SOIL STIFFNESS TABLE * * | * * LATERAL SOIL STIFFNESS TABLE * * | * * LATERAL SOIL STIFFNESS TABLE * * | * * LATERAL SOIL STIFFNESS TABLE * * | * * LATERAL SOIL STIFFNESS TABLE * * | * * LATERAL SOIL STIFFNESS TABLE * * | * * LATERAL SOIL STIFFNESS TABLE * * | * * LATERAL SOIL STIFFNESS TABLE * * |
| SOIL TABLE ID NUMBER OF SOIL STRATA = SOL1 NUMBER OF POINTS/CURVE = 30 P-Y DATA DIAMETER = 20.000 IN | SOIL TABLE ID NUMBER OF SOIL STRATA = SOL1 NUMBER OF POINTS/CURVE = 30 P-Y DATA DIAMETER = 20.000 IN | SOIL TABLE ID NUMBER OF SOIL STRATA = SOL1 NUMBER OF POINTS/CURVE = 30 P-Y DATA DIAMETER = 20.000 IN | SOIL TABLE ID NUMBER OF SOIL STRATA = SOL1 NUMBER OF POINTS/CURVE = 30 P-Y DATA DIAMETER = 20.000 IN | SOIL TABLE ID NUMBER OF SOIL STRATA = SOL1 NUMBER OF POINTS/CURVE = 30 P-Y DATA DIAMETER = 20.000 IN | SOIL TABLE ID NUMBER OF SOIL STRATA = SOL1 NUMBER OF POINTS/CURVE = 30 P-Y DATA DIAMETER = 20.000 IN | SOIL TABLE ID NUMBER OF SOIL STRATA = SOL1 NUMBER OF POINTS/CURVE = 30 P-Y DATA DIAMETER = 20.000 IN | SOIL TABLE ID NUMBER OF SOIL STRATA = SOL1 NUMBER OF POINTS/CURVE = 30 P-Y DATA DIAMETER = 20.000 IN | SOIL TABLE ID NUMBER OF SOIL STRATA = SOL1 NUMBER OF POINTS/CURVE = 30 P-Y DATA DIAMETER = 20.000 IN | SOIL TABLE ID NUMBER OF SOIL STRATA = SOL1 NUMBER OF POINTS/CURVE = 30 P-Y DATA DIAMETER = 20.000 IN | SOIL TABLE ID NUMBER OF SOIL STRATA = SOL1 NUMBER OF POINTS/CURVE = 30 P-Y DATA DIAMETER = 20.000 IN | SOIL TABLE ID NUMBER OF SOIL STRATA = SOL1 NUMBER OF POINTS/CURVE = 30 P-Y DATA DIAMETER = 20.000 IN | SOIL TABLE ID NUMBER OF SOIL STRATA = SOL1 NUMBER OF POINTS/CURVE = 30 P-Y DATA DIAMETER = 20.000 IN | SOIL TABLE ID NUMBER OF SOIL STRATA = SOL1 NUMBER OF POINTS/CURVE = 30 P-Y DATA DIAMETER = 20.000 IN |
| STRATA DESCRIPTION | APPLIED FACTOR | FROM DEPTH FT | TO DEPTH FT | P K/IN | Y IN | P K/IN | Y IN | P K/IN | Y IN | P K/IN | Y IN | P K/IN | Y IN |
| 1 | 0.10000E-01 | 0.00 |  | 0.0000 | 0.000 | 0.0082 | 0.134 | 0.0102 | 0.201 | 0.0102 | 0.240 |  |  |
| 2 | 0.10000E-01 | 18.04 |  | 0.0000 | 0.000 | 0.0176 | 0.331 | 0.0226 | 0.496 | 0.0254 | 0.594 | 0.0254 | 0.709 |
| 3 | 0.10000E-01 | 30.42 |  | 0.0000 0.1757 | 0.000 2.160 | 0.1676 | 0.331 | 0.1700 | 0.496 | 0.1733 | 0.594 | 0.1757 | 0.709 |
| 4 | 0.10000E-01 | 36.42 |  | 0.0000 0.1267 | 0.000 2.160 | 0.1257 | 0.331 | 0.1257 | 0.496 | 0.1257 | 0.594 | 0.1257 | 0.709 |
| 5 | 0.10000E-01 | 54.12 |  | 0.0000 0.1892 | 0.000 2.160 | 0.1257 | 0.331 | 0.1257 | 0.496 | 0.1841 | 0.594 | 0.1876 | 0.709 |
| 6 | 0.10000E-01 | 54.13 |  | 0.0000 0.1892 | 0.000 2.160 | 0.1027 | 0.323 | 0.1027 | 0.484 | 0.1838 | 0.583 | 0.1876 | 0.709 |
| 7 | 0.10000E-01 | 59.71 |  | 0.0000 | 0.000 | 0.1027 | 0.323 | 0.2026 | 0.583 | 0.2070 | 0.709 | 0.2086 | 2.160 |
| 8 | 0.10000E-01 | 72.17 | 0.0000 | 0.000 | 0.2515 | 0.331 | 0.2515 | 0.496 | 0.2516 | 0.594 |  |  |  |
| 9 | 0.10000E-01 | 72.18 | 0.0000 | 0.000 | 0.0736 | 0.122 | 0.1358 | 0.248 | 0.1927 | 0.413 | 0.2289 | 0.618 |  |
|  |  |  | 0.2438 | 2.090 | 0.2496 | 2.620 | 0.2516 | 3.140 |  |  |  |  |  |
| 10 | 0.10000E-01 | 73.49 | 160.00 | 0.0000 | 0.000 | 0.1027 | 0.673 | 0.1027 | 1.012 | 0.2568 | 1.213 | 0.2856 | 1.300 |





| PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | DATE 02-SEP-2020 TIME 17:40:23 PSI PAGE 106 | DATE 02-SEP-2020 TIME 17:40:23 PSI PAGE 106 | DATE 02-SEP-2020 TIME 17:40:23 PSI PAGE 106 | DATE 02-SEP-2020 TIME 17:40:23 PSI PAGE 106 | DATE 02-SEP-2020 TIME 17:40:23 PSI PAGE 106 | DATE 02-SEP-2020 TIME 17:40:23 PSI PAGE 106 | DATE 02-SEP-2020 TIME 17:40:23 PSI PAGE 106 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS |
| * * * PILE MAXIMUM UNI TY CHECK SUMMARY * * * | * * * PILE MAXIMUM UNI TY CHECK SUMMARY * * * | * * * PILE MAXIMUM UNI TY CHECK SUMMARY * * * | * * * PILE MAXIMUM UNI TY CHECK SUMMARY * * * | * * * PILE MAXIMUM UNI TY CHECK SUMMARY * * * | * * * PILE MAXIMUM UNI TY CHECK SUMMARY * * * | * * * PILE MAXIMUM UNI TY CHECK SUMMARY * * * | * * * PILE MAXIMUM UNI TY CHECK SUMMARY * * * | * * * PILE MAXIMUM UNI TY CHECK SUMMARY * * * | * * * PILE MAXIMUM UNI TY CHECK SUMMARY * * * | * * * PILE MAXIMUM UNI TY CHECK SUMMARY * * * | * * * PILE MAXIMUM UNI TY CHECK SUMMARY * * * | * * * PILE MAXIMUM UNI TY CHECK SUMMARY * * * | * * * PILE MAXIMUM UNI TY CHECK SUMMARY * * * | * * * PILE MAXIMUM UNI TY CHECK SUMMARY * * * | * * * PILE MAXIMUM UNI TY CHECK SUMMARY * * * |
| PILE GRUP LOAD | AXIAL KIPS | PILEHEAD FORCES LATERAL KIPS | MOMENT IN-KIP | * PILEHEAD DISPLACEMENTS AXIAL IN | LATERAL IN | ROTATION RAD | DEPTH FT | AXIAL FBY KSI | STRESSES AT MAX. UNITY CHECK FBZ KSI | UNITY CHECK COMB. SHEAR | UNITY CHECK KSI | UNITED KINGDOM | UNITED KINGDOM | UNITED KINGDOM | UNITED KINGDOM |
| JT. | AXIAL KIPS | PILEHEAD FORCES LATERAL KIPS | MOMENT IN-KIP | * PILEHEAD DISPLACEMENTS AXIAL IN | LATERAL IN | ROTATION RAD | DEPTH FT | AXIAL FBY KSI | STRESSES AT MAX. UNITY CHECK FBZ KSI | UNITY CHECK COMB. SHEAR | UNITY CHECK KSI | UNITED KINGDOM | UNITED KINGDOM | UNITED KINGDOM | UNITED KINGDOM |
| 102 PL1 | OPR1 | -511.86 | 1.63 | 194.1 | 0.07 | 0.09 | 0.000240 | 0.0 | -4.66 | -0.12 | -0.17 | 0.03 | -4.86 | 0.161 |  |
|  | OPR2 | -485.44 | 11.68 | 1360.7 | 0.07 | 0.61 | 0.001298 | 35.1 | -2.24 | -2.33 | 0.06 | 0.07 | -4.57 | 0.194 |  |
|  | OPR3 | -555.44 | 23.64 | 3173.2 | 0.08 | 1.35 | 0.002763 | 35.1 | -2.56 | 5.14 | -0.04 | 0.15 | -7.70 | 0.318 |  |
|  | STM1 | 98.56 | 53.49 | 8828.6 | -0.01 | 4.46 | 0.007665 | 36.4 | 0.40 | -13.37 | -0.05 | 0.02 | 13.77 | 0.403 |  |
|  | STM2 | 184.82 | 43.11 | 6257.3 | -0.02 | 2.96 | 0.005559 | 35.1 | 0.82 | -10.30 | 0.05 | 0.13 | 11.12 | 0.328 |  |
|  | STM3 | -161.10 | 41.75 | 6393.5 | 0.02 | 2.85 | 0.005319 | 35.1 | -0.76 | -10.06 | 0.00 | 0.14 | -10.82 | 0.319 |  |
| 104 PL2 | OPR1 | -522.75 | 2.24 | 184.2 | 0.07 | 0.13 | 0.000350 | 0.0 | -4.75 | 0.12 | 0.16 | 0.04 | -4.95 | 0.164 |  |
|  | OPR2 | -418.30 | 11.40 | 1228.4 | 0.06 | 0.62 | 0.001347 | 35.1 | -1.94 | -2.34 | 0.01 | 0.07 | -4.28 | 0.181 |  |
|  | OPR3 | -293.37 | 23.52 | 2967.4 | 0.04 | 1.36 | 0.002816 | 35.1 | -1.37 | -5.13 | 0.01 | 0.15 | -6.49 | 0.262 |  |
|  | STM1 | -983.79 | 48.74 | 9088.1 | 0.13 | 4.37 | 0.007682 | 35.1 | -4.52 | -13.73 | 0.21 | 0.06 | -18.25 | 0.557 |  |
|  | STM2 | -516.11 | 41.74 | 6655.0 | 0.07 | 3.04 | 0.005692 | 35.1 | -2.38 | -10.67 | 0.06 | 0.13 | -13.05 | 0.394 |  |
|  | STM3 | 66.02 | 42.87 | 6444.9 | -0.01 | 2.94 | 0.005448 | 35.1 | 0.28 | -10.23 | 0.04 | 0.12 | 10.51 | 0.307 |  |
| 106 PL1 | OPR1 | -493.97 | 1.42 | 130.0 | 0.07 | 0.09 | 0.000254 | 0.0 | -4.49 | 0.05 | -0.13 | 0.03 | -4.63 | 0.154 |  |
|  | OPR2 | -598.53 | 10.07 | 1360.0 | 0.08 | 0.47 | 0.000901 | 0.0 | -5.44 | -1.44 | 0.21 | 0.19 | -6.90 | 0.221 |  |
|  | OPR3 | -722.70 | 22.37 | 3153.0 | 0.10 | 1.25 | 0.002504 | 35.1 | -3.32 | -4.76 | -0.05 | 0.13 | -8.08 | 0.338 |  |
|  | STM1 | 111.26 | 53.89 | 8943.7 | -0.01 | 4.50 | 0.007688 | 36.4 | 0.46 | 13.41 | -0.03 | 0.03 | 13.87 | 0.406 |  |
|  | STM2 | -352.84 | 41.60 | 6550.4 | 0.05 | 2.89 | 0.005389 | 35.1 | -1.63 | 10.21 | -0.02 | 0.14 | -11.85 | 0.354 |  |
|  | STM3 | -931.04 | 39.76 | 6789.8 | 0.13 | 2.77 | 0.005108 | 35.1 | -4.27 | 9.97 | 0.13 | 0.15 | -14.25 | 0.439 |  |
| 108 PL2 | OPR1 | -551.75 | 2.30 | 95.1 | 0.08 | 0.14 | 0.000372 | 0.0 | -5.02 | 0.10 | -0.02 | 0.04 | -5.12 | 0.170 |  |
|  | OPR2 | -577.22 | 10.30 | 1297.3 | 0.08 | 0.51 | 0.001052 | 0.0 | -5.25 | 1.35 | -0.30 | 0.20 | -6.64 | 0.213 |  |
|  | OPR3 | -506.55 | 23.08 | 3108.5 | 0.07 | 1.31 | 0.002675 | 35.1 | -2.34 | -4.97 | -0.04 | 0.14 | -7.31 | 0.301 |  |
|  | STM1 | -1012.73 | 48.75 | 9160.9 | 0.14 | 4.37 | 0.007657 | 35.1 | -4.65 | 13.72 | 0.20 | 0.07 | -18.38 | 0.561 |  |
|  | STM2 | -1099.88 | 38.31 | 6475.2 | 0.15 | 2.76 | 0.005229 | 35.1 | -5.05 | 10.03 | 0.01 | 0.17 | -15.08 | 0.468 |  |
|  | STM3 | -751.45 | 41.67 | 7088.7 | 0.10 | 2.98 | 0.005449 | 35.1 | -3.46 | -10.52 | -0.06 | 0.12 | -13.98 | 0.426 |  |



## 7.2 SINGLE PILE ANALYSIS

Sample Problem 2 is a single pile analysis used to determine the equivalent pile stub of the soil/pile foundation. In lieu of curves to define the soil load displacement relationships, general soil properties were input. Pile used this information to form the soil load displacement relationship per API-RP2A recommendations.

The following is the input file used for the equivalent pile stub analysis along with a description of the input lines:



|  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | 12345678901234567890123456789012345678901234567890123456789012345678901234567890 | 12345678901234567890123456789012345678901234567890123456789012345678901234567890 | 12345678901234567890123456789012345678901234567890123456789012345678901234567890 | 12345678901234567890123456789012345678901234567890123456789012345678901234567890 | 12345678901234567890123456789012345678901234567890123456789012345678901234567890 | 12345678901234567890123456789012345678901234567890123456789012345678901234567890 | 12345678901234567890123456789012345678901234567890123456789012345678901234567890 | 12345678901234567890123456789012345678901234567890123456789012345678901234567890 |
| 1 | PLOPT ENUC 100 |  |  | 490.0PTPT |  | S3 | S |  |
| 2 | PLTRQ SD |  |  |  |  |  |  |  |
| 3 | PLGRP |  |  |  |  |  |  |  |
| 4 | PLGRUP PL1 | 28.0 | 1.0 |  | 50.0 | 50.0 |  |  |
| 5 | PLGRP PL1 | 28.0 | 0.75 |  | 36.0 | 175.0 |  |  |
| 6 | PILE |  |  |  |  |  |  |  |
| 7 | PILE 2 | PL1 | 1.0 | 1.0 | 8.0 |  | SOL1 |  |
| 8 | SOIL |  |  |  |  |  |  |  |
| 9 | SOIL AXIAL | HEAD 8 |  | SOL1 |  |  |  |  |
| 10 | SOIL API AXL SLOC | 0.0 | 20.0 | SILT 1.0 | 110.0 |  |  |  |
| 11 | SOIL API AXL SLOC | 20.0 | 60.0 | SNSL 1.0 | 112.0 |  |  |  |
| 12 | SOIL API AXL SLOC | 60.0 |  | SLSN 1.0 | 115.0 |  |  |  |
| 13 | SOIL API AXL SLOC | 160.0 |  | SAND 0.9 | 130.0 |  |  |  |
| 14 | SOIL API AXL SLOC | 200.0 |  | CLOC 20.0 | 130.0 |  |  |  |
| 15 | SOIL API AXL SLOC | 228.0 |  | CLUC 40.0 | 130.0 |  |  |  |
| 16 | SOIL API AXL SLOC | 260.0 |  | CLAY 70.0 | 130.0 |  |  |  |
| 17 | SOIL API AXL SLOC | 300.0 | 400.0 | ROCK 100.0 | 200.0 | 130.0 |  |  |
| 18 | SOIL TORSION HEAD |  |  | 1000.SOL1 |  | N |  |  |
| 19 | SOIL LATERAL HEAD | 6 | 28.0 | SOL1 |  | NN | N |  |
| 20 | SOIL API LAT SLOC | SILTSA |  | 20.0 | 110. | 10.0 | 20.0 |  |
| 21 | SOIL API LAT SLOC | SNSLCA | 20.0 | 60.0 | 112. | 15.0 | 25.0 |  |
| 22 | SOIL API LAT SLOC | SLSNSA | 60.0 | 120.0 | 115. | 40.0 | 30.0 |  |
| 23 | SOIL API LAT SLOC | SANDSA | 120.0 | 140.0 | 130. | 80.0 | 35.0 |  |
| 24 | SOIL API LAT SLOC | SANDSA | 140.0 | 200.0 | 130. | 80.0 | 35.0 |  |
| 25 | SOIL API LAT SLOC | SANDSA | 200.0 | 400.0 | 130. | 100.0 | 35.0 |  |
| 26 | PLSTUB D10020 |  | 2.802 | 0.01306 | 625.4 |  |  |  |
| 27 | END |  |  |  |  |  |  |  |



Line 1. The PILOPT line specifies English units (col. 10-12) and that a pile code check is to be executed.   
Line 2. The PLTRQ line request that soil data plots be generated.

Lines 4-5. The PLGRUP lines designate pile group PL1 as a 28 inch diameter segmented member 1.5 inch wall and 50 ksi, for the first 50 feet and 0.75 inch wall 36 ksi for the remaining 175 feet.

Line 7. Pilehead joint 2 is assigned member properties defined by group PL1 and use soil properties defined by soil group SOL1 for the pile local X-Z and X-Y planes.   
Line 9. The SOIL AXIAL HEAD line indicates that the soil axial properties will be described for eight soil strata. The program will generate skin friction and bearing based on API-RP2A recommendations. These soil properties are assigned to soil group SOL1.   
Line 10. The elevation of each soil layer, the type of soil and the characteristics of the soil layer are specified on the SOIL API AXL SLOC line.   
Line 18. A torsional spring with stiffness value of 1000.0 in-kip/radian for soil group SOL1 is designated on the SOIL TORSION HEAD line.

Line 19. The SOIL LATERAL HEAD line specifies that six soil strata will be used to define the lateral load deflection relationship of the soil/pile system. The pile reference diameter is 28.0 inches.

Line 20. The SOIL API LAT SLOC lines specify the soil properties to be used to develop P-Y curves based on API-RP2A recommendations. The soil type, elevation and soil properties for each soil layer are specified.

Line 26. The PLSTUB input line designates the loads or deformations that are to be used to determine an equivalent pile stub. In this sample, the D in column 10 designates that pilehead displacements will be input. A reference joint name 1002 in columns 11 to 14 is designated and a lateral displacement of 2.2802 inches and a rotation of 0.01306 radians are specified. The corresponding axial load of 625.4 is also specified.

The following is the neutral picture file and a portion of the Pile output listing for Sample Problem 2.

![](SACS2024_PSI/chunk1_bd8cd9ec2b5eb348ad8b28559c6b031e5c515affce0fe6b799203ed35bbac42d.jpg)

![](SACS2024_PSI/chunk1_77aba6039e82130281c39e6f17abfbd1f0c510c2a9c1dcfd8639bc3ab3ee3cc1.jpg)



| * * PILE GROUP DESCRIPTI ON * * | * * PILE GROUP DESCRIPTI ON * * | * * PILE GROUP DESCRIPTI ON * * | * * PILE GROUP DESCRIPTI ON * * | * * PILE GROUP DESCRIPTI ON * * | * * PILE GROUP DESCRIPTI ON * * | * * PILE GROUP DESCRIPTI ON * * | * * PILE GROUP DESCRIPTI ON * * | * * PILE GROUP DESCRIPTI ON * * | * * PILE GROUP DESCRIPTI ON * * | * * PILE GROUP DESCRIPTI ON * * |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LABELSGROUP SECTION | TUBE SECTIONO.D.IN | SECTIONTWIN | MATERIAL PROPERTIESE*10-3KSI | G*10-3KSI | FYKSI | SEGMENTLENGTHFT | SURFACEASIN | DIMENSIONSBSIN | TFACTOR | BEARINGAREAFT**2 |
| PL1 | 28.00 | 1.000 | 29.00 | 11.60 | 50.00 | 50.00 | 28.00 | 1.00 | 1.00 | 0.00 |
| PL1 | 28.00 | 0.750 | 29.00 | 11.60 | 36.00 | 175.00 | 28.00 | 0.75 | 1.00 | 0.00 |
| SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | Company: Bentley SytemsDATE 03-SEP-2020 TIME 11:08:58PIL PAGE 3 | Company: Bentley SytemsDATE 03-SEP-2020 TIME 11:08:58PIL PAGE 3 | Company: Bentley SytemsDATE 03-SEP-2020 TIME 11:08:58PIL PAGE 3 | Company: Bentley SytemsDATE 03-SEP-2020 TIME 11:08:58PIL PAGE 3 |
| * * PILE DESCRIPTION * * | * * PILE DESCRIPTION * * | * * PILE DESCRIPTION * * | * * PILE DESCRIPTION * * | * * PILE DESCRIPTION * * | * * PILE DESCRIPTION * * | * * PILE DESCRIPTION * * | * * PILE DESCRIPTION * * | * * PILE DESCRIPTION * * | * * PILE DESCRIPTION * * | * * PILE DESCRIPTION * * |
| * PILE JOINTS *HEAD BATTER | GROUP LABEL | * * BATTERXFT | INCREMENTSEXFT | * YFT | * ZFT | CHORD ANGLEDEG | SOIL TABLESXZXYMUDLINEFT | HGT ABOVE |  |  |
| 2 | PL1 | 1.00 | 1.00 | 8.00 | 0.00 | SOL1 | 0.00 |  |  |  |
| SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | Company: Bentley SytemsDATE 03-SEP-2020 TIME 11:08:58PIL PAGE 4 | Company: Bentley SytemsDATE 03-SEP-2020 TIME 11:08:58PIL PAGE 4 | Company: Bentley SytemsDATE 03-SEP-2020 TIME 11:08:58PIL PAGE 4 | Company: Bentley SytemsDATE 03-SEP-2020 TIME 11:08:58PIL PAGE 4 |
| * AXIAL SOIL ADHESION TABLE * | * AXIAL SOIL ADHESION TABLE * | * AXIAL SOIL ADHESION TABLE * | * AXIAL SOIL ADHESION TABLE * | * AXIAL SOIL ADHESION TABLE * | * AXIAL SOIL ADHESION TABLE * | * AXIAL SOIL ADHESION TABLE * | * AXIAL SOIL ADHESION TABLE * | * AXIAL SOIL ADHESION TABLE * | * AXIAL SOIL ADHESION TABLE * | * AXIAL SOIL ADHESION TABLE * |
| SOIL TABLE IDNUMBER OF SOIL STRATA = UNIT BEARING CAPACITY = LINEAR STIFFNESS VALUE = | SOIL TABLE IDNUMBER OF SOIL STRATA = UNIT BEARING CAPACITY = LINEAR STIFFNESS VALUE = | SOIL TABLE IDNUMBER OF SOIL STRATA = UNIT BEARING CAPACITY = LINEAR STIFFNESS VALUE = | SOIL TABLE IDNUMBER OF SOIL STRATA = UNIT BEARING CAPACITY = LINEAR STIFFNESS VALUE = | SOIL TABLE IDNUMBER OF SOIL STRATA = UNIT BEARING CAPACITY = LINEAR STIFFNESS VALUE = | SOIL TABLE IDNUMBER OF SOIL STRATA = UNIT BEARING CAPACITY = LINEAR STIFFNESS VALUE = | SOIL TABLE IDNUMBER OF SOIL STRATA = UNIT BEARING CAPACITY = LINEAR STIFFNESS VALUE = | SOL18200.00 K/SF0.00 K/IN | SOL18200.00 K/SF0.00 K/IN | SOL18200.00 K/SF0.00 K/IN | SOL18200.00 K/SF0.00 K/IN |
| SOIL STRATALOCATIONSTENSION LOADSADHESIONINTERNALKSF | SOIL STRATALOCATIONSTENSION LOADSADHESIONINTERNALKSF | SOIL STRATALOCATIONSTENSION LOADSADHESIONINTERNALKSF | SOIL STRATALOCATIONSTENSION LOADSADHESIONINTERNALKSF | SOIL STRATALOCATIONSTENSION LOADSADHESIONINTERNALKSF | SOIL STRATALOCATIONSTENSION LOADSADHESIONINTERNALKSF | SOIL STRATALOCATIONSTENSION LOADSADHESIONINTERNALKSF | COMPRESSIONADHESIONEXTERNALKSF | COMPRESSIONADHESIONEXTERNALKSF | COMPRESSIONADHESIONEXTERNALKSF | COMPRESSIONADHESIONEXTERNALKSF |
| FT FROM | TO | FROM | TO | FROM | TO | FROM | TO | FROM | TO |  |
| 0.000 | 20.000 | 0.295 | 0.295 | 0.000 | 0.000 | 0.295 | 0.295 | 0.000 | 0.000 |  |
| 20.000 | 60.000 | 1.400 | 1.400 | 0.000 | 0.000 | 1.400 | 1.400 | 0.000 | 0.000 |  |
| 60.000 | 160.000 | 1.700 | 1.700 | 0.000 | 0.000 | 1.700 | 1.700 | 0.000 | 0.000 |  |
| 160.000 | 200.000 | 2.000 | 2.000 | 0.000 | 0.000 | 2.000 | 2.000 | 0.000 | 0.000 |  |
| 200.000 | 228.000 | 11.225 | 11.225 | 0.000 | 0.000 | 11.225 | 11.225 | 0.000 | 0.000 |  |
| 228.000 | 260.000 | 18.471 | 18.471 | 0.000 | 0.000 | 18.471 | 18.471 | 0.000 | 0.000 |  |
| 260.000 | 300.000 | 29.171 | 29.171 | 0.000 | 0.000 | 29.171 | 29.171 | 0.000 | 0.000 |  |
| 300.000 | 400.000 | 100.000 | 100.000 | 0.000 | 0.000 | 100.000 | 100.000 | 0.000 | 0.000 |  |



* * LATERAL SOIL STIFFNESS TABLE * *

```txt
SOIL TABLE ID SOL1  
NUMBER OF SOIL STRATA = 6  
NUMBER OF POINTS/CURVE = 30  
P-Y DATA DIAMETER = 28.000 IN 
```



| STRATA DESCRIPTION | APPLIED FACTOR | FROM DEPTHFT | TO DEPTHFT | P Y | P Y | P Y | P Y | P Y | P Y | P Y | P Y | P Y | P Y |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| STRATA DESCRIPTION | APPLIED FACTOR | FROM DEPTHFT | TO DEPTHFT | K/IN | IN | K/IN | IN | K/IN | IN | K/IN | IN | K/IN | IN |
| 1 | 1.0000 | 0.00 | 20.00 | 0.0000 | 0.000 | 0.0920 | 0.077 | 0.1822 | 0.154 | 0.2773 | 0.238 | 0.3663 | 0.323 |
| 1 | 1.0000 | 0.00 | 20.00 | 0.4619 | 0.423 | 0.5519 | 0.531 | 0.6473 | 0.669 | 0.7388 | 0.846 | 0.8302 | 1.131 |
| 1 | 1.0000 | 0.00 | 20.00 | 0.8766 | 1.407 | 0.9042 | 1.761 | 0.9137 | 2.038 | 0.9229 | 4.615 | 0.9229 | 5.537 |
| 2 | 1.0000 | 20.00 | 60.00 | 0.0000 | 0.000 | 1.1617 | 0.162 | 2.3005 | 0.324 | 3.5017 | 0.502 | 4.6263 | 0.680 |
| 2 | 1.0000 | 20.00 | 60.00 | 5.8337 | 0.890 | 6.9696 | 1.117 | 8.1747 | 1.408 | 9.3300 | 1.781 | 10.4848 | 2.380 |
| 2 | 1.0000 | 20.00 | 60.00 | 11.0705 | 2.962 | 11.4186 | 3.707 | 11.5395 | 4.290 | 11.6551 | 9.713 | 11.6551 | 11.655 |
| 3 | 1.0000 | 60.00 | 120.00 | 0.0000 | 0.000 | 4.9473 | 0.115 | 9.7973 | 0.230 | 14.9130 | 0.356 | 19.7028 | 0.483 |
| 3 | 1.0000 | 60.00 | 120.00 | 24.8447 | 0.632 | 29.6825 | 0.793 | 34.8147 | 1.000 | 39.7350 | 1.264 | 44.6531 | 1.689 |
| 3 | 1.0000 | 60.00 | 120.00 | 47.1473 | 2.103 | 48.6301 | 2.631 | 49.1447 | 3.045 | 49.6372 | 6.894 | 49.6372 | 8.273 |
| 4 | 1.0000 | 120.00 | 140.00 | 0.0000 | 0.000 | 14.0151 | 0.113 | 27.7545 | 0.225 | 42.2468 | 0.349 | 55.8155 | 0.473 |
| 4 | 1.0000 | 120.00 | 140.00 | 70.3820 | 0.620 | 84.0869 | 0.777 | 98.6256 | 0.980 | 112.5644 | 1.239 | 126.4965 | 1.656 |
| 4 | 1.0000 | 120.00 | 140.00 | 133.5624 | 2.062 | 137.7630 | 2.580 | 139.2209 | 2.986 | 140.6160 | 6.760 | 140.6160 | 8.113 |
| 5 | 1.0000 | 140.00 | 200.00 | 0.0000 | 0.000 | 18.9128 | 0.116 | 37.4536 | 0.233 | 57.0104 | 0.360 | 75.3209 | 0.488 |
| 5 | 1.0000 | 140.00 | 200.00 | 94.9779 | 0.640 | 113.4721 | 0.802 | 133.0916 | 1.012 | 151.9014 | 1.279 | 170.7023 | 1.709 |
| 5 | 1.0000 | 140.00 | 200.00 | 180.2374 | 2.128 | 185.9059 | 2.663 | 187.8734 | 3.081 | 189.7560 | 6.976 | 189.7560 | 8.372 |
| 6 | 1.0000 | 200.00 | 400.00 | 0.0000 | 0.000 | 34.8305 | 0.097 | 68.9758 | 0.194 | 104.9923 | 0.301 | 138.7134 | 0.408 |
| 6 | 1.0000 | 200.00 | 400.00 | 174.9144 | 0.534 | 208.9740 | 0.670 | 245.1059 | 0.845 | 279.7466 | 1.068 | 314.3711 | 1.427 |
| 6 | 1.0000 | 200.00 | 400.00 | 331.9313 | 1.776 | 342.3706 | 2.223 | 345.9939 | 2.572 | 349.4610 | 5.824 | 349.4610 | 6.989 |



SACS CONNECT Edition V(14.3) - CL

Company: Bentley Sytems

DATE 03-SEP-2020 TIME 11:08:58 PIL PAGE 7

PILE STUB DESIGN FOR PILE JOINT 2

INPUT PILEHEAD DEFLECTION .... 2.80200 IN

ROTATION .. 0.0130600 RAD

OUTPUT PILEHEAD FORCE .. 149.35 KIPS

MOMENT -4308.61 IN-KIP

AXIAL FORCE ... 625.400 KIPS

AXIAL DEFL ... 0.180 IN

STIFFNESS TERMS

AXIAL SPRING 3478.9 K/IN

TRANSLATIONAL SPRING 120.74 K/IN

ROTATIONAL SPRING 0.27745E+07 IN-KIP

ROT./TRANS COUPLING 12921. KIPS

TRANS/ROT COUPLING 16018. KIPS

STUB PROPERTIES

MEMBER LENGTH 321.576 IN

AXIAL OFFSET 40.950 IN

JOINT TO JOINT LENGTH 280.625 IN

MOMENT OF INERTIA ... 11538.04 IN**4

AXIAL AREA 38.58 IN**2

************************* SACS SAMPLE CARD IMAGES *************************

1 2 3 4 5 6 7 8

12345678901234567890123456789012345678901234567890123456789012345678901234567890

SECT PILSTUB PRI38.57711538.0 11538.0 11538.0 10.0 10.0

GRUP STB PILSTUB

MEMBER21002 2 STBSK

MEMBER OFFSETS 41.0

JOINT 2 0.0 0.0 0.0 0.0 0.0 0.0

JOINT 1002 -280.6 111111

1 2 3 4 5 6 7 8

12345678901234567890123456789012345678901234567890123456789012345678901234567890

## 7.3 MUDSLIDE ANALYSIS

Sample Problem 3 is the same as Sample Problem 1 except that a mudslide in the global X direction was is specified in the P-Y data. The mudslide was modeled by giving the first lateral stratum no stiffness.

The following is the PSI input file, followed by a description of the lines.



|  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | 1234567890123456789012345678901234567890123456789012345678901234567890 | 1234567890123456789012345678901234567890123456789012345678901234567890 | 1234567890123456789012345678901234567890123456789012345678901234567890 | 1234567890123456789012345678901234567890123456789012345678901234567890 | 1234567890123456789012345678901234567890123456789012345678901234567890 | 1234567890123456789012345678901234567890123456789012345678901234567890 | 1234567890123456789012345678901234567890123456789012345678901234567890 | 1234567890123456789012345678901234567890123456789012345678901234567890 |
| 1 | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS |
| 2 | PSIOPT +ZENG Y SM | PSIOPT +ZENG Y SM | PSIOPT +ZENG Y SM | PSIOPT +ZENG Y SM | PSIOPT +ZENG Y SM | S3 100 | 0.5 | 490. |
| 3 | LCSEL EX FSEX FSEY ESEX ESEY | LCSEL EX FSEX FSEY ESEX ESEY | LCSEL EX FSEX FSEY ESEX ESEY | LCSEL EX FSEX FSEY ESEX ESEY | LCSEL EX FSEX FSEY ESEX ESEY | LCSEL EX FSEX FSEY ESEX ESEY | LCSEL EX FSEX FSEY ESEX ESEY | LCSEL EX FSEX FSEY ESEX ESEY |
| 4 | PLTRQ SD DL LS DA UC | PLTRQ SD DL LS DA UC | PLTRQ SD DL LS DA UC | PLTRQ SD DL LS DA UC | PLTRQ SD DL LS DA UC | PLTRQ SD DL LS DA UC | PLTRQ SD DL LS DA UC | PLTRQ SD DL LS DA UC |
| 5 | PLGRP |  |  |  |  |  |  |  |
| 6 | PLGRP PL1 | 36.00 | 1.000 | 29.00 | 11.60 | 50.00 | 35.00 |  |
| 7 | PLGRP PL1 | 36.00 | 0.625 | 29.00 | 11.60 | 36.00 | 95.0 | 7.07 |
| 8 | PLGRP PL2 | 36.00 | 1.000 | 29.00 | 11.60 | 50.00 | 35.00 |  |
| 9 | PLGRP PL2 | 36.00 | 0.625 | 29.00 | 11.60 | 36.00 | 95.0 | 7.07 |
| 10 | PILE |  |  |  |  |  |  |  |
| 11 | PILE 102 202 PL1 |  |  |  |  | 180. | SOL1 | SOL2 |
| 12 | PILE 104 204 PL2 |  |  |  |  | 138.66 | SOL1 | SOL2 |
| 13 | PILE 106 206 PL1 |  |  |  |  | 0.0 | SOL1 | SOL2 |
| 14 | PILE 108 208 PL2 |  |  |  |  | 38.66 | SOL1 | SOL2 |
| 15 | SOIL |  |  |  |  |  |  |  |
| 16 | SOIL TZAXIAL HEAD 7 5 SOL1 | SOIL TZAXIAL HEAD 7 5 SOL1 | SOIL TZAXIAL HEAD 7 5 SOL1 | SOIL TZAXIAL HEAD 7 5 SOL1 | SOIL TZAXIAL HEAD 7 5 SOL1 | SOIL TZAXIAL HEAD 7 5 SOL1 | SOIL TZAXIAL HEAD 7 5 SOL1 | SOIL TZAXIAL HEAD 7 5 SOL1 |
| 17 | SOIL SLOCSM 5 0.00 17.88 0.0909 | SOIL SLOCSM 5 0.00 17.88 0.0909 | SOIL SLOCSM 5 0.00 17.88 0.0909 | SOIL SLOCSM 5 0.00 17.88 0.0909 | SOIL SLOCSM 5 0.00 17.88 0.0909 | SOIL SLOCSM 5 0.00 17.88 0.0909 | SOIL SLOCSM 5 0.00 17.88 0.0909 | SOIL SLOCSM 5 0.00 17.88 0.0909 |
| 18 | SOIL T-Z 0.00.00000.20200.1181 .4040.2362 .6730.3937 .6730.5906 | SOIL T-Z 0.00.00000.20200.1181 .4040.2362 .6730.3937 .6730.5906 | SOIL T-Z 0.00.00000.20200.1181 .4040.2362 .6730.3937 .6730.5906 | SOIL T-Z 0.00.00000.20200.1181 .4040.2362 .6730.3937 .6730.5906 | SOIL T-Z 0.00.00000.20200.1181 .4040.2362 .6730.3937 .6730.5906 | SOIL T-Z 0.00.00000.20200.1181 .4040.2362 .6730.3937 .6730.5906 | SOIL T-Z 0.00.00000.20200.1181 .4040.2362 .6730.3937 .6730.5906 | SOIL T-Z 0.00.00000.20200.1181 .4040.2362 .6730.3937 .6730.5906 |
| 19 | SOIL SLOCSM 5 17.88 36.25 0.0909 | SOIL SLOCSM 5 17.88 36.25 0.0909 | SOIL SLOCSM 5 17.88 36.25 0.0909 | SOIL SLOCSM 5 17.88 36.25 0.0909 | SOIL SLOCSM 5 17.88 36.25 0.0909 | SOIL SLOCSM 5 17.88 36.25 0.0909 | SOIL SLOCSM 5 17.88 36.25 0.0909 | SOIL SLOCSM 5 17.88 36.25 0.0909 |
| 20 | SOIL T-Z 0.00.00000.26800.1181 .5360.2362 .8940.3937 .8940.5906 | SOIL T-Z 0.00.00000.26800.1181 .5360.2362 .8940.3937 .8940.5906 | SOIL T-Z 0.00.00000.26800.1181 .5360.2362 .8940.3937 .8940.5906 | SOIL T-Z 0.00.00000.26800.1181 .5360.2362 .8940.3937 .8940.5906 | SOIL T-Z 0.00.00000.26800.1181 .5360.2362 .8940.3937 .8940.5906 | SOIL T-Z 0.00.00000.26800.1181 .5360.2362 .8940.3937 .8940.5906 | SOIL T-Z 0.00.00000.26800.1181 .5360.2362 .8940.3937 .8940.5906 | SOIL T-Z 0.00.00000.26800.1181 .5360.2362 .8940.3937 .8940.5906 |
| 21 | SOIL SLOCSM 5 36.25 54.13 0.0909 | SOIL SLOCSM 5 36.25 54.13 0.0909 | SOIL SLOCSM 5 36.25 54.13 0.0909 | SOIL SLOCSM 5 36.25 54.13 0.0909 | SOIL SLOCSM 5 36.25 54.13 0.0909 | SOIL SLOCSM 5 36.25 54.13 0.0909 | SOIL SLOCSM 5 36.25 54.13 0.0909 | SOIL SLOCSM 5 36.25 54.13 0.0909 |
| 22 | SOIL T-Z 0.00.00000.22500.1181 .4500.2362 .7500.3937 .7500.5906 | SOIL T-Z 0.00.00000.22500.1181 .4500.2362 .7500.3937 .7500.5906 | SOIL T-Z 0.00.00000.22500.1181 .4500.2362 .7500.3937 .7500.5906 | SOIL T-Z 0.00.00000.22500.1181 .4500.2362 .7500.3937 .7500.5906 | SOIL T-Z 0.00.00000.22500.1181 .4500.2362 .7500.3937 .7500.5906 | SOIL T-Z 0.00.00000.22500.1181 .4500.2362 .7500.3937 .7500.5906 | SOIL T-Z 0.00.00000.22500.1181 .4500.2362 .7500.3937 .7500.5906 | SOIL T-Z 0.00.00000.22500.1181 .4500.2362 .7500.3937 .7500.5906 |
| 23 | SOIL SLOCSM 5 54.13 59.71 0.0909 | SOIL SLOCSM 5 54.13 59.71 0.0909 | SOIL SLOCSM 5 54.13 59.71 0.0909 | SOIL SLOCSM 5 54.13 59.71 0.0909 | SOIL SLOCSM 5 54.13 59.71 0.0909 | SOIL SLOCSM 5 54.13 59.71 0.0909 | SOIL SLOCSM 5 54.13 59.71 0.0909 | SOIL SLOCSM 5 54.13 59.71 0.0909 |
| 24 | SOIL T-Z 0.00.00000.20200.1181 .4040.2362 .6730.3937 .6730.5906 | SOIL T-Z 0.00.00000.20200.1181 .4040.2362 .6730.3937 .6730.5906 | SOIL T-Z 0.00.00000.20200.1181 .4040.2362 .6730.3937 .6730.5906 | SOIL T-Z 0.00.00000.20200.1181 .4040.2362 .6730.3937 .6730.5906 | SOIL T-Z 0.00.00000.20200.1181 .4040.2362 .6730.3937 .6730.5906 | SOIL T-Z 0.00.00000.20200.1181 .4040.2362 .6730.3937 .6730.5906 | SOIL T-Z 0.00.00000.20200.1181 .4040.2362 .6730.3937 .6730.5906 | SOIL T-Z 0.00.00000.20200.1181 .4040.2362 .6730.3937 .6730.5906 |
| 25 | SOIL SLOCSM 5 59.71 72.01 0.0909 | SOIL SLOCSM 5 59.71 72.01 0.0909 | SOIL SLOCSM 5 59.71 72.01 0.0909 | SOIL SLOCSM 5 59.71 72.01 0.0909 | SOIL SLOCSM 5 59.71 72.01 0.0909 | SOIL SLOCSM 5 59.71 72.01 0.0909 | SOIL SLOCSM 5 59.71 72.01 0.0909 | SOIL SLOCSM 5 59.71 72.01 0.0909 |
| 26 | SOIL T-Z 0.00.00000.35900.1181 .7180.2362 1.1970.3937 1.1970.5906 | SOIL T-Z 0.00.00000.35900.1181 .7180.2362 1.1970.3937 1.1970.5906 | SOIL T-Z 0.00.00000.35900.1181 .7180.2362 1.1970.3937 1.1970.5906 | SOIL T-Z 0.00.00000.35900.1181 .7180.2362 1.1970.3937 1.1970.5906 | SOIL T-Z 0.00.00000.35900.1181 .7180.2362 1.1970.3937 1.1970.5906 | SOIL T-Z 0.00.00000.35900.1181 .7180.2362 1.1970.3937 1.1970.5906 | SOIL T-Z 0.00.00000.35900.1181 .7180.2362 1.1970.3937 1.1970.5906 | SOIL T-Z 0.00.00000.35900.1181 .7180.2362 1.1970.3937 1.1970.5906 |
| 27 | SOIL SLOCSM 5 72.01 73.49 0.0909 | SOIL SLOCSM 5 72.01 73.49 0.0909 | SOIL SLOCSM 5 72.01 73.49 0.0909 | SOIL SLOCSM 5 72.01 73.49 0.0909 | SOIL SLOCSM 5 72.01 73.49 0.0909 | SOIL SLOCSM 5 72.01 73.49 0.0909 | SOIL SLOCSM 5 72.01 73.49 0.0909 | SOIL SLOCSM 5 72.01 73.49 0.0909 |
| 28 | SOIL T-Z 0.00.00000.07200.1181 .1440.2362 .2390.3937 .2390.5906 | SOIL T-Z 0.00.00000.07200.1181 .1440.2362 .2390.3937 .2390.5906 | SOIL T-Z 0.00.00000.07200.1181 .1440.2362 .2390.3937 .2390.5906 | SOIL T-Z 0.00.00000.07200.1181 .1440.2362 .2390.3937 .2390.5906 | SOIL T-Z 0.00.00000.07200.1181 .1440.2362 .2390.3937 .2390.5906 | SOIL T-Z 0.00.00000.07200.1181 .1440.2362 .2390.3937 .2390.5906 | SOIL T-Z 0.00.00000.07200.1181 .1440.2362 .2390.3937 .2390.5906 | SOIL T-Z 0.00.00000.07200.1181 .1440.2362 .2390.3937 .2390.5906 |
| 29 | SOIL SLOCSM 5 73.49 160.0 0.0909 | SOIL SLOCSM 5 73.49 160.0 0.0909 | SOIL SLOCSM 5 73.49 160.0 0.0909 | SOIL SLOCSM 5 73.49 160.0 0.0909 | SOIL SLOCSM 5 73.49 160.0 0.0909 | SOIL SLOCSM 5 73.49 160.0 0.0909 | SOIL SLOCSM 5 73.49 160.0 0.0909 | SOIL SLOCSM 5 73.49 160.0 0.0909 |
| 30 | SOIL T-Z 0.00.00000.20200.1181 .4040.2362 .6730.3937 .6730.5906 | SOIL T-Z 0.00.00000.20200.1181 .4040.2362 .6730.3937 .6730.5906 | SOIL T-Z 0.00.00000.20200.1181 .4040.2362 .6730.3937 .6730.5906 | SOIL T-Z 0.00.00000.20200.1181 .4040.2362 .6730.3937 .6730.5906 | SOIL T-Z 0.00.00000.20200.1181 .4040.2362 .6730.3937 .6730.5906 | SOIL T-Z 0.00.00000.20200.1181 .4040.2362 .6730.3937 .6730.5906 | SOIL T-Z 0.00.00000.20200.1181 .4040.2362 .6730.3937 .6730.5906 | SOIL T-Z 0.00.00000.20200.1181 .4040.2362 .6730.3937 .6730.5906 |
| 31 | SOIL BEARING HEAD 1 2 SOL1 | SOIL BEARING HEAD 1 2 SOL1 | SOIL BEARING HEAD 1 2 SOL1 | SOIL BEARING HEAD 1 2 SOL1 | SOIL BEARING HEAD 1 2 SOL1 | SOIL BEARING HEAD 1 2 SOL1 | SOIL BEARING HEAD 1 2 SOL1 | SOIL BEARING HEAD 1 2 SOL1 |
| 32 | SOIL SLOCSM 2 0.00 160.0 .00015 | SOIL SLOCSM 2 0.00 160.0 .00015 | SOIL SLOCSM 2 0.00 160.0 .00015 | SOIL SLOCSM 2 0.00 160.0 .00015 | SOIL SLOCSM 2 0.00 160.0 .00015 | SOIL SLOCSM 2 0.00 160.0 .00015 | SOIL SLOCSM 2 0.00 160.0 .00015 | SOIL SLOCSM 2 0.00 160.0 .00015 |
| 33 | SOIL T-Z 0.00.0000 1.00 39.37 | SOIL T-Z 0.00.0000 1.00 39.37 | SOIL T-Z 0.00.0000 1.00 39.37 | SOIL T-Z 0.00.0000 1.00 39.37 | SOIL T-Z 0.00.0000 1.00 39.37 | SOIL T-Z 0.00.0000 1.00 39.37 | SOIL T-Z 0.00.0000 1.00 39.37 | SOIL T-Z 0.00.0000 1.00 39.37 |
| 34 | SOIL TORSION HEAD 1000.0 SOL1 | SOIL TORSION HEAD 1000.0 SOL1 | SOIL TORSION HEAD 1000.0 SOL1 | SOIL TORSION HEAD 1000.0 SOL1 | SOIL TORSION HEAD 1000.0 SOL1 | SOIL TORSION HEAD 1000.0 SOL1 | SOIL TORSION HEAD 1000.0 SOL1 | SOIL TORSION HEAD 1000.0 SOL1 |
| 35 | SOIL LATERAL HEAD 10 YEXP 20.0 SOL1 N | SOIL LATERAL HEAD 10 YEXP 20.0 SOL1 N | SOIL LATERAL HEAD 10 YEXP 20.0 SOL1 N | SOIL LATERAL HEAD 10 YEXP 20.0 SOL1 N | SOIL LATERAL HEAD 10 YEXP 20.0 SOL1 N | SOIL LATERAL HEAD 10 YEXP 20.0 SOL1 N | SOIL LATERAL HEAD 10 YEXP 20.0 SOL1 N | SOIL LATERAL HEAD 10 YEXP 20.0 SOL1 N |
| 36 | SOIL SLOCSM 4 0.0 .010 0.0 | SOIL SLOCSM 4 0.0 .010 0.0 | SOIL SLOCSM 4 0.0 .010 0.0 | SOIL SLOCSM 4 0.0 .010 0.0 | SOIL SLOCSM 4 0.0 .010 0.0 | SOIL SLOCSM 4 0.0 .010 0.0 | SOIL SLOCSM 4 0.0 .010 0.0 | SOIL SLOCSM 4 0.0 .010 0.0 |
| 37 | SOIL P-Y 0.00 0.00 0.82 0.134 1.02 0.201 1.02 0.240 | SOIL P-Y 0.00 0.00 0.82 0.134 1.02 0.201 1.02 0.240 | SOIL P-Y 0.00 0.00 0.82 0.134 1.02 0.201 1.02 0.240 | SOIL P-Y 0.00 0.00 0.82 0.134 1.02 0.201 1.02 0.240 | SOIL P-Y 0.00 0.00 0.82 0.134 1.02 0.201 1.02 0.240 | SOIL P-Y 0.00 0.00 0.82 0.134 1.02 0.201 1.02 0.240 | SOIL P-Y 0.00 0.00 0.82 0.134 1.02 0.201 1.02 0.240 | SOIL P-Y 0.00 0.00 0.82 0.134 1.02 0.201 1.02 0.240 |
| 38 | SOIL SLOCSM 5 18.04 .010 0.0 | SOIL SLOCSM 5 18.04 .010 0.0 | SOIL SLOCSM 5 18.04 .010 0.0 | SOIL SLOCSM 5 18.04 .010 0.0 | SOIL SLOCSM 5 18.04 .010 0.0 | SOIL SLOCSM 5 18.04 .010 0.0 | SOIL SLOCSM 5 18.04 .010 0.0 | SOIL SLOCSM 5 18.04 .010 0.0 |
| 39 | SOIL P-Y 0.00 0.00 1.76 0.331 2.26 0.496 2.54 0.594 2.54 0.709 | SOIL P-Y 0.00 0.00 1.76 0.331 2.26 0.496 2.54 0.594 2.54 0.709 | SOIL P-Y 0.00 0.00 1.76 0.331 2.26 0.496 2.54 0.594 2.54 0.709 | SOIL P-Y 0.00 0.00 1.76 0.331 2.26 0.496 2.54 0.594 2.54 0.709 | SOIL P-Y 0.00 0.00 1.76 0.331 2.26 0.496 2.54 0.594 2.54 0.709 | SOIL P-Y 0.00 0.00 1.76 0.331 2.26 0.496 2.54 0.594 2.54 0.709 | SOIL P-Y 0.00 0.00 1.76 0.331 2.26 0.496 2.54 0.594 2.54 0.709 | SOIL P-Y 0.00 0.00 1.76 0.331 2.26 0.496 2.54 0.594 2.54 0.709 |
| 40 | SOIL SLOCSM 6 30.42 .010 0.0 | SOIL SLOCSM 6 30.42 .010 0.0 | SOIL SLOCSM 6 30.42 .010 0.0 | SOIL SLOCSM 6 30.42 .010 0.0 | SOIL SLOCSM 6 30.42 .010 0.0 | SOIL SLOCSM 6 30.42 .010 0.0 | SOIL SLOCSM 6 30.42 .010 0.0 | SOIL SLOCSM 6 30.42 .010 0.0 |
| 41 | SOIL P-Y 0.00 0.00 16.76 0.331 17.0 0.496 17.33 0.594 17.57 0.709 | SOIL P-Y 0.00 0.00 16.76 0.331 17.0 0.496 17.33 0.594 17.57 0.709 | SOIL P-Y 0.00 0.00 16.76 0.331 17.0 0.496 17.33 0.594 17.57 0.709 | SOIL P-Y 0.00 0.00 16.76 0.331 17.0 0.496 17.33 0.594 17.57 0.709 | SOIL P-Y 0.00 0.00 16.76 0.331 17.0 0.496 17.33 0.594 17.57 0.709 | SOIL P-Y 0.00 0.00 16.76 0.331 17.0 0.496 17.33 0.594 17.57 0.709 | SOIL P-Y 0.00 0.00 16.76 0.331 17.0 0.496 17.33 0.594 17.57 0.709 | SOIL P-Y 0.00 0.00 16.76 0.331 17.0 0.496 17.33 0.594 17.57 0.709 |
| 42 | SOIL P-Y 17.57 2.16 | SOIL P-Y 17.57 2.16 | SOIL P-Y 17.57 2.16 | SOIL P-Y 17.57 2.16 | SOIL P-Y 17.57 2.16 | SOIL P-Y 17.57 2.16 | SOIL P-Y 17.57 2.16 | SOIL P-Y 17.57 2.16 |
| 43 | SOIL SLOCSM 6 36.42 .010 0.0 | SOIL SLOCSM 6 36.42 .010 0.0 | SOIL SLOCSM 6 36.42 .010 0.0 | SOIL SLOCSM 6 36.42 .010 0.0 | SOIL SLOCSM 6 36.42 .010 0.0 | SOIL SLOCSM 6 36.42 .010 0.0 | SOIL SLOCSM 6 36.42 .010 0.0 | SOIL SLOCSM 6 36.42 .010 0.0 |
| 44 | SOIL P-Y 0.00 0.00 12.57 0.331 12.57 0.496 12.57 0.594 12.57 0.709 | SOIL P-Y 0.00 0.00 12.57 0.331 12.57 0.496 12.57 0.594 12.57 0.709 | SOIL P-Y 0.00 0.00 12.57 0.331 12.57 0.496 12.57 0.594 12.57 0.709 | SOIL P-Y 0.00 0.00 12.57 0.331 12.57 0.496 12.57 0.594 12.57 0.709 | SOIL P-Y 0.00 0.00 12.57 0.331 12.57 0.496 12.57 0.594 12.57 0.709 | SOIL P-Y 0.00 0.00 12.57 0.331 12.57 0.496 12.57 0.594 12.57 0.709 | SOIL P-Y 0.00 0.00 12.57 0.331 12.57 0.496 12.57 0.594 12.57 0.709 | SOIL P-Y 0.00 0.00 12.57 0.331 12.57 0.496 12.57 0.594 12.57 0.709 |
| 45 | SOIL P-Y 12.67 2.16 | SOIL P-Y 12.67 2.16 | SOIL P-Y 12.67 2.16 | SOIL P-Y 12.67 2.16 | SOIL P-Y 12.67 2.16 | SOIL P-Y 12.67 2.16 | SOIL P-Y 12.67 2.16 | SOIL P-Y 12.67 2.16 |
| 46 | SOIL SLOCSM 6 54.13 .010 0.0 | SOIL SLOCSM 6 54.13 .010 0.0 | SOIL SLOCSM 6 54.13 .010 0.0 | SOIL SLOCSM 6 54.13 .010 0.0 | SOIL SLOCSM 6 54.13 .010 0.0 | SOIL SLOCSM 6 54.13 .010 0.0 | SOIL SLOCSM 6 54.13 .010 0.0 | SOIL SLOCSM 6 54.13 .010 0.0 |
| 47 | SOIL P-Y 0.00 0.00 12.57 0.331 12.57 0.496 18.41 0.594 18.76 0.709 | SOIL P-Y 0.00 0.00 12.57 0.331 12.57 0.496 18.41 0.594 18.76 0.709 | SOIL P-Y 0.00 0.00 12.57 0.331 12.57 0.496 18.41 0.594 18.76 0.709 | SOIL P-Y 0.00 0.00 12.57 0.331 12.57 0.496 18.41 0.594 18.76 0.709 | SOIL P-Y 0.00 0.00 12.57 0.331 12.57 0.496 18.41 0.594 18.76 0.709 | SOIL P-Y 0.00 0.00 12.57 0.331 12.57 0.496 18.41 0.594 18.76 0.709 | SOIL P-Y 0.00 0.00 12.57 0.331 12.57 0.496 18.41 0.594 18.76 0.709 | SOIL P-Y 0.00 0.00 12.57 0.331 12.57 0.496 18.41 0.594 18.76 0.709 |
| 48 | SOIL P-Y 18.92 2.16 | SOIL P-Y 18.92 2.16 | SOIL P-Y 18.92 2.16 | SOIL P-Y 18.92 2.16 | SOIL P-Y 18.92 2.16 | SOIL P-Y 18.92 2.16 | SOIL P-Y 18.92 2.16 | SOIL P-Y 18.92 2.16 |
| 49 | SOIL SLOCSM 6 54.13 .010 0.0 | SOIL SLOCSM 6 54.13 .010 0.0 | SOIL SLOCSM 6 54.13 .010 0.0 | SOIL SLOCSM 6 54.13 .010 0.0 | SOIL SLOCSM 6 54.13 .010 0.0 | SOIL SLOCSM 6 54.13 .010 0.0 | SOIL SLOCSM 6 54.13 .010 0.0 | SOIL SLOCSM 6 54.13 .010 0.0 |
| 50 | SOIL P-Y 0.00 0.00 10.27 0.323 10.27 0.484 18.38 0.583 18.76 0.709 | SOIL P-Y 0.00 0.00 10.27 0.323 10.27 0.484 18.38 0.583 18.76 0.709 | SOIL P-Y 0.00 0.00 10.27 0.323 10.27 0.484 18.38 0.583 18.76 0.709 | SOIL P-Y 0.00 0.00 10.27 0.323 10.27 0.484 18.38 0.583 18.76 0.709 | SOIL P-Y 0.00 0.00 10.27 0.323 10.27 0.484 18.38 0.583 18.76 0.709 | SOIL P-Y 0.00 0.00 10.27 0.323 10.27 0.484 18.38 0.583 18.76 0.709 | SOIL P-Y 0.00 0.00 10.27 0.323 10.27 0.484 18.38 0.583 18.76 0.709 | SOIL P-Y 0.00 0.00 10.27 0.323 10.27 0.484 18.38 0.583 18.76 0.709 |
| 51 | SOIL P-Y 18.92 2.16 | SOIL P-Y 18.92 2.16 | SOIL P-Y 18.92 2.16 | SOIL P-Y 18.92 2.16 | SOIL P-Y 18.92 2.16 | SOIL P-Y 18.92 2.16 | SOIL P-Y 18.92 2.16 | SOIL P-Y 18.92 2.16 |
| 52 | SOIL SLOCSM 5 59.71 .010 0.0 | SOIL SLOCSM 5 59.71 .010 0.0 | SOIL SLOCSM 5 59.71 .010 0.0 | SOIL SLOCSM 5 59.71 .010 0.0 | SOIL SLOCSM 5 59.71 .010 0.0 | SOIL SLOCSM 5 59.71 .010 0.0 | SOIL SLOCSM 5 59.71 .010 0.0 | SOIL SLOCSM 5 59.71 .010 0.0 |
| 53 | SOIL P-Y 0.00 0.00 10.27 0.323 20.26 0.583 20.70 0.709 20.86 2.16 | SOIL P-Y 0.00 0.00 10.27 0.323 20.26 0.583 20.70 0.709 20.86 2.16 | SOIL P-Y 0.00 0.00 10.27 0.323 20.26 0.583 20.70 0.709 20.86 2.16 | SOIL P-Y 0.00 0.00 10.27 0.323 20.26 0.583 20.70 0.709 20.86 2.16 | SOIL P-Y 0.00 0.00 10.27 0.323 20.26 0.583 20.70 0.709 20.86 2.16 | SOIL P-Y 0.00 0.00 10.27 0.323 20.26 0.583 20.70 0.709 20.86 2.16 | SOIL P-Y 0.00 0.00 10.27 0.323 20.26 0.583 20.70 0.709 20.86 2.16 | SOIL P-Y 0.00 0.00 10.27 0.323 20.26 0.583 20.70 0.709 20.86 2.16 |
| 54 | SOIL SLOCSM 4 72.18 .010 0.0 | SOIL SLOCSM 4 72.18 .010 0.0 | SOIL SLOCSM 4 72.18 .010 0.0 | SOIL SLOCSM 4 72.18 .010 0.0 | SOIL SLOCSM 4 72.18 .010 0.0 | SOIL SLOCSM 4 72.18 .010 0.0 | SOIL SLOCSM 4 72.18 .010 0.0 | SOIL SLOCSM 4 72.18 .010 0.0 |
| 55 | SOIL P-Y 0.00 0.00 25.15 0.331 25.15 0.496 25.16 0.594 | SOIL P-Y 0.00 0.00 25.15 0.331 25.15 0.496 25.16 0.594 | SOIL P-Y 0.00 0.00 25.15 0.331 25.15 0.496 25.16 0.594 | SOIL P-Y 0.00 0.00 25.15 0.331 25.15 0.496 25.16 0.594 | SOIL P-Y 0.00 0.00 25.15 0.331 25.15 0.496 25.16 0.594 | SOIL P-Y 0.00 0.00 25.15 0.331 25.15 0.496 25.16 0.594 | SOIL P-Y 0.00 0.00 25.15 0.331 25.15 0.496 25.16 0.594 | SOIL P-Y 0.00 0.00 25.15 0.331 25.15 0.496 25.16 0.594 |
| 56 | SOIL SLOCSM 8 72.18 .010 0.0 | SOIL SLOCSM 8 72.18 .010 0.0 | SOIL SLOCSM 8 72.18 .010 0.0 | SOIL SLOCSM 8 72.18 .010 0.0 | SOIL SLOCSM 8 72.18 .010 0.0 | SOIL SLOCSM 8 72.18 .010 0.0 | SOIL SLOCSM 8 72.18 .010 0.0 | SOIL SLOCSM 8 72.18 .010 0.0 |
| 57 | SOIL P-Y 0.00 0.00 7.36 0.122 13.58 0.248 19.27 0.413 22.89 0.618 | SOIL P-Y 0.00 0.00 7.36 0.122 13.58 0.248 19.27 0.413 22.89 0.618 | SOIL P-Y 0.00 0.00 7.36 0.122 13.58 0.248 19.27 0.413 22.89 0.618 | SOIL P-Y 0.00 0.00 7.36 0.122 13.58 0.248 19.27 0.413 22.89 0.618 | SOIL P-Y 0.00 0.00 7.36 0.122 13.58 0.248 19.27 0.413 22.89 0.618 | SOIL P-Y 0.00 0.00 7.36 0.122 13.58 0.248 19.27 0.413 22.89 0.618 | SOIL P-Y 0.00 0.00 7.36 0.122 13.58 0.248 19.27 0.413 22.89 0.618 | SOIL P-Y 0.00 0.00 7.36 0.122 13.58 0.248 19.27 0.413 22.89 0.618 |
| 58 | SOIL P-Y 24.38 2.09 24.96 2.62 25.16 3.14 | SOIL P-Y 24.38 2.09 24.96 2.62 25.16 3.14 | SOIL P-Y 24.38 2.09 24.96 2.62 25.16 3.14 | SOIL P-Y 24.38 2.09 24.96 2.62 25.16 3.14 | SOIL P-Y 24.38 2.09 24.96 2.62 25.16 3.14 | SOIL P-Y 24.38 2.09 24.96 2.62 25.16 3.14 | SOIL P-Y 24.38 2.09 24.96 2.62 25.16 3.14 | SOIL P-Y 24.38 2.09 24.96 2.62 25.16 3.14 |
| 59 | SOIL SLOCSM 5 73.49 160 .010 0.0 | SOIL SLOCSM 5 73.49 160 .010 0.0 | SOIL SLOCSM 5 73.49 160 .010 0.0 | SOIL SLOCSM 5 73.49 160 .010 0.0 | SOIL SLOCSM 5 73.49 160 .010 0.0 | SOIL SLOCSM 5 73.49 160 .010 0.0 | SOIL SLOCSM 5 73.49 160 .010 0.0 | SOIL SLOCSM 5 73.49 160 .010 0.0 |



```csv
60 SOIL P-Y 0.00 0.00 10.27 0.673 10.27 1.012 25.68 1.213 28.56 1.3  
61 SOIL TZAXIAL HEAD 7 5 SOL2  
62 SOIL SLOCSM 5 0.00 17.88 0.0909  
63 SOIL T-Z 0.00.00000.20200.1181 .4040.2362 .6730.3937 .6730.5906  
64 SOIL SLOCSM 5 17.88 36.25 0.0909  
65 SOIL T-Z 0.00.00000.26800.1181 .5360.2362 .8940.3937 .8940.5906  
66 SOIL SLOCSM 5 36.25 54.13 0.0909  
67 SOIL T-Z 0.00.00000.22500.1181 .4500.2362 .7500.3937 .7500.5906  
68 SOIL SLOCSM 5 54.13 59.71 0.0909  
69 SOIL T-Z 0.00.00000.20200.1181 .4040.2362 .6730.3937 .6730.5906  
70 SOIL SLOCSM 5 59.71 72.01 0.0909  
71 SOIL T-Z 0.00.00000.35900.1181 .7180.2362 1.1970.3937 1.1970.5906  
72 SOIL SLOCSM 5 72.01 73.49 0.0909  
73 SOIL T-Z 0.00.00000.07200.1181 .1440.2362 .2390.3937 .2390.5906  
74 SOIL SLOCSM 5 73.49 160.0 0.0909  
75 SOIL T-Z 0.00.00000.20200.1181 .4040.2362 .6730.3937 .6730.5906  
76 SOIL BEARING HEAD 1 2 SOL2  
77 SOIL SLOCSM 2 0.00 160.0 .00015  
78 SOIL T-Z 0.00.0000 1.00 39.37  
79 SOIL TORSION HEAD 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
```

Line 2. The PSIOPT line specifies English units (col. 10-12) and that a final pile analysis is to be executed with summarized output reports. The weight of the pile is to be included, and calculated using a density of 490 lbs/cu.ft.

Lines 11-14. Pilehead joints 102, 104, 106 and 108 are assigned reference joints 202, 204, 206 and 208 respectively. All piles have member properties defined by group PL1 or PL2 and use soil properties in the local pile coordinate system X-Z and X-Y planes defined by soil groups SOL1 and SOL2 respectively. Also, pile chord angles of 180, 138.66, 0 and 38.66 degrees for pilehead joints 102, 104, 106, and 108 respectively, have been assigned to align the pile X-Y plane with the global X-Z plane.

Line 61. The second SOIL TZAXIAL HEAD line indicates that two soil layers will be defined by T-Z curves for soil group SOL2. The procedure for T-Z curves for SOL2 is the same used for SOL1.

Line 80. The SOIL LATERAL HEAD line specifies that nine soil strata, will be used to define the mudslide lateral load deflection relationship of the soil/pile system. The reference diameter is 28.0 inches.

Line 82. The P-Y curve for the top soil layer is entered without the SM option to indicate that the curve is not symmetrical. Multiple Y values are entered with the same P value so that this layer does not have any stiffness.

The following are three of the plot files created in Sample Problem 3. A portion of the PSI listing file follows on the subsequent pages.

![](SACS2024_PSI/chunk1_2f7f44cce0d2eddbb0a40058f14c84a44c870a9c03a054efbb23452de0d3f0cc.jpg)

LATERAL P-Y DATA

SOIL ID SOL2

REF. OD 20.00 IM

![](SACS2024_PSI/chunk1_48aa66f2432607785510c81b04def82849907d6b1b8c3adb360f64f7731f2562.jpg)  
LATERAL DISPLACEMENTS (Y AND Z)

|PILE JOINT 102

LOAD CASE OPR1

![](SACS2024_PSI/chunk1_e6c591f19e39aa0485a4725795276408067930ab116a91a0b194e5b4c09adbde.jpg)



| PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| * * PILE GROUP DESCRIPTION | * * PILE GROUP DESCRIPTION | * * PILE GROUP DESCRIPTION | * * PILE GROUP DESCRIPTION | * * PILE GROUP DESCRIPTION | * * PILE GROUP DESCRIPTION | * * PILE GROUP DESCRIPTION | * * PILE GROUP DESCRIPTION | * * PILE GROUP DESCRIPTION | * * PILE GROUP DESCRIPTION | * * PILE GROUP DESCRIPTION | * * PILE GROUP DESCRIPTION | * * PILE GROUP DESCRIPTION | * * PILE GROUP DESCRIPTION | * * PILE GROUP DESCRIPTION | * * PILE GROUP DESCRIPTION | * * PILE GROUP DESCRIPTION |
| LABELS | LABELS | TUBE SECTION | TUBE SECTION | MATERIAL PROPERTIES | MATERIAL PROPERTIES | MATERIAL PROPERTIES | MATERIAL PROPERTIES | SEGMENT LENGTH | SEGMENT LENGTH | SURFACE AS BS | SURFACE AS BS | DIMENSIONS T FACTOR | DIMENSIONS T FACTOR | BEARING AREA FT**2 | BEARING AREA FT**2 |  |
| GROUP | SECTION | O.D. | TW | E*10-3 | G*10-3 | FY KSI | KSI | SEGMENT LENGTH | SEGMENT LENGTH | SURFACE AS BS | SURFACE AS BS | DIMENSIONS T FACTOR | DIMENSIONS T FACTOR | BEARING AREA FT**2 | BEARING AREA FT**2 |  |
|  |  | IN | IN |  |  |  |  |  |  | IN | IN |  |  |  |  |  |
| PL1 | PL1 | 36.00 | 1.000 | 29.00 | 11.60 | 50.00 | 35.00 | 36.00 | 1.00 | 1.00 | 0.00 |  |  |  |  |  |
| PL1 | PL1 | 36.00 | 0.625 | 29.00 | 11.60 | 36.00 | 95.00 | 36.00 | 0.62 | 1.00 | 7.07 |  |  |  |  |  |
| PL2 | PL2 | 36.00 | 1.000 | 29.00 | 11.60 | 50.00 | 35.00 | 36.00 | 1.00 | 1.00 | 0.00 |  |  |  |  |  |
| PL2 | PL2 | 36.00 | 0.625 | 29.00 | 11.60 | 36.00 | 95.00 | 36.00 | 0.62 | 1.00 | 7.07 |  |  |  |  |  |
| SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL |
| PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS |
| * * PILE DESCRIPTION | * * PILE DESCRIPTION | * * PILE DESCRIPTION | * * PILE DESCRIPTION | * * PILE DESCRIPTION | * * PILE DESCRIPTION | * * PILE DESCRIPTION | * * PILE DESCRIPTION | * * PILE DESCRIPTION | * * PILE DESCRIPTION | * * PILE DESCRIPTION | * * PILE DESCRIPTION | * * PILE DESCRIPTION | * * PILE DESCRIPTION | * * PILE DESCRIPTION | * * PILE DESCRIPTION | * * PILE DESCRIPTION |
| * PILE JOINTS * | * PILE JOINTS * | * PILE JOINTS * | * PILE JOINTS * | GROUP * BATTER INCREMENTS * CHORD ANGLE XZ XY | GROUP * BATTER INCREMENTS * CHORD ANGLE XZ XY | GROUP * BATTER INCREMENTS * CHORD ANGLE XZ XY | GROUP * BATTER INCREMENTS * CHORD ANGLE XZ XY | GROUP * BATTER INCREMENTS * CHORD ANGLE XZ XY | GROUP * BATTER INCREMENTS * CHORD ANGLE XZ XY | GROUP * BATTER INCREMENTS * CHORD ANGLE XZ XY | GROUP * BATTER INCREMENTS * CHORD ANGLE XZ XY | GROUP * BATTER INCREMENTS * CHORD ANGLE XZ XY | GROUP * BATTER INCREMENTS * CHORD ANGLE XZ XY | GROUP * BATTER INCREMENTS * CHORD ANGLE XZ XY | GROUP * BATTER INCREMENTS * CHORD ANGLE XZ XY | GROUP * BATTER INCREMENTS * CHORD ANGLE XZ XY |
| HEAD | BATTER | LABEL | X Y Z DEG | X Y Z DEG | X Y Z DEG | X Y Z DEG | X Y Z DEG | X Y Z DEG | X Y Z DEG | X Y Z DEG | X Y Z DEG | X Y Z DEG | X Y Z DEG | X Y Z DEG | X Y Z DEG | X Y Z DEG |
|  |  |  | FT | FT | FT |  |  |  |  |  |  |  |  |  |  |  |
| 102 | 202 | PL1 |  |  |  |  |  | 180.00 | SOL1 SOL2 |  |  |  |  |  |  |  |
| 104 | 204 | PL2 |  |  |  |  |  | 141.34 | SOL1 SOL2 |  |  |  |  |  |  |  |
| 106 | 206 | PL1 |  |  |  |  |  | 0.00 | SOL1 SOL2 |  |  |  |  |  |  |  |
| 108 | 208 | PL2 |  |  |  |  |  | 38.66 | SOL1 SOL2 |  |  |  |  |  |  |  |
| SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL |
| PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS |
| * AXIAL SOIL STIFFNESS TABLE * | * AXIAL SOIL STIFFNESS TABLE * | * AXIAL SOIL STIFFNESS TABLE * | * AXIAL SOIL STIFFNESS TABLE * | * AXIAL SOIL STIFFNESS TABLE * | * AXIAL SOIL STIFFNESS TABLE * | * AXIAL SOIL STIFFNESS TABLE * | * AXIAL SOIL STIFFNESS TABLE * | * AXIAL SOIL STIFFNESS TABLE * | * AXIAL SOIL STIFFNESS TABLE * | * AXIAL SOIL STIFFNESS TABLE * | * AXIAL SOIL STIFFNESS TABLE * | * AXIAL SOIL STIFFNESS TABLE * | * AXIAL SOIL STIFFNESS TABLE * | * AXIAL SOIL STIFFNESS TABLE * | * AXIAL SOIL STIFFNESS TABLE * | * AXIAL SOIL STIFFNESS TABLE * |
| SOIL TABLE ID | SOIL TABLE ID | SOIL TABLE ID | SOIL TABLE ID | SOIL TABLE ID | SOIL TABLE ID | SOIL TABLE ID | SOIL TABLE ID | SOIL TABLE ID | SOIL TABLE ID | SOIL TABLE ID | SOIL TABLE ID | SOIL TABLE ID | SOIL TABLE ID | SOIL TABLE ID | SOIL TABLE ID | SOIL TABLE ID |
| NUMBER OF SOIL STRATA = 7 | NUMBER OF SOIL STRATA = 7 | NUMBER OF SOIL STRATA = 7 | NUMBER OF SOIL STRATA = 7 | NUMBER OF SOIL STRATA = 7 | NUMBER OF SOIL STRATA = 7 | NUMBER OF SOIL STRATA = 7 | NUMBER OF SOIL STRATA = 7 | NUMBER OF SOIL STRATA = 7 | NUMBER OF SOIL STRATA = 7 | NUMBER OF SOIL STRATA = 7 | NUMBER OF SOIL STRATA = 7 | NUMBER OF SOIL STRATA = 7 | NUMBER OF SOIL STRATA = 7 | NUMBER OF SOIL STRATA = 7 | NUMBER OF SOIL STRATA = 7 | NUMBER OF SOIL STRATA = 7 |
| NUMBER OF POINTS/CURVE = 5 | NUMBER OF POINTS/CURVE = 5 | NUMBER OF POINTS/CURVE = 5 | NUMBER OF POINTS/CURVE = 5 | NUMBER OF POINTS/CURVE = 5 | NUMBER OF POINTS/CURVE = 5 | NUMBER OF POINTS/CURVE = 5 | NUMBER OF POINTS/CURVE = 5 | NUMBER OF POINTS/CURVE = 5 | NUMBER OF POINTS/CURVE = 5 | NUMBER OF POINTS/CURVE = 5 | NUMBER OF POINTS/CURVE = 5 | NUMBER OF POINTS/CURVE = 5 | NUMBER OF POINTS/CURVE = 5 | NUMBER OF POINTS/CURVE = 5 | NUMBER OF POINTS/CURVE = 5 | NUMBER OF POINTS/CURVE = 5 |
| STRATA DESCRIPTION | APPLIED FACTOR | FROM DEPTH F | TO DEPTH FT | T KSI | Z IN | Z KSI | T IN | Z KSI | Z IN | T KSI | Z IN | T KSI | Z IN | T KSI | Z IN |  |
| 1 | 0.90900E-01 | 0.00 | 17.88 | 0.0000 | 0.000 | 0.0184 | 0.118 | 0.0367 | 0.236 | 0.0612 | 0.394 | 0.0612 | 0.591 |  |  |  |
| 2 | 0.90900E-01 | 17.88 | 36.25 | 0.0000 | 0.000 | 0.0244 | 0.118 | 0.0487 | 0.236 | 0.0813 | 0.394 | 0.0813 | 0.591 |  |  |  |





| 3 | 0.90900E-01 | 36.25 | 54.13 | 0.0000 | 0.000 | 0.0205 | 0.118 | 0.0409 | 0.236 | 0.0682 | 0.394 | 0.0682 | 0.591 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4 | 0.90900E-01 | 54.13 | 59.71 | 0.0000 | 0.000 | 0.0184 | 0.118 | 0.0367 | 0.236 | 0.0612 | 0.394 | 0.0612 | 0.591 |
| 5 | 0.90900E-01 | 59.71 | 72.01 | 0.0000 | 0.000 | 0.0326 | 0.118 | 0.0653 | 0.236 | 0.1088 | 0.394 | 0.1088 | 0.591 |
| 6 | 0.90900E-01 | 72.01 | 73.49 | 0.0000 | 0.000 | 0.0065 | 0.118 | 0.0131 | 0.236 | 0.0217 | 0.394 | 0.0217 | 0.591 |
| 7 | 0.90900E-01 | 73.49 | 160.00 | 0.0000 | 0.000 | 0.0184 | 0.118 | 0.0367 | 0.236 | 0.0612 | 0.394 | 0.0612 | 0.591 |
| SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | Company: Bentley Sytems | Company: Bentley Sytems | Company: Bentley Sytems | Company: Bentley Sytems | Company: Bentley Sytems | Company: Bentley Sytems |
| PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | DATE 03-SEP-2020 | TIME 15:57:04 | PSI PAGE | 6 |  |  |
| * * TORSIONAL SOIL ADHESION TABLE | * * TORSIONAL SOIL ADHESION TABLE | * * TORSIONAL SOIL ADHESION TABLE | * * TORSIONAL SOIL ADHESION TABLE | * * TORSIONAL SOIL ADHESION TABLE | * * TORSIONAL SOIL ADHESION TABLE | * * TORSIONAL SOIL ADHESION TABLE | * * TORSIONAL SOIL ADHESION TABLE |  |  |  |  |  |  |
| SOIL TABLE ID | SOIL TABLE ID | SOIL TABLE ID | SOIL TABLE ID | SOIL TABLE ID | SOIL TABLE ID | SOIL TABLE ID | SOIL TABLE ID | SOL1 | SOL1 | SOL1 | SOL1 | SOL1 | SOL1 |
| NUMBER OF SOIL STRATA = 0 | NUMBER OF SOIL STRATA = 0 | NUMBER OF SOIL STRATA = 0 | NUMBER OF SOIL STRATA = 0 | NUMBER OF SOIL STRATA = 0 | NUMBER OF SOIL STRATA = 0 | NUMBER OF SOIL STRATA = 0 | NUMBER OF SOIL STRATA = 0 | NUMBER OF SOIL STRATA = 0 | NUMBER OF SOIL STRATA = 0 | NUMBER OF SOIL STRATA = 0 | NUMBER OF SOIL STRATA = 0 | NUMBER OF SOIL STRATA = 0 | NUMBER OF SOIL STRATA = 0 |
| LINEAR STIFFNESS VALUE = 1000.00 INKP/RAD | LINEAR STIFFNESS VALUE = 1000.00 INKP/RAD | LINEAR STIFFNESS VALUE = 1000.00 INKP/RAD | LINEAR STIFFNESS VALUE = 1000.00 INKP/RAD | LINEAR STIFFNESS VALUE = 1000.00 INKP/RAD | LINEAR STIFFNESS VALUE = 1000.00 INKP/RAD | LINEAR STIFFNESS VALUE = 1000.00 INKP/RAD | LINEAR STIFFNESS VALUE = 1000.00 INKP/RAD | LINEAR STIFFNESS VALUE = 1000.00 INKP/RAD | LINEAR STIFFNESS VALUE = 1000.00 INKP/RAD | LINEAR STIFFNESS VALUE = 1000.00 INKP/RAD | LINEAR STIFFNESS VALUE = 1000.00 INKP/RAD | LINEAR STIFFNESS VALUE = 1000.00 INKP/RAD | LINEAR STIFFNESS VALUE = 1000.00 INKP/RAD |
| SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | Company: Bentley Sytems | Company: Bentley Sytems | Company: Bentley Sytems | Company: Bentley Sytems | Company: Bentley Sytems | Company: Bentley Sytems |
| PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | DATE 03-SEP-2020 | TIME 15:57:04 | PSI PAGE | 7 |  |  |
| * * END-BEARING SOIL STIFFNESS TABLE | * * END-BEARING SOIL STIFFNESS TABLE | * * END-BEARING SOIL STIFFNESS TABLE | * * END-BEARING SOIL STIFFNESS TABLE | * * END-BEARING SOIL STIFFNESS TABLE | * * END-BEARING SOIL STIFFNESS TABLE | * * END-BEARING SOIL STIFFNESS TABLE | * * END-BEARING SOIL STIFFNESS TABLE |  |  |  |  |  |  |
| SOIL TABLE ID | SOIL TABLE ID | SOIL TABLE ID | SOIL TABLE ID | SOIL TABLE ID | SOIL TABLE ID | SOIL TABLE ID | SOIL TABLE ID | SOL1 | SOL1 | SOL1 | SOL1 | SOL1 | SOL1 |
| NUMBER OF SOIL STRATA = 1 | NUMBER OF SOIL STRATA = 1 | NUMBER OF SOIL STRATA = 1 | NUMBER OF SOIL STRATA = 1 | NUMBER OF SOIL STRATA = 1 | NUMBER OF SOIL STRATA = 1 | NUMBER OF SOIL STRATA = 1 | NUMBER OF SOIL STRATA = 1 | NUMBER OF SOIL STRATA = 1 | NUMBER OF SOIL STRATA = 1 | NUMBER OF SOIL STRATA = 1 | NUMBER OF SOIL STRATA = 1 | NUMBER OF SOIL STRATA = 1 | NUMBER OF SOIL STRATA = 1 |
| NUMBER OF POINTSCURVE = 2 | NUMBER OF POINTSCURVE = 2 | NUMBER OF POINTSCURVE = 2 | NUMBER OF POINTSCURVE = 2 | NUMBER OF POINTSCURVE = 2 | NUMBER OF POINTSCURVE = 2 | NUMBER OF POINTSCURVE = 2 | NUMBER OF POINTSCURVE = 2 | NUMBER OF POINTSCURVE = 2 | NUMBER OF POINTSCURVE = 2 | NUMBER OF POINTSCURVE = 2 | NUMBER OF POINTSCURVE = 2 | NUMBER OF POINTSCURVE = 2 | NUMBER OF POINTSCURVE = 2 |
| STRATA DESCRIPTION | APPLIED FACTOR | FROM DEPTHFT | TO DEPTHFT | T KSI | Z IN | T KSI | Z IN | T KSI | Z IN | T KSI | Z IN | T KSI | Z IN |
| 1 | 0.15000E-03 | 0.00 | 160.00 | 0.0000 | 0.000 | 0.0001 | 39.370 |  |  |  |  |  |  |
| SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | Company: Bentley Sytems | Company: Bentley Sytems | Company: Bentley Sytems | Company: Bentley Sytems | Company: Bentley Sytems | Company: Bentley Sytems |
| PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | DATE 03-SEP-2020 | TIME 15:57:04 | PSI PAGE | 8 |  |  |
| * * LATERAL SOIL STIFFNESS TABLE | * * LATERAL SOIL STIFFNESS TABLE | * * LATERAL SOIL STIFFNESS TABLE | * * LATERAL SOIL STIFFNESS TABLE | * * LATERAL SOIL STIFFNESS TABLE | * * LATERAL SOIL STIFFNESS TABLE | * * LATERAL SOIL STIFFNESS TABLE | * * LATERAL SOIL STIFFNESS TABLE |  |  |  |  |  |  |
| SOIL TABLE ID | SOIL TABLE ID | SOIL TABLE ID | SOIL TABLE ID | SOIL TABLE ID | SOIL TABLE ID | SOIL TABLE ID | SOIL TABLE ID | SOL1 | SOL1 | SOL1 | SOL1 | SOL1 | SOL1 |
| NUMBER OF SOIL STRATA = 10 | NUMBER OF SOIL STRATA = 10 | NUMBER OF SOIL STRATA = 10 | NUMBER OF SOIL STRATA = 10 | NUMBER OF SOIL STRATA = 10 | NUMBER OF SOIL STRATA = 10 | NUMBER OF SOIL STRATA = 10 | NUMBER OF SOIL STRATA = 10 | NUMBER OF SOIL STRATA = 10 | NUMBER OF SOIL STRATA = 10 | NUMBER OF SOIL STRATA = 10 | NUMBER OF SOIL STRATA = 10 | NUMBER OF SOIL STRATA = 10 | NUMBER OF SOIL STRATA = 10 |
| NUMBER OF POINTSCURVE = 30 | NUMBER OF POINTSCURVE = 30 | NUMBER OF POINTSCURVE = 30 | NUMBER OF POINTSCURVE = 30 | NUMBER OF POINTSCURVE = 30 | NUMBER OF POINTSCURVE = 30 | NUMBER OF POINTSCURVE = 30 | NUMBER OF POINTSCURVE = 30 | NUMBER OF POINTSCURVE = 30 | NUMBER OF POINTSCURVE = 30 | NUMBER OF POINTSCURVE = 30 | NUMBER OF POINTSCURVE = 30 | NUMBER OF POINTSCURVE = 30 | NUMBER OF POINTSCURVE = 30 |



P-Y DATA DIAMETER = 20.000 IN



| STRATA DESCRIPTION | APPLIED FACTOR | FROM DEPTH FT | TO DEPTH FT | P Y | P Y | P Y | P Y | P Y | P Y | P Y | P Y | P Y | P Y |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| STRATA DESCRIPTION | APPLIED FACTOR | FROM DEPTH FT | TO DEPTH FT | K/IN | IN | K/IN | IN | K/IN | IN | K/IN | IN | K/IN | IN |
| 1 | 0.10000E-01 | 0.00 |  | 0.0000 | 0.000 | 0.0082 | 0.134 | 0.0102 | 0.201 | 0.0102 | 0.240 |  |  |
| 2 | 0.10000E-01 | 18.04 |  | 0.0000 | 0.000 | 0.0176 | 0.331 | 0.0226 | 0.496 | 0.0254 | 0.594 | 0.0254 | 0.709 |
| 3 | 0.10000E-01 | 30.42 |  | 0.0000 | 0.000 | 0.1676 | 0.331 | 0.1700 | 0.496 | 0.1733 | 0.594 | 0.1757 | 0.709 |
| 4 | 0.10000E-01 | 36.42 |  | 0.0000 | 0.000 | 0.1257 | 0.331 | 0.1257 | 0.496 | 0.1257 | 0.594 | 0.1257 | 0.709 |
| 5 | 0.10000E-01 | 54.12 |  | 0.0000 | 0.000 | 0.1257 | 0.331 | 0.1257 | 0.496 | 0.1841 | 0.594 | 0.1876 | 0.709 |
| 6 | 0.10000E-01 | 54.13 |  | 0.0000 | 0.000 | 0.1027 | 0.323 | 0.1027 | 0.484 | 0.1838 | 0.583 | 0.1876 | 0.709 |
| 7 | 0.10000E-01 | 59.71 |  | 0.0000 | 0.000 | 0.1027 | 0.323 | 0.2026 | 0.583 | 0.2070 | 0.709 | 0.2086 | 2.160 |
| 8 | 0.10000E-01 | 72.17 |  | 0.0000 | 0.000 | 0.2515 | 0.331 | 0.2515 | 0.496 | 0.2516 | 0.594 |  |  |
| 9 | 0.10000E-01 | 72.18 |  | 0.0000 | 0.000 | 0.0736 | 0.122 | 0.1358 | 0.248 | 0.1927 | 0.413 | 0.2289 | 0.618 |
| 10 | 0.10000E-01 | 73.49 | 160.00 | 0.0000 | 0.000 | 0.1027 | 0.673 | 0.1027 | 1.012 | 0.2568 | 1.213 | 0.2856 | 1.300 |
| SACS CONNECT Edition V(14.3) - CL PSI SAMPLE ANALYSIS | SACS CONNECT Edition V(14.3) - CL PSI SAMPLE ANALYSIS | SACS CONNECT Edition V(14.3) - CL PSI SAMPLE ANALYSIS | SACS CONNECT Edition V(14.3) - CL PSI SAMPLE ANALYSIS | SACS CONNECT Edition V(14.3) - CL PSI SAMPLE ANALYSIS | SACS CONNECT Edition V(14.3) - CL PSI SAMPLE ANALYSIS | SACS CONNECT Edition V(14.3) - CL PSI SAMPLE ANALYSIS | SACS CONNECT Edition V(14.3) - CL PSI SAMPLE ANALYSIS | Company: Bentley Sytems DATE 03-SEP-2020 TIME 15:57:04 PSI PAGE | Company: Bentley Sytems DATE 03-SEP-2020 TIME 15:57:04 PSI PAGE | Company: Bentley Sytems DATE 03-SEP-2020 TIME 15:57:04 PSI PAGE | Company: Bentley Sytems DATE 03-SEP-2020 TIME 15:57:04 PSI PAGE | Company: Bentley Sytems DATE 03-SEP-2020 TIME 15:57:04 PSI PAGE | Company: Bentley Sytems DATE 03-SEP-2020 TIME 15:57:04 PSI PAGE |



* * AXIAL SOIL STIFFNESS TABLE * *

SOIL TABLE ID SOL2

NUMBER OF SOIL STRATA = 7

NUMBER OF POINTS/CURVE = 5



| STRATA DESCRIPTION | APPLIED FACTOR | FROM DEPTH | TO DEPTH | T Z | T Z | T Z | T Z | T Z | T Z | T Z | T Z | T Z | T Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| STRATA DESCRIPTION | APPLIED FACTOR | FT | FT | KSI | IN | KSI | IN | KSI | IN | KSI | IN | KSI | IN |
| 1 | 0.90900E-01 | 0.00 | 17.88 | 0.0000 | 0.000 | 0.0184 | 0.118 | 0.0367 | 0.236 | 0.0612 | 0.394 | 0.0612 | 0.591 |
| 2 | 0.90900E-01 | 17.88 | 36.25 | 0.0000 | 0.000 | 0.0244 | 0.118 | 0.0487 | 0.236 | 0.0813 | 0.394 | 0.0813 | 0.591 |
| 3 | 0.90900E-01 | 36.25 | 54.13 | 0.0000 | 0.000 | 0.0205 | 0.118 | 0.0409 | 0.236 | 0.0682 | 0.394 | 0.0682 | 0.591 |
| 4 | 0.90900E-01 | 54.13 | 59.71 | 0.0000 | 0.000 | 0.0184 | 0.118 | 0.0367 | 0.236 | 0.0612 | 0.394 | 0.0612 | 0.591 |
| 5 | 0.90900E-01 | 59.71 | 72.01 | 0.0000 | 0.000 | 0.0326 | 0.118 | 0.0653 | 0.236 | 0.1088 | 0.394 | 0.1088 | 0.591 |
| 6 | 0.90900E-01 | 72.01 | 73.49 | 0.0000 | 0.000 | 0.0065 | 0.118 | 0.0131 | 0.236 | 0.0217 | 0.394 | 0.0217 | 0.591 |
| 7 | 0.90900E-01 | 73.49 | 160.00 | 0.0000 | 0.000 | 0.0184 | 0.118 | 0.0367 | 0.236 | 0.0612 | 0.394 | 0.0612 | 0.591 |
| SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | Company: Bentley Sytems | Company: Bentley Sytems | Company: Bentley Sytems | Company: Bentley Sytems | Company: Bentley Sytems | Company: Bentley Sytems |
| PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | DATE 03-SEP-2020 | TIME 15:57:04 | PSI PAGE | 10 |  |  |
| * * TORSIONAL SOIL ADHESION TABLE * * | * * TORSIONAL SOIL ADHESION TABLE * * | * * TORSIONAL SOIL ADHESION TABLE * * | * * TORSIONAL SOIL ADHESION TABLE * * | * * TORSIONAL SOIL ADHESION TABLE * * | * * TORSIONAL SOIL ADHESION TABLE * * | * * TORSIONAL SOIL ADHESION TABLE * * | * * TORSIONAL SOIL ADHESION TABLE * * | * * TORSIONAL SOIL ADHESION TABLE * * | * * TORSIONAL SOIL ADHESION TABLE * * | * * TORSIONAL SOIL ADHESION TABLE * * | * * TORSIONAL SOIL ADHESION TABLE * * | * * TORSIONAL SOIL ADHESION TABLE * * | * * TORSIONAL SOIL ADHESION TABLE * * |
| SOIL TABLE ID | SOIL TABLE ID | SOIL TABLE ID | SOIL TABLE ID | SOIL TABLE ID | SOIL TABLE ID | SOIL TABLE ID | SOIL TABLE ID | SOL2 | SOL2 | SOL2 | SOL2 | SOL2 | SOL2 |
| NUMBER OF SOIL STRATA = 0 | NUMBER OF SOIL STRATA = 0 | NUMBER OF SOIL STRATA = 0 | NUMBER OF SOIL STRATA = 0 | NUMBER OF SOIL STRATA = 0 | NUMBER OF SOIL STRATA = 0 | NUMBER OF SOIL STRATA = 0 | NUMBER OF SOIL STRATA = 0 | NUMBER OF SOIL STRATA = 0 | NUMBER OF SOIL STRATA = 0 | NUMBER OF SOIL STRATA = 0 | NUMBER OF SOIL STRATA = 0 | NUMBER OF SOIL STRATA = 0 | NUMBER OF SOIL STRATA = 0 |
| LINEAR STIFFNESS VALUE = 1000.00 INKP/RAD | LINEAR STIFFNESS VALUE = 1000.00 INKP/RAD | LINEAR STIFFNESS VALUE = 1000.00 INKP/RAD | LINEAR STIFFNESS VALUE = 1000.00 INKP/RAD | LINEAR STIFFNESS VALUE = 1000.00 INKP/RAD | LINEAR STIFFNESS VALUE = 1000.00 INKP/RAD | LINEAR STIFFNESS VALUE = 1000.00 INKP/RAD | LINEAR STIFFNESS VALUE = 1000.00 INKP/RAD | LINEAR STIFFNESS VALUE = 1000.00 INKP/RAD | LINEAR STIFFNESS VALUE = 1000.00 INKP/RAD | LINEAR STIFFNESS VALUE = 1000.00 INKP/RAD | LINEAR STIFFNESS VALUE = 1000.00 INKP/RAD | LINEAR STIFFNESS VALUE = 1000.00 INKP/RAD | LINEAR STIFFNESS VALUE = 1000.00 INKP/RAD |
| SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | Company: Bentley Sytems | Company: Bentley Sytems | Company: Bentley Sytems | Company: Bentley Sytems | Company: Bentley Sytems | Company: Bentley Sytems |
| PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | DATE 03-SEP-2020 | TIME 15:57:04 | PSI PAGE | 11 |  |  |
| * * END-BEARING SOIL STIFFNESS TABLE * * | * * END-BEARING SOIL STIFFNESS TABLE * * | * * END-BEARING SOIL STIFFNESS TABLE * * | * * END-BEARING SOIL STIFFNESS TABLE * * | * * END-BEARING SOIL STIFFNESS TABLE * * | * * END-BEARING SOIL STIFFNESS TABLE * * | * * END-BEARING SOIL STIFFNESS TABLE * * | * * END-BEARING SOIL STIFFNESS TABLE * * | * * END-BEARING SOIL STIFFNESS TABLE * * | * * END-BEARING SOIL STIFFNESS TABLE * * | * * END-BEARING SOIL STIFFNESS TABLE * * | * * END-BEARING SOIL STIFFNESS TABLE * * | * * END-BEARING SOIL STIFFNESS TABLE * * | * * END-BEARING SOIL STIFFNESS TABLE * * |
| SOIL TABLE ID | SOIL TABLE ID | SOIL TABLE ID | SOIL TABLE ID | SOIL TABLE ID | SOIL TABLE ID | SOIL TABLE ID | SOIL TABLE ID | SOL2 | SOL2 | SOL2 | SOL2 | SOL2 | SOL2 |
| NUMBER OF SOIL STRATA = 1 | NUMBER OF SOIL STRATA = 1 | NUMBER OF SOIL STRATA = 1 | NUMBER OF SOIL STRATA = 1 | NUMBER OF SOIL STRATA = 1 | NUMBER OF SOIL STRATA = 1 | NUMBER OF SOIL STRATA = 1 | NUMBER OF SOIL STRATA = 1 | NUMBER OF SOIL STRATA = 1 | NUMBER OF SOIL STRATA = 1 | NUMBER OF SOIL STRATA = 1 | NUMBER OF SOIL STRATA = 1 | NUMBER OF SOIL STRATA = 1 | NUMBER OF SOIL STRATA = 1 |
| NUMBER OF POINTSCURVE = 2 | NUMBER OF POINTSCURVE = 2 | NUMBER OF POINTSCURVE = 2 | NUMBER OF POINTSCURVE = 2 | NUMBER OF POINTSCURVE = 2 | NUMBER OF POINTSCURVE = 2 | NUMBER OF POINTSCURVE = 2 | NUMBER OF POINTSCURVE = 2 | NUMBER OF POINTSCURVE = 2 | NUMBER OF POINTSCURVE = 2 | NUMBER OF POINTSCURVE = 2 | NUMBER OF POINTSCURVE = 2 | NUMBER OF POINTSCURVE = 2 | NUMBER OF POINTSCURVE = 2 |
| STRATA DESCRIPTION | APPLIED FACTOR | FROM DEPTHFT | TO DEPTHFT | T KSI | Z IN | T KSI | Z IN | T KSI | Z IN | T KSI | Z IN | T KSI | Z IN |
| 1 | 0.15000E-03 | 0.00 | 160.00 | 0.0000 | 0.000 | 0.0001 | 39.370 |  |  |  |  |  |  |
| SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | SACS CONNECT Edition V(14.3) - CL | Company: Bentley Sytems | Company: Bentley Sytems | Company: Bentley Sytems | Company: Bentley Sytems | Company: Bentley Sytems | Company: Bentley Sytems |
| PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | DATE 03-SEP-2020 | TIME 15:57:04 | PSI PAGE | 12 |  |  |
| * * LATERAL SOIL STIFFNESS TABLE * * | * * LATERAL SOIL STIFFNESS TABLE * * | * * LATERAL SOIL STIFFNESS TABLE * * | * * LATERAL SOIL STIFFNESS TABLE * * | * * LATERAL SOIL STIFFNESS TABLE * * | * * LATERAL SOIL STIFFNESS TABLE * * | * * LATERAL SOIL STIFFNESS TABLE * * | * * LATERAL SOIL STIFFNESS TABLE * * | * * LATERAL SOIL STIFFNESS TABLE * * | * * LATERAL SOIL STIFFNESS TABLE * * | * * LATERAL SOIL STIFFNESS TABLE * * | * * LATERAL SOIL STIFFNESS TABLE * * | * * LATERAL SOIL STIFFNESS TABLE * * | * * LATERAL SOIL STIFFNESS TABLE * * |





| SOIL TABLE ID | SOL2 |
| --- | --- |
| NUMBER OF SOIL STRATA = 9 | NUMBER OF SOIL STRATA = 9 |
| NUMBER OF POINTS/CURVE = 30 | NUMBER OF POINTS/CURVE = 30 |
| P-Y DATA DIAMETER = 20.000 IN | P-Y DATA DIAMETER = 20.000 IN |





| STRATA DESCRIPTION | APPLIED FACTOR | FROM DEPTH FT | TO DEPTH FT | P Y | P Y | P Y | P Y | P Y | P Y | P Y | P Y | P Y | P Y |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| STRATA DESCRIPTION | APPLIED FACTOR | FROM DEPTH FT | TO DEPTH FT | K/IN | IN | K/IN | IN | K/IN | IN | K/IN | IN | K/IN | IN |
| 1 | 0.10000E-01 | 0.00 | 30.42 | -0.0075 | -10.000 | -0.0075 | 0.000 | -0.0075 | 10.000 | 0.0000 | 0.000 |  |  |
| 2 | 0.10000E-01 | 30.42 |  | 0.0000 0.1757 | 0.000 2.160 | 0.1676 | 0.331 | 0.1700 | 0.496 | 0.1733 | 0.594 | 0.1757 | 0.709 |
| 3 | 0.10000E-01 | 36.42 |  | 0.0000 0.1267 | 0.000 2.160 | 0.1257 | 0.331 | 0.1257 | 0.496 | 0.1257 | 0.594 | 0.1257 | 0.709 |
| 4 | 0.10000E-01 | 54.12 |  | 0.0000 0.1892 | 0.000 2.160 | 0.1257 | 0.331 | 0.1257 | 0.496 | 0.1841 | 0.594 | 0.1876 | 0.709 |
| 5 | 0.10000E-01 | 54.13 |  | 0.0000 0.1892 | 0.000 2.160 | 0.1027 | 0.323 | 0.1027 | 0.484 | 0.1838 | 0.583 | 0.1876 | 0.709 |
| 6 | 0.10000E-01 | 59.71 |  | 0.0000 | 0.000 | 0.1027 | 0.323 | 0.2026 | 0.583 | 0.2070 | 0.709 | 0.2086 | 2.160 |
| 7 | 0.10000E-01 | 72.17 |  | 0.0000 | 0.000 | 0.2515 | 0.331 | 0.2515 | 0.496 | 0.2516 | 0.594 |  |  |
| 8 | 0.10000E-01 | 72.18 |  | 0.0000 0.2438 | 0.000 2.090 | 0.0736 0.2496 | 0.122 2.620 | 0.1358 0.2516 | 0.248 3.140 | 0.1927 | 0.413 | 0.2289 | 0.618 |
| 9 | 0.10000E-01 | 73.49 | 160.00 | 0.0000 | 0.000 | 0.1027 | 0.673 | 0.1027 | 1.012 | 0.2568 | 1.213 | 0.2856 | 1.300 |





| PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | DATE 03-SEP-2020 TIME 15:57:04 PSI PAGE 103 | DATE 03-SEP-2020 TIME 15:57:04 PSI PAGE 103 | DATE 03-SEP-2020 TIME 15:57:04 PSI PAGE 103 | DATE 03-SEP-2020 TIME 15:57:04 PSI PAGE 103 | DATE 03-SEP-2020 TIME 15:57:04 PSI PAGE 103 | DATE 03-SEP-2020 TIME 15:57:04 PSI PAGE 103 | DATE 03-SEP-2020 TIME 15:57:04 PSI PAGE 103 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS | PSI SAMPLE ANALYSIS |
| * * * PILE MAXIMUM UNI TY CHECK SUMMARY * * * | * * * PILE MAXIMUM UNI TY CHECK SUMMARY * * * | * * * PILE MAXIMUM UNI TY CHECK SUMMARY * * * | * * * PILE MAXIMUM UNI TY CHECK SUMMARY * * * | * * * PILE MAXIMUM UNI TY CHECK SUMMARY * * * | * * * PILE MAXIMUM UNI TY CHECK SUMMARY * * * | * * * PILE MAXIMUM UNI TY CHECK SUMMARY * * * | * * * PILE MAXIMUM UNI TY CHECK SUMMARY * * * | * * * PILE MAXIMUM UNI TY CHECK SUMMARY * * * | * * * PILE MAXIMUM UNI TY CHECK SUMMARY * * * | * * * PILE MAXIMUM UNI TY CHECK SUMMARY * * * | * * * PILE MAXIMUM UNI TY CHECK SUMMARY * * * | * * * PILE MAXIMUM UNI TY CHECK SUMMARY * * * | * * * PILE MAXIMUM UNI TY CHECK SUMMARY * * * | * * * PILE MAXIMUM UNI TY CHECK SUMMARY * * * | * * * PILE MAXIMUM UNI TY CHECK SUMMARY * * * |
| PILE GRUP LOAD CASE | AXIAL KIPS | PILEHEAD FORCES LATERAL KIPS | MOMENT IN-KIP | * PILEHEAD DISPLACEMENTS AXIAL IN | LATERAL IN | ROTATION RAD | DEPTH FT | AXIAL FBY KSI | STRESSES AT MAX. FREQUENCY FBZ KSI | UNI TY CHECK COMB. | UNITY CHECK |  |  |  |  |
| 102 PL1 OPR1 | -510.74 | 1.94 | 241.2 | 0.07 | 0.20 | 0.000288 | 0.0 | -4.65 | -0.25 | 0.04 | -4.90 | 0.162 |  |  |  |
| 102 PL1 OPR1 | OPR2 | -485.78 | 11.80 | 1411.6 | 0.07 | 0.65 | 0.001320 | 35.1 | -2.24 | -1.40 | 1.88 | 0.06 | -4.58 | 0.195 |  |
| 102 PL1 OPR1 | OPR3 | -558.58 | 23.60 | 4195.4 | 0.08 | 2.00 | 0.003394 | 35.1 | -2.57 | -5.68 | 2.64 | 0.13 | -8.84 | 0.362 |  |
| 102 PL1 OPR1 | STM1 | 113.27 | 54.00 | 15368.9 | -0.01 | 9.69 | 0.011728 | 49.4 | 0.29 | 19.01 | -0.11 | 0.05 | 19.30 | 0.564 |  |
| 102 PL1 OPR1 | STM2 | 192.06 | 43.05 | 9125.9 | -0.02 | 5.09 | 0.007353 | 41.6 | 0.66 | 11.79 | 4.65 | 0.30 | 13.33 | 0.392 |  |
| 102 PL1 OPR1 | STM3 | -164.26 | 41.19 | 6264.6 | 0.02 | 2.83 | 0.005248 | 35.1 | -0.77 | -4.34 | 8.87 | 0.19 | -10.65 | 0.314 |  |
| 104 PL2 OPR1 | -523.91 | 1.87 | 320.1 | 0.07 | 0.13 | 0.000195 | 0.0 | -4.76 | -0.32 | 0.12 | 0.03 | -5.11 | 0.168 |  |  |
| 104 PL2 OPR1 | OPR2 | -418.11 | 11.33 | 1268.5 | 0.06 | 0.66 | 0.001371 | 35.1 | -1.94 | -1.56 | 1.75 | 0.06 | -4.29 | 0.181 |  |
| 104 PL2 OPR1 | OPR3 | -290.73 | 23.52 | 3999.5 | 0.04 | 2.03 | 0.003469 | 35.1 | -1.35 | -5.76 | 2.45 | 0.14 | -7.62 | 0.306 |  |
| 104 PL2 OPR1 | STM1 | -998.26 | 46.88 | 16002.5 | 0.13 | 9.62 | 0.012029 | 45.5 | -3.10 | 19.41 | 0.25 | 0.24 | -22.51 | 0.673 |  |
| 104 PL2 OPR1 | STM2 | -525.19 | 41.64 | 9555.8 | 0.07 | 5.11 | 0.007508 | 40.3 | -1.98 | 11.83 | 5.50 | 0.36 | -15.02 | 0.449 |  |
| 104 PL2 OPR1 | STM3 | 68.32 | 43.18 | 6465.8 | -0.01 | 2.98 | 0.005490 | 35.1 | 0.29 | -4.33 | 9.32 | 0.17 | 10.57 | 0.309 |  |
| 106 PL1 OPR1 | -493.11 | 1.70 | 318.5 | 0.07 | 0.22 | 0.000314 | 0.0 | -4.48 | -0.34 | -0.05 | 0.03 | -4.82 | 0.159 |  |  |
| 106 PL1 OPR1 | OPR2 | -598.71 | 10.17 | 1409.3 | 0.08 | 0.52 | 0.000951 | 0.0 | -5.45 | 0.98 | -1.14 | 0.19 | -6.95 | 0.223 |  |
| 106 PL1 OPR1 | OPR3 | -725.01 | 22.18 | 4211.5 | 0.10 | 1.96 | 0.003227 | 35.1 | -3.33 | -5.75 | 1.82 | 0.12 | -9.37 | 0.389 |  |
| 106 PL1 OPR1 | STM1 | 126.15 | 54.32 | 15469.6 | -0.02 | 9.73 | 0.011741 | 49.4 | 0.32 | 19.06 | 0.12 | 0.04 | 19.39 | 0.566 |  |
| 106 PL1 OPR1 | STM2 | -343.43 | 41.46 | 9362.3 | 0.05 | 5.00 | 0.007279 | 40.3 | -1.30 | 11.74 | 4.92 | 0.32 | -14.02 | 0.416 |  |
| 106 PL1 OPR1 | STM3 | -930.37 | 39.40 | 6798.1 | 0.13 | 2.85 | 0.005133 | 35.1 | -4.27 | -5.35 | 8.36 | 0.20 | -14.20 | 0.437 |  |
| 108 PL2 OPR1 | -552.64 | 2.19 | 384.8 | 0.08 | 0.18 | 0.000270 | 0.0 | -5.03 | -0.41 | 0.05 | 0.04 | -5.44 | 0.179 |  |  |
| 108 PL2 OPR1 | OPR2 | -576.92 | 10.11 | 1330.0 | 0.08 | 0.57 | 0.001093 | 0.0 | -5.25 | 0.91 | -1.09 | 0.19 | -6.67 | 0.214 |  |
| 108 PL2 OPR1 | OPR3 | -503.75 | 22.89 | 4129.5 | 0.07 | 2.02 | 0.003384 | 35.1 | -2.33 | -5.86 | 2.00 | 0.12 | -8.52 | 0.348 |  |
| 108 PL2 OPR1 | STM1 | -1027.42 | 46.85 | 16086.6 | 0.14 | 9.62 | 0.012004 | 45.5 | -3.19 | 19.42 | -0.32 | 0.24 | -22.61 | 0.676 |  |
| 108 PL2 OPR1 | STM2 | -1107.30 | 37.67 | 9443.1 | 0.15 | 4.87 | 0.007196 | 36.4 | -4.81 | 10.94 | 5.50 | 0.52 | -17.05 | 0.523 |  |
| 108 PL2 OPR1 | STM3 | -751.37 | 42.29 | 7257.4 | 0.10 | 3.12 | 0.005591 | 35.1 | -3.46 | -5.56 | 9.19 | 0.19 | -14.20 | 0.433 |  |



# 8 REFERENCES

[1] S. J. Brandenberg, R. W. Boulanger, B. L. Kutter, and D. Chang, “Static Pushover Analyses of Pile Groups in Liquefied and Laterally Spreading Ground in Centrifuge Tests,” Journal of Geotechnical and Geoenvironmental Engineering, vol. 133, no. 9, pp. 1055–1066, Sep. 2007, doi: 10.1061/(ASCE)1090-0241(2007)133:9(1055).   
[2] T. L. Youd and I. M. Idriss, “LIQUEFACTION RESISTANCE OF SOILS: SUMMARY REPORT FROM THE 1996 NCEER AND 1998 NCEER/NSF WORKSHOPS ON EVALUATION OF LIQUEFACTION RESISTANCE OF SOILSa,” p. 17.   
[3] R. W. Boulanger and I. M. Idriss, “CPT and SPT Based Liquefaction Triggering Procedures,” UCD/CGM-14/01, Apr. 2014.   
[4] S. J. Brandenberg, “Behavior of Pile Foundations in Liquefied and Laterally Spreading Ground,” p. 350.   
[5] B. W. Byrne et al., “PISA design model for monopiles for offshore wind turbines: application to a stiff glacial clay till,” Géotechnique, vol. 70, no. 11, pp. 1030–1047, Nov. 2020, doi: 10.1680/jgeot.18.P.255.   
[6] H. J. Burd et al., “PISA design model for monopiles for offshore wind turbines: application to a marine sand,” Géotechnique, vol. 70, no. 11, pp. 1048–1066, Nov. 2020, doi: 10.1680/jgeot.18.P.277.

9 INPUT LINES

SOIL (CLAY) API AXIAL STRATUM LINE

COLUMNS

COMMENTARY

GENERAL THIS LINE SET IS USED TO SPECIFY THE SOIL PROPERTIES FOR EACHCLAY STRATUM. THE PROGRAM WILL USE THESE PROPERTIES TOCALCULATE AXIAL ADHESION AND BEARING CAPACITIES OR T-Z AXIALAND Q-Z END BEARING CURVES.

( 1- 4) ENTER 'SOIL'.   
( 6-12) ENTER 'API AXL'.   
( 13 ) IF THE API RP2A 10TH EDITION SOIL PROPERTIES ARE DESIRED ENTER A '1' HERE. OTHERWISE, LEAVE BLANK.   
(14-17) ENTER 'SLOC'.   
(19-24) ENTER THE DISTANCE FROM THE PILEHEAD TO THE TOP OF THIS SOIL STRATUM. THIS DISTANCE IS VERTICALLY DOWN AND NOT ALONG THE AXIS OF THE PILE, WHICH MAY BE BATTERED.   
(25-30) IF THIS DATA IS BEING USED FOR ADHESION, ENTER THE DISTANCE TO THE BOTTOM OF THIS STRATUM. IF THIS DATA IS BEING USED FOR T-Z AXIAL, ENTER THE DISTANCE FROM THE PILEHEAD TO BOTTOM OF THIS STRATUM IF THE T-Z DATA IS TO BE CONSTANT FOR THIS STRATUM. IF LEFT BLANK, THE T-Z DATA WILL VARY LINEARLY TO THE TOP OF THE NEXT STRATUM. NO GAPS SHOULD BE LEFT BETWEEN STRATA.   
(32-35) ENTER THE SOIL TYPE. SELECT FROM AMONG THE FOLLOWING:

'CLAY' - NORMAL.

'CLOC' - OVER-CONSOLIDATED GULF OF MEXICO CLAY (API 10TH ONLY).

'CLUC' - UNDER-CONSOLIDATED GULF OF MEXICO CLAY (API 10TH ONLY).

COLUMNS

COMMENTARY

(36-41) ENTER THE UNDRAINED SHEAR STRENGTH.   
(48-53) ENTER THE SUBMERGED UNIT WEIGHT.   
(66-71) ENTER THE OVERBURDEN PRESSURE IF THE INTERNALLY CALCULATED VALUE IS NOT ACCEPTABLE.   
(72-77) ENTER THE SOIL RESIDUAL FACTOR ( Tres / Tmax).  
(78-80) ENTER ZPEAK RATIO TO PILE DIAMETER (ONLY FOR API 22ND EDITION). ZPEAK IS THE DISPLACEMENT TO MAXIMUM SOIL PILE ADHESION OR UNIT SKIN FRICTION (ONLY FOR API RP 22ND EDITION) A DEFAULT VALUE FOR ZPEAK OF 1% OF THE PILE OUTER DIAMETER IS RECOMMENDED BY API 22ND EDITION. HOWEVER, THE VALUE MAY VARY FROM 0.25 TO



| LINE LABEL | AUTOMATIC AXIAL RESISTANCE GENERATION | API EDITION SELECTION | LINE TYPE | TOP OF STRATUM | BOTTOM OF STRATUM | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | ZPEAK RATIO TO PILE DIAMETER (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | AUTOMATIC AXIAL RESISTANCE GENERATION | API EDITION SELECTION | LINE TYPE | TOP OF STRATUM | BOTTOM OF STRATUM | SOIL TYPE | UNDRAINED SHEAR STRENGTH | SUBMERGED DENSITY | OVER- BURDEN PRESSURE | RESIDUAL FACTOR | ZPEAK RATIO TO PILE DIAMETER (%) |
| SOIL | API AXL |  | SLOC |  |  |  |  |  |  |  |  |
| 1--4 | 6--12 | 13 | 14--17 | 19<--24 | 25<--30 | 32--35 | 36<--41 | 48<--53 | 66<--71 | 72<--77 | 78<--80 |
| DEFAULT |  | 20TH |  |  |  |  |  |  |  | 0.7 | 1 |
| ENGLISH |  |  |  | FT | FT |  | KIP/SQ.FT | LB/CU.FT | KIP/SQ.FT |  |  |
| METRIC (KN) |  |  |  | M | M |  | KN/SQ.CM | TONNE/CU.M | KN/SQ.CM |  |  |
| METRIC (KG) |  |  |  | M | M |  | KG/SQ.CM | TONNE/CU.M | KG/SQ.CM |  |  |



SOIL (ROCK) API AXIAL STRATUM LINE

COLUMNS

COMMENTARY

GENERAL THIS LINE SET IS USED TO SPECIFY THE SOIL PROPERTIES FOR EACHROCK STRATUM. THE PROGRAM WILL USE THESE PROPERTIES TOCALCULATE AXIAL ADHESION AND BEARING CAPACITIES OR T-Z AXIALAND Q-Z END BEARING CURVES.

( 1- 4) ENTER 'SOIL'.   
( 6-12) ENTER 'API AXL'.   
( 13 ) IF THE API RP2A 10TH EDITION SOIL PROPERTIES ARE DESIRED ENTER A '1' HERE. OTHERWISE, LEAVE BLANK.   
(14-17) ENTER 'SLOC'.   
(19-24) ENTER THE DISTANCE FROM THE PILEHEAD TO THE TOP OF THIS SOIL STRATUM. THIS DISTANCE IS VERTICALLY DOWN AND NOT ALONG THE AXIS OF THE PILE, WHICH MAY BE BATTERED.   
(25-30) IF THIS DATA IS BEING USED FOR ADHESION, ENTER THE DISTANCE TO THE BOTTOM OF THIS STRATUM. IF THIS DATA IS BEING USED FOR T-Z AXIAL, ENTER THE DISTANCE FROM THE PILEHEAD TO BOTTOM OF THIS STRATUM IF THE T-Z DATA IS TO BE CONSTANT FOR THIS STRATUM. IF LEFT BLANK, THE T-Z DATA WILL VARY LINEARLY TO THE TOP OF THE NEXT STRATUM. NO GAPS SHOULD BE LEFT BETWEEN STRATA.   
(32-35) ENTER THE SOIL TYPE OF 'ROCK'.

COLUMNS

COMMENTARY

(36-41) ENTER THE UNIT SKIN FRICTION CAPACITY.   
(42-47) ENTER THE BEARING CAPACITY.   
(48-53) ENTER THE SUBMERGED UNIT WEIGHT.   
(78-80) ENTER ZPEAK RATIO TO PILE DIAMETER (ONLY FOR API 22ND EDITION). ZPEAK IS THE DISPLACEMENT TO MAXIMUM SOIL PILE ADHESION OR UNIT SKIN FRICTION (ONLY FOR API RP 22ND EDITION) A DEFAULT VALUE FOR ZPEAK OF 1% OF THE PILE OUTER DIAMETER IS RECOMMENDED BY API 22ND EDITION. HOWEVER, THE VALUE MAY VARY FROM 0.25 TO



| LINE LABEL | AUTOMATIC AXIAL RESISTANCE GENERATION | API EDITION SELECTION | LINE TYPE | TOP OF STRATUM | BOTTOM OF STRATUM | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | LEAVE BLANK | ZPEAK RATIO TO PILE DIAMETER (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | AUTOMATIC AXIAL RESISTANCE GENERATION | API EDITION SELECTION | LINE TYPE | TOP OF STRATUM | BOTTOM OF STRATUM | SOIL TYPE | UNIT SKIN FRICTION CAPACITY | BEARING CAPACITY | SUBMERGED DENSITY | LEAVE BLANK | ZPEAK RATIO TO PILE DIAMETER (%) |
| SOIL | API AXL |  | SLOC |  |  |  |  |  |  |  |  |
| 1--4 | 6--12 | 13 | 14--17 | 19<--24 | 25<--30 | 32--35 | 36<--41 | 42<--47 | 48<--53 | 54<--77 | 78--80 |
| DEFAULT |  | 20TH |  |  |  |  |  |  |  |  | 1 |
| ENGLISH |  |  |  | FT | FT |  | KIP/SQ.FT | KIP/SQ.FT | LB/CU.FT |  |  |
| METRIC (KN) |  |  |  | M | M |  | KN/SQ.CM | KN/SQ.CM | TONNE/CU.M |  |  |
| METRIC (KG) |  |  |  | M | M |  | KG/SQ.CM | KG/SQ.CM | TONNE/CU.M |  |  |



SOIL (SAND) API AXIAL STRATUM LINE

COLUMNS

COMMENTARY

GENERAL THIS LINE SET IS USED TO SPECIFY THE SOIL PROPERTIES FOR EACHSAND STRATUM. THE PROGRAM WILL USE THESE PROPERTIES TOCALCULATE AXIAL ADHESION AND BEARING CAPACITIES OR T-Z AXIALAND Q-Z END BEARING CURVES.

( 1- 4) ENTER 'SOIL'.   
( 6-12) ENTER 'API AXL'.   
( 13 ) IF THE API RP2A 10TH EDITION SOIL PROPERTIES ARE DESIRED ENTER A '1' HERE. OTHERWISE, LEAVE BLANK.   
(14-17) ENTER 'SLOC'.   
(19-24) ENTER THE DISTANCE FROM THE PILEHEAD TO THE TOP OF THIS SOIL STRATUM. THIS DISTANCE IS VERTICALLY DOWN AND NOT ALONG THE AXIS OF THE PILE, WHICH MAY BE BATTERED.   
(25-30) IF THIS DATA IS BEING USED FOR ADHESION, ENTER THE DISTANCE TO THE BOTTOM OF THIS STRATUM. IF THIS DATA IS BEING USED FOR T-Z AXIAL, ENTER THE DISTANCE FROM THE PILEHEAD TO BOTTOM OF THIS STRATUM IF THE T-Z DATA IS TO BE CONSTANT FOR THIS STRATUM. IF LEFT BLANK, THE T-Z DATA WILL VARY LINEARLY TO THE TOP OF THE NEXT STRATUM. NO GAPS SHOULD BE LEFT BETWEEN STRATA.   
(32-35) ENTER THE SOIL TYPE. SELECT FROM AMONG THE FOLLOWING:



| SOIL TYPE | API DESCRIPTION | FRICION ANGLE | LIMITING FRICION | BEARING FACTOR | LIMITING BEARING |
| --- | --- | --- | --- | --- | --- |
| 'GRAV' - | GRAVEL | 35.0 | 2.4 | 50.0 | 250.0 |
| 'SAND' - | DENSE SAND | 30.0 | 2.0 | 40.0 | 200.0 |
| 'SLN' - | DENSE SAND-SILT | 25.0 | 1.7 | 20.0 | 100.0 |
| 'SNSL' - | MEDIUM SAND-SILT | 20.0 | 1.4 | 12.0 | 60.0 |
| 'SILT' - | MEDIUM SILT | 15.0 | 1.0 | 8.0 | 40.0 |



COLUMNS

COMMENTARY

(36-41) ENTER THE COEFFICIENT OF LATERAL EARTH PRESSURE.   
(42-47) ENTER THE LIMITING END BEARING VALUE IF THE DEFAULT IS NOT ACCEPTABLE.   
(48-53) ENTER THE SUBMERGED UNIT WEIGHT.   
(54-59) ENTER THE FRICTION ANGLE IF THE DEFAULT IS NOT ACCEPTABLE.   
(60-65) ENTER THE BEARING CAPACITY FACTOR IF THE DEFAULT IS NOT ACCEPTABLE.   
(66-71) ENTER THE OVERBURDEN PRESSURE IF THE INTERNALLY CALCULATED VALUE IS NOT ACCEPTABLE.   
(72-77) ENTER THE LIMITING SKIN FRICTION VALUE IF THE DEFAULT IS NOT ACCEPTABLE.   
(78-80) ENTER ZPEAK RATIO TO PILE DIAMETER (ONLY FOR API 22ND EDITION). ZPEAK IS THE DISPLACEMENT TO MAXIMUM SOIL PILE ADHESION OR UNIT SKIN FRICTION (ONLY FOR API RP 22ND EDITION) A DEFAULT VALUE FOR ZPEAK OF 1% OF THE PILE OUTER DIAMETER IS RECOMMENDED BY API 22ND EDITION. HOWEVER, THE VALUE MAY VARY FROM 0.25 TO



| LINE LABEL | AUTOMATIC AXIAL RESISTANCE GENERATION | API EDITION SELECTION | LINE TYPE | TOP OF STRATUM | BOTTOM OF STRATUM | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | ZPEAK RATIO TO PILE DIAMETER (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | AUTOMATIC AXIAL RESISTANCE GENERATION | API EDITION SELECTION | LINE TYPE | TOP OF STRATUM | BOTTOM OF STRATUM | SOIL TYPE | COEFF. OF LATERAL EARTH PRESSURE | LIMITING END BEARING CAP. | SUBMERGED DENSITY | FRICTION ANGLE | BEARING CAPACITY FACTOR | OVER-BURDEN PRESSURE | LIMITING SKIN FRICTION | ZPEAK RATIO TO PILE DIAMETER (%) |
| SOIL | API AXL |  | SLOC |  |  |  |  |  |  |  |  |  |  |  |
| 1--4 | 6--12 | 13 | 14--17 | 19<--24 | 25<--30 | 32--35 | 36<--41 | 42<--47 | 48<--53 | 54<--59 | 60<--65 | 66<--71 | 72<--77 | 78<--80 |
| DEFAULT |  | 20TH |  |  |  |  | 1 | ABOVE |  | ABOVE | ABOVE |  | ABOVE | 1 |
| ENGLISH |  |  |  | FT | FT |  |  | KIP/SQ.FT | LB/CU.FT | DEG |  | KIP/SQ.FT | KIP/SQ.FT |  |
| METRIC (KN) |  |  |  | M | M |  |  | KN/SQ.CM | TONNE/CU.M | DEG |  | KN/SQ.CM | KN/SQ.CM |  |
| METRIC (KG) |  |  |  | M | M |  |  | KG/SQ.CM | TONNE/CU.M | DEG |  | KG/SQ.CM | KG/SQ.CM |  |



SOIL AXIAL ADHESION HEADER LINE

COLUMNS

COMMENTARY

COLUMNS

COMMENTARY

GENERAL

THIS LINE AND THE 'SLOC' LINE ARE USED TO MODEL THE AXIAL LOAD TRANSFER TO THE SOIL BY ADHESION. AN AXIAL ADHESION CAPACITY IS SPECIFIED AT THE TOP AND BOTTOM OF EACH SOIL STRATUM. IF THE VALUES ARE DIFFERENT AN AVERAGE IS USED. STARTING AT THE TOP STRATUM THE LENGTH OVER WHICH THE ADHESION MUST ACT IN ORDER TO TRANSFER THE PILE AXIAL LOAD IS COMPUTED. IF THIS LENGTH IS LESS THAN THE THICKNESS OF THAT STRATUM THE AXIAL LOAD IS COMPLETELY TRANSFERRED TO THE SOIL OVER THAT LENGTH. IF THE COMPUTED LENGTH IS GREATER THAN THE THICKNESS OF THE STRATUM THE AXIAL IS ONLY PARTIALLY TRANSFERRED IN THAT STRATUM. THE EXCESS PILE LOAD IS TRANSFERRED IN THE NEXT DEEPER SOIL STRATUM. THE PROCEDURE IS REPEATED FOR EACH SOIL STRATUM IN TURN UNTIL THE ENTIRE AXIAL LOAD IS TRANSFERRED OR UNTIL ALL SOIL STRATA HAVE REACHED THEIR CAPACITIES. ANY EXCESS AXIAL LOAD IS THEN TRANSFERRED BY END BEARING UNTIL THE BEARING CAPACITY IS REACHED. IF THE TOTAL PILE AXIAL LOAD HAS NOT THEN BEEN TRANSFERRED THE PILE LOAD EXCEEDS ITS CAPACITY AND IT FAILS, A REPORT TO THIS EFFECT IS ISSUED.

THIS SOIL MODEL TAKES NO ACCOUNT OF SOIL DEFORMATIONS IN THE AXIAL DIRECTION. THE AXIAL DISPLACEMENT AT THE PILEHEAD IS TAKEN TO BE EQUAL TO THE COMPRESSIVE (OR TENSILE) DEFORMATION OF THE PILE.

( 1- 4) ENTER 'SOIL'.   
( 6-10) ENTER 'AXIAL'.   
(14-17) ENTER 'HEAD'.   
(18-20) ENTER THE NUMBER OF SOIL STRATA TO BE DESCRIBED FOR ADHESION SOIL DATA.   
(21-30) ENTER THE END BEARING CAPACITY FOR THIS SOIL TABLE.   
(41-44) ENTER AN ALPHANUMERIC SOIL TABLE IDENTIFIER. THIS IDENTIFIER IS USED ON ONE OR MORE 'PILE' LINES TO ASSOCIATE THESE AXIAL SOIL PROPERTIES WITH THOSE PILES.   
(45-60) ENTER ANY DESCRIPTIVE REMARKS FOR THIS AXIAL SOIL DATA.   
(62-64) ENTER THE METHOD TO BE USED IN CONJUNCTION WITH CPT STRATA.

SELECT FROM THE FOLLOWING:

'ICP' - SIMPLIFIED ICP-05.   
'UWA' - OFFSHORE UWA-05.   
'FUG' - FUGRO-05.   
'NGI' - NGI-05.

(66-71) ENTER THE DIAMETER OF THE CONE PENETRATION TOOL FOR CPT STRATA.



| LINE LABEL | AXIAL LABEL | HEAD LABEL | NUMBER OF SOIL STRATA | END BEARING CAPACITY | SOIL TABLE ID | SOIL DESCRIPTION OR OTHER REMARKS | CPT METHOD | CPT TOOL DIAMETER | LEAVE BLANK |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOIL | AXIAL | HEAD |  |  |  |  |  |  |  |
| 1--4 | 6--10 | 14--17 | 18--->20 | 21<--30 | 41<--44 | 45----60 | 62--64 | 66--71 | 72--80 |
| DEFAULT |  |  |  |  |  |  | 'ICP' | 36mm |  |
| ENGLISH |  |  |  | KIP/SQ.FT |  |  |  | IN |  |
| METRIC (KN) |  |  |  | KN/SQ.CM |  |  |  | CM |  |
| METRIC (KG) |  |  |  | KG/SQ.CM |  |  |  | CM |  |



SOIL (CLAY) API AXIAL STRATUM LINE

COLUMNS

COMMENTARY

GENERAL THIS LINE SET IS USED TO SPECIFY THE SOIL PROPERTIES FOR EACHCLAY STRATUM. THE PROGRAM WILL USE THESE PROPERTIES TOCALCULATE AXIAL ADHESION AND BEARING CAPACITIES OR T-Z AXIALAND Q-Z END BEARING CURVES.

( 1- 4) ENTER 'SOIL'.   
( 6-12) ENTER 'API AXL'.   
( 13 ) IF THE API RP2A 10TH EDITION SOIL PROPERTIES ARE DESIRED ENTER A '1' HERE. OTHERWISE, LEAVE BLANK.   
(14-17) ENTER 'SLOC'.   
(19-24) ENTER THE DISTANCE FROM THE PILEHEAD TO THE TOP OF THIS SOIL STRATUM. THIS DISTANCE IS VERTICALLY DOWN AND NOT ALONG THE AXIS OF THE PILE, WHICH MAY BE BATTERED.   
(25-30) IF THIS DATA IS BEING USED FOR ADHESION, ENTER THE DISTANCE TO THE BOTTOM OF THIS STRATUM. IF THIS DATA IS BEING USED FOR T-Z AXIAL, ENTER THE DISTANCE FROM THE PILEHEAD TO BOTTOM OF THIS STRATUM IF THE T-Z DATA IS TO BE CONSTANT FOR THIS STRATUM. IF LEFT BLANK, THE T-Z DATA WILL VARY LINEARLY TO THE TOP OF THE NEXT STRATUM. NO GAPS SHOULD BE LEFT BETWEEN STRATA.   
(32-35) ENTER THE SOIL TYPE. SELECT FROM AMONG THE FOLLOWING:

'CLAY' - NORMAL.

'CLOC' - OVER-CONSOLIDATED GULF OF MEXICO CLAY (API 10TH ONLY).

'CLUC' - UNDER-CONSOLIDATED GULF OF MEXICO CLAY (API 10TH ONLY).

COLUMNS

COMMENTARY

(36-41) ENTER THE UNDRAINED SHEAR STRENGTH.   
(48-53) ENTER THE SUBMERGED UNIT WEIGHT.   
(66-71) ENTER THE OVERBURDEN PRESSURE IF THE INTERNALLY CALCULATED VALUE IS NOT ACCEPTABLE.   
(72-77) ENTER THE SOIL RESIDUAL FACTOR ( Tres / Tmax).  
(78-80) ENTER ZPEAK RATIO TO PILE DIAMETER (ONLY FOR API 22ND EDITION). ZPEAK IS THE DISPLACEMENT TO MAXIMUM SOIL PILE ADHESION OR UNIT SKIN FRICTION (ONLY FOR API RP 22ND EDITION) A DEFAULT VALUE FOR ZPEAK OF 1% OF THE PILE OUTER DIAMETER IS RECOMMENDED BY API 22ND EDITION. HOWEVER, THE VALUE MAY VARY FROM 0.25 TO



| LINE LABEL | AUTOMATIC AXIAL RESISTANCE GENERATION | API EDITION SELECTION | LINE TYPE | TOP OF STRATUM | BOTTOM OF STRATUM | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | ZPEAK RATIO TO PILE DIAMETER (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | AUTOMATIC AXIAL RESISTANCE GENERATION | API EDITION SELECTION | LINE TYPE | TOP OF STRATUM | BOTTOM OF STRATUM | SOIL TYPE | UNDRAINED SHEAR STRENGTH | SUBMERGED DENSITY | OVER- BURDEN PRESSURE | RESIDUAL FACTOR | ZPEAK RATIO TO PILE DIAMETER (%) |
| SOIL | API AXL |  | SLOC |  |  |  |  |  |  |  |  |
| 1--4 | 6--12 | 13 | 14--17 | 19<--24 | 25<--30 | 32--35 | 36<--41 | 48<--53 | 66<--71 | 72<--77 | 78<--80 |
| DEFAULT |  | 20TH |  |  |  |  |  |  |  | 0.7 | 1 |
| ENGLISH |  |  |  | FT | FT |  | KIP/SQ.FT | LB/CU.FT | KIP/SQ.FT |  |  |
| METRIC (KN) |  |  |  | M | M |  | KN/SQ.CM | TONNE/CU.M | KN/SQ.CM |  |  |
| METRIC (KG) |  |  |  | M | M |  | KG/SQ.CM | TONNE/CU.M | KG/SQ.CM |  |  |



SOIL (CPT) API AXIAL STRATUM LINE

COLUMNS

COMMENTARY

GENERAL THIS LINE SET IS USED TO SPECIFY THE SOIL PROPERTIES FOR EACHCPT STRATUM. THE PROGRAM WILL USE THESE PROPERTIES TOCALCULATE AXIAL ADHESION AND BEARING CAPACITIES OR T-Z AXIALAND Q-Z END BEARING CURVES.

( 1- 4) ENTER 'SOIL'.   
( 6-12) ENTER 'API AXL'.   
(14-17) ENTER 'SLOC'.   
(19-24) ENTER THE DISTANCE FROM THE PILEHEAD TO THE TOP OF THIS SOIL STRATUM. THIS DISTANCE IS VERTICALLY DOWN AND NOT ALONG THE AXIS OF THE PILE, WHICH MAY BE BATTERED.   
(25-30) IF THIS DATA IS BEING USED FOR ADHESION, ENTER THE DISTANCE TO THE BOTTOM OF THIS STRATUM. IF THIS DATA IS BEING USED FOR T-Z AXIAL, ENTER THE DISTANCE FROM THE PILEHEAD TO BOTTOM OF THIS STRATUM IF THE T-Z INPUT DATA ARE TO BE CONSTANT FOR THIS STRATUM. IF LEFT BLANK, THE T-Z INPUT DATA WILL VARY LINEARLY TO THE TOP OF THE NEXT STRATUM. NO GAPS SHOULD BE LEFT BETWEEN STRATA.   
(32-34) ENTER 'CPT'

COLUMNS

COMMENTARY

(36-41) ENTER THE COEFFICIENT OF LATERAL EARTH PRESSURE.   
(42-47) ENTER THE CONE TIP RESISTANCE FOR THE TOP OF THE STRATUM.   
(48-53) ENTER THE SUBMERGED DENSITY.   
(54-59) ENTER THE CONSTANT VOLUME INTERFACE FRICTION ANGLE FOR THE TOP OF THE STRATUM IF THE DEFAULT IS NOT ACCEPTABLE.   
(78-80) ENTER ZPEAK RATIO TO PILE DIAMETER (ONLY FOR API 22ND EDITION). ZPEAK IS THE DISPLACEMENT TO MAXIMUM SOIL PILE ADHESION OR UNIT SKIN FRICTION (ONLY FOR API RP 22ND EDITION) A DEFAULT VALUE FOR ZPEAK OF 1% OF THE PILE OUTER DIAMETER IS RECOMMENDED BY API 22ND EDITION. HOWEVER, THE VALUE MAY VARY FROM 0.25 TO



| LINE LABEL | AUTOMATIC AXIAL RESISTANCE GENERATION | API EDITION SELECTION | LINE TYPE | TOP OF STRATUM | BOTTOM OF STRATUM | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | ZPEAK RATIO TO PILE DIAMETER (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | AUTOMATIC AXIAL RESISTANCE GENERATION | API EDITION SELECTION | LINE TYPE | TOP OF STRATUM | BOTTOM OF STRATUM | SOIL TYPE | COEFF. OF LATERAL EARTH PRESSURE | CONE TIP RESISTANCE | SUBMERGED DENSITY | INTERFACE FRICTION ANGLE | LEAVE BLANK | ZPEAK RATIO TO PILE DIAMETER (%) |
| SOIL | API AXL |  | SLOC |  |  | CPT |  |  |  |  |  |  |
| 1--4 | 6--12 | 13 | 14--17 | 19<--24 | 25<--30 | 32--34 | 36<--41 | 42<--47 | 48<--53 | 54<--59 | 60--77 | 78<--80 |
| DEFAULT |  | 21ST |  |  |  |  | 1 |  |  | 28.8 |  | 1 |
| ENGLISH |  |  |  | FT | FT | CPT |  | KSI. | LB/CU.FT | DEG |  |  |
| METRIC (KN) |  |  |  | M | M | CPT |  | MPa | TONNE/CU.M | DEG |  |  |
| METRIC (KG) |  |  |  | M | M | CPT |  | KG/SQ.MM | TONNE/CU.M | DEG |  |  |



SOIL (ROCK) API AXIAL STRATUM LINE

COLUMNS

COMMENTARY

GENERAL THIS LINE SET IS USED TO SPECIFY THE SOIL PROPERTIES FOR EACHROCK STRATUM. THE PROGRAM WILL USE THESE PROPERTIES TOCALCULATE AXIAL ADHESION AND BEARING CAPACITIES OR T-Z AXIALAND Q-Z END BEARING CURVES.

( 1- 4) ENTER 'SOIL'.   
( 6-12) ENTER 'API AXL'.   
( 13 ) IF THE API RP2A 10TH EDITION SOIL PROPERTIES ARE DESIRED ENTER A '1' HERE. OTHERWISE, LEAVE BLANK.   
(14-17) ENTER 'SLOC'.   
(19-24) ENTER THE DISTANCE FROM THE PILEHEAD TO THE TOP OF THIS SOIL STRATUM. THIS DISTANCE IS VERTICALLY DOWN AND NOT ALONG THE AXIS OF THE PILE, WHICH MAY BE BATTERED.   
(25-30) IF THIS DATA IS BEING USED FOR ADHESION, ENTER THE DISTANCE TO THE BOTTOM OF THIS STRATUM. IF THIS DATA IS BEING USED FOR T-Z AXIAL, ENTER THE DISTANCE FROM THE PILEHEAD TO BOTTOM OF THIS STRATUM IF THE T-Z DATA IS TO BE CONSTANT FOR THIS STRATUM. IF LEFT BLANK, THE T-Z DATA WILL VARY LINEARLY TO THE TOP OF THE NEXT STRATUM. NO GAPS SHOULD BE LEFT BETWEEN STRATA.   
(32-35) ENTER THE SOIL TYPE OF 'ROCK'.

COLUMNS

COMMENTARY

(36-41) ENTER THE UNIT SKIN FRICTION CAPACITY.   
(42-47) ENTER THE BEARING CAPACITY.   
(48-53) ENTER THE SUBMERGED UNIT WEIGHT.   
(78-80) ENTER ZPEAK RATIO TO PILE DIAMETER (ONLY FOR API 22ND EDITION). ZPEAK IS THE DISPLACEMENT TO MAXIMUM SOIL PILE ADHESION OR UNIT SKIN FRICTION (ONLY FOR API RP 22ND EDITION) A DEFAULT VALUE FOR ZPEAK OF 1% OF THE PILE OUTER DIAMETER IS RECOMMENDED BY API 22ND EDITION. HOWEVER, THE VALUE MAY VARY FROM 0.25 TO



| LINE LABEL | AUTOMATIC AXIAL RESISTANCE GENERATION | API EDITION SELECTION | LINE TYPE | TOP OF STRATUM | BOTTOM OF STRATUM | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | LEAVE BLANK | ZPEAK RATIO TO PILE DIAMETER (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | AUTOMATIC AXIAL RESISTANCE GENERATION | API EDITION SELECTION | LINE TYPE | TOP OF STRATUM | BOTTOM OF STRATUM | SOIL TYPE | UNIT SKIN FRICTION CAPACITY | BEARING CAPACITY | SUBMERGED DENSITY | LEAVE BLANK | ZPEAK RATIO TO PILE DIAMETER (%) |
| SOIL | API AXL |  | SLOC |  |  |  |  |  |  |  |  |
| 1--4 | 6--12 | 13 | 14--17 | 19<--24 | 25<--30 | 32--35 | 36<--41 | 42<--47 | 48<--53 | 54<--77 | 78--80 |
| DEFAULT |  | 20TH |  |  |  |  |  |  |  |  | 1 |
| ENGLISH |  |  |  | FT | FT |  | KIP/SQ.FT | KIP/SQ.FT | LB/CU.FT |  |  |
| METRIC (KN) |  |  |  | M | M |  | KN/SQ.CM | KN/SQ.CM | TONNE/CU.M |  |  |
| METRIC (KG) |  |  |  | M | M |  | KG/SQ.CM | KG/SQ.CM | TONNE/CU.M |  |  |



SOIL (SAND) API AXIAL STRATUM LINE

COLUMNS

COMMENTARY

GENERAL THIS LINE SET IS USED TO SPECIFY THE SOIL PROPERTIES FOR EACHSAND STRATUM. THE PROGRAM WILL USE THESE PROPERTIES TOCALCULATE AXIAL ADHESION AND BEARING CAPACITIES OR T-Z AXIALAND Q-Z END BEARING CURVES.

( 1- 4) ENTER 'SOIL'.   
( 6-12) ENTER 'API AXL'.   
( 13 ) IF THE API RP2A 10TH EDITION SOIL PROPERTIES ARE DESIRED ENTER A '1' HERE. OTHERWISE, LEAVE BLANK.   
(14-17) ENTER 'SLOC'.   
(19-24) ENTER THE DISTANCE FROM THE PILEHEAD TO THE TOP OF THIS SOIL STRATUM. THIS DISTANCE IS VERTICALLY DOWN AND NOT ALONG THE AXIS OF THE PILE, WHICH MAY BE BATTERED.   
(25-30) IF THIS DATA IS BEING USED FOR ADHESION, ENTER THE DISTANCE TO THE BOTTOM OF THIS STRATUM. IF THIS DATA IS BEING USED FOR T-Z AXIAL, ENTER THE DISTANCE FROM THE PILEHEAD TO BOTTOM OF THIS STRATUM IF THE T-Z DATA IS TO BE CONSTANT FOR THIS STRATUM. IF LEFT BLANK, THE T-Z DATA WILL VARY LINEARLY TO THE TOP OF THE NEXT STRATUM. NO GAPS SHOULD BE LEFT BETWEEN STRATA.   
(32-35) ENTER THE SOIL TYPE. SELECT FROM AMONG THE FOLLOWING:



| SOIL TYPE | API DESCRIPTION | FRICION ANGLE | LIMITING FRICION | BEARING FACTOR | LIMITING BEARING |
| --- | --- | --- | --- | --- | --- |
| 'GRAV' - | GRAVEL | 35.0 | 2.4 | 50.0 | 250.0 |
| 'SAND' - | DENSE SAND | 30.0 | 2.0 | 40.0 | 200.0 |
| 'SLN' - | DENSE SAND-SILT | 25.0 | 1.7 | 20.0 | 100.0 |
| 'SNSL' - | MEDIUM SAND-SILT | 20.0 | 1.4 | 12.0 | 60.0 |
| 'SILT' - | MEDIUM SILT | 15.0 | 1.0 | 8.0 | 40.0 |



COLUMNS

COMMENTARY

(36-41) ENTER THE COEFFICIENT OF LATERAL EARTH PRESSURE.   
(42-47) ENTER THE LIMITING END BEARING VALUE IF THE DEFAULT IS NOT ACCEPTABLE.   
(48-53) ENTER THE SUBMERGED UNIT WEIGHT.   
(54-59) ENTER THE FRICTION ANGLE IF THE DEFAULT IS NOT ACCEPTABLE.   
(60-65) ENTER THE BEARING CAPACITY FACTOR IF THE DEFAULT IS NOT ACCEPTABLE.   
(66-71) ENTER THE OVERBURDEN PRESSURE IF THE INTERNALLY CALCULATED VALUE IS NOT ACCEPTABLE.   
(72-77) ENTER THE LIMITING SKIN FRICTION VALUE IF THE DEFAULT IS NOT ACCEPTABLE.   
(78-80) ENTER ZPEAK RATIO TO PILE DIAMETER (ONLY FOR API 22ND EDITION). ZPEAK IS THE DISPLACEMENT TO MAXIMUM SOIL PILE ADHESION OR UNIT SKIN FRICTION (ONLY FOR API RP 22ND EDITION) A DEFAULT VALUE FOR ZPEAK OF 1% OF THE PILE OUTER DIAMETER IS RECOMMENDED BY API 22ND EDITION. HOWEVER, THE VALUE MAY VARY FROM 0.25 TO



| LINE LABEL | AUTOMATIC AXIAL RESISTANCE GENERATION | API EDITION SELECTION | LINE TYPE | TOP OF STRATUM | BOTTOM OF STRATUM | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | ZPEAK RATIO TO PILE DIAMETER (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | AUTOMATIC AXIAL RESISTANCE GENERATION | API EDITION SELECTION | LINE TYPE | TOP OF STRATUM | BOTTOM OF STRATUM | SOIL TYPE | COEFF. OF LATERAL EARTH PRESSURE | LIMITING END BEARING CAP. | SUBMERGED DENSITY | FRICTION ANGLE | BEARING CAPACITY FACTOR | OVER-BURDEN PRESSURE | LIMITING SKIN FRICTION | ZPEAK RATIO TO PILE DIAMETER (%) |
| SOIL | API AXL |  | SLOC |  |  |  |  |  |  |  |  |  |  |  |
| 1--4 | 6--12 | 13 | 14--17 | 19<--24 | 25<--30 | 32--35 | 36<--41 | 42<--47 | 48<--53 | 54<--59 | 60<--65 | 66<--71 | 72<--77 | 78<--80 |
| DEFAULT |  | 20TH |  |  |  |  | 1 | ABOVE |  | ABOVE | ABOVE |  | ABOVE | 1 |
| ENGLISH |  |  |  | FT | FT |  |  | KIP/SQ.FT | LB/CU.FT | DEG |  | KIP/SQ.FT | KIP/SQ.FT |  |
| METRIC (KN) |  |  |  | M | M |  |  | KN/SQ.CM | TONNE/CU.M | DEG |  | KN/SQ.CM | KN/SQ.CM |  |
| METRIC (KG) |  |  |  | M | M |  |  | KG/SQ.CM | TONNE/CU.M | DEG |  | KG/SQ.CM | KG/SQ.CM |  |



SOIL T-Z API AXIAL HEADER LINE

COLUMNS

COMMENTARY

GENERAL

THIS LINE IS USED TO SPECIFY THE NUMBER OF SOIL STRATA AND THE SOIL IDENTIFIER FOR A T-Z AXIAL SOIL DESCRIPTION. IT IS FOLLOWED BY SOIL STRATUM LINES.

A T-Z API AXIAL SOIL DESCRIPTION ACCOUNTS FOR SOIL DEFORMATION RESULTING FROM THE TRANSFER OF PILE AXIAL LOAD TO THE SOIL THROUGH THE ACTION OF SHEAR FORCES BETWEEN THE PILE LATERAL SURFACE AND THE SURROUNDING SOIL. THIS DATA SET WILL AUTOMATICALLY GENERATE THE T-Z DATA AND THE END BEARING Q-Z DATA ACCORDING TO THE API RP2A 20TH AND 21ST EDITIONS.

THE SEQUENCE OF LINES REQUIRED FOR A T-Z SOIL DESCRIPTION ISAS FOLLOWS:

1. THIS SOIL T-Z API AXIAL HEADER LINE.   
2. SOIL API AXL RECORD FOR EACH STRATUM.

COLUMNS

COMMENTARY

( 1- 4) ENTER 'SOIL'.   
( 6-10) ENTER 'TZAPI'.   
(14-17) ENTER 'HEAD'.   
(18-20) ENTER THE NUMBER OF SOIL STRATA FOR THIS T-Z DESCRIPTION.   
(21-27) ENTER THE EFFECTIVE PILE LENGTH. ONLY NEEDED FOR THE KOLK AND VAN DER VELDE OVERRIDE FOR CLAY STRATA.   
(28-33) ENTER A FACTOR THAT WILL SCALE THE API-GENERATED T-VALUES.   
(34-40) ENTER A FACTOR THAT WILL SCALE THE API-GENERATED Z-VALUES.   
(41-44) ENTER A SOIL TABLE IDENTIFIER. THIS IDENTIFIER IS USED ON ONE OR MORE 'PILE' LINES TO ASSOCIATE THIS SOIL TABLE WITH THOSE PILES.   
(45-60) ENTER ANY DESCRIPTIVE COMMENTS DESIRED.   
(62-64) ENTER THE METHOD TO BE USED IN CONJUNCTION WITH CPT STRATA. SELECT FROM THE FOLLOWING:

'ICP' - SIMPLIFIED ICP-05.   
'UWA' - OFFSHORE UWA-05.   
'FUG' - FUGRO-05.   
'NGI' - NGI-05.

(66-71) ENTER THE DIAMETER OF THE CONE PENETRATION TOOL FOR CPT STRATA.   
(73-73) ENTER 'K' IN ORDER TO OVERRIDE THE SKIN FRICTION CALCULATION FOR CLAY BY USING THE KOLK AND VAN DER VELDE METHOD.   
(75-80) ENTER AN EFFECTIVE PILE OD. ONLY NEEDED FOR THE KOLK AND VAN DER VELDE OVERRIDE FOR CLAY STRATA.



| LINE LABEL | T-Z AXIAL LABEL | HEAD LABEL | NUMBER OF SOIL STRATA | EFFECTIVE PILE LENGTH | T FACTOR | Z FACTOR | SOIL TABLE ID | SOIL DESCRIPTION OR OTHER REMARKS | CPT METHOD | CPT TOOL DIAMETER | KOLK VD VELDE OVERRIDE | KOLK VD VELDE PILE OD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOIL | TZAPI | HEAD |  |  |  |  |  |  |  |  |  |  |
| 1--4 | 6--10 | 14--17 | 18-->20 | 21--27 | 28--33 | 34--40 | 41--44 | 45--60 | 62--64 | 66--71 | 73 | 75--80 |
| DEFAULT |  |  |  |  |  |  |  |  |  |  |  |  |
| ENGLISH |  |  |  | FT |  |  |  |  |  | IN |  | IN |
| METRIC |  |  |  | M |  |  |  |  |  | CM |  | CM |



PILEHEAD AXIAL SPRING LINE

COLUMNS

COMMENTARY

GENERAL

THIS LINE IS USED IF THE PILE AXIAL BEHAVIOR IS TO BE MODELED AS A LINEAR SPRING AT THE PILEHEAD. FOR THE SUBSEQUENT LATERAL SOLUTION, THE INTERNAL AXIAL FORCE IN THE PILE IS ASSUMED TO VARY LINEARLY FROM THE PILEHEAD AXIAL LOAD TO ZERO AT THE BOTTOM OF THE PILE. IF THIS LINE IS USED, THEN NO OTHER SOIL AXIAL OR BEARING LINES ARE USED.

( 1- 4) ENTER 'SOIL'.   
( 6-10) ENTER 'AXIAL'.   
(14-17) ENTER 'HEAD'.   
(31-40) ENTER THE LINEAR STIFFNESS VALUE FOR THE PILEHEAD SPRING.   
(41-44) ENTER AN ALPHANUMERIC SOIL TABLE IDENTIFIER. THIS IDENTIFIER IS USED ON ONE OR MORE 'PILE' LINES TO ASSOCIATE THIS SPRING WITH PARTICULAR PILES.   
(45-60) ENTER ANY DESCRIPTIVE REMARKS.



| LINE LABEL | AXIAL LABEL | HEAD LABEL | LINEAR STIFFNESS VALUE | SOIL TABLE ID | REMARKS | LEAVE BLANK |
| --- | --- | --- | --- | --- | --- | --- |
| SOIL | AXIAL | HEAD |  |  |  |  |
| 1--4 | 6--10 | 14--17 | 31<--40 | 41<--44 | 45----60 | 61--80 |
| DEFAULT |  |  |  |  |  |  |
| ENGLISH |  |  | KIP/IN |  |  |  |
| METRIC (KN) |  |  | KN/M |  |  |  |
| METRIC (KG) |  |  | KG/CM |  |  |  |



SOIL AXIAL ADHESION STRATA LINE

COLUMNS

COMMENTARY

LOCATION THIS LINE SET FOLLOWS THE ADHESION HEADER LINE AND ISFOLLOWED BY SOIL ADHESION CAPACITY LINE.

GENERAL THE ADHESION SOIL STRATA LOCATIONS ARE DEFINED USING THIS LINE. THESE STRATA LOCATIONS ARE MEASURED FROM THE PILEHEAD. FIVE STRATA ARE INPUT PER LINE AND THIS LINE TYPE IS REPEATED UNTIL THE NUMBER OF STRATA DESIGNATED ON THE SOIL AXIAL HEAD LINE HAVE BEEN DESCRIBED.

( 1- 4) ENTER 'SOIL'.   
( 6- 9) ENTER 'ADHA'.   
(14-17) ENTER 'SLOC'.   
(19-78) ENTER THE DISTANCES FROM THE PILEHEAD TO THE TOP AND BOTTOM OF EACH STRATUM. THE LOCATION OF THE BOTTOM OF THE LAST STRATUM ENTERED MUST BE AT LEAST TO THE BOTTOM OF THE DEEPEST PILE TO WHICH THIS TABLE APPLIES. THE LOCATION OF THE TOP OF A STRATUM MUST BE THE SAME AS THE BOTTOM OF THE PRECEDING STRATUM. THESE DISTANCES ARE VERTICALLY DOWN AND NOT ALONG THE AXIS OF THE PILE, WHICH MAY BE BATTERED.



| LINE LABEL | AXIAL ADHESION | LINE TYPE | AXIAL ADHESION STRATA LOCATIONS | AXIAL ADHESION STRATA LOCATIONS | AXIAL ADHESION STRATA LOCATIONS | AXIAL ADHESION STRATA LOCATIONS | AXIAL ADHESION STRATA LOCATIONS | AXIAL ADHESION STRATA LOCATIONS | AXIAL ADHESION STRATA LOCATIONS | AXIAL ADHESION STRATA LOCATIONS | AXIAL ADHESION STRATA LOCATIONS | AXIAL ADHESION STRATA LOCATIONS |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | AXIAL ADHESION | LINE TYPE | 1ST STRATUM | 1ST STRATUM | 2ND STRATUM | 2ND STRATUM | 3RD STRATUM | 3RD STRATUM | 4TH STRATUM | 4TH STRATUM | 5TH STRATUM | 5TH STRATUM |
| LINE LABEL | AXIAL ADHESION | LINE TYPE | TOP | BOTTOM | TOP | BOTTOM | TOP | BOTTOM | TOP | BOTTOM | TOP | BOTTOM |
| SOIL | ADHA | SLOC |  |  |  |  |  |  |  |  |  |  |
| 1-- 4 | 6-- 9 | 14--17 | 19<--24 | 25<--30 | 31<--36 | 37<--42 | 43<--48 | 49<--54 | 55<--60 | 61<--66 | 67<--72 | 73<--78 |
| DEFAULT |  |  |  |  |  |  |  |  |  |  |  |  |
| ENGLISH |  |  | FT | FT | FT | FT | FT | FT | FT | FT | FT | FT |
| METRIC |  |  | M | M | M | M | M | M | M | M | M | M |



SOIL AXIAL ADHESION CAPACITY LINE

COLUMNS

COMMENTARY

LOCATION THIS LINE FOLLOWS THE SOIL LOCATION LINES FOR ADHESION DATA.

GENERAL THIS LINE SET IS USED TO ENTER THE AXIAL ADHESION CAPACITIES FOR THE TOP AND BOTTOM OF EACH STRATUM DEFINED BY THE SOIL ADHESION STRATA LINES. THE ADHESION CAPACITY IS CONSTANT WITHIN A STRATUM AND EQUALS THE AVERAGE OF THE VALUES INPUT AT ITS TOP AND BOTTOM.

( 1- 4) ENTER 'SOIL'.   
( 6- 9) ENTER 'ADHA'.   
(14-16) ENTER 'EXT' IF THE VALUES ENTERED ON THIS LINE ARE FOR ADHESION ON THE EXTERIOR SURFACE OF THE PILE. ENTER 'INT' IF THE VALUES ENTERED ARE FOR ADHESION ON THE INTERIOR SURFACE OF THE PILE. IF LEFT BLANK THE VALUES WILL BE FOR BOTH THE EXTERIOR AND INTERIOR SURFACES. IF DATA IS INPUT FOR EXTERIOR ADHESION AND NOT FOR INTERIOR ADHESION THEN THERE WILL BE NO INTERIOR ADHESION AND VICE VERSA.   
( 17 ) ENTER 'C' IF THE VALUES ENTERED ON THIS LINE ARE FOR RESISTING COMPRESSION IN THE PILE AND 'T' IF FOR RESISTING PILE TENSION. IF LEFT BLANK THEN THESE VALUES WILL APPLY TO EITHER PILE TENSION OR COMPRESSION.   
(19-78) ENTER THE ADHESION CAPACITIES AT THE TOP AND BOTTOM OF EACH STRATUM. IF MORE THAN FIVE STRATA ARE USED, REPEAT THIS LINE UNTIL ALL STRATA ARE DEFINED.



| LINE LABEL | AXIAL ADHESION | EXTERNAL OR INTERNAL ADHESION | TENSION OR COMPRESSION RESISTANCE | SOIL AXIAL ADHESION CAPACITIES | SOIL AXIAL ADHESION CAPACITIES | SOIL AXIAL ADHESION CAPACITIES | SOIL AXIAL ADHESION CAPACITIES | SOIL AXIAL ADHESION CAPACITIES | SOIL AXIAL ADHESION CAPACITIES | SOIL AXIAL ADHESION CAPACITIES | SOIL AXIAL ADHESION CAPACITIES | SOIL AXIAL ADHESION CAPACITIES | SOIL AXIAL ADHESION CAPACITIES |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | AXIAL ADHESION | EXTERNAL OR INTERNAL ADHESION | TENSION OR COMPRESSION RESISTANCE | 1ST STRATUM | 1ST STRATUM | 2ND STRATUM | 2ND STRATUM | 3RD STRATUM | 3RD STRATUM | 4TH STRATUM | 4TH STRATUM | 5TH STRATUM | 5TH STRATUM |
| LINE LABEL | AXIAL ADHESION | EXTERNAL OR INTERNAL ADHESION | TENSION OR COMPRESSION RESISTANCE | TOP | BOTTOM | TOP | BOTTOM | TOP | BOTTOM | TOP | BOTTOM | TOP | BOTTOM |
| SOIL | ADHA |  |  |  |  |  |  |  |  |  |  |  |  |
| 1-- 4 | 6-- 9 | 14--16 | 17 | 19<--24 | 25<--30 | 31<--36 | 37<--42 | 43<--48 | 49<--54 | 55<--60 | 61<--66 | 67<--72 | 73<--78 |
| DEFAULT |  | BOTH | BOTH |  |  |  |  |  |  |  |  |  |  |
| ENGLISH |  |  |  | KIP/SQ.FT | KIP/SQ.FT | KIP/SQ.FT | KIP/SQ.FT | KIP/SQ.FT | KIP/SQ.FT | KIP/SQ.FT | KIP/SQ.FT | KIP/SQ.FT | KIP/SQ.FT |
| METRIC (KN) |  |  |  | KN/SQ.CM | KN/SQ.CM | KN/SQ.CM | KN/SQ.CM | KN/SQ.CM | KN/SQ.CM | KN/SQ.CM | KN/SQ.CM | KN/SQ.CM | KN/SQ.CM |
| METRIC (KG) |  |  |  | KG/SQ.CM | KG/SQ.CM | KG/SQ.CM | KG/SQ.CM | KG/SQ.CM | KG/SQ.CM | KG/SQ.CM | KG/SQ.CM | KG/SQ.CM | KG/SQ.CM |



SOIL AXIAL ADHESION HEADER LINE

COLUMNS

COMMENTARY

COLUMNS

COMMENTARY

GENERAL

THIS LINE AND THE 'SLOC' LINE ARE USED TO MODEL THE AXIAL LOAD TRANSFER TO THE SOIL BY ADHESION. AN AXIAL ADHESION CAPACITY IS SPECIFIED AT THE TOP AND BOTTOM OF EACH SOIL STRATUM. IF THE VALUES ARE DIFFERENT AN AVERAGE IS USED. STARTING AT THE TOP STRATUM THE LENGTH OVER WHICH THE ADHESION MUST ACT IN ORDER TO TRANSFER THE PILE AXIAL LOAD IS COMPUTED. IF THIS LENGTH IS LESS THAN THE THICKNESS OF THAT STRATUM THE AXIAL LOAD IS COMPLETELY TRANSFERRED TO THE SOIL OVER THAT LENGTH. IF THE COMPUTED LENGTH IS GREATER THAN THE THICKNESS OF THE STRATUM THE AXIAL IS ONLY PARTIALLY TRANSFERRED IN THAT STRATUM. THE EXCESS PILE LOAD IS TRANSFERRED IN THE NEXT DEEPER SOIL STRATUM. THE PROCEDURE IS REPEATED FOR EACH SOIL STRATUM IN TURN UNTIL THE ENTIRE AXIAL LOAD IS TRANSFERRED OR UNTIL ALL SOIL STRATA HAVE REACHED THEIR CAPACITIES. ANY EXCESS AXIAL LOAD IS THEN TRANSFERRED BY END BEARING UNTIL THE BEARING CAPACITY IS REACHED. IF THE TOTAL PILE AXIAL LOAD HAS NOT THEN BEEN TRANSFERRED THE PILE LOAD EXCEEDS ITS CAPACITY AND IT FAILS, A REPORT TO THIS EFFECT IS ISSUED.

THIS SOIL MODEL TAKES NO ACCOUNT OF SOIL DEFORMATIONS IN THE AXIAL DIRECTION. THE AXIAL DISPLACEMENT AT THE PILEHEAD IS TAKEN TO BE EQUAL TO THE COMPRESSIVE (OR TENSILE) DEFORMATION OF THE PILE.

( 1- 4) ENTER 'SOIL'.   
( 6-10) ENTER 'AXIAL'.   
(14-17) ENTER 'HEAD'.   
(18-20) ENTER THE NUMBER OF SOIL STRATA TO BE DESCRIBED FOR ADHESION SOIL DATA.   
(21-30) ENTER THE END BEARING CAPACITY FOR THIS SOIL TABLE.   
(41-44) ENTER AN ALPHANUMERIC SOIL TABLE IDENTIFIER. THIS IDENTIFIER IS USED ON ONE OR MORE 'PILE' LINES TO ASSOCIATE THESE AXIAL SOIL PROPERTIES WITH THOSE PILES.   
(45-60) ENTER ANY DESCRIPTIVE REMARKS FOR THIS AXIAL SOIL DATA.   
(62-64) ENTER THE METHOD TO BE USED IN CONJUNCTION WITH CPT STRATA.

SELECT FROM THE FOLLOWING:

'ICP' - SIMPLIFIED ICP-05.   
'UWA' - OFFSHORE UWA-05.   
'FUG' - FUGRO-05.   
'NGI' - NGI-05.

(66-71) ENTER THE DIAMETER OF THE CONE PENETRATION TOOL FOR CPT STRATA.



| LINE LABEL | AXIAL LABEL | HEAD LABEL | NUMBER OF SOIL STRATA | END BEARING CAPACITY | SOIL TABLE ID | SOIL DESCRIPTION OR OTHER REMARKS | CPT METHOD | CPT TOOL DIAMETER | LEAVE BLANK |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOIL | AXIAL | HEAD |  |  |  |  |  |  |  |
| 1--4 | 6--10 | 14--17 | 18--->20 | 21<--30 | 41<--44 | 45----60 | 62--64 | 66--71 | 72--80 |
| DEFAULT |  |  |  |  |  |  | 'ICP' | 36mm |  |
| ENGLISH |  |  |  | KIP/SQ.FT |  |  |  | IN |  |
| METRIC (KN) |  |  |  | KN/SQ.CM |  |  |  | CM |  |
| METRIC (KG) |  |  |  | KG/SQ.CM |  |  |  | CM |  |



SOIL T-Z AXIAL STRATUM LOCATION LINE

COLUMNS

COMMENTARY

GENERAL

THIS LINE IS USED FOR EACH STRATUM TO SPECIFY WHETHER THE T-Z CURVE IS SYMMETRICAL, THE NUMBER OF POINTS DEFINING IT, THE LOCATIONS OF THE TOP AND BOTTOM OF THE STRATUM AND TO ENTER A T FACTOR FOR MULTIPLYING THE T VALUES ENTERED ON THE FOLLOWING T-Z LINE.

THE T-Z STRATA LOCATIONS NEED NOT COINCIDE WITH THE P-Y STRATA LOCATIONS.

( 1- 4) ENTER 'SOIL'.   
(14-17) ENTER 'SLOC'.   
(18-19) ENTER 'SM' IF THE T-Z CURVE FOR THIS STRATUM HAS THE SAME SHAPE WHETHER THE PILE IS IN TENSION OR COMPRESSION. IF 'SM' IS ENTERED THEN THE FOLLOWING T-Z LINES FOR THIS STRATUM MUST HAVE ENTRIES ONLY FOR POSITIVE T AND Z VALUES. THE ORIGIN, T=0, Z=0, MUST BE THE FIRST POINT ENTERED IN THIS CASE.   
(22-23) ENTER THE NUMBER OF POINTS ON THE FOLLOWING T-Z CURVE. ONE POINT CONSISTS OF A T VALUE AND A Z VALUE. THE NUMBER ENTERED HERE MAY NOT BE GREATER THAN THE VALUE ENTERED IN COLUMNS 22-23 OF THE T-Z AXIAL HEADER LINE ('SOIL TZAXIAL HEAD' LINE SET) OR 30 IF THOSE COLUMNS ARE BLANK.   
(25-30) ENTER THE DISTANCE FROM THE PILEHEAD TO THE TOP OF THIS STRATUM. THE STRATUM AND T-Z LINES ARE ENTERED IN ORDER OF INCREASING DEPTH. THESE DISTANCES ARE VERTICALLY DOWN AND NOT ALONG THE AXIS OF THE PILE, WHICH MAY BE BATTERED. THE FIRST POINT NEED NOT BE AT THE PILEHEAD.   
(31-36) IF THE FOLLOWING T-Z DATA IS CONSTANT FOR THIS STRATUM, ENTER THE DISTANCE FROM THE PILEHEAD TO THE BOTTOM OF THIS STRATUM. IF LEFT BLANK, THE T-Z DATA WILL VARY LINEARLY TO THE TOP OF THE NEXT STRATUM. NO GAPS SHOULD BE LEFT BETWEEN STRATA.   
(39-44) T ON THE T-Z LINES FOR THIS STRATUM WILL BE MULTIPLIED BY THIS VALUE. THIS ENTRY CAN BE USED TO CHANGE INPUT INTO MORE CONVENIENT UNITS IF DESIRED.   
(45-60) ENTER ANY DESCRIPTIVE REMARKS DESIRED.



| LINE LABEL | LINE TYPE | SYMMETRICAL T-Z CURVE | NUMBER OF POINTS PER CURVE | STRATUM LOCATION | STRATUM LOCATION | T FACTOR | SOIL STRATUM DESCRIPTION | LEAVE BLANK |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | LINE TYPE | SYMMETRICAL T-Z CURVE | NUMBER OF POINTS PER CURVE | TOP | BOTTOM | T FACTOR | SOIL STRATUM DESCRIPTION | LEAVE BLANK |
| SOIL | SLOC |  |  |  |  |  |  |  |
| 1-- 4 | 14--17 | 18--19 | 22--->23 | 25<--30 | 31<--36 | 39<--44 | 45<----60 | 61--80 |
| DEFAULT |  |  |  |  |  | 1 |  |  |
| ENGLISH |  |  |  | FT | FT |  |  |  |
| METRIC |  |  |  | M | M |  |  |  |



SOIL T-Z LINE

COLUMNS

COMMENTARY

GENERAL THIS LINE IS USED TO ENTER THE T-Z DATA FOR THE SOIL STRATUM DEFINED ON THE IMMEDIATELY PRECEDING STRATUM LOCATION LINE. THE NUMBER OF POINTS ENTERED MUST BE THE SAME AS SPECIFIED IN COLUMNS 22-23 OF THAT LINE. FOR A SYMMETRICAL T-Z CURVE ('SM' IN COLUMNS 18-19 OF THE STRATUM LOCATION LINE) ONLY POINTS HAVING POSITIVE T AND Z VALUES SHOULD BE ENTERED AND THE FIRST POINT MUST BE T=0, Z=0. UP TO 5 POINTS PER LINE MAY BE ENTERED AND AS MANY LINES AS NECESSARY MAY BE ENTERED. FOR VALUES OF Z GREATER THAN THE LAST ENTERED VALUE THE PROGRAM USES THE LAST ENTERED T VALUE, THAT IS, THE CURVE IS FLAT.

( 1- 4) ENTER 'SOIL'.   
(14-16) ENTER 'T-Z'.   
(18-77) ENTER THE T-Z DATA FOR THIS STRATUM.



| LINE LABEL | LINE TYPE | T-Z CURVE DATA POINTS | T-Z CURVE DATA POINTS | T-Z CURVE DATA POINTS | T-Z CURVE DATA POINTS | T-Z CURVE DATA POINTS | T-Z CURVE DATA POINTS | T-Z CURVE DATA POINTS | T-Z CURVE DATA POINTS | T-Z CURVE DATA POINTS | T-Z CURVE DATA POINTS | LEAVE BLANK |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | LINE TYPE | 1ST POINT | 1ST POINT | 2ND POINT | 2ND POINT | 3RD POINT | 3RD POINT | 4TH POINT | 4TH POINT | 5TH POINT | 5TH POINT | LEAVE BLANK |
| LINE LABEL | LINE TYPE | T | Z | T | Z | T | Z | T | Z | T | Z | LEAVE BLANK |
| SOIL | T-Z |  |  |  |  |  |  |  |  |  |  |  |
| 1-- 4 | 14--16 | 18<--23 | 24<--29 | 30<--35 | 36<--41 | 42<--47 | 48<--53 | 54<--59 | 60<--65 | 66<--71 | 72<--77 | 78--80 |
| DEFAULT |  |  |  |  |  |  |  |  |  |  |  |  |
| ENGLISH |  | KSI | IN | KSI | IN | KSI | IN | KSI | IN | KSI | IN |  |
| METRIC (KN) |  | KN/SQ.CM | CM | KN/SQ.CM | CM | KN/SQ.CM | CM | KN/SQ.CM | CM | KN/SQ.CM | CM |  |
| METRIC (KG) |  | KG/SQ.CM | CM | KG/SQ.CM | CM | KG/SQ.CM | CM | KG/SQ.CM | CM | KG/SQ.CM | CM |  |



SOIL T-Z AXIAL HEADER LINE

COLUMNS

COMMENTARY

GENERAL

THIS LINE IS USED TO SPECIFY THE NUMBER OF SOIL STRATA, THE MAXIMUM NUMBER OF POINTS DEFINING THE T-Z CURVES AND THE SOIL IDENTIFIER FOR A T-Z AXIAL SOIL DESCRIPTION.

A T-Z AXIAL SOIL DESCRIPTION ACCOUNTS FOR SOIL DEFORMATION RESULTING FROM THE TRANSFER OF PILE AXIAL LOAD TO THE SOIL THROUGH THE ACTION OF SHEAR FORCES BETWEEN THE PILE LATERAL SURFACE AND THE SURROUNDING SOIL.

THE SEQUENCE OF LINES REQUIRED FOR A T-Z SOIL DESCRIPTION ISAS FOLLOWS:

1. THIS SOIL T-Z AXIAL HEADER LINE.   
2. AN AXIAL STRATUM LOCATION LINE FOR THE UPPERMOST STRATUM.

3. ONE OR MORE T-Z LINES FOR THE UPPERMOST STRATUM.   
4. AN AXIAL STRATUM LOCATION LINE FOR THE SECOND STRATUM.

5. T-Z LINES FOR THE SECOND STRATUM.ETC.

COLUMNS

COMMENTARY

( 1- 4) ENTER 'SOIL'.   
( 6-12) ENTER 'TZAXIAL'.   
(14-17) ENTER 'HEAD'.   
(18-20) ENTER THE NUMBER OF SOIL STRATA FOR THIS T-Z DESCRIPTION.   
(22-23) IF ANY T-Z CURVE ENTERED IS DEFINED AT MORE THAN 30 POINTS ENTER THAT NUMBER HERE. OTHERWISE, LEAVE BLANK.   
(28-33) ENTER THE FACTOR TO BE APPLIED TO ALL T INPUT VALUES.   
(34-40) ENTER THE FACTOR TO BE APPLIED TO ALL Z INPUT VALUES.   
(41-44) ENTER A SOIL TABLE IDENTIFIER. THIS IDENTIFIER IS USED ON ONE OR MORE 'PILE' LINES TO ASSOCIATE THIS SOIL TABLE WITH THOSE PILES.   
(45-60) ENTER ANY DESCRIPTIVE COMMENTS DESIRED.



| LINE LABEL | T-Z AXIAL LABEL | HEAD LABEL | NUMBER OF SOIL STRATA | MORE THAN 30 DATA POINTS FOR T-Z CURVE | T FACTOR | Z FACTOR | SOIL TABLE ID | SOIL DESCRIPTION OR OTHER REMARKS | LEAVE BLANK |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOIL | TZAXIAL | HEAD |  |  |  |  |  |  |  |
| 1--4 | 6--12 | 14--17 | 18--->20 | 22--->23 | 28<--33 | 34<--40 | 41--44 | 45-----60 | 61--80 |
| DEFAULT |  |  |  |  | 1 | 1 |  |  |  |



SOIL BM-T BASE MOMENT HEADER LINE

COLUMNS

COMMENTARY

GENERAL THIS LINE FOLLOWED BY 'SLOC' LINES IS USED TO MODEL PILE ENDBASE MOMENT ACCOUNTING FOR THE RESILIENCE OF THE SOIL.

THIS LINE SETS UP THE GENERAL PARAMETERS AND TABLE IDENTIFICATION FOR THE BASE MOMENT BM-T DATA. THE BASE MOMENT LINE ORDER IS AS FOLLOWS:

1. THIS SOIL BASE MOMENT HEADER LINE.   
2. A SOIL BASE MOMENT STRATUM LINE.   
3. ONE OR MORE BASE MOMENT BM-T LINES.

ONLY ONE BASE MOMENT SOIL REACTION CURVE IS EXPECTED.

COLUMNS

COMMENTARY

( 1- 4) ENTER 'SOIL'.   
( 6-12) ENTER 'BASEMOM'.   
(14-17) ENTER 'HEAD'.   
(22-23) IF ANY BM-T CURVE ENTERED ('SOIL BM-T' LINE) IS DEFINED AT MORE THAN 30 POINTS, ENTER THAT NUMBER HERE. OTHERWISE, LEAVE BLANK.   
(28-33) ENTER THE FACTOR TO BE APPLIED TO ALL "MOMENT" INPUT VALUES.   
(34-40) ENTER THE FACTOR TO BE APPLIED TO ALL "THETA" INPUT VALUES.   
(41-44) ENTER THE UNIQUE ALPHANUMERIC SOIL TABLE IDENTIFIER. THIS IDENTIFIER IS USED ON ONE OR MORE 'PILE' LINES TO ASSOCIATE THIS TABLE WITH THOSE PILES.   
(45-51) ENTER THE DIAMETER FOR WHICH THIS BM-T DATA IS GENERATED. THE INPUT "MOMENT" VALUES WILL BE MULTIPLIED BY THE RATIO OF THE PILE DIAMETER TO THIS REFERENCE DIAMETER.   
(52-67) ENTER ANY DESCRIPTIVE COMMENTS DESIRED.



| LINE LABEL | BASE MOMENT LABEL | HEAD LABEL | MORE THAN 30 DATA POINTS FOR T-Z CURVE | BASE MOMENT FACTOR | DISP. FACTOR | SOIL TABLE ID | REFERENCE PILE DIAMETER | SOIL TABLE DESCRIPTION | LEAVE BLANK |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOIL | BASEMOM | HEAD |  |  |  |  |  |  |  |
| 1--4 | 6--12 | 14--17 | 22--->23 | 28--->33 | 34--->40 | 41<--44 | 45--->51 | 45-----60 | 61--80 |
| DEFAULT |  |  |  | 1 | 1 |  |  |  |  |



SOIL BM-T BASE MOMENT STRATUM LINE

COLUMNS

COMMENTARY

GENERAL THIS LINE IS USED FOR EACH SOIL STRATUM TO SPECIFY THE NUMBER OF POINTS ON THE BM-T BASE MOMNENT CURVE, AND IF THE BM-T CURVE IS SYMMETRICAL.

( 1- 4) ENTER 'SOIL'.   
(14-17) ENTER 'SLOC'.   
(18-19) ENTER 'SM' IF THE SOIL BM-T CURVE IS THE SAME IN THE POSITIVE AND NEGATIVE DISPLACEMENT DIRECTIONS. IN THIS CASE ONLY POSITIVE VALUES OF MOMENT AND THETA WILL BE ENTERED ON THE FOLLOWING BM-T LINES ('SOIL BM-T' LINE SET). THE ORIGIN (MOMENT=0.0, DISP.=0.0) MUST BE THE FIRST POINT ENTERED ON THAT LINE.   
(22-23) ENTER THE NUMBER OF POINTS ON THE FOLLOWING BM-T CURVE. ONE POINT CONSISTS OF A MOMENT VALUE AND A THETA VALUE. THE NUMBER ENTERED HERE MAY NOT BE GREATER THAN THE VALUE ENTERED IN COLUMNS 22-23 OF THE BASE MOMENT HEADER LINE ('SOIL BASEMOM'HEAD' LINE SET) OR 30 IF THOSE COLUMNS ARE BLANK.   
(45-60) ENTER ANY DESCRIPTIVE REMARKS ABOUT THIS SOIL STRATUM.



| LINE LABEL | LINE TYPE | SYMMETRY INDICATOR | NUMBER OF POINTS PER CURVE | SOIL STRATUM DESCRIPTION | LEAVE BLANK |
| --- | --- | --- | --- | --- | --- |
| SOIL | SLOC |  |  |  |  |
| 1--4 | 14--17 | 18--19 | 22--->23 | 45----60 | 61--80 |
| DEFAULT |  |  |  |  |  |
| ENGLISH |  |  |  |  |  |
| METRIC |  |  |  |  |  |



SOIL BM-T BASE MOMENT DATA LINE

COLUMNS

COMMENTARY

GENERAL THIS LINE SET IS USED TO INPUT THE BASE MOMENT BM-T DATA FOR THE SOIL STRATUM DEFINED ON THE IMMEDIATELY PRECEDING STRATUM LOCATION LINE. THE NUMBER OF POINTS ENTERED MUST BE THE SAME AS SPECIFIED IN COLUMNS 22-23 OF THAT LINE. THIS LINE MAY BE REPEATED AS REQUIRED UNTIL ALL POINTS ON THE STRATUM ARE DEFINED.

( 1- 4) ENTER 'SOIL'.   
(14-16) ENTER 'BM-T'.   
(18-77) ENTER THE POINTS ON THE BASE MOMENT VERSUS THETA CURVE FOR THIS STRATUM.



| LINE LABEL | LINE TYPE | BM-T CURVE DATA POINTS | BM-T CURVE DATA POINTS | BM-T CURVE DATA POINTS | BM-T CURVE DATA POINTS | BM-T CURVE DATA POINTS | BM-T CURVE DATA POINTS | BM-T CURVE DATA POINTS | BM-T CURVE DATA POINTS | BM-T CURVE DATA POINTS | BM-T CURVE DATA POINTS |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | LINE TYPE | 1ST ENTRY | 1ST ENTRY | 2ND ENTRY | 2ND ENTRY | 3RD ENTRY | 3RD ENTRY | 4TH ENTRY | 4TH ENTRY | 5TH ENTRY | 5TH ENTRY |
| LINE LABEL | LINE TYPE | MOMENT | THETA | MOMENT | THETA | MOMENT | THETA | MOMENT | THETA | MOMENT | THETA |
| SOIL | BM-T |  |  |  |  |  |  |  |  |  |  |
| 1--4 | 14--17 | 18<--23 | 24<--29 | 30<--35 | 36<--41 | 42<--47 | 48<--53 | 54<--59 | 60<--65 | 66<--71 | 72<--77 |
| DEFAULT |  |  |  |  |  |  |  |  |  |  |  |
| ENGLISH |  | IN-KIP | RAD | IN-KIP | RAD | IN-KIP | RAD | IN-KIP | RAD | IN-KIP | RAD |
| METRIC (KN) |  | KN-M | RAD | KN-M | RAD | KN-M | RAD | KN-M | RAD | KN-M | RAD |
| METRIC (KG) |  | KG-CM | RAD | KG-CM | RAD | KG-CM | RAD | KG-CM | RAD | KG-CM | RAD |



SOIL BH-V BASE SHEAR HEADER LINE

COLUMNS

COMMENTARY

GENERAL THIS LINE FOLLOWED BY 'SLOC' LINES IS USED TO MODEL PILE ENDBASE SHEAR ACCOUNTING FOR THE RESILIENCE OF THE SOIL.

THIS LINE SETS UP THE GENERAL PARAMETERS AND TABLE IDENTIFICATION FOR THE BASE SHEAR BH-V DATA. THE BASE SHEAR LINE ORDER IS AS FOLLOWS:

1. THIS SOIL BASE SHEAR HEADER LINE.   
2. A SOIL BASE SHEAR STRATUM LINE.   
3. ONE OR MORE BASE SHEAR BH-V LINES.

ONLY ONE BASE SHEAR SOIL REACTION CURVE IS EXPECTED.

COLUMNS

COMMENTARY

( 1- 4) ENTER 'SOIL'.   
( 6-12) ENTER 'BASESHR'.   
(14-17) ENTER 'HEAD'.   
(22-23) IF ANY BH-V CURVE ENTERED ('SOIL BH-V' LINE) IS DEFINED AT MORE THAN 30 POINTS, ENTER THAT NUMBER HERE. OTHERWISE, LEAVE BLANK.   
(28-33) ENTER THE FACTOR TO BE APPLIED TO ALL "SHEAR" INPUT VALUES.   
(34-40) ENTER THE FACTOR TO BE APPLIED TO ALL "DISP." INPUT VALUES.   
(41-44) ENTER THE UNIQUE ALPHANUMERIC SOIL TABLE IDENTIFIER. THIS IDENTIFIER IS USED ON ONE OR MORE 'PILE' LINES TO ASSOCIATE THIS TABLE WITH THOSE PILES.   
(45-51) ENTER THE DIAMETER FOR WHICH THIS BH-V DATA IS GENERATED. THE INPUT "SHEAR" VALUES WILL BE MULTIPLIED BY THE RATIO OF THE PILE DIAMETER TO THIS REFERENCE DIAMETER.   
(52-67) ENTER ANY DESCRIPTIVE COMMENTS DESIRED.



| LINE LABEL | BASE SHEAR LABEL | HEAD LABEL | MORE THAN 30 DATA POINTS FOR T-Z CURVE | BASE SHEAR FACTOR | DISP. FACTOR | SOIL TABLE ID | REFERENCE PILE DIAMETER | SOIL TABLE DESCRIPTION | LEAVE BLANK |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOIL | BASESHR | HEAD |  |  |  |  |  |  |  |
| 1--4 | 6--12 | 14--17 | 22--->23 | 28--->33 | 34--->40 | 41<--44 | 45--->51 | 45-----60 | 61--80 |
| DEFAULT |  |  |  | 1 | 1 |  |  |  |  |



SOIL BM-T BASE MOMENT STRATUM LINE

COLUMNS

COMMENTARY

GENERAL THIS LINE IS USED FOR EACH SOIL STRATUM TO SPECIFY THE NUMBER OF POINTS ON THE BM-T BASE MOMNENT CURVE, AND IF THE BM-T CURVE IS SYMMETRICAL.

( 1- 4) ENTER 'SOIL'.   
(14-17) ENTER 'SLOC'.   
(18-19) ENTER 'SM' IF THE SOIL BM-T CURVE IS THE SAME IN THE POSITIVE AND NEGATIVE DISPLACEMENT DIRECTIONS. IN THIS CASE ONLY POSITIVE VALUES OF MOMENT AND THETA WILL BE ENTERED ON THE FOLLOWING BM-T LINES ('SOIL BM-T' LINE SET). THE ORIGIN (SHEAR=0.0, DISP.=0.0) MUST BE THE FIRST POINT ENTERED ON THAT LINE.   
(22-23) ENTER THE NUMBER OF POINTS ON THE FOLLOWING BM-T CURVE. ONE POINT CONSISTS OF A MOMENT VALUE AND A THETA VALUE. THE NUMBER ENTERED HERE MAY NOT BE GREATER THAN THE VALUE ENTERED IN COLUMNS 22-23 OF THE BASE MOMENT HEADER LINE ('SOIL BASEMOM'HEAD' LINE SET) OR 30 IF THOSE COLUMNS ARE BLANK.   
(45-60) ENTER ANY DESCRIPTIVE REMARKS ABOUT THIS SOIL STRATUM.



| LINE LABEL | LINE TYPE | SYMMETRY INDICATOR | NUMBER OF POINTS PER CURVE | SOIL STRATUM DESCRIPTION | LEAVE BLANK |
| --- | --- | --- | --- | --- | --- |
| SOIL | SLOC |  |  |  |  |
| 1--4 | 14--17 | 18--19 | 22--->23 | 45----60 | 61--80 |
| DEFAULT |  |  |  |  |  |
| ENGLISH |  |  |  |  |  |
| METRIC |  |  |  |  |  |



SOIL BH-V BASE SHEAR DATA LINE

COLUMNS

COMMENTARY

GENERAL THIS LINE SET IS USED TO INPUT THE BASE SHEAR BH-V DATA FORTHE SOIL STRATUM DEFINED ON THE IMMEDIATELY PRECEDINGSTRATUM LOCATION LINE. THE NUMBER OF POINTS ENTERED MUST BETHE SAME AS SPECIFIED IN COLUMNS 22-23 OF THAT LINE. THISLINE MAY BE REPEATED AS REQUIRED UNTIL ALL POINTS ON THESTRATUM ARE DEFINED.

( 1- 4) ENTER 'SOIL'.   
(14-16) ENTER 'BH-V'.   
(18-77) ENTER THE POINTS ON THE BASE SHEAR VERSUS DISPLACEMENT CURVE FOR THIS STRATUM.



| LINE LABEL | LINE TYPE | BH-V CURVE DATA POINTS | BH-V CURVE DATA POINTS | BH-V CURVE DATA POINTS | BH-V CURVE DATA POINTS | BH-V CURVE DATA POINTS | BH-V CURVE DATA POINTS | BH-V CURVE DATA POINTS | BH-V CURVE DATA POINTS | BH-V CURVE DATA POINTS | BH-V CURVE DATA POINTS |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | LINE TYPE | 1ST ENTRY | 1ST ENTRY | 2ND ENTRY | 2ND ENTRY | 3RD ENTRY | 3RD ENTRY | 4TH ENTRY | 4TH ENTRY | 5TH ENTRY | 5TH ENTRY |
| LINE LABEL | LINE TYPE | SHEAR | DISP. | SHEAR | DISP. | SHEAR | DISP. | SHEAR | DISP. | SHEAR | DISP. |
| SOIL | BH-V |  |  |  |  |  |  |  |  |  |  |
| 1-- 4 | 14--17 | 18<--23 | 24<--29 | 30<--35 | 36<--41 | 42<--47 | 48<--53 | 54<--59 | 60<--65 | 66<--71 | 72<--77 |
| DEFAULT |  |  |  |  |  |  |  |  |  |  |  |
| ENGLISH |  | KIP | IN | KIP | IN | KIP | IN | KIP | IN | KIP | IN |
| METRIC (KN) |  | KN | CM | KN | CM | KN | CM | KN | CM | KN | CM |
| METRIC (KG) |  | KG | CM | KG | CM | KG | CM | KG | CM | KG | CM |



SOIL T-Z END BEARING STRATUM LINE

COLUMNS

COMMENTARY

GENERAL THIS LINE IS USED FOR EACH SOIL STRATUM TO SPECIFY THE NUMBER OF POINTS ON THE T-Z END BEARING CURVE, THE LOCATIONS OF THE TOP AND BOTTOM OF THE STRATUM, AND TO ENTER A T FACTOR FOR MULTIPLYING THE T VALUES ENTERED ON THE FOLLOWING T-Z LINE ('SOIL T-Z' END BEARING LINE SET).

( 1- 4) ENTER 'SOIL'.   
(14-17) ENTER 'SLOC'.   
(22-23) ENTER THE NUMBER OF POINTS ON THE FOLLOWING T-Z CURVE. ONE POINT CONSISTS OF A T VALUE AND A Z VALUE. THE NUMBER ENTERED HERE MAY NOT BE GREATER THAN THE VALUE ENTERED IN COLUMNS 22-23 OF THE BEARING HEADER LINE ('SOIL BEARING HEAD' LINE SET) OR 30 IF THOSE COLUMNS ARE BLANK.   
(25-30) ENTER THE DISTANCE FROM THE PILEHEAD TO THE TOP OF THIS SOIL STRATUM. THIS DISTANCE IS VERTICALLY DOWN AND NOT ALONG THE AXIS OF THE PILE, WHICH MAY BE BATTERED.   
(31-36) ENTER THE DISTANCE FROM THE PILEHEAD TO THE BOTTOM OF THESOIL STRATUM IF THE T-Z DATA IS CONSTANT THROUGHOUT THISSTRATUM. IF LEFT BLANK, THE T-Z DATA WILL VARY LINEARLY TOTHE TOP OF THE NEXT STRATUM. FOR THE LAST STRATUM THE BOTTOMDISTANCE SHOULD BE ENTERED AS SOME VALUE DEEPER THAN THE PILETIP (TAKING PILE BATTER INTO ACCOUNT).  
(39-44) ENTER THE T FACTOR FOR THIS T-Z CURVE. THIS FACTOR IS USED TO MODIFY THE T VALUES INPUT FOR THIS SOIL STRATUM. IT IS INDEPENDENT OF THE T FACTOR ENTERED ON THE 'PLGRUP' LINES. THIS FACTOR MAY BE USED IN CONJUNCTION WITH NORMALIZED T-Z CURVES TO OBTAIN THE CORRECT T MAGNITUDES OR IT MAY BE USED FOR UNIT CONVERSIONS.   
(45-60) ENTER ANY DESCRIPTIVE REMARKS ABOUT THIS SOIL STRATUM.



| LINE LABEL | LINE TYPE | NUMBER OF POINTS PER CURVE | STRATUM LOCATION | STRATUM LOCATION | T FACTOR | SOIL STRATUM DESCRIPTION | LEAVE BLANK |
| --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | LINE TYPE | NUMBER OF POINTS PER CURVE | TOP | BOTTOM | T FACTOR | SOIL STRATUM DESCRIPTION | LEAVE BLANK |
| SOIL | SLOC |  |  |  |  |  |  |
| 1--4 | 14--17 | 22--->23 | 25<--30 | 31<--36 | 39<--44 | 45----60 | 61--80 |
| DEFAULT |  |  |  |  | 1 |  |  |
| ENGLISH |  |  | FT | FT |  |  |  |
| METRIC |  |  | M | M |  |  |  |



SOIL T-Z END BEARING HEADER LINE

COLUMNS

COMMENTARY

GENERAL

THIS LINE FOLLOWED BY 'SLOC' LINES IS USED TO MODEL PILE END BEARING ACCOUNTING FOR THE RESILIENCE OF THE SOIL. THE T-Z BEARING DATA MAY BE ENTERED FOR BOTH POSITIVE (BEARING) AND NEGATIVE (SUCTION) VALUES OF FORCE AND DISPLACEMENT. IF ONLY POSITIVE VALUES ARE ENTERED, THEN THE SUCTION RESISTANCE IS ZERO FOR ALL NEGATIVE DISPLACEMENTS. FOR VALUES OF Z GREATER THAN THE LAST VALUE ENTERED, THE VALUE OF T IS TAKEN TO BE THE LAST ENTERED VALUE AND SIMILARLY FOR THE FIRST, I.E. THE CURVE IS EXTRAPOLATED FLAT AT BOTH ENDS. IN ORDER TO USE THESE LINES THE SOIL AXIAL BEHAVIOR MUST BE MODELED WITH T-Z DATA ('SOIL BEARING HEAD', 'SOIL SLOC', AND 'SOIL T-Z' LINES). THIS LINE WILL THEN FOLLOW THOSE T-Z AXIAL LINES. THIS LINE SETS UP THE GENERAL PARAMETERS AND TABLE IDENTIFICATION FOR THE END BEARING T-Z DATA. THE END BEARING LINE ORDER IS AS FOLLOWS:

THIS SOIL BEARING HEADER LINE.

SOIL END BEARING STRATUM LINE FOR 1ST STRATUM.

SOIL END BEARING T-Z LINES FOR 1ST STRATUM.

SOIL END BEARING STRATUM LINE FOR 2ND STRATUM.

SOIL END BEARING T-Z LINES FOR 2ND STRATUM.

ETC.

COLUMNS

COMMENTARY

( 1- 4) ENTER 'SOIL'.   
( 6-12) ENTER 'BEARING'.   
(14-17) ENTER 'HEAD'.   
(18-20) ENTER THE NUMBER OF SOIL STRATA FOR THIS END BEARING T-Z DESCRIPTION. DO NOT LEAVE THIS FIELD BLANK. THE PROGRAM PERMITS END BEARING TO BE SPECIFIED AT SEVERAL POINTS ALONG THE PILE SO THAT STEPPED PILES CAN BE MODELED. IN THE USUAL CASE, END BEARING WILL ONLY EXIST AT THE PILE TIP. IN THIS CASE IT IS ONLY NECESSARY TO ENTER ONE STRATUM WHICH WILL INCLUDE THE PILE TIP.   
(22-23) IF ANY T-Z CURVE ENTERED ('SOIL T-Z' LINE) IS DEFINED AT MORE THAN 30 POINTS, ENTER THAT NUMBER HERE. OTHERWISE, LEAVE BLANK.   
(34-40) ENTER THE FACTOR TO BE APPLIED TO ALL "Z" INPUT VALUES.   
(41-44) ENTER THE UNIQUE ALPHANUMERIC SOIL TABLE IDENTIFIER. THIS IDENTIFIER IS USED ON ONE OR MORE 'PILE' LINES TO ASSOCIATE THIS TABLE WITH THOSE PILES.   
(45-60) ENTER ANY DESCRIPTIVE COMMENTS DESIRED.



| LINE LABEL | BEARING LABEL | HEAD LABEL | NUMBER OF SOIL STRATA | MORE THAN 30 DATA POINTS FOR T-Z CURVE | Z FACTOR | SOIL TABLE ID | SOIL TABLE DESCRIPTION | LEAVE BLANK |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOIL | BEARING | HEAD |  |  |  |  |  |  |
| 1--4 | 6--12 | 14--17 | 18--->20 | 22--->23 | 34<--40 | 41<--44 | 45-----60 | 61--80 |
| DEFAULT |  |  |  |  | 1 |  |  |  |



SOIL T-Z END BEARING DATA LINE

COLUMNS

COMMENTARY

GENERAL THIS LINE SET IS USED TO INPUT THE END BEARING T-Z DATA FOREACH SOIL STRATUM DEFINED ON THE IMMEDIATELY PRECEDINGSTRATUM LOCATION LINE. THE NUMBER OF POINTS ENTERED MUST BETHE SAME AS SPECIFIED IN COLUMNS 22-23 OF THAT LINE. THISLINE MAY BE REPEATED AS REQUIRED UNTIL ALL STRATA ARE DEFINED.

( 1- 4) ENTER 'SOIL'.   
(14-16) ENTER 'T-Z'.   
(18-77) ENTER THE POINTS ON THE BEARING PRESSURE (T) VERSUS DISPLACEMENT (Z) CURVE FOR THIS STRATUM.



| LINE LABEL | LINE TYPE | T-Z CURVE DATA POINTS | T-Z CURVE DATA POINTS | T-Z CURVE DATA POINTS | T-Z CURVE DATA POINTS | T-Z CURVE DATA POINTS | T-Z CURVE DATA POINTS | T-Z CURVE DATA POINTS | T-Z CURVE DATA POINTS | T-Z CURVE DATA POINTS | T-Z CURVE DATA POINTS |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | LINE TYPE | 1ST ENTRY | 1ST ENTRY | 2ND ENTRY | 2ND ENTRY | 3RD ENTRY | 3RD ENTRY | 4TH ENTRY | 4TH ENTRY | 5TH ENTRY | 5TH ENTRY |
| LINE LABEL | LINE TYPE | T | Z | T | Z | T | Z | T | Z | T | Z |
| SOIL | T-Z |  |  |  |  |  |  |  |  |  |  |
| 1-- 4 | 14--16 | 18<--23 | 24<--29 | 30<--35 | 36<--41 | 42<--47 | 48<--53 | 54<--59 | 60<--65 | 66<--71 | 72<--77 |
| DEFAULT |  |  |  |  |  |  |  |  |  |  |  |
| ENGLISH |  | KSI | IN | KSI | IN | KSI | IN | KSI | IN | KSI | IN |
| METRIC (KN) |  | KN/SQ.CM | CM | KN/SQ.CM | CM | KN/SQ.CM | CM | KN/SQ.CM | CM | KN/SQ.CM | CM |
| METRIC (KG) |  | KG/SQ.CM | CM | KG/SQ.CM | CM | KG/SQ.CM | CM | KG/SQ.CM | CM | KG/SQ.CM | CM |



SOIL BENDING HEADER LINE

COLUMNS

COMMENTARY

GENERAL

THIS LINE AND THE SOIL LOCATION AND M-T LINES ARE USED TO MODEL RESILIENT BEHAVIOR OF THE SOIL SUBJECT TO MOMENTS EXERTED ALONG THE LENGTH OF THE PILE.

MOMENT DATA IS INPUT AS MOMENT PER UNIT LENGTH ALONG A PILE OF SPECIFIED REFERENCE DIAMETER (COLUMNS 45-51).

THIS LINE IS USED TO SPECIFY PARAMETERS DEFINING THE SOILROTATIONAL STIFFNESS. THE ORDER OF LINES FOR M-T DATA INPUT IS:

1. THIS BENDING HEADER LINE.   
2. A MOMENT STRATUM LINE ('SOIL SLOC' LINE SET) FOR THE FIRST STRATUM.   
3. ONE OR MORE MOMENT M-T LINES ('SOIL M-T' LINE SET) AS NEEDED FOR THE FIRST STRATUM.   
4. A MOMENT STRATUM LINE FOR THE SECOND STRATUM.   
5. MOMENT M-T LINES FOR THE SECOND STRATUM.ETC.

( 1- 4) ENTER 'SOIL'.   
( 6-12) ENTER 'BENDING'.   
(14-17) ENTER 'HEAD'.

COLUMNS

COMMENTARY

(18-20) ENTER THE NUMBER OF SOIL STRATA FOR THIS M-T DESCRIPTION. DO NOT LEAVE THIS FIELD BLANK.   
(22-23) IF ANY M-T CURVE ENTERED ('SOIL M-T' LINE SET) IS DEFINED AT MORE THAN 30 POINTS, ENTER THAT NUMBER HERE. OTHERWISE, LEAVE BLANK.   
(28-33) ENTER THE FACTOR FOR THE "M" VALUES. THIS FACTOR WILL BE USED TO MULTIPLY THE INPUT "M" VALUES.   
(34-40) ENTER THE FACTOR FOR THE "THETA" VALUES. THIS FACTOR WILL BE USED TO MULTIPLY THE INPUT "THETA" VALUES.   
(41-44) ENTER THE SOIL TABLE IDENTIFYING LABEL. THIS IDENTIFIER IS USED ON ONE OR MORE 'PILE' LINES TO ASSOCIATE THIS SOIL TABLE WITH THOSE PILES.   
(45-51) ENTER THE DIAMETER FOR WHICH THIS M-T DATA IS GENERATED. THE INPUT "M" VALUES WILL BE MULTIPLIED BY THE RATIO OF THE PILE DIAMETER TO THIS REFERENCE DIAMETER FOR SAND AND THE RATIO OF OF THE PILE DIAMETER SQUARED TO THE REFERENCE DIAMETER SQUARED FOR CLAY.   
(52-67) ENTER ANY DESCRIPTIVE REMARKS DESIRED.



| LINE LABEL | LATERAL LABEL | HEAD LABEL | NUMBER OF SOIL STRATA | MORE THAN 30 DATA POINTS FOR M-T CURVE | M FACTOR | THETA FACTOR | SOIL TABLE ID | REFERENCE DIAMETER | SOIL DESCRIPTION OR OTHER REMARKS | LEAVE BLANK |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOIL | BENDING | HEAD |  |  |  |  |  |  |  |  |
| 1-- 4 | 6--12 | 14--17 | 18--->20 | 22--->23 | 28--->33 | 34--->40 | 41<--44 | 45--->51 | 52--67 | 68--80 |
| DEFAULT |  |  |  |  | 1 | 1 |  |  |  |  |
| ENGLISH |  |  |  |  |  |  |  | IN |  |  |
| METRIC |  |  |  |  |  |  |  | CM |  |  |



SOIL M-T STRATUM LINE

COLUMNS

COMMENTARY

GENERAL THE LOCATION OF EACH SOIL STRATUM IS DEFINED USING THIS LINE.THE M-T DATA FOR THIS STRATUM FOLLOWS THIS LINE.

( 1- 4) ENTER 'SOIL'.   
(14-17) ENTER 'SLOC'.   
(18-19) ENTER 'SM' IF THE SOIL M-T CURVE IS THE SAME IN THE POSITIVE AND NEGATIVE ROTATION DIRECTIONS. IN THIS CASE ONLY POSITIVE VALUES OF M AND THETA WILL BE ENTERED ON THE FOLLOWING M-T LINE ('SOIL M-T' LINE SET). THE ORIGIN (M=0.0, THETA=0.0) MUST BE THE FIRST POINT ENTERED ON THAT LINE.   
(22-23) ENTER THE NUMBER OF POINTS ON THE FOLLOWING M-T CURVE. ONE POINT CONSISTS OF A "M" VALUE AND A "THETA" VALUE. THE NUMBER ENTERED HERE MAY NOT BE GREATER THAN THE VALUE ENTERED IN COLUMNS 22-23 OF THE M-T LATERAL HEADER LINE ('SOIL BENDING HEAD' LINE) OR 30 IF THOSE COLUMNS ARE BLANK.   
(25-30) ENTER THE DISTANCE FROM THE PILEHEAD TO THE TOP OF THIS SOIL STRATUM. THIS DISTANCE IS VERTICALLY DOWN AND NOT ALONG THE AXIS OF THE PILE, WHICH MAY BE BATTERED.   
(31-36) ENTER THE DISTANCE FROM THE PILEHEAD TO THE BOTTOM OF THIS SOIL STRATUM IF THE M-T DATA IS CONSTANT THROUGHOUT THIS STRATUM. IF LEFT BLANK, THE M-T DATA WILL VARY LINEARLY TO THE TOP OF THE NEXT STRATUM.   
(39-44) ENTER THE "M" FACTOR FOR THIS M-T CURVE. THIS FACTOR IS USED TO MODIFY THE INPUT "M" VALUES FOR THIS SOIL STRATUM.   
(45-60) ENTER ANY DESCRIPTIVE REMARKS ABOUT THIS SOIL STRATUM.   
(70-76) ENTER THE SOIL LAYER TYPE. THIS WILL CONTROL THE NORMALIZATION PARAMETERS WHEN CONVERTING THE M-T CURVE TO THE MODELED PILE DIAMETER:

'S' - SAND - NORMALIZED M = M/D 'C' - CLAY - NORMALIZED M = M/D^2



| LINE LABEL | LINE TYPE | SYMMETRY INDICATOR | NUMBER OF POINTS PER CURVE | STRATUM LOCATION | STRATUM LOCATION | M FACTOR | SOIL DESCRIPTION OR OTHER REMARKS | SOIL LAYER TYPE | LEAVE BLANK |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | LINE TYPE | SYMMETRY INDICATOR | NUMBER OF POINTS PER CURVE | TOP | BOTTOM | M FACTOR | SOIL DESCRIPTION OR OTHER REMARKS | SOIL LAYER TYPE | LEAVE BLANK |
| SOIL | SLOC |  |  |  |  |  |  |  |  |
| 1--4 | 14--17 | 18--19 | 22--->23 | 25<--30 | 31<--36 | 39<--44 | 45--59 | 62 | 63--80 |
| DEFAULT |  |  |  |  |  | 1 |  | S |  |
| ENGLISH |  |  |  | FT | FT |  |  |  |  |
| METRIC |  |  |  | M | M |  |  |  |  |



SOIL M-T DATA LINE

COLUMNS

COMMENTARY

GENERAL THIS LINE IS USED TO INPUT THE BENDING MOMENT-ROTATION (M-T) DATA FOR EACH SOIL STRATUM. IF A SYMMETRICAL M-T CURVE IS ENTERED ('SM' IN COLUMNS 18-19 OF THE PRECEDING M-T STRATUM LINE) ONLY THE POSITIVE HALF OF THE M-T CURVE SHOULD BE ENTERED, THE FIRST POINT IN THIS CASE MUST BE THE ORIGIN (M=0.0, THETA=0.0). THE DATA MUST BE ENTERED IN ORDER OF INCREASING VALUES OF THE ROTATION, THETA.

FOR VALUES OF THETA GREATER THAN THE LARGEST SPECIFIED VALUE OR SMALLER THAN THE SMALLEST SPECIFIED VALUE THE VALUE OF M IS ASSUMED TO BE CONSTANT AND EQUAL TO THE VALUE CORRESPONDING TO THOSE THETA VALUES.

( 1- 4) ENTER 'SOIL'.   
(14-16) ENTER 'M-T'.   
(18-77) ENTER THE "M" AND "THETA" VALUES TO DESCRIBE THE M-T CURVE. THIS LINE MAY BE REPEATED AS NECESSARY TO ENTER THE NUMBER OF POINTS SPECIFIED ON THE PRECEDING M-T STRATUM LINE ('SOIL SLOC' LINE SET).



| LINE LABEL | LINE TYPE | M-T CURVE DATA POINTS | M-T CURVE DATA POINTS | M-T CURVE DATA POINTS | M-T CURVE DATA POINTS | M-T CURVE DATA POINTS | M-T CURVE DATA POINTS | M-T CURVE DATA POINTS | M-T CURVE DATA POINTS | M-T CURVE DATA POINTS | M-T CURVE DATA POINTS |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | LINE TYPE | 1ST POINT | 1ST POINT | 2ND POINT | 2ND POINT | 3RD POINT | 3RD POINT | 4TH POINT | 4TH POINT | 5TH POINT | 5TH POINT |
| LINE LABEL | LINE TYPE | M | THETA | M | THETA | M | THETA | M | THETA | M | THETA |
| SOIL | M-T |  |  |  |  |  |  |  |  |  |  |
| 1-- 4 | 14--16 | 18<--23 | 24<--29 | 30<--35 | 36<--41 | 42<--47 | 48<--53 | 54<--59 | 60<--65 | 66<--71 | 72<--77 |
| DEFAULT |  |  |  |  |  |  |  |  |  |  |  |
| ENGLISH |  | KIP-FT/IN | RAD | KIP-FT/IN | RAD | KIP-FT/IN | RAD | KIP-FT/IN | RAD | KIP-FT/IN | RAD |
| METRIC (KN) |  | KN-M/CM | RAD | KN-M/CM | RAD | KN-M/CM | RAD | KN-M/CM | RAD | KN-M/CM | RAD |
| METRIC (KG) |  | KG-M/CM | RAD | KG-M/CM | RAD | KG-M/CM | RAD | KG-M/CM | RAD | KG-M/CM | RAD |



AXIAL LOAD DISTRIBUTION

COLUMNS

COMMENTARY

GENERAL

THIS LINE IS USED IN PLACE OF AXIAL SPRING, ADHESION, T-Z AND END BEARING DATA ('SOIL' LINE SETS). THE USER INPUTS THE PILE INTERNAL AXIAL FORCE AT SEVERAL POINTS ALONG ITS LENGTH, WITH COMPRESSION POSITIVE. THE PROGRAM USES LINEAR INTERPOLATION TO DETERMINE THE INTERNAL AXIAL FORCES BETWEEN THE INPUT POINTS. IF THE LAST POINT ENTERED IS NOT THE END OF THE PILE, THE INTERNAL AXIAL FORCE FROM THAT POINT TO THE END IS TAKEN AS THE LAST ENTERED VALUE. THE VALUE ENTERED AT THE PILEHEAD IS THE AXIAL LOAD ON THE PILE. ANY PILEHEAD AXIAL LOAD ENTERED ON A LATER 'PLLOAD' LINE WILL BE IGNORED. THE FIRST POINT ENTERED SHOULD BE AT THE PILEHEAD (0.0 IN COLUMNS 24-29)

THIS LINE MAY BE REPEATED AS NECESSARY TO ENTER AS MANY POINTS AS DESIRED.

( 1- 6) ENTER 'AXLOAD'. THE FIRST LINE IS A HEADER HAVING ONLY THIS ENTRY.   
(14-16) ENTER THE NUMBER OF POINTS ALONG THE PILE WHERE THE INTERNAL AXIAL FORCE WILL BE ENTERED. IF MORE THAN ONE 'AXLOAD' LINE IS USED, THIS NUMBER IS ENTERED ONLY ON THE FIRST LINE.   
(18-23) IF THIS IS THE FIRST 'AXLOAD' LINE (NON-HEADER) ENTER THE PILEHEAD FORCE (COMPRESSION IS POSITIVE). FOR SUBSEQUENT LINES ENTER THE PILEHEAD INTERNAL AXIAL FORCE.   
(24-29) IF THIS IS THE FIRST 'AXLOAD' LINE (NON-HEADER) ENTER 0.0; FOR SUBSEQUENT LINES ENTER THE DISTANCE FROM THE PILEHEAD.   
(30-77) ENTER THE FORCES AND DISTANCES FOR THE REMAINING POINTS.



| LINE LABEL | NUMBER OF POINTS | PILE INTERNAL AXIAL FORCE DISTRIBUTION DATA | PILE INTERNAL AXIAL FORCE DISTRIBUTION DATA | PILE INTERNAL AXIAL FORCE DISTRIBUTION DATA | PILE INTERNAL AXIAL FORCE DISTRIBUTION DATA | PILE INTERNAL AXIAL FORCE DISTRIBUTION DATA | PILE INTERNAL AXIAL FORCE DISTRIBUTION DATA | PILE INTERNAL AXIAL FORCE DISTRIBUTION DATA | PILE INTERNAL AXIAL FORCE DISTRIBUTION DATA | PILE INTERNAL AXIAL FORCE DISTRIBUTION DATA | PILE INTERNAL AXIAL FORCE DISTRIBUTION DATA |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | NUMBER OF POINTS | POINT NUMBER 1 | POINT NUMBER 1 | POINT NUMBER 2 | POINT NUMBER 2 | POINT NUMBER 3 | POINT NUMBER 3 | POINT NUMBER 4 | POINT NUMBER 4 | POINT NUMBER 5 | POINT NUMBER 5 |
| LINE LABEL | NUMBER OF POINTS | AXIAL FORCE | DISTANCE FROM PILEHEAD | AXIAL FORCE | DISTANCE FROM PILEHEAD | AXIAL FORCE | DISTANCE FROM PILEHEAD | AXIAL FORCE | DISTANCE FROM PILEHEAD | AXIAL FORCE | DISTANCE FROM PILEHEAD |
| AXLOAD |  |  |  |  |  |  |  |  |  |  |  |
| 1--6 | 14-->16 | 18<--23 | 24<--29 | 30<--35 | 36<--41 | 42<--47 | 48<--53 | 54<--59 | 60<--65 | 66<--71 | 72<--77 |
| DEFAULT |  |  |  |  |  |  |  |  |  |  |  |
| ENGLISH |  | KIP | FT | KIP | FT | KIP | FT | KIP | FT | KIP | FT |
| METRIC (KN) |  | KN | M | KN | M | KN | M | KN | M | KN | M |
| METRIC (KG) |  | KG | M | KG | M | KG | M | KG | M | KG | M |



PILE DESCRIPTION

COLUMNS

COMMENTARY

GENERAL

THIS LINE IS REQUIRED FOR EACH PILE THAT IS TO BE INCLUDED IN THE ANALYSIS. IT IS USED TO SPECIFY EACH PILE'S GEOMETRY AND TO DESIGNATE THE SOIL TABLE THAT IS TO BE USED FOR ITS ANALYSIS.

( 1- 4)

ENTER 'PILE'. THE FIRST LINE IS A HEADER WITH ONLY THIS ENTRY.

( 7-10)

ENTER THE JOINT NAME IN THE STRUCTURAL MODEL THAT CONNECTS TO THIS PILE. THIS INPUT IS NOT REQUIRED.

(16-18)

ENTER THE PILE GROUP LABEL THAT IDENTIFIES THE 'PLGRUP' WHERETHE PROPERTIES FOR THIS PILE ARE SPECIFIED.

(21-50)

ENTER THE X, Y, AND Z DISTANCES (GLOBAL DIRECTIONS) FROM THE PILEHEAD TO A POINT ABOVE IT. THE AXIS OF THE PILE WILL BE ON THE LINE FROM THE PILEHEAD TO THIS POINT. FOR EXAMPLE X=1.0, Y=0.0, Z=8.0 WOULD DEFINE A BATTER OF 1:8 WITH POSITIVE SLOPE IN THE X-Z PLANE.

(57-64)

ENTER THE PILEHEAD VERTICAL HEIGHT RELATIVE TO MUDLINE. A POSITIVE VALUE IS ABOVE THE MUDINE.

(69-72)

ENTER THE SOIL TABLE IDENTIFIER TO DEFINE THE SOIL PROPERTIES ASSOCIATED WITH THIS PILE IN THE LOCAL X-Z PLANE. THE ENTRY MUST MATCH AN ENTRY IN THE SOIL TABLE INPUT.



| LINE LABEL | PILEHEAD JOINT NAME | PILE GRUP LABEL | BATTER DEFINITION COORDINATES | BATTER DEFINITION COORDINATES | BATTER DEFINITION COORDINATES | PILEHEAD HEIGHT | SOIL TABLE ID X-Z PLANE | LEAVE BLANK |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | PILEHEAD JOINT NAME | PILE GRUP LABEL | X | Y | Z | PILEHEAD HEIGHT | SOIL TABLE ID X-Z PLANE | LEAVE BLANK |
| PILE |  |  |  |  |  |  |  |  |
| 1--4 | 7-->10 | 16<!--18 | 21<!--30 | 31<!--40 | 41<!--50 | 57<!--64 | 69<!--72 | 73----80 |
| DEFAULT |  |  |  |  |  |  |  |  |
| ENGLISH |  |  | IN | IN | IN | FT |  |  |
| METRIC |  |  | CM | CM | CM | M |  |  |



PILE GROUP DESCRIPTION LINE

COLUMNS

COMMENTARY

GENERAL THIS LINE IS USED TO SPECIFY PROPERTIES OF A PILE OR GROUP OFPILES. A PILE WITH PROPERTIES THAT VARY ALONG ITS LENGTH ISDESCRIBED WITH SEVERAL 'PLGRUP' LINES HAVING THE SAME GROUPLABEL. EACH 'PLGRUP' LINE SPECIFIES THE PROPERTIES FOR ASEGMENT OF THE PILE. THE 'PLGRUP' LINES IN THIS CASE AREINPUT IN ORDER FROM THE PILEHEAD DOWN.

( 1- 6) ENTER 'PLGRUP'. THE FIRST LINE IS A HEADER LINE HAVING ONLY THIS ENTRY.   
( 8-10) ENTER THE UNIQUE GROUP LABEL FOR THIS PILE TYPE. THIS GROUP LABEL WILL BE REFERENCED BY SUBSEQUENT 'PILE' LINES.   
(12-18) IF THIS PILE HAS CROSS SECTION PROPERTIES SPECIFIED ON A'PLSECT' LINE, ENTER THE CROSS SECTION LABEL.  
(19-19) ENTER A 'U' IF A PILE FROM THIS PILE GROUP IS TO BE CONSIDERED 'DRIVEN UNPLUGGED' FOR THE PURPOSE OF CALCULATING AXIAL SOIL RESISTANCE USING API GUIDELINES. ONLY APPLIES TO THE END SEGMENT.   
(20-31) IF THE CROSS SECTION PROPERTIES HAVE NOT BEEN DESCRIBED ON A'PLSECT' LINE, ENTER THE OUTSIDE DIAMETER AND WALL THICKNESSHERE. THE PROGRAM WILL COMPUTE THE STIFFNESS PROPERTIES.  
(32-49) ENTER THE MATERIAL PROPERTIES OF THE PILE.   
(50-57) ENTER THE LENGTH OF THIS SEGMENT OF THE PILE. THE SUM OF THE LENGTHS OF ALL SEGMENTS WITH THE SAME GROUP LABEL EQUALS THE TOTAL PILE LENGTH.   
(58-69) THE PILE DIMENSIONS FOR SOIL RESISTANCE CALCULATIONS MAY BE OVERRIDDEN BY THESE ENTRIES. IF LEFT BLANK THE TRUE DIMENSIONS ARE USED. FOR TUBES ENTER THE EFFECTIVE OUTER DIAMETER AND WALL THICKNESS. FOR 'H' PILES ENTER THE EFFECTIVE WIDTH AND DEPTH (SEE THE ACCOMPANYING FIGURES).   
(70-74) THIS FACTOR IS USED TO MODIFY THE T-Z DATA FOR THIS PILE SEGMENT. THE AXIAL SOIL FORCE PER UNIT LENGTH IS CALCULATED BY MULTIPLYING THE PILE PERIMETER BY THE SOIL RESISTANCE "T" AND THIS FACTOR.   
(75-80) ENTER THE EFFECTIVE END BEARING AREA FOR THIS PILE SEGMENT. THE USER MAY SPECIFY END BEARING AREAS FOR THE BOTTOM OF EACH PILE SEGMENT TO MODEL A STEPPED PILE. HOWEVER, IN THE USUAL CASE, ONLY THE LAST SEGMENT WILL HAVE AN END BEARING AREA.



| LINE LABEL | GROUP LABEL | CROSS SECTION LABEL | DRIVEN UNPLG. | TUBULAR DIMENSIONS | TUBULAR DIMENSIONS | MATERIAL PROPERTIES | MATERIAL PROPERTIES | MATERIAL PROPERTIES | PILE SEGMENT LENGTH | PILE SURFACE DIMENSIONSB | PILE SURFACE DIMENSIONSB | T FACTOR | AVAILABLE END BEARING AREA |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | GROUP LABEL | CROSS SECTION LABEL | DRIVEN UNPLG. | OUTSIDE DIAMETER | WALL THICKNESS | E X 1000 | G X 1000 | SY | PILE SEGMENT LENGTH | A | WALL THK. | T FACTOR | AVAILABLE END BEARING AREA |
| LINE LABEL | GROUP LABEL | CROSS SECTION LABEL | DRIVEN UNPLG. | OUTSIDE DIAMETER | WALL THICKNESS | E X 1000 | G X 1000 | SY | PILE SEGMENT LENGTH | O.D. | DEPTH | T FACTOR | AVAILABLE END BEARING AREA |
| LINE LABEL | GROUP LABEL | CROSS SECTION LABEL | DRIVEN UNPLG. | OUTSIDE DIAMETER | WALL THICKNESS | E X 1000 | G X 1000 | SY | PILE SEGMENT LENGTH | FL. WIDTH |  | T FACTOR | AVAILABLE END BEARING AREA |
| PLGRP |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 1--6 | 8<--10 | 12<--18 | 19 | 20<--25 | 26<--31 | 32<--37 | 38<--43 | 44<--49 | 50<--57 | 58<--63 | 64<--69 | 70<--74 | 75<--80 |
| DEFAULT |  |  |  |  |  | 29.0 ENGL | 11.6 ENGL | 36.0 ENGL |  |  | IN | 1 |  |
| ENGLISH |  |  |  | IN | IN | KSI | KSI | KSI | FT | IN | CM |  | SQ.FT |
| METRIC (KN) |  |  |  | CM | CM | KN/SQ.CM | KN/SQ.CM | KN/SQ.CM | M | CM | CM |  | SQ.M |
| METRIC (KG) |  |  |  | CM | CM | KG/SQ.CM | KG/SQ.CM | KG/SQ.CM | M | CM |  |  | SQ.M |



PILE OPTIONS LINE

COLUMNS

COMMENTARY

GENERAL THIS LINE IS REQUIRED IN ANY PILE RUN. IT IS USED TO SPECIFY THE INPUT AND OUTPUT UNITS, ANALYSIS PARAMETERS, AND OUTPUT REPORTS AND PLOTS DESIRED. THIS LINE REPLACES THE 'PSIOPT' LINE IN THE PSI DATA FILE.

( 1- 5) ENTER 'PLOPT'.

( 7- 8) ENTER THE INPUT UNITS. CHOOSE FROM THE FOLLOWING: 'EN' - ENGLISH. THIS IS THE DEFAULT. 'MN' - METRIC WITH NEWTONS AS THE FORCE UNIT. 'ME' - METRIC WITH KILOGRAMS AS THE FORCE UNIT.

( 9-10) ENTER THE DESIRED STRESS OR UNITY CHECK CODE ALONG THE PILE: 'UC' - API RP2A-WSD 21ST EDITION. 'LR' - API RP2A-LRFD 1ST EDITION. '16' - 16TH EDITION API-RP2A. 'NP' - 1984 NPD CODE. 'DC' - 1984 DANISH CODE. 'IS' - ISO 19902 (2007).

IF LEFT BLANK ONLY PILEHEAD FORCES AND DISPLACEMENTS ARE REPORTED.

(11-12) ENTER THE OUTPUT UNITS, CHOOSE FROM 'EN', 'MN', OR 'ME' AS FOR THE INPUT UNITS. IF LEFT BLANK THE OUTPUT UNITS WILL BE THE SAME AS THE INPUT.   
(13-15) ENTER THE NUMBER OF INCREMENTAL PILE LENGTHS FOR THE FINITE DIFFERENCE SOLUTION. THE OUTPUT STRESSES, DISPLACEMENTS, SHEAR, MOMENT AND UNITY CHECKS WILL BE REPORTED AT THESE POINTS ALONG THE PILE LENGTH. THE MAXIMUM NUMBER OF INCREMENTS IS 300.   
(18-20) ENTER THE MAXIMUM NUMBER OF ITERATIONS ALLOWED. THIS NUMBER WILL BE USED AS THE MAXIMUM FOR BOTH THE AXIAL AND LATERAL SOLUTIONS. DEFAULT VALUE IS 100.   
(21-30) ENTER THE CONVERGENCE TOLERANCE FOR PILE DEFLECTION FOR SUCCESSIVE ITERATIONS. ITERATION WILL PROCEED UNTIL ALL POINTS ALONG THE PILE CONVERGE TO WITHIN THIS TOLERANCE OR UNTIL THE MAXIMUM NUMBER OF ITERATIONS IS EXCEEDED. THE DEFAULT VALUE IS 0.001 INCHES.

COLUMNS

COMMENTARY

(31-40) ENTER THE MATERIAL WEIGHT DENSITY IF THE PILE'S SELF WEIGH IS TO BE INCLUDED. IF LEFT BLANK THE PILE IS ASSUMED TO BE WEIGHTLESS.   
(41-42) ENTER 'PT' IF AN INPUT ECHO IS TO BE PRINTED.   
(43-44) A NEUTRAL PICTURE FILE CAN BE PRODUCED WHICH CAN BE PLOTTED LATER AT THE TERMINAL (IF IT HAS GRAPHICS CAPABILITIES) OR ON A HARD COPY PLOTTER. IF 'PT' IS ENTERED HERE ALL T-Z PLOTS FOR THE SOIL STRATA WILL BE ON ONE PLOT, ALL BEARING T-Z PLOTS ON ANOTHER, AND ALL P-Y PLOTS ON A THIRD. IF 'SP' IS ENTERED THEN EACH PLOT WILL BE ON A SEPARATE SHEET. IF LEFT BLANK NO PLOTS ARE PRODUCED.   
(45-47) ENTER 'TTZ' IF AXIAL AND TORSION LOADS ARE TO BE COUPLED.   
(57-58) ENTER 'PP' IF A PILE SOLUTION FILE IS TO BE CREATED.   
(59-60) ENTER 'S3' TO USE API-RP2A WSD 21ST Supplement 3   
(61-62) ENTER 'PT' IF A REPORT OF THE SOIL REACTIONS AT EACH STATION ALONG THE PILE IS TO BE PRINTED.   
(63-65) IF THIS PILE EXECUTION IS CREATING A POST FILE FOR A SUBSEQUENT FATIGUE ANALYSIS, ENTER THE OPTION TO CALCULATE THE STRESS CONCENTRATION FACTORS WHERE THERE IS A CHANGE IN PILE THICKNESS OR DIAMETER. SELECT FROM THE FOLLOWING OPTIONS BASED ON OTC PAPER 5550: 'AWS' - AMERICAN WELDING SOCIETY. 'DNV' - DET NORSKE VERITAS. 'DE ' - DEPARTMENT OF ENERGY. 'BS ' - BRITISH STANDARDS.   
(66-66) SELECT PILE CAPACITY METHOD. SACS METHOD ANALYZES PILE-SOIL



| LINE LABEL | INPUT UNITS | STRESS AND UNITY CHECKS | OUTPUT UNITS | NUMBER OF LENGTH INCREMENTS | MAXIMUM NUMBER OF ITERATIONS | LATERAL DEFLECTION CONVERGENCE TOLERANCE | MATERIAL WEIGHT DENSITY | INPUT ECHO | PLOT OPTION | AXIAL TORSION COUPLING | PILE FILE OPTION | API 21ST SPT.3 OPT. | PRINT SOIL REACTIONS | SCF OPTION | PILE CAPACITY METHOD | LEAVE THIS FIELD BLANK |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PLOPT |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 1--5 | 7--8 | 9--10 | 11--12 | 13-->15 | 18-->20 | 21<--30 | 31<--40 | 41--42 | 43--44 | 45--47 | 57-58 | 59--60 | 61--62 | 63--65 | 66 | 67--80 |
| DEFAULT | 'EN' |  | INPUT | 100 | 100 | .001 ENGL | 0 |  |  |  |  |  |  |  | 'S' |  |
| ENGLISH |  |  |  |  |  | IN | LB/CU.FT |  |  |  |  |  |  |  |  |  |
| METRIC |  |  |  |  |  | CM | TONNE/CU.M |  |  |  |  |  |  |  |  |  |



PILE CROSS SECTION PROPERTY LINE

COLUMNS

COMMENTARY

GENERAL THIS LINE IS USED TO SPECIFY CROSS SECTION PROPERTIES FOR 'H'PILES OR TUBULAR PILES WITH PROPERTIES DIFFERENT FROM THOSEOF STANDARD TUBES, FOR EXAMPLE, A TUBE GROUTED INSIDE OFANOTHER TUBE.

( 1- 6) ENTER 'PLSECT' ON EACH LINE OF THIS SET. THE FIRST LINE IS A HEADER LINE HAVING ONLY THIS ENTRY.   
( 8-14) ENTER THE UNIQUE CROSS SECTION LABEL FOR THIS PARTICULAR CROSS SECTION. THIS LABEL WILL BE USED ON SUBSEQUENT 'PLGRUP' LINES. ANY COMBINATION OF ALPHANUMERIC CHARACTERS MAY BE USED.   
(16-18) ENTER 'TUB' OR 'H ' FOR TUBULAR OR 'H' TYPE CROSS SECTIONS. FOR A GROUTED DOUBLE TUBULAR, ENTER 'TUB' AND THEN ADD THE APPROPRIATE DIMENSIONS UNDER PROPERTY LABELS C AND D.   
(19-48) ENTER THE CROSS SECTION PROPERTIES FOR STIFFNESS CALCULATIONS (AREA, TORSIONAL CONSTANT, AND MOMENTS OF INERTIA ABOUT THE LOCAL Y AND Z AXES).   
(51-74) ENTER THE CROSS SECTIONAL PROPERTIES FOR STRESS CALCULATIONS ACCORDING TO THE FOLLOWING SCHEDULE (SEE THE ACCOMPANYING FIGURES):

PROPERTY

TUBULAR

'H'

LABEL

PILE

PILE

(51-56) A OUTER DIAMETER FLANGE WIDTH   
(57-62) B WALL THICKNESS DEPTH   
(63-68) C INNER TUBE OD SHEAR AREA IN Y DIRECTION   
(69-74) D INNER TUBE WT SHEAR AREA IN Z DIRECTION *

* THIS IS THE AREA USED FOR CALCULATING SHEAR STRESS. FOR TUBES IT IS TAKEN AS ONE HALF OF THE AREA OF THE CROSS SECTION.

(75-80) THE USER MAY ENTER THE WEIGHT PER UNIT LENGTH OF THE PILE. IF SO ENTERED, THE VALUE ENTERED HERE WILL OVERRIDE THE MATERIAL DENSITY ENTERED ON THE 'PSIOPT' LINE.



| LINE LABEL | CROSS SECTION LABEL | CROSS SECTION TYPE | CROSS SECTION STIFFNESS PROPERTIES | CROSS SECTION STIFFNESS PROPERTIES | CROSS SECTION STIFFNESS PROPERTIES | CROSS SECTION STIFFNESS PROPERTIES | CROSS SECTION DETAILS FOR STRESS CALCULATIONSBCD | CROSS SECTION DETAILS FOR STRESS CALCULATIONSBCD | CROSS SECTION DETAILS FOR STRESS CALCULATIONSBCD | CROSS SECTION DETAILS FOR STRESS CALCULATIONSBCD | WEIGHT PER UNIT LENGTH |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | CROSS SECTION LABEL | CROSS SECTION TYPE | AREA | J | IY | IZ | O.D. | WALL THK. | INNER O.D. | INNER W.T. | WEIGHT PER UNIT LENGTH |
| LINE LABEL | CROSS SECTION LABEL | CROSS SECTION TYPE | AREA | J | IY | IZ | FL. WIDTH | DEPTH | Y SHEAR AREA | Z SHEAR AREA | WEIGHT PER UNIT LENGTH |
| PLSECT |  |  |  |  |  |  |  |  |  |  |  |
| 1--6 | 8<--14 | 16<--18 | 19<--24 | 25<--32 | 33<--40 | 41<--48 | 51<--56 | 57<--62 | 63<--68 | 69<--74 | 75<--80 |
| DEFAULT |  |  |  |  |  |  |  | IN | SQ.IN | SQ.IN |  |
| ENGLISH |  |  | SQ.IN | IN**4 | IN**4 | IN**4 | IN | CM | SQ.CM | SQ.CM | KIP/FT |
| METRIC |  |  | SQ.CM | CM**4 | CM**4 | CM**4 | CM |  |  |  | TONNE/M |



LOAD CASE PLOT SELECTION LINE

COLUMNS

COMMENTARY

GENERAL THIS LINE IS USED TO SPECIFY THE LOAD CASES TO BE INCLUDEDFOR PLOTTING. IF OMITTED, ALL LOAD CASES WILL BEAUTOMATICALLY INCLUDED.

( 7-80) ENTER THE LOAD CASE NAMES FOR ALL LOAD CASES TO BE PLOTTED. THE LOAD CASES CAN BE IN ANY ORDER.



| LINE LABEL | LOAD CASE SELECTIONS FOR PLOTTING | LOAD CASE SELECTIONS FOR PLOTTING | LOAD CASE SELECTIONS FOR PLOTTING | LOAD CASE SELECTIONS FOR PLOTTING | LOAD CASE SELECTIONS FOR PLOTTING | LOAD CASE SELECTIONS FOR PLOTTING | LOAD CASE SELECTIONS FOR PLOTTING | LOAD CASE SELECTIONS FOR PLOTTING | LOAD CASE SELECTIONS FOR PLOTTING | LOAD CASE SELECTIONS FOR PLOTTING | LOAD CASE SELECTIONS FOR PLOTTING | LOAD CASE SELECTIONS FOR PLOTTING | LOAD CASE SELECTIONS FOR PLOTTING | LOAD CASE SELECTIONS FOR PLOTTING | LOAD CASE SELECTIONS FOR PLOTTING |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | 1ST | 2ND | 3RD | 4TH | 5TH | 6TH | 7TH | 8TH | 9TH | 10TH | 11TH | 12TH | 13TH | 14TH | 15TH |
| PLTLC |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 1-- 5 | 7-->10 | 12-->15 | 17-->20 | 22-->25 | 27-->30 | 32-->35 | 37-->40 | 42-->45 | 47-->50 | 52-->55 | 57-->60 | 62-->65 | 67-->70 | 72-->75 | 76-->80 |



PLOT REQUEST LINE

COLUMNS

COMMENTARY

GENERAL THIS LINE IS USED TO SPECIFY THE PLOTS AND PLOT OPTIONS DESIRED. IF OMITTED, NO NEUTRAL CHART FILE WILL BE GENERATED.

ENTER THE DESIRED SELECTIONS IN ANY ORDER FROM THE FOLLOWING LIST:

( 7- 9) 'SD' - SOIL DATA (P-Y, T-Z, ADHESION, ETC.).   
(12-14) 'DA' - AXIAL DEFLECTIONS.   
(17-19) 'DL' - LATERAL DEFLECTIONS (Y AND Z SHOWN SEPARATELY). 'DT' - LATERAL DEFLECTIONS (VECTOR SUM OF Y AND Z).   
(22-24) 'RL' - LATERAL ROTATIONS (Y AND Z SHOWN SEPARATELY). 'RT' - LATERAL ROTATIONS (VECTOR SUM OF Y AND Z).   
(27-29) 'ML' - BENDING MOMENTS (Y AND Z SHOWN SEPARATELY). 'MT' - BENDING MOMENTS (VECTOR SUM OF Y AND Z).   
(32-34) 'AL' - AXIAL LOADS.   
(37-39) 'SL' - SHEAR LOADS (Y AND Z SHOWN SEPARATELY). 'ST' - SHEAR LOADS (VECTOR SUM OF Y AND Z).   
(42-44) 'AS' - AXIAL SOIL REACTIONS.   
(47-48) 'LS' - LATERAL SOIL REACTIONS (Y AND Z SHOWN SEPARATELY). 'TS' - LATERAL SOIL REACTIONS (VECTOR SUM OF Y AND Z).   
(52-54) 'UC' - UNITY CHECK RATIO.   
(57-59) 'PR' - PILE REDESIGN (PILE THICKNESS REQUIRED VERSUS DEPTH).   
(62-64) 'LG' - LIGHT GRID (MAJOR AXIS DIVISIONS). 'DG' - DENSE GRID (ALL AXIS DIVISIONS). 'XH' - CROSS HATCHING.   
(72-74) 'RA' - Torsional Rotation   
(77-79) 'MA' - Torsional Moment   
(NOTE) FOR THE SELECTIONS 'DA', 'DL', 'DT', 'RL', 'RT', 'ML', 'MT', 'AL', 'SL', 'ST', 'AS', 'LS', 'TS', AND 'UC', THE ENVELOPE FOR ALL LOAD CASES MAY BE REQUESTED BY APPENDING AN 'E' TO THE REQUEST, SUCH AS 'DAE' FOR THE AXIAL DEFLECTION ENVELOPE.



| LINE LABEL | PLOT SELECTIONS | PLOT SELECTIONS | PLOT SELECTIONS | PLOT SELECTIONS | PLOT SELECTIONS | PLOT SELECTIONS | PLOT SELECTIONS | PLOT SELECTIONS | PLOT SELECTIONS | PLOT SELECTIONS | PLOT SELECTIONS | PLOT SELECTIONS | PLOT SELECTIONS | PLOT SELECTIONS | PLOT SELECTIONS | PLOT SELECTIONS | LEAVE BLANK |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | SOIL DATA | AXIAL DEFLECTIONS | LATERAL DEFLECTION | LATERAL ROTATION | MOMENT PLOTS | AXIAL LOADS | SHEAR LOADS | AXIAL SOIL REACTION | LATERAL SOIL REACTION | UNITY CHECK RATIO | PILE REDESIGN | GRID | CROSS HATCHING | TORSIONAL ROTATION | TORSIONAL MOMENT |  |  |
| PLTRQ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 1--5 | 7--9 | 12--14 | 17--19 | 22--24 | 27--29 | 32--34 | 37--39 | 42--44 | 47--49 | 52--54 | 57--59 | 62--64 | 67--69 | 72-74 | 77-79 | 72--80 |  |



PLOT SIZE SELECTION LINE

COLUMNS

COMMENTARY

GENERAL THIS LINE IS USED TO SPECIFY THE SIZE PARAMETERS FOR PLOTTING. IF OMITTED, THE DEFAULT VALUES WILL BE USED.

( 6-11) ENTER THE SIZE OF THE OVERALL PLOT IN THE X-DIRECTION.   
(12-17) ENTER THE SIZE OF THE OVERALL PLOT IN THE Y-DIRECTION.   
(18-23) ENTER THE SIZE OF THE CHARACTERS USED.   
(24-29) ENTER THE SPACING BETWEEN LINES USED FOR CROSS HATCHING. CROSS HATCHING IS USED FOR AREA FILLING.   
(30-32) IF YOU HAVE A MULTI-PEN PLOTTER, THE DIFFERENT VARIABLES PLOTTED ON THE SAME GRAPH CAN BE SHOWN IN DIFFERENT COLORS. ENTER THE NUMBER OF DIFFERENT PENS TO BE USED FOR YOUR SPECIFIC PLOTTER.



| LINE LABEL | X SIZE | Y SIZE | CHAR. SIZE | CROSS HATCH SPACING | NUMBER OF PENS |
| --- | --- | --- | --- | --- | --- |
| PLTSZ |  |  |  |  |  |
| 1--5 | 6<-11 | 12<-17 | 18<-23 | 24<-29 | 30->>32 |
| DEFAULT | 8.5 ENGL | 11.0 ENGL | 0.10 ENGL | 0.1 ENGL | 1 |
| ENGLISH | IN | IN | IN | IN |  |
| METRIC | CM | CM | CM | CM |  |



SCOUR

COLUMNS

COMMENTARY

GENERAL

THIS LINE SPECIFIES THE OVERALL SEABED EROSION DEPTH THAT IS TO BE ACCOUNTED FOR WHEN HAVING PSI OR PILE3D AUTOMATICALLY GENERATE LOAD TRANSFER CURVES USING METHODS PRESENTED IN API-RP2A WSD 21ST EDITION SUPPLEMENT 3. NOTE THAT SOILS WITH USER-GENERATED T-Z AND P-Y INPUT ARE UNAFFECTED BY THIS LINE. SPECIFICATION OF A SCOUR DEPTH WILL ENSURE THAT A SCOUR REDUCTION FACTOR IS APPLIED TO THE CONE TIP RESISTANCE FOR STRATA WHOSE AXIAL RESISTANCE IS TO BE DETERMINED FROM CPT DATA. FURTHERMORE, FOR STRATA WHOSE LATERAL RESISTANCE IS CALCULATED IN ACCORDANCE WITH RP2A RECOMMENDATIONS, THE VERTICAL EFFECTIVE STRESS AND SUBGRADE MODULUS REACTION VALUES ARE LOWERED IN ACCORDANCE WIH THE SUGGESTIONS OF THE COMMENTARY ON SOIL REACTION FOR LATERALLY LOADED PILES (C6.8).

(7- 7)

SPECIFY THE CALCULATION METHOD FOR THE SCOUR REDUCTION FACTOR.LEAVE BLANK TO USE THE RATIO OF VERTICAL EFFECTIVE STRESS THATHAS BEEN PROPOSED BY NNI.'F' => USE THE FUGRO FORMULA FOR HIGH GENERAL SCOUR DEPTHS(SEE API-RP2A WSD 21ST EDITION SUPPLEMENT 3, C6.4.3e)

(9-14)

ENTER THE "GENERAL SCOUR DEPTH" OR "OVERALL SEABED EROSION DEPTH"



| LINE LABEL | SCOUR REDUCTION METHOD | GENERAL SCOUR DEPTH | LEAVE BLANK |
| --- | --- | --- | --- |
| SCOUR |  |  |  |
| 1--5 | 7 | 9<-14 | 15--------80 |
| DEFAULT | NNI | 0 |  |
| ENGLISH |  | FT |  |
| METRIC |  | M |  |



PILE TITLE LINE

COLUMNS

COMMENTARY

GENERAL THIS LINE IS OPTIONAL. IT MAY BE USED TO ENTER AN IDENTIFYING TITLE OR OTHER DESCRIPTIVE INFORMATION CONCERNING THE PILE RUN. THIS LINE REPLACES THE PSI TITLE LINE; THE TITLE INFORMATION IS PRINTED AT THE TOP OF EACH PAGE OF THE OUTPUT REPORT.

( 7-80) ENTER THE TITLE OR OTHER DESCRIPTIVE INFORMATION.



| LINE LABEL | ENTER ANY TITLE OR OTHER DESCRIPTIVE INFORMATION DESIRED |
| --- | --- |
| TITLE |  |
| 1-- 5 | 7-80 |



SOIL (CLAY) API LATERAL STRATUM LINE

COLUMNS

COMMENTARY

GENERAL THIS LINE SET IS USED TO SPECIFY THE SOIL PROPERTIES FOR EACHCLAY STRATUM. THE PROGRAM WILL USE THESE PROPERTIES TOCALCULATE P-Y DATA FOR THE SOIL ACCORDING TO APIRECOMMENDATIONS.

( 1- 4) ENTER 'SOIL'.   
( 6-12) ENTER 'API LAT'.   
(14-17) ENTER 'SLOC'.   
(19-22) ENTER THE SOIL TYPE 'CLAY'.   
( 23 ) ENTER 'C' IF THE P-Y CURVE GENERATED IS FOR CYCLIC LOAD CONDITIONS, OR 'S' IF FOR STATIC LOAD CONDITIONS.   
(25-36) ENTER THE DISTANCES FROM THE PILEHEAD TO THE TOP AND BOTTOM OF THIS SOIL STRATUM. THESE DISTANCES ARE VERTICALLY DOWN AND NOT ALONG THE AXIS OF THE PILE, WHICH MAY BE BATTERED.

COLUMNS

COMMENTARY

(37-40) ENTER THE "P" FACTOR FOR THIS P-Y CURVE. THIS FACTOR IS USED TO MODIFY THE GENERATED "P" VALUES FOR THIS SOIL STRATUM.   
(41-44) ENTER THE AMOUNT TO BE ADDED TO THE GENERATED "Y" VALUES. THIS IN EFFECT SHIFTS THE P-Y CURVE ALONG THE Y-AXIS. THIS SHIFT CAN BE USED WITH BOTH SYMMETRICAL AND NONSYMMETRICAL P-Y CURVES AND IS USEFUL FOR MODELING MUDSLIDES.   
(45-50) ENTER THE UNDRAINED SHEAR STRENGTH.   
(51-56) ENTER THE EFFECTIVE UNIT WEIGHT OF THE SOIL.   
(57-62) ENTER THE API RP2A EMPIRICAL PARAMETER "J".   
(63-68) ENTER THE API RP2A REFERENCE STRAIN.   
(70-76) ENTER A HIGH PRECISION "P" FACTOR FOR THIS P-Y CURVE. THIS FACTOR MAY BE USED TO SCALE THE "P" VALUES FOR THIS STRATUM. IF A "P" FACTOR HAS BEEN SPECIFIED IN COLUMNS 37-40 , THE HIGH PRECISION "P" FACTOR BECOMES A MULTIPLIER FOR THE ORIGINAL "P" FACTOR.



| LINE LABEL | AUTOMATIC LATERAL RESISTANCE GENERATION | LINE TYPE | SOIL TYPE | STATIC OR CYCLIC | TOP OF STRATUM | BOTTOM OF STRATUM | P FACTOR | Y SHIFT | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | HIGH PRECISION P FACTOR |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | AUTOMATIC LATERAL RESISTANCE GENERATION | LINE TYPE | SOIL TYPE | STATIC OR CYCLIC | TOP OF STRATUM | BOTTOM OF STRATUM | P FACTOR | Y SHIFT | UNDRAINED SHEAR STRENGTH | EFFECTIVE UNIT WEIGHT OF SOIL | API RP2A EMPIRICAL PARAMETER "J" | API RP2A REFERENCE STRAIN | HIGH PRECISION P FACTOR |
| SOIL | API LAT | SLOC |  |  |  |  |  |  |  |  |  |  |  |
| 1--4 | 6--12 | 14--17 | 19--22 | 23 | 25<--30 | 31<--36 | 37<--40 | 41<--44 | 45<--50 | 51<--56 | 57<--62 | 63<--68 | 70--76 |
| DEFAULT |  |  |  | 's' |  |  | 1 | 0 |  |  | 0.5 |  | 1 |
| ENGLISH |  |  |  |  | FT | FT |  | IN | KIP/SQ.FT | LB/CU.FT |  |  |  |
| METRIC (KN) |  |  |  |  | M | M |  | CM | KN/SQ.CM | TONNE/CU.M |  |  |  |
| METRIC (KG) |  |  |  |  | M | M |  | CM | KG/SQ.CM | TONNE/CU.M |  |  |  |



SOIL (SAND) API LATERAL STRATUM LINE

COLUMNS

COMMENTARY

GENERAL THIS LINE SET IS USED TO SPECIFY THE SOIL PROPERTIES FOR EACHSAND STRATUM. THE PROGRAM WILL USE THESE PROPERTIES TOCALCULATE P-Y DATA FOR THE SOIL ACCORDING TO APIRECOMMENDATIONS.

( 1- 4) ENTER 'SOIL'.   
( 6-12) ENTER 'API LAT'.   
(14-17) ENTER 'SLOC'.   
(19-22) ENTER THE SOIL TYPE. THE PROGRAM WILL USE THE LISTED VALUES FOR THE ANGLE OF INTERNAL FRICTION UNLESS OVERRIDDEN IN COLUMNS 63-68.



| INPUT | SOIL CLASS | FRCTION ANGLE |
| --- | --- | --- |
| 'GRAV' | GRAVEL | 40.0 |
| 'SAND' | CLEAN SAND | 35.0 |
| 'SLSN' | SILTY SAND | 30.0 |
| 'SNSL' | SANDY SILT | 25.0 |
| 'SILT' | SILT | 20.0 |



( 23 ) ENTER 'C' IF THE P-Y CURVE GENERATED IS FOR CYCLIC LOAD CONDITIONS, OR 'S' IF FOR STATIC LOAD CONDITIONS.   
( 24 ) ENTER SOIL LOCATION RELATIVE TO THE WATER TABLE. 'A' - ABOVE WATER TABLE 'B' - BELOW WATER TABLE   
(25-36) ENTER THE DISTANCES FROM THE PILEHEAD TO THE TOP AND BOTTOM OF THIS SOIL STRATUM. THESE DISTANCES ARE VERTICALLY DOWN AND NOT ALONG THE AXIS OF THE PILE, WHICH MAY BE BATTERED.

COLUMNS

COMMENTARY

(37-40) ENTER THE "P" FACTOR FOR THIS P-Y CURVE. THIS FACTOR IS USED TO MODIFY THE GENERATED "P" VALUES FOR THIS SOIL STRATUM.   
(41-44) ENTER THE AMOUNT TO BE ADDED TO THE GENERATED "Y" VALUES. THIS IN EFFECT SHIFTS THE P-Y CURVE ALONG THE Y-AXIS. THIS SHIFT CAN BE USED WITH BOTH SYMMETRICAL AND NONSYMMETRICAL P-Y CURVES AND IS USEFUL FOR MODELING MUDSLIDES.   
(51-56) ENTER THE EFFECTIVE UNIT WEIGHT OF THE SOIL.   
(57-62) ENTER THE INITIAL MODULUS OF SUBGRADE REACTION. IF LEFT BLANK, THE PROGRAM WILL CALCULATE A VALUE BASED ON FIGURE 6.8.7-1 OF API RP2A 20TH EDITION.   
(63-68) ENTER THE FRICTION ANGLE IF YOU WISH TO OVERRIDE THE RP2A DEFAULT VALUES LISTED IN THE TABLE IN THE ADJACENT COLUMN OF THIS COMMENTARY.   
(70-76) ENTER A HIGH PRECISION "P" FACTOR FOR THIS P-Y CURVE. THIS FACTOR MAY BE USED TO SCALE THE "P" VALUES FOR THIS STRATUM. IF A "P" FACTOR HAS BEEN SPECIFIED IN COLUMNS 37-40 , THE HIGH PRECISION "P" FACTOR BECOMES A MULTIPLIER FOR THE ORIGINAL "P" FACTOR.



| LINE LABEL | AUTOMATIC LATERAL RESISTANCE GENERATION | LINE TYPE | SOIL TYPE | STATIC OR CYCLIC | SAND STRATUM LOCATION | TOP OF STRATUM | BOTTOM OF STRATUM | P FACTOR | Y SHIFT | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | HIGH PRECISION P FACTOR |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | AUTOMATIC LATERAL RESISTANCE GENERATION | LINE TYPE | SOIL TYPE | STATIC OR CYCLIC | SAND STRATUM LOCATION | TOP OF STRATUM | BOTTOM OF STRATUM | P FACTOR | Y SHIFT | EFF. UNIT WT OF SOIL | INIT. MOD SUBGRADE REACT. | INTERNAL FRICTION ANGLE | HIGH PRECISION P FACTOR |
| SOIL | API LAT | SLOC |  |  |  |  |  |  |  |  |  |  |  |
| 1--4 | 6--12 | 14--17 | 19--22 | 23 | 24 | 25<--30 | 31<--36 | 37<--40 | 41<--44 | 51<--56 | 57<--62 | 63<--68 | 70--76 |
| DEFAULT |  |  |  | 'S' | 'A' |  |  | 1 | 0 |  |  |  | 1 |
| ENGLISH |  |  |  |  |  | FT | FT |  | IN | LB/CU.FT | LB/CU.IN | DEG |  |
| METRIC (KN) |  |  |  |  |  | M | M |  | CM | TONNE/CU.M | KN/CU.CM | DEG |  |
| METRIC (KG) |  |  |  |  |  | M | M |  | CM | TONNE/CU.M | KG/CU.CM | DEG |  |



SOIL API LATERAL HEADER LINE

COLUMNS

COMMENTARY

GENERAL

THIS LINE FOLLOWED BY THE 'API 10TH EDITION LATERAL STRATUM'LINE SET IS USED TO ENTER THE SOIL PROPERTIES REQUIRED FORTHE PROGRAM TO GENERATE P-Y CURVES ACCORDING TORECOMMENDATIONS IN RP2A. THESE LINE SETS ARE USED IN PLACE OFLINES 'SOIL LATERAL HEAD', 'SOIL SLOC' AND 'SOIL P-Y'.

P-Y CURVES ARE GENERATED FOR A PILE OF SPECIFIED DIAMETER(COLUMNS 28-33). WORKING P-Y CURVES FOR PILES OF DIFFERENTDIAMETER ARE GENERATED BY ONE OF TWO TECHNIQUES AT THE USER'SOPTION:

1. IF 'YEXP' IS ENTERED IN COLUMNS 24-27 THEN BOTH THE

INPUT P AND Y DATA ARE SCALED BY THE RATIO OF PILE

DIAMETER TO THE REFERENCE DIAMETER.

2. IF COLUMNS 24-27 ARE BLANK THEN ONLY THE P VALUES ARE SCALED.

( 1- 4) ENTER 'SOIL'.   
( 6-12) ENTER 'LATERAL'.   
(14-17) ENTER 'HEAD'.   
(18-20) ENTER THE NUMBER OF SOIL STRATA FOR THIS P-Y DESCRIPTION. DO NOT LEAVE THIS FIELD BLANK.

COLUMNS

COMMENTARY

(24-27) ENTER 'YEXP' TO CAUSE BOTH THE INPUT P AND Y VALUES TO BE MULTIPLIED BY THE RATIO OF THE PILE DIAMETER TO THE REFERENCE DIAMETER TO PRODUCE THE WORKING P-Y CURVE FOR THE PILE. IF LEFT BLANK ONLY THE P VALUES WILL BE MULTIPLIED BY THE DIAMETER RATIO.   
(28-33) ENTER THE DIAMETER FOR WHICH THIS P-Y DATA IS GENERATED. THE INPUT P VALUES WILL BE MULTIPLIED BY THE RATIO OF THE PILE DIAMETER TO THIS REFERENCE DIAMETER. IN ADDITION IF 'YEXP' IS ENTERED IN COLUMNS 24-27 THEN THE Y VALUES WILL ALSO BE MULTIPLIED BY THIS RATIO.   
(41-44) ENTER THE UNIQUE ALPHANUMERIC SOIL TABLE IDENTIFIER. THIS IDENTIFIER IS USED ON ONE OR MORE 'PILE' LINES TO ASSOCIATE THIS SOIL TABLE WITH THOSE PILES.   
(45-60) ENTER ANY DESCRIPTIVE REMARKS DESIRED.



| LINE LABEL | LATERAL LABEL | HEAD LABEL | NUMBER OF SOIL STRATA | P-Y CURVE SCALING | REFERENCE DIAMETER | SOIL TABLE ID | SOIL DESCRIPTION OR OTHER REMARKS | LEAVE BLANK |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOIL | LATERAL | HEAD |  |  |  |  |  |  |
| 1--4 | 6--12 | 14--17 | 18-->20 | 24--27 | 28<--33 | 41<--44 | 45----60 | 61--80 |
| DEFAULT |  |  |  |  |  |  |  |  |
| ENGLISH |  |  |  |  | IN |  |  |  |
| METRIC |  |  |  |  | CM |  |  |  |



API 10TH EDITION LATERAL STRATUM

COLUMNS

COMMENTARY

GENERAL THIS LINE SET IS USED TO SPECIFY THE SOIL PROPERTIES FOR EACHSTRATUM. THE PROGRAM WILL USE THESE PROPERTIES TO CALCULATEP-Y DATA FOR THE SOIL ACCORDING TO API RECOMMENDATIONS.

( 1- 4) ENTER 'SOIL'.   
( 6-12) ENTER 'API LAT'.   
( 13 ) ENTER '1'.   
(14-17) ENTER 'SLOC'.   
(19-22) ENTER THE SOIL TYPE. FOR ALL EXCEPT CLAY THE PROGRAM WILL USE THE LISTED VALUES FOR THE ANGLE OF INTERNAL FRICTION.

INPUT SOIL CLASS FRICTIONANGLE

'CLAY' CLAY NOT APPLICABLE   
'SAND' CLEAN SAND 35.0   
'SLSN' SILTY SAND 30.0   
'SNSL' SANDY SILT 25.0   
'SILT' SILT 20.0

( 23 ) IF THE SOIL TYPE IS CLAY LEAVE THIS FIELD BLANK. OTHERWISE, ENTER 'C' IF THE P-Y CURVE GENERATED IS FOR CYCLIC LOAD CONDITIONS, OR 'S' IF FOR STATIC LOAD CONDITIONS.   
( 24 ) ENTER 'A' OR LEAVE BLANK FOR SAND ABOVE THE WATER TABLE. ENTER 'B' FOR SAND BELOW THE WATER TABLE.   
(25-36) ENTER THE DISTANCES FROM THE PILEHEAD TO THE TOP AND BOTTOM OF THIS SOIL STRATUM. THESE DISTANCES ARE VERTICALLY DOWN AND NOT ALONG THE AXIS OF THE PILE, WHICH MAY BE BATTERED.

COLUMNS

COMMENTARY

(37-40) ENTER THE P FACTOR FOR THIS P-Y CURVE. THIS FACTOR IS USED TO MODIFY THE GENERATED P VALUES FOR THIS SOIL STRATUM.   
(41-44) ENTER THE AMOUNT TO BE ADDED TO THE GENERATED Y VALUES. THIS IN EFFECT SHIFTS THE P-Y CURVE ALONG THE Y-AXIS. THIS SHIFT CAN BE USED WITH BOTH SYMMETRICAL AND NONSYMMETRICAL P-Y CURVES AND IS USEFUL FOR MODELING MUDSLIDES.   
(45-50) IF THE SOIL TYPE IS CLAY, ENTER THE UNDRAINED SHEAR STRENGTH. OTHERWISE, LEAVE THIS FIELD BLANK.   
(51-56) ENTER THE EFFECTIVE UNIT WEIGHT OF THE SOIL.   
(57-62) IF THE SOIL TYPE IS CLAY ENTER THE RP2A EMPIRICAL PARAMETER, "J". APPROPRIATE VALUES ARE FROM 0.25 TO 0.50, WITH 0.50 THE USUAL VALUE FOR GULF OF MEXICO CLAYS. FOR ALL OTHER SOIL TYPES ENTER THE INITIAL SLOPE, K1. VALUES SUGGESTED BY RP2A ARE:

LOOSE SOILS 20.0 (LB/SQ.IN)/IN MEDIUM SOILS 60.0 (LB/SQ.IN)/IN DENSE SOILS 125.0 (LB/SQ.IN)/IN

(63-68) IF THE SOIL TYPE IS CLAY, ENTER THE RP2A REFERENCE STRAIN. THIS IS DEFINED IN RP2A AS THE "STRAIN WHICH OCCURS AT ONE-HALF THE MAXIMUM STRESS ON LABORATORY UNDRAINED COMPRESSION TESTS OF UNDISTURBED SOIL SAMPLES."

FOR ALL OTHER SOIL TYPES ENTER THE FRICTION ANGLE IF YOU WISH TO OVERRIDE THE RP2A DEFAULT VALUES LISTED IN THE TABLE IN THE ADJACENT COLUMN OF THIS COMMENTARY.



| LINE LABEL | AUTOMATIC LATERAL RESISTANCE GENERATION | API 10TH EDITION FLAG | LINE TYPE | SOIL TYPE | STATIC OR CYCLIC | WATER TABLE LEVEL | TOP OF STRatum | BOTTOM OF STRatum | P FACTOR | Y SHIFT | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | AUTOMATIC LATERAL RESISTANCE GENERATION | API 10TH EDITION FLAG | LINE TYPE | SOIL TYPE | STATIC OR CYCLIC | WATER TABLE LEVEL | TOP OF STRatum | BOTTOM OF STRatum | P FACTOR | Y SHIFT | UNDRAINED SHEAR STRENGTH (FOR CLAY) | EFFECTIVE UNIT WEIGHT OF SOIL | SOIL PARAMETER (SEE ABOVE) | SOIL PARAMETER (SEE ABOVE) |
| SOIL | API LAT | 1 | SLOC |  |  |  |  |  |  |  |  |  |  |  |
| 1--4 | 6--12 | 13 | 14--17 | 19--22 | 23 | 24 | 25<--30 | 31<--36 | 37<--40 | 41<--44 | 45<--50 | 51<--56 | 57<--62 | 63<--68 |
| DEFAULT |  |  |  |  | 'S' |  |  |  | 1 | 0 |  |  |  |  |
| ENGLISH |  |  |  |  |  |  | FT | FT |  | IN | KIP/SQ.FT | LB/CU.FT | NONE, LB/CU.IN | NONE, DEG |
| METRIC (KN) |  |  |  |  |  |  | M | M |  | CM | KN/SQ.CM | TONNE/CU.M | NONE, KN/CU.CM | NONE, DEG |
| METRIC (KG) |  |  |  |  |  |  | M | M |  | CM | KG/SQ.CM | TONNE/CU.M | NONE, KG/CU.CM | NONE, DEG |



SOIL LATERAL HEADER LINE

COLUMNS

COMMENTARY

GENERAL

THIS LINE AND THE SOIL LOCATION AND P-Y LINES ARE USED TO MODEL RESILIENT BEHAVIOR OF THE SOIL SUBJECT TO PRESSURE EXERTED BY THE LATERAL SURFACE OF THE PILE.

LATERAL PRESSURE DATA IS INPUT AS FORCE PER UNIT LENGTH ALONG A PILE OF SPECIFIED REFERENCE DIAMETER (COLUMNS 28-33). WORKING "P-Y" CURVES FOR PILES OF DIFFERENT DIAMETER ARE PRODUCED BY ONE OF TWO TECHNIQUES AT THE USER'S OPTION:

1. IF 'YEXP' IS ENTERED IN COLUMNS 24-27 THEN BOTH THE INPUT "P" AND "Y" DATA ARE SCALED BY THE RATIO OF PILE METER TO THE REFERENCE DIAMETER.   
2. IF COLUMNS 24-27 ARE BLANK THEN ONLY THE "P" VALUES ARE SCALED.

THIS LINE IS USED TO SPECIFY PARAMETERS DEFINING THE SOILLATERAL STIFFNESS. THE ORDER OF LINES FOR P-Y DATA INPUT IS:

1. THIS LATERAL HEADER LINE.   
2. A LATERAL STRATUM LINE ('SOIL SLOC' LINE SET) FOR THE FIRST STRATUM.   
3. ONE OR MORE LATERAL P-Y LINES ('SOIL P-Y' LINE SET) AS NEEDED FOR THE FIRST STRATUM.   
4. A LATERAL STRATUM LINE FOR THE SECOND STRATUM.   
5. LATERAL P-Y LINES FOR THE SECOND STRATUM.ETC.

( 1- 4) ENTER 'SOIL'.   
( 6-12) ENTER 'LATERAL'.   
(14-17) ENTER 'HEAD'.

COLUMNS

COMMENTARY

(18-20) ENTER THE NUMBER OF SOIL STRATA FOR THIS P-Y DESCRIPTION. DO NOT LEAVE THIS FIELD BLANK.   
(22-23) IF ANY P-Y CURVE ENTERED ('SOIL T-Z' LINE SET) IS DEFINED AT MORE THAN 30 POINTS, ENTER THAT NUMBER HERE. OTHERWISE, LEAVE BLANK.   
(24-27) ENTER 'YEXP' TO CAUSE BOTH THE INPUT "P" AND "Y" VALUES TO BE MULTIPLIED BY THE RATIO OF THE PILE DIAMETER TO THE REFERENCE DIAMETER TO PRODUCE THE WORKING "P-Y" CURVE FOR THE PILE. IF LEFT BLANK, ONLY THE "P" VALUES WILL BE MULTIPLIED BY THE DIAMETER RATIO.   
(28-33) ENTER THE DIAMETER FOR WHICH THIS P-Y DATA IS GENERATED. THE INPUT "P" VALUES WILL BE MULTIPLIED BY THE RATIO OF THE PILE DIAMETER TO THIS REFERENCE DIAMETER.   
(34-40) ENTER THE FACTOR FOR THE "Y" VALUES. THIS FACTOR WILL BE USED TO MULTIPLY THE INPUT "Y" VALUES.   
(41-44) ENTER THE SOIL TABLE IDENTIFYING LABEL TO BE USED ON 'PILE' LINE TO ASSOCIATE THIS SOIL TABLE WITH THOSE PILES.   
(45-60) ENTER ANY DESCRIPTIVE REMARKS DESIRED.   
(61) ENTER 'Y' TO CALCULATE THE BASE SHEAR USING THE EXTENDED WINKLER METHOD.   
(62) ENTER 'Y' TO CALCULATE THE BASE MOMENT USING THE EXTENDED WINKLER METHOD.   
(64-65) ENTER THE NUMBER OF CROSS-SECTIONAL PARTS USED IN THE CALCULATION OF THE EXTENDED WINKLER METHOD.   
(67) ENTER 'Y' IF DISTRIBUTED MOMENT IS TO BE CONSIDERED ALONG THE PILE. THIS OPTION REQUIRES M-THETA INPUT ('SOIL BENDING HEAD' LINE). ENTER 'T' TO CALCULATE DISTRIBUTED MOMENT USING THE EXTENDED WINKLER METHOD.



| LINE LABEL | LATERAL LABEL | HEAD LABEL | NUMBER OF SOIL STRATA | MORE THAN 30 DATA POINTS FOR P-Y CURVE | P-Y CURVE SCALING | REFERENCE DIAMETER | Y FACTOR | SOIL TABLE ID | REMARKS | BASE SHEAR | BASE MOMENT | NUMBER OF PARTS | DISTRIBUTED MOMENT | LEAVE BLANK |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOIL | LATERAL | HEAD |  |  |  |  |  |  |  |  |  |  |  |  |
| 1--4 | 6--12 | 14--17 | 18--->20 | 22--->23 | 24--27 | 28<--33 | 34<--40 | 41<--44 | 45--60 | 61 | 62 | 64--->65 | 67 | 68--80 |
| DEFAULT |  |  |  |  |  |  | 1 |  |  | N | N | 10 | Y |  |
| ENGLISH |  |  |  |  |  | IN |  |  |  |  |  |  |  |  |
| METRIC |  |  |  |  |  | CM |  |  |  |  |  |  |  |  |



SOIL LATERAL HEADER LINE

COLUMNS

COMMENTARY

GENERAL

THIS LINE AND THE SOIL LOCATION AND P-Y LINES ARE USED TO MODEL RESILIENT BEHAVIOR OF THE SOIL SUBJECT TO PRESSURE EXERTED BY THE LATERAL SURFACE OF THE PILE.

LATERAL PRESSURE DATA IS INPUT AS FORCE PER UNIT LENGTH ALONG A PILE OF SPECIFIED REFERENCE DIAMETER (COLUMNS 28-33). WORKING "P-Y" CURVES FOR PILES OF DIFFERENT DIAMETER ARE PRODUCED BY ONE OF TWO TECHNIQUES AT THE USER'S OPTION:

1. IF 'YEXP' IS ENTERED IN COLUMNS 24-27 THEN BOTH THE INPUT "P" AND "Y" DATA ARE SCALED BY THE RATIO OF PILE METER TO THE REFERENCE DIAMETER.   
2. IF COLUMNS 24-27 ARE BLANK THEN ONLY THE "P" VALUES ARE SCALED.

THIS LINE IS USED TO SPECIFY PARAMETERS DEFINING THE SOILLATERAL STIFFNESS. THE ORDER OF LINES FOR P-Y DATA INPUT IS:

1. THIS LATERAL HEADER LINE.   
2. A LATERAL STRATUM LINE ('SOIL SLOC' LINE SET) FOR THE FIRST STRATUM.   
3. ONE OR MORE LATERAL P-Y LINES ('SOIL P-Y' LINE SET) AS NEEDED FOR THE FIRST STRATUM.   
4. A LATERAL STRATUM LINE FOR THE SECOND STRATUM.   
5. LATERAL P-Y LINES FOR THE SECOND STRATUM.ETC.

( 1- 4) ENTER 'SOIL'.   
( 6-12) ENTER 'LATERAL'.   
(14-17) ENTER 'HEAD'.

COLUMNS

COMMENTARY

(18-20) ENTER THE NUMBER OF SOIL STRATA FOR THIS P-Y DESCRIPTION. DO NOT LEAVE THIS FIELD BLANK.   
(22-23) IF ANY P-Y CURVE ENTERED ('SOIL T-Z' LINE SET) IS DEFINED AT MORE THAN 30 POINTS, ENTER THAT NUMBER HERE. OTHERWISE, LEAVE BLANK.   
(24-27) ENTER 'YEXP' TO CAUSE BOTH THE INPUT "P" AND "Y" VALUES TO BE MULTIPLIED BY THE RATIO OF THE PILE DIAMETER TO THE REFERENCE DIAMETER TO PRODUCE THE WORKING "P-Y" CURVE FOR THE PILE. IF LEFT BLANK, ONLY THE "P" VALUES WILL BE MULTIPLIED BY THE DIAMETER RATIO.   
(28-33) ENTER THE DIAMETER FOR WHICH THIS P-Y DATA IS GENERATED. THE INPUT "P" VALUES WILL BE MULTIPLIED BY THE RATIO OF THE PILE DIAMETER TO THIS REFERENCE DIAMETER. IN ADDITION, IF 'YEXP' IS ENTERED IN COLUMNS 24-27, THEN THE "Y" VALUES WILL ALSO BE MULTIPLIED BY THIS RATIO.   
(34-40) ENTER THE FACTOR FOR THE "Y" VALUES. THIS FACTOR WILL BE USED TO MULTIPLY THE INPUT "Y" VALUES.   
(41-44) ENTER THE SOIL TABLE IDENTIFYING LABEL. THIS IDENTIFIER IS USED ON ONE OR MORE 'PILE' LINES TO ASSOCIATE THIS SOIL TABLE WITH THOSE PILES.   
(61) ENTER 'Y' IF BASE SHEAR IS TO BE CONSIDERED AT THE PILE TIP.   
(62) ENTER 'Y' IF BASE MOMENT IS TO BE CONSIDERED AT THE PILE TIP.   
(64-65) ENTER THE NUMBER OF CROSS-SECTIONAL PARTS USED TO CALCULATE THE BASE MOMENT.   
(67) ENTER 'Y' IF DISTRIBUTED MOMENT IS TO BE CONSIDERD ALONG THE PILE. THIS OPTION REQUIRES M-THETA INPUT ('SOIL BENDING HEAD' LINE).   
(45-60) ENTER ANY DESCRIPTIVE REMARKS DESIRED.



| LINE LABEL | LATERAL LABEL | HEAD LABEL | NUMBER OF SOIL STRATA | MORE THAN 30 DATA POINTS FOR P-Y CURVE | P-Y CURVE SCALING | REFERENCE DIAMETER | Y FACTOR | SOIL TABLE ID | REMARKS | BASE SHEAR | BASE MOMENT | NUMBER OF PARTS | DISTRIBUTED MOMENT | LEAVE BLANK |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOIL | LATERAL | HEAD |  |  |  |  |  |  |  |  |  |  |  |  |
| 1--4 | 6--12 | 14--17 | 18--->20 | 22--->23 | 24--27 | 28<--33 | 34<--40 | 41<--44 | 45--60 | 61 | 62 | 64--->65 | 67 | 68--80 |
| DEFAULT |  |  |  |  |  |  | 1 |  |  | Y' | Y' | 10 | Y' |  |
| ENGLISH |  |  |  |  |  | IN |  |  |  |  |  |  |  |  |
| METRIC |  |  |  |  |  | CM |  |  |  |  |  |  |  |  |



SOIL P-Y STRATUM LINE

COLUMNS

COMMENTARY

GENERAL THE LOCATION OF EACH SOIL STRATUM IS DEFINED USING THIS LINE.THE P-Y DATA FOR THIS STRATUM FOLLOWS THIS LINE.

( 1- 4) ENTER 'SOIL'.   
(14-17) ENTER 'SLOC'.   
(18-19) ENTER 'SM' IF THE SOIL P-Y CURVE IS THE SAME IN THE POSITIVE AND NEGATIVE DISPLACEMENT DIRECTIONS. IN THIS CASE ONLY POSITIVE VALUES OF P AND Y WILL BE ENTERED ON THE FOLLOWING P-Y LINE ('SOIL P-Y' LINE SET). THE ORIGIN (P=0.0, Y=0.0) MUST BE THE FIRST POINT ENTERED ON THAT LINE.   
(22-23) ENTER THE NUMBER OF POINTS ON THE FOLLOWING P-Y CURVE. ONE POINT CONSISTS OF A "P" VALUE AND A "Y" VALUE. THE NUMBER ENTERED HERE MAY NOT BE GREATER THAN THE VALUE ENTERED IN COLUMNS 22-23 OF THE P-Y LATERAL HEADER LINE ('SOIL LATERAL HEAD' LINE) OR 30 IF THOSE COLUMNS ARE BLANK.   
(25-30) ENTER THE DISTANCE FROM THE PILEHEAD TO THE TOP OF THIS SOIL STRATUM. THIS DISTANCE IS VERTICALLY DOWN AND NOT ALONG THE AXIS OF THE PILE, WHICH MAY BE BATTERED.   
(31-36) ENTER THE DISTANCE FROM THE PILEHEAD TO THE BOTTOM OF THIS SOIL STRATUM IF THE P-Y DATA IS CONSTANT THROUGHOUT THIS STRATUM. IF LEFT BLANK, THE P-Y DATA WILL VARY LINEARLY TO THE TOP OF THE NEXT STRATUM.   
(37-40) ENTER THE "P" FACTOR FOR THIS P-Y CURVE. THIS FACTOR IS USED TO MODIFY THE INPUT "P" VALUES FOR THIS SOIL STRATUM.   
(41-44) ENTER THE AMOUNT TO BE ADDED TO THE INPUT "Y" VALUES. THIS IN EFFECT SHIFTS THE P-Y CURVE ALONG THE Y-AXIS. THIS SHIFT CAN BE USED WITH BOTH SYMMETRICAL AND NONSYMMETRICAL INPUT CURVES AND IS USEFUL FOR MODELING MUDSLIDES.   
(45-60) ENTER ANY DESCRIPTIVE REMARKS ABOUT THIS SOIL STRATUM.   
(70-76) ENTER A HIGH PRECISION "P" FACTOR FOR THIS P-Y CURVE. THIS



| LINE LABEL | LINE TYPE | SYMMETRY INDICATOR | NUMBER OF POINTS PER CURVE | STRATUM LOCATION | STRATUM LOCATION | P FACTOR | Y SHIFT | SOIL DESCRIPTION OR OTHER REMARKS | HIGH PRECISION P FACTOR | LEAVE BLANK |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | LINE TYPE | SYMMETRY INDICATOR | NUMBER OF POINTS PER CURVE | TOP | BOTTOM | P FACTOR | Y SHIFT | SOIL DESCRIPTION OR OTHER REMARKS | HIGH PRECISION P FACTOR | LEAVE BLANK |
| SOIL | SLOC |  |  |  |  |  |  |  |  |  |
| 1--4 | 14--17 | 18--19 | 22--->23 | 25<--30 | 31<--36 | 37<--40 | 41<--44 | 45--60 | 70--76 | 77--80 |
| DEFAULT |  |  |  |  |  | 1 | 0 |  | 1 |  |
| ENGLISH |  |  |  | FT | FT |  | IN |  |  |  |
| METRIC |  |  |  | M | M |  | CM |  |  |  |



SOIL P-Y DATA LINE

COLUMNS

COMMENTARY

GENERAL THIS LINE IS USED TO INPUT THE LATERAL FORCE-DISPLACEMENT (P-Y) DATA FOR EACH SOIL STRATUM. IF A SYMMETRICAL P-Y CURVE IS ENTERED ('SM' IN COLUMNS 18-19 OF THE PRECEDING P-Y STRATUM LINE) ONLY THE POSITIVE HALF OF THE P-Y CURVE SHOULD BE ENTERED, THE FIRST POINT IN THIS CASE MUST BE THE ORIGIN (P=0.0, Y=0.0). THE DATA MUST BE ENTERED IN ORDER OF INCREASING VALUES OF THE DISPLACEMENT, Y.

FOR VALUES OF Y GREATER THAN THE LARGEST SPECIFIED VALUE OR SMALLER THAN THE SMALLEST SPECIFIED VALUE THE VALUE OF P IS ASSUMED TO BE CONSTANT AND EQUAL TO THE VALUE CORRESPONDING TO THOSE Y VALUES.

( 1- 4) ENTER 'SOIL'.   
(14-16) ENTER 'P-Y'.   
(18-77) ENTER THE "P" AND "Y" VALUES TO DESCRIBE THE P-Y CURVE. THIS LINE MAY BE REPEATED AS NECESSARY TO ENTER THE NUMBER OF POINTS SPECIFIED ON THE PRECEDING P-Y STRATUM LINE ('SOIL SLOC' LINE SET).



| LINE LABEL | LINE TYPE | P-Y CURVE DATA POINTS | P-Y CURVE DATA POINTS | P-Y CURVE DATA POINTS | P-Y CURVE DATA POINTS | P-Y CURVE DATA POINTS | P-Y CURVE DATA POINTS | P-Y CURVE DATA POINTS | P-Y CURVE DATA POINTS | P-Y CURVE DATA POINTS | P-Y CURVE DATA POINTS |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | LINE TYPE | 1ST POINT | 1ST POINT | 2ND POINT | 2ND POINT | 3RD POINT | 3RD POINT | 4TH POINT | 4TH POINT | 5TH POINT | 5TH POINT |
| LINE LABEL | LINE TYPE | P | Y | P | Y | P | Y | P | Y | P | Y |
| SOIL | P-Y |  |  |  |  |  |  |  |  |  |  |
| 1-- 4 | 14--16 | 18<--23 | 24<--29 | 30<--35 | 36<--41 | 42<--47 | 48<--53 | 54<--59 | 60<--65 | 66<--71 | 72<--77 |
| DEFAULT |  |  |  |  |  |  |  |  |  |  |  |
| ENGLISH |  | KIP/IN | IN | KIP/IN | IN | KIP/IN | IN | KIP/IN | IN | KIP/IN | IN |
| METRIC (KN) |  | KN/CM | CM | KN/CM | CM | KN/CM | CM | KN/CM | CM | KN/CM | CM |
| METRIC (KG) |  | KG/CM | CM | KG/CM | CM | KG/CM | CM | KG/CM | CM | KG/CM | CM |



SOIL LIQUEFACTION HEADER LINE

COLUMNS

COMMENTARY

GENERAL

THIS LINE IS USED TO SPECIFY THE NUMBER OF SOIL STRATA ANDTHE SOIL IDENTIFIER FOR LIQUEFACTION DESCRIPTION. IT ISFOLLOWED BY SOIL LIQUEFACTION STRATUM LINES.LIQUEFACTION OF SOIL ACCOUNTS FOR REDUCTION IN SOIL SHEARSTRENGTH RESULTING FROM THE BUILDING UP OF PORE PRESSURE INSATURATED SANDY SOILS DUE TO SEVERE EARTHQUAKE SHAKING.THIS DATA SET WILL AUTOMATICALLY CALCULATE THE POTENTIAL FOLIQUEFACTION IN A SOIL STARTUM AND CHNAGE THE SOIL SKINFRICTION AND LATERAL LOAD RESISTANCE PROPERTIES ACCORDINGLY.

THE SEQUENCE OF LINES REQUIRED FOR A LIQUEFACTION DESCRIPTION IS AS FOLLOWS:

1. SOIL LIQUEFACTION HEADER LINE.   
2. SOIL LIQUEFACTION DETAILS FOR EACH STRATUM.

COLUMNS

COMMENTARY

( 1- 4) ENTER 'SOIL'.   
( 6-12) ENTER 'LIQUEFY'.   
(14-17) ENTER 'HEAD'.   
(18-20) ENTER THE NUMBER OF SOIL STRATA FOR THIS DESCRIPTION.   
(21-26) ENTER THE VALUE OF HORIZONTAL SHIFT (%) IN CYCLIC RESISTANCE RATIO (CRR) CURVE. DEFAULT VALUE IS ZERO. ENTER A +VE VALUE FOR AN UNCONSERVATIVE AND A -VE VALUE FOR A CONSERVATIVE ESTIMATE OF THE LIQUEFACTION FACTOR OF SAFETY.   
(27-32) ENTER THE VALUE OF VERTICAL SHIFT (%) IN CYCLIC RESISTANCE RATIO (CRR) CURVE. DEFAULT VALUE IS ZERO. ENTER A +VE VALUE FOR AN UNCONSERVATIVE AND A -VE VALUE FOR A CONSERVATIVE ESTIMATE OF THE LIQUEFACTION FACTOR OF SAFETY.   
(34-36) ENTER THE VALUE OF EARTHQUAKE MAGNITUDE. THE VALUE SHOULD BE BETWEEN 5.5 AND 8.5. DEFAULT IS 7.5.   
(37-40) ENTER THE VALUE OF PEAK GROUND ACCELEATION AS A FRACTION OF GRA VITY. THE VALUE SHOULD BE BETWEEN 0.0 AND 1.0. DEFAULT IS 0.5.   
(41-44) ENTER A SOIL TABLE IDENTIFIER. THIS IDENTIFIER IS USED ON ONE OR MORE 'PILE' LINES TO ASSOCIATE THIS SOIL TABLE WITH THOSE PILES.   
(45-50) ENTER A FACTOR THAT WILL SCALE THE CALCULATED LIQUEFACTION MULTIPLIER. THE VALUE SHOULD BE GREATER THAN ZERO. DEFAULT VALUE IS 1.0.   
(51-60) ENTER ANY DESCRIPTIVE COMMENTS DESIRED.



| LINE LABEL | LIQUEFACTION LABEL | HEAD LABEL | NUMBER OF SOIL STRATA | PERCENT HORIZONTAL SHIFT IN CRR CURVE | PERCENT VERTICAL SHIFT IN CRR CURVE | (Mw) EARTHQUAKE MAGNITUDE | (amax) PEAK GROUND ACCELERATION | SOIL TABLE ID | LIQUEFACTION MULTIPLIER FACTOR | SOIL DESCRIPTION OR OTHER REMARKS |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOIL | LIQUEFY | HEAD |  |  |  |  |  |  |  |  |
| 1--4 | 6--12 | 14--17 | 18--->20 | 21--26 | 27--32 | 34--36 | 37--40 | 41--44 | 45--50 | 51--60 |
| DEFAULT |  |  |  | 0 | 0 | 7.5 | 0.5 |  | 1 |  |
| ENGLISH |  |  |  |  |  |  |  |  |  |  |
| METRIC |  |  |  |  |  |  |  |  |  |  |



SOIL LIQUEFACTION STRATUM LINE

COLUMNS

COMMENTARY

GENERAL THIS LINE SET IS USED TO SPECIFY THE SOIL AND EARQUAKE PROPERTIES. THE PROGRAM WILL USE THESE PROPERTIES TO CALCULATE LIQUEFACTION POTENTIAL OF EACH STRATUM AND MODIFY THE SOIL T-Z AND P-Y CURVES ACCORDINGLY.

( 1- 4) ENTER 'SOIL'.   
( 6-12) ENTER 'LIQUEFY'.   
(14-17) ENTER 'SLOC'.   
( 18 ) ENTER 'A' FOR STRATUM ABOVE THE WATER TABLE. ENTER 'B' OR LEAVE BLANK FOR STRATUM BELOW THE WATER TABLE.   
(19-30) ENTER THE DISTANCES FROM THE PILEHEAD TO THE TOP AND BOTTOM OF THIS SOIL STRATUM. THESE DISTANCES ARE VERTICALLY DOWN AND NOT ALONG THE AXIS OF THE PILE, WHICH MAY BE BATTERED.

COLUMNS

COMMENTARY

(31-33) ENTER 'CPT' TO USE CPT BASED METHOD. ENTER 'N ' IF LIQUEFACTION IS NOT TO BE CONSIDERED FOR THIS STRATUM.   
(34-37) ENTER 'SAND', 'CLAY', OR 'SILT'. LEAVE BLANK IF SOIL TYPE IS NOT KNOWN. SOIL TYPE 'CLAY' WOULD MEAN NO LIQUEFACTION IN THIS STRATUM.   
(45-50) ENTER THE CONE TIP RESISTANCE FOR THE STRATUM.   
(51-56) ENTER THE SLEEVE FRICTION FOR THE STRATUM.   
(57-62) ENTER THE SEBMERGED UNIT WEIGHT.



| LINE LABEL | LIQUEFACTION LABEL | LINE TYPE | WATER TABLE | TOP OF STRATUM | BOTTOM OF STRATUM | CALCULATION METHOD | SOIL TYPE | CONE TIP RESISTANCE | SLEEVE FRICTION | SEBMERGED UNIT WEIGHT |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOIL | LIQUEFY | SLOC |  |  |  |  |  |  |  |  |
| 1--4 | 6--12 | 14--17 | 18 | 19<--24 | 25<--30 | 31--33 | 34--37 | 45<--50 | 51<--56 | 57<--62 |
| DEFAULT |  |  | 'B' |  |  | 'CPT' |  |  |  |  |
| ENGLISH |  |  |  | FT | FT |  |  | KSI | KSI | LB/CU.FT |
| METRIC (KN) |  |  |  | M | M |  |  | MPa | MPa | TONNE/CU.M |
| METRIC (KG) |  |  |  | M | M |  |  | KG/SQ.MM | KG/SQ.MM | TONNE/CU.M |



DEPTH LOADS DATA

COLUMNS

COMMENTARY

GENERAL

THIS DATA SET ENABLES THE APPLICATION OF FORCES AND MOMENTS AT A LOCATION BELOW THE PILEHEAD. THE FORCES AND MOMENTS ARE INPUT IN EITHER LOCAL OR GLOBAL COORDINATES. THE GLOBAL COORDINATES ARE DEFINED AS 'Z' POSITIVE UP.

( 1- 6)

ENTER 'DEPLOD' ON EACH LINE IN THIS SET. EACH DEPLOD LINE WILL CREATE A PILE ANALYSIS.

( 7 )

SELECT THE PILEHEAD LOADING COORDINATE SYSTEM. 'L' - LOCAL 'G' - GLOBAL

( 8-14)

ENTER THE VERTICAL DEPTH RELATIVE TO MUDLINE WHERE THE LOADS ARE TO BE APPLIED.

(16-22)

FORCE IN X DIRECTION AT THIS DEPTH.

(23-29)

FORCE IN Y DIRECTION AT THIS DEPTH.

(30-36)

FORCE IN Z DIRECTION AT THIS DEPTH.

(37-43)

MOMENT ACTING IN X DIRECTION AT THIS DEPTH.

(44-50)

MOMENT ACTING IN Y DIRECTION AT THIS DEPTH.

(51-57)

MOMENT ACTING IN Z DIRECTION AT THIS DEPTH.

(71-75)

ENTER THE ALLOWABLE STRESS MODIFIER FOR THIS LOAD CASE OR THE NPD MATERIAL FACTOR. DEFAULTS ARE 1.0 AND 1.15, RESPECTIVELY.



| LINE LABEL | LOAD COORD. | DEPTH OF LOAD POINT | FORCES | FORCES | FORCES | MOMENTS | MOMENTS | MOMENTS | AMOD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | LOAD COORD. | DEPTH OF LOAD POINT | Fx | Fy | Fz | Mx | My | Mz | AMOD |
| DEPLED |  |  |  |  |  |  |  |  |  |
| 1--6 | 7 | 8<--14 | 16<--22 | 23<--29 | 30<--36 | 37<--43 | 44<--50 | 51<--57 | 71<--75 |
| DEFAULT | 'G' |  |  |  |  |  |  |  |  |
| ENGLISH |  | FT | KIP | KIP | KIP | KIP-IN | KIP-IN | KIP-IN |  |
| METRIC (KN) |  | M | KN | KN | KN | KN-M | KN-M | KN-M |  |
| METRIC (KG) |  | M | KG | KG | KG | KG-CM | KG-CM | KG-CM |  |



FATIGUE LOADS LINE

COLUMNS

COMMENTARY

GENERAL THIS LINE SET ENABLES THE APPLICATION OF FORCES AND MOMENTS OBTAINED FROM A SACS IV ANALYSIS TO CREATE A POSTFILE FOR THE PILE FOR SUBSEQUENT FATIGUE ANALYSIS.

( 1- 4) ENTER 'LOAD' ON EACH LINE IN THIS SET. EACH 'LOAD' LINE WILL CREATE A LOAD CASE ON THE OUTPUT POSTFILE.   
( 8-11) ENTER THE JOINT NAME TO IDENTIFY THE PILEHEAD JOINT FROM WHICH THESE LOADS ARE TAKEN. (OPTIONAL FOR USER CONVENIENCE ONLY.)   
(17-23) FORCE IN X DIRECTION ON THIS PILEHEAD.   
(24-30) FORCE IN Y DIRECTION ON THIS PILEHEAD.   
(31-37) FORCE IN Z DIRECTION ON THIS PILEHEAD.   
(38-44) MOMENT ACTING IN X DIRECTION ON THIS PILEHEAD.   
(46-52) MOMENT ACTING IN Y DIRECTION ON THIS PILEHEAD.   
(53-59) MOMENT ACTING IN Z DIRECTION ON THIS PILEHEAD.   
(61-64) ENTER 'GLOB' IF THE GLOBAL CARTESIAN COORDINATE SYSTEM IS TO BE USED. IN THIS CASE, THE COORDINATE SYSTEM IS DEFINED WITH 'X' ALONG THE PILE AXIS WITH POSITIVE DOWN. IF THE LOADS ARE TAKEN FROM AN INTERNAL LOADS REPORT FOR A MEMBER, THEN 'MEMB' SHOULD BE USED AND THE LOADS CAN BE TAKEN DIRECTLY FROM THE INTERNAL LOAD REPORT.   
(66-69) ENTER 'INTL' IF THE MEMBER INTERNAL LOADS COORDINATE SYSTEM IS BEING USED WITH THE TIMOSHENKO SIGN CONVENTION. OTHERWISE, LEAVE BLANK.   
(73-80) ENTER ANY REMARKS.



| LINE LABEL | JOINT NAME | PILEHEAD FORCE AND MOMENT DATA | PILEHEAD FORCE AND MOMENT DATA | PILEHEAD FORCE AND MOMENT DATA | PILEHEAD FORCE AND MOMENT DATA | PILEHEAD FORCE AND MOMENT DATA | PILEHEAD FORCE AND MOMENT DATA | COORD. SYSTEM | LOAD CONVENTION | REMARKS |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | JOINT NAME | FORCE | FORCE | FORCE | MOMENT | MOMENT | MOMENT | COORD. SYSTEM | LOAD CONVENTION | REMARKS |
| LINE LABEL | JOINT NAME | Fx | Fy | Fz | Mx | My | Mz | COORD. SYSTEM | LOAD CONVENTION | REMARKS |
| LOAD |  |  |  |  |  |  |  |  |  |  |
| 1-- 4 | 8-->11 | 17<--23 | 24<--30 | 31<--37 | 38<--44 | 46<--52 | 53<--59 | 61--64 | 66--69 | 73--80 |
| DEFAULT |  |  |  |  |  |  |  | 'GLOB' |  |  |
| ENGLISH |  | KIP | KIP | KIP | KIP-IN | KIP-IN | KIP-IN |  |  |  |
| METRIC (KN) |  | KN | KN | KN | KN-M | KN-M | KN-M |  |  |  |
| METRIC (KG) |  | KG | KG | KG | KG-CM | KG-CM | KG-CM |  |  |  |



AXIAL LOAD VERSUS DEFLECTION LINE

COLUMNS

COMMENTARY

GENERAL

THIS LINE IS USED TO CALCULATE THE AXIAL COMPRESSION AND TENSION PILEHEAD LOADS VERSUS DEFLECTION.

( 7-10)

ENTER THE NUMBER OF INCREMENTS THAT THE PILEHEAD AXIAL LOAD VERSUS DEFLECTION IS TO BE CALCULATED.

(11-20)

ENTER THE MAXIMUM AXIAL DEFLECTION FOR THE PILEHEAD.



| LINE LABEL | NUMBER OF DEFLECTION INCREMENTS | MAXIMUM AXIAL DEFLECTION | LEAVE THIS FIELD BLANK |
| --- | --- | --- | --- |
| LODFL |  |  |  |
| 1--5 | 7-->10 | 11<--20 | 21--------80 |
| DEFAULT |  |  |  |
| ENGLISH |  | IN |  |
| METRIC |  | CM |  |



LATERAL LOAD VERSUS DEFLECTION LINE

COLUMNS

COMMENTARY

GENERAL THIS LINE IS USED TO CALCULATE THE LATERAL PILEHEAD LOAD VERSUS DEFLECTION FOR BOTH (i) ZERO MOMENT AND (ii) ZERO ROTATION PILEHEAD BOUNADRY CONDITIONS. THE LATERAL LOADS CAN BE CALCULATED IN CONJUNCTION WITH EITHER (i) AN AXIAL LOAD THAT IS APPLIED AT THE PILEHEAD OR (ii) A PRESCRIBED PILEHEAD AXIAL DEFLECTION.

( 7-10) ENTER THE NUMBER OF INCREMENTS FOR WHICH THE PILEHEAD LATERAL LOAD VERSUS DEFLECTION IS TO BE CALCULATED.   
(11-20) ENTER THE MAXIMUM LATERAL DEFLECTION FOR THE PILEHEAD.   
(41-60) ENTER EITHER THE PRESCRIBED AXIAL LOAD OR DEFLECTION, BUT NOT BOTH. DEFAULT IS NO LOAD OR DISPLACEMENT.   
(41-50) ENTER THE AXIAL LOAD.   
(51-60) ENTER THE AXIAL DEFLECTION.



| LINE LABEL | NUMBER OF DEFLECTION INCREMENTS | MAXIMUM LATERAL DEFLECTION | SPECIFIED AXIAL LOAD | SPECIFIED AXIAL DEFLECTION | LEAVE THIS FIELD BLANK |
| --- | --- | --- | --- | --- | --- |
| LTDFL |  |  |  |  |  |
| 1--5 | 7-->10 | 11<--20 | 41--50 | 51--60 | 61--------80 |
| DEFAULT |  |  |  |  |  |
| ENGLISH |  | IN | KIPS | IN |  |
| METRIC |  | CM | KN | CM |  |



PILEHEAD SPRING DATA

COLUMNS

COMMENTARY

GENERAL

THIS LINE IS USED TO MODEL ELASTIC BOUNDARY CONDITIONS AT THEPILEHEAD USING TRANSLATIONAL AND ROTATIONAL SPRINGS. THESESPRINGS WILL BE USED UNTIL ANOTHER PHSPG OR PLSPRG LINE ISENCOUNTERED. THE SPRING COORDINATES ARE IN THE PILE LOCALCOORDINATES.

( 7-10)

ENTER THE SOIL IDENTIFIER FOR THE PILES CONNECTING TO THESE SPRINGS.

(11-20)

TRANSLATIONAL SPRING IN X DIRECTION

(21-30)

TRANSLATIONAL SPRING IN Y DIRECTION

(31-40)

TRANSLATIONAL SPRING IN Z DIRECTION

(41-50)

ROTATIONAL SPRING IN X DIRECTION

(51-60)

ROTATIONAL SPRING IN Y DIRECTION

(61-70)

ROTATIONAL SPRING IN Z DIRECTION



| LINE LABEL | SOIL ID | TRANSLATIONAL SPRINGS | TRANSLATIONAL SPRINGS | TRANSLATIONAL SPRINGS | ROTATIONAL SPRINGS | ROTATIONAL SPRINGS | ROTATIONAL SPRINGS | LEAVE BLANK |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | SOIL ID | Fx | Fy | Fz | Mx | My | Mz | LEAVE BLANK |
| PHSPG |  |  |  |  |  |  |  |  |
| 1-- 5 | 7--10 | 11<--20 | 21<--30 | 31<--40 | 41<--50 | 51<--60 | 61<--70 | 71<--80 |
| DEFAULT |  |  |  |  |  |  |  |  |
| ENGLISH |  | KIP/IN | KIP/IN | KIP/IN | KIP-IN/RAD | KIP-IN/RAD | KIP-IN/RAD |  |
| METRIC (KN) |  | KN/M | KN/M | KN/M | KN-M/RAD | KN-M/RAD | KN-M/RAD |  |
| METRIC (KG) |  | KG/CM | KG/CM | KG/CM | KG-CM/RAD | KG-CM/RAD | KG-CM/RAD |  |



PILE CAPACITY VERSUS LENGTH

COLUMNS

COMMENTARY

GENERAL THIS RECORD IS USED TO SPECIFY THAT AN ANALYSIS OF PILE CAPACITIES VERSUS PILE LENGTH IS TO BE PERFORMED.

( 1- 5) ENTER 'PLCAP'. THE PROGRAM WILL AUTOMATICALLY CHANGE THE PILE LENGTH BY ADDING ONE INCREMENT AT A TIME STARTING AT ZERO AND RECOMPUTING THE PILE CAPACITY. THE PILE CAPACITY VERSUS LENGTH IS AUTOMATICALLY PLOTTED.

( 7-10) ENTER THE NUMBER OF INCREMENTS.



| LINE LABEL | NUMBER OF INCREMENTS | LEAVE BLANK |
| --- | --- | --- |
| PLCAP |  |  |
| 1-- 5 | 7-->10 | 11--------80 |
| DEFAULT | 50 |  |



PILEHEAD LOAD LINE

COLUMNS

COMMENTARY

GENERAL THIS LINE IS USED TO SPECIFY THE LOADS OR DEFORMATIONS THAT ARE PRESCRIBED AT THE PILEHEAD. AS MANY 'PLLOAD' LINES AS DESIRED MAY BE INPUT. EACH OF THESE LINES DEFINES A LOAD CASE, SO THAT MANY LOAD CONDITIONS ON A GIVEN PILE-SOIL SYSTEM CAN BE RUN WITHOUT HAVING TO REENTER THE SOIL OR PILE PROPERTIES.

( 1- 6) ENTER 'PLLOAD'. THE FIRST OF THESE LINES IS A HEADER HAVING ONLY THIS ENTRY.   
( 10 ) ENTER 'F' OR 'D' IF A PILEHEAD LATERAL FORCE OR DISPLACEMENT IS PRESCRIBED.   
( 11 ) ENTER 'M' OR 'R' IF A PILEHEAD BENDING MOMENT OR ROTATION IS PRESCRIBED.   
(21-30) ENTER THE PRESCRIBED PILEHEAD LATERAL FORCE OR DISPLACEMENT, DEPENDING ON WHETHER 'F' OR 'D' APPEARS IN COLUMN 10. DEFAULT IS 0.0.

COLUMNS

COMMENTARY

(31-40) ENTER THE PRESCRIBED PILEHEAD BENDING MOMENT OR ROTATION, DEPENDING ON WHETHER 'M' OR 'R' APPEARS IN COLUMN 11. DEFAULT IS 0.0.   
(41-60) ENTER EITHER THE PRESCRIBED AXIAL LOAD OR DEFLECTION, BUT NOT BOTH. DEFAULT IS NO LOAD OR DISPLACEMENT.   
(62-70) UNDER SOME CONDITIONS OF LARGE DISPLACEMENTS AND/OR UNUSUAL SOIL CONDITIONS CONVERGENCE OF THE LATERAL OR AXIAL PILE SOLUTION MAY BE DIFFICULT TO ACHIEVE IN A REASONABLE NUMBER OF ITERATIONS. UNDER THESE CIRCUMSTANCES ONE MAY BE ABLE TO OBTAIN THE SOLUTION BY RUNNING SEVERAL LOAD CASES WITH THE PILEHEAD LOADS OR DISPLACEMENTS GRADUALLY INCREASED IN EACH LOAD CASE AND USING THE PREVIOUS LOAD CASE SOLUTION AS THE INITIAL VALUE FOR THE PRESENT ANALYSIS.

ENTER 'PREV' TO USE THE RESULTS OF THE PREVIOUS LOAD CASE AS INITIAL VALUES FOR THE PRESENT LOAD CASE FOR EITHER THE LATERAL OR AXIAL SOLUTION OR BOTH.

(71-75) ENTER THE ALLOWABLE STRESS MODIFIER FOR THIS LOAD CASE OR THE NPD MATERIAL FACTOR. DEFAULTS ARE 1.0 AND 1.15, RESPECTIVELY.



| LINE LABEL | FORCE OR DISPLACEMENT | MOMENT OR ROTATION | PILEHEAD LATERAL LOADING CONDITION | PILEHEAD LATERAL LOADING CONDITION | PILEHEAD AXIAL LOADING CONDITION | PILEHEAD AXIAL LOADING CONDITION | START FROM PREVIOUS SOLUTION | START FROM PREVIOUS SOLUTION | AMOD OR MATERIAL FACTOR |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | FORCE OR DISPLACEMENT | MOMENT OR ROTATION | LATERAL LOAD OR DISPLACEMENT | MOMENT OR ROTATION | AXIAL LOAD | AXIAL DISPLACEMENT | LATERAL | AXIAL | AMOD OR MATERIAL FACTOR |
| PLLOAD |  |  |  |  |  |  |  |  |  |
| 1--6 | 10 | 11 | 21<--30 | 31<--40 | 41<--50 | 51<--60 | 62--65 | 67--70 | 71--75 |
| DEFAULT |  |  | 0 | 0 | 0 | 0 |  |  |  |
| ENGLISH |  |  | KIP OR IN | KIP-IN OR RAD | KIP | IN |  |  |  |
| METRIC (KN) |  |  | KN OR CM | KN-M OR RAD | KN | CM |  |  |  |
| METRIC (KG) |  |  | KG OR CM | KG-CM OR RAD | KG | CM |  |  |  |



PILEHEAD 3D LOAD LINE

COLUMNS

COMMENTARY

GENERAL THIS RECORD IS USED TO SPECIFY THE LOADS OR DEFORMATIONS THAT ARE PRESCRIBED AT THE PILEHEAD. AS MANY PLOD3D RECORDS AS DESIRED MAY BE INPUT. EACH OF THESE RECORDS DEFINES A LOAD CASE, SO THAT MANY LOAD CONDITIONS ON A GIVEN PILE-SOIL SYSTEM CAN BE EXECUTED WITHOUT HAVING TO REENTER THE SOIL OR PILE PROPERTIES.

ALL PILEHEAD LOADS OR DISPLACEMENTS ARE INPUT IN THE PILE LOCAL COORDINATE SYSTEM. THE LOCAL X COORDINATE IS DOWNWARD ALONG THE PILE. THE Y AND Z LOCAL COORDINATE ARE PERPENDICULAR TO THE PILE.

( 1- 6) ENTER 'PLOD3D'.   
( 11 ) ENTER 'F' OR 'D' IF A PILEHEAD AXIAL FORCE OR DISPLACEMENT IS PRESCRIBED.   
(12-18) ENTER THE AXIAL FORCE OR AXIAL DISPLACEMENT. POSITIVE IS DOWN.   
( 19 ) ENTER 'F' OR 'D' IF A PILEHEAD LATERAL FORCE OR DISPLACEMENT IS PRESCRIBED IN THE Y-DIRECTION.   
(20-26) ENTER THE LATERAL Y FORCE OR LATERAL Y DISPLACEMENT.   
( 27 ) ENTER 'F' OR 'D' IF A PILEHEAD LATERAL FORCE OR DISPLACEMENT IS PRESCRIBED IN THE Z-DIRECTION.

COLUMNS

COMMENTARY

(28-34) ENTER THE LATERAL Z FORCE OR LATERAL Z DISPLACEMENT.

( 35 ) ENTER 'M' OR 'R' IF A PILEHEAD TORSION MOMENT OR ROTATION IS PRESCRIBED.   
(36-42) ENTER THE TORSION MOMENT OR TORSIONAL ROTATION.   
( 43 ) ENTER 'M' OR 'R' IF A PILEHEAD MOMENT OR ROTATION IS PRESCRIBED ABOUT THE PILEHEAD Y-AXIS.   
(44-50) ENTER THE MOMENT OR ROTATION ABOUT THE PILEHEAD Y-AXIS.   
( 51 ) ENTER 'M' OR 'R' IF A PILEHEAD MOMENT OR ROTATION IS PRESCRIBED ABOUT THE PILEHEAD Z-AXIS.   
(52-58) ENTER THE MOMENT OR ROTATION ABOUT THE PILEHEAD Z-AXIS.   
(71-75) ENTER THE ALLOWABLE STRESS MODIFIER FOR THIS LOAD CASE OR THE NPD MATERIAL FACTOR. DEFAULTS ARE 1.0 AND 1.15, RESPECTIVELY.



| LINE LABEL | FORCES AND DISPLACEMENTS | FORCES AND DISPLACEMENTS | FORCES AND DISPLACEMENTS | FORCES AND DISPLACEMENTS | FORCES AND DISPLACEMENTS | FORCES AND DISPLACEMENTS | MOMENTS AND ROTATIONS | MOMENTS AND ROTATIONS | MOMENTS AND ROTATIONS | MOMENTS AND ROTATIONS | MOMENTS AND ROTATIONS | MOMENTS AND ROTATIONS | LEAVE BLANK | AMOD OR MATERIAL FACTOR |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | AXIAL | AXIAL | LATERAL Y | LATERAL Y | LATERAL Z | LATERAL Z | TORSION | TORSION | Y-Axis | Y-Axis | Z-Axis | Z-Axis | LEAVE BLANK | AMOD OR MATERIAL FACTOR |
| LINE LABEL | 'F' OR 'D' | FORCE OR DISPLACEMENT | 'F' OR 'D' | FORCE OR DISPLACEMENT | 'F' OR 'D' | FORCE OR DISPLACEMENT | 'M' OR 'R' | MOMENT OR ROTATION | 'M' OR 'R' | MOMENT OR ROTATION | 'M' OR 'R' | MOMENT OR ROTATION | LEAVE BLANK | AMOD OR MATERIAL FACTOR |
| PLOD3D |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 1--6 | 11 | 12<--18 | 19 | 20<--26 | 27 | 28<--34 | 35 | 36<--42 | 43 | 44<--50 | 51 | 52<--58 | 59--70 | 71--75 |
| DEFAULT |  | 0 |  | 0 |  | 0 |  | 0 |  | 0 |  | 0 |  |  |
| ENGLISH |  | KIP OR IN |  | KIP OR IN |  | KIP OR IN |  | KIP-IN OR RAD |  | KIP-IN OR RAD |  | KIP-IN OR RAD |  |  |
| METRIC (KN) |  | KN OR CM |  | KN OR CM |  | KN OR CM |  | KN-M OR RAD |  | KN-M OR RAD |  | KN-M OR RAD |  |  |
| METRIC (KG) |  | KG OR CM |  | KG OR CM |  | KG OR CM |  | KG-CM OR RAD |  | KG-CM OR RAD |  | KG-CM OR RAD |  |  |



PILEHEAD SPRING LINE

COLUMNS

COMMENTARY

GENERAL

THIS LINE IS USED TO MODEL ELASTIC BOUNDARY CONDITIONS AT THE PILEHEAD USING TRANSLATIONAL AND ROTATIONAL SPRINGS. SPRINGS MAY BE INTRODUCED IN THE LATERAL DIRECTION AND FOR ROTATION IN THE PLANE OF THE PILE DEFORMATION.

( 1- 6)

ENTER 'PLSPRG'. THE FIRST LINE IS A HEADER HAVING ONLY THIS ENTRY.

(11-18)

ENTER 'LATERAL ' OR 'ROTATION' IF THIS IS A TRANSLATIONAL OR ROTATIONAL SPRING.

(21-30)

ENTER THE SPRING STIFFNESS.

(31-50)

IF THERE IS A SECOND SPRING, ENTER ITS CHARACTERISTICS HERE.



| LINE LABEL | FIRST PILLEHEAD SPRING | FIRST PILLEHEAD SPRING | SECOND PILLEHEAD SPRING | SECOND PILLEHEAD SPRING | LEAVE THIS FIELD BLANK |
| --- | --- | --- | --- | --- | --- |
| LINE LABEL | SPRING TYPE | SPRING CONSTANT | SPRING TYPE | SPRING CONSTANT | LEAVE THIS FIELD BLANK |
| PLSPRG |  |  |  |  |  |
| 1-- 6 | 11<--18 | 21<--30 | 31<--38 | 41<--50 | 51----80 |
| DEFAULT |  |  |  |  |  |
| ENGLISH |  | KIP/IN OR KIP-IN/RAD |  | KIP/IN OR KIP-IN/RAD |  |
| METRIC(KN) |  | KN/M OR KN-M/RAD |  | KN/M OR KN-M/RAD |  |
| METRIC(KG) |  | KG/CM OR KG-CM/RAD |  | KG/CM OR KG-CM/RAD |  |



PILE STUB DESIGN LINE

COLUMNS

COMMENTARY

GENERAL THIS LINE IS USED TO SPECIFY THE LOADS OR DEFORMATIONS THAT ARE TO BE USED TO CALCULATE AN EQUIVALENT PILE STUB THAT WILL GIVE THE SAME DEFLECTIONS AND ROTATIONS AS THE PILE FOR THESE LOADS.

( 10 ) THE EQUIVALENT PILE STUB CAN BE CALCULATED USING A FORCE AND A MOMENT OR USING A DEFLECTION AND A ROTATION. IF THE FORCE AND MOMENT ARE TO BE ENTERED, INPUT AN 'F'. OTHERWISE, INPUT A 'D' FOR DEFLECTION AND ROTATION.   
(11-14) ENTER THE JOINT NAME TO BE USED FOR THE LOWER END OF THE PILE STUB. THIS NAME IS ONLY USED ON THE SAMPLE SACS IV INPUT LINES AND WILL NOT AFFECT THE PILE STUB CALCULATIONS.   
( 15 ) SELECT THE PILE STUB METHOD FROM THE FOLLOWING:

'0' - INCLUDE OFF-DIAGONAL TERMS.

'1' - INCLUDE OFF-DIAGONAL TERMS AND ADJUST FOR

MOMENT/SHEAR INTERACTION.

'2' - IGNORE OFF-DIAGONAL TERMS.

COLUMNS

COMMENTARY

(21-30) ENTER THE PRESCRIBED PILEHEAD LATERAL FORCE OR DISPLACEMENT, DEPENDING ON WHETHER 'F' OR 'D' APPEARS IN COLUMN 10. DO NOT LEAVE BLANK OR ENTER '0.'. IF A PILE STUB IS TO BE CALCULATED FOR THE LINEAR RANGE, ENTER A SMALL BUT REASONABLE VALUE.   
(31-40) ENTER THE PRESCRIBED PILEHEAD BENDING MOMENT OR ROTATION, DEPENDING ON WHETHER 'F' OR 'D' APPEARS IN COLUMN 10. DO NOT LEAVE BLANK OR ENTER '0.'. THE PROGRAM NEEDS TO HAVE A NONZERO VALUE TO CALCULATE STIFFNESS.   
(41-60) ENTER EITHER THE PRESCRIBED AXIAL LOAD OR DEFLECTION, BUT NOT BOTH. SINCE THE AXIAL LOAD OR DISPLACEMENT VALUE WILL BE USED TO CALCULATE THE PILEHEAD AXIAL STIFFNESS, DO NOT ENTER A '0.' OR LEAVE BLANK.



| LINE LABEL | FORCE AND MOMENT OR DEFLECTION AND ROTATION | PILE STUB JOINT NAME | ANALYSIS METHOD | PILEHEAD LATERAL LOADING CONDITION | PILEHEAD LATERAL LOADING CONDITION | PILEHEAD AXIAL LOADING CONDITION | PILEHEAD AXIAL LOADING CONDITION | LEAVE BLANK |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | FORCE AND MOMENT OR DEFLECTION AND ROTATION | PILE STUB JOINT NAME | ANALYSIS METHOD | LATERAL LOAD OR DISPLACEMENT | MOMENT OR ROTATION | AXIAL LOAD | AXIAL DISPLACEMENT | LEAVE BLANK |
| PLSTUB |  |  |  |  |  |  |  |  |
| 1--6 | 10 | 11-->14 | 15 | 21<!--30 | 31<!--40 | 41<!--50 | 51<!--60 | 61--80 |
| DEFAULT |  |  |  | 0 | 0 | 0 | 0 |  |
| ENGLISH |  |  |  | KIP OR IN | KIP-IN OR RAD | KIP | IN |  |
| METRIC (KN) |  |  |  | KN OR CM | KN-M OR RAD | KN | CM |  |
| METRIC (KG) |  |  |  | KG OR CM | KG-CM OR RAD | KG | CM |  |



SOIL TORSION ADHESION HEADER LINE

COLUMNS

COMMENTARY

COLUMNS

COMMENTARY

GENERAL EITHER THIS LINE FOLLOWED BY 'SLOC' AND CAPACITY LINE SETS,OR TORSION SPRING LINE SHOULD BE INCLUDED IN ANY PSI INPUTFILE.

THIS LINE IS USED TO MODEL THE TORSIONAL RESISTANCE OF THEPILE RESULTING FROM ADHESION OF THE SURROUNDING SOIL.

STARTING AT THE TOP STRATUM THE LENGTH OVER WHICH THE ADHESION MUST ACT TO TRANSFER THE PILE TORQUE TO THE SOIL IS COMPUTED. IF THIS LENGTH IS LESS THAN THE THICKNESS OF THE STRATUM, THE TORQUE IS COMPLETELY TRANSFERRED TO THE SOIL OVER THAT LENGTH. IF THE COMPUTED LENGTH IS GREATER THAN THE STRATUM THICKNESS THE TORQUE IS ONLY PARTIALLY TRANSFERRED IN THAT STRATUM. THE EXCESS PILE TORQUE IS TRANSFERRED IN THE NEXT DEEPER SOIL STRATUM. THE PROCEDURE IS REPEATED FOR EACH STRATUM IN TURN UNTIL THE ENTIRE PILE TORQUE IS TRANSFERRED OR UNTIL ALL SOIL STRATA HAVE REACHED THEIR CAPACITIES.

IF THE PILE TORQUE HAS NOT BEEN TRANSFERRED AFTER ALL STRATA HAVE REACHED THEIR CAPACITIES THE PILE FAILS IN TORSION AND A REPORT TO THAT EFFECT IS ISSUED.

THIS SOIL MODEL TAKES NO ACCOUNT OF SOIL DEFORMATIONS. THE TORSIONAL ROTATION AT THE PILEHEAD IS TAKEN TO BE EQUAL TO THE ELASTIC TWIST OF THE PILE.

( 1- 4) ENTER 'SOIL'.   
( 6-12) ENTER 'TORSION'.   
(14-17) ENTER 'HEAD'.   
(18-20) ENTER THE NUMBER OF SOIL STRATA TO BE DESCRIBED ON THE FOLLOWING LINES ('SOIL SLOC' AND 'SOIL' LINE SETS).   
(41-44) ENTER AN ALPHANUMERIC SOIL TABLE IDENTIFIER. THIS IDENTIFIER IS USED ON ONE OR MORE 'PILE' LINES TO ASSOCIATE THIS SOIL TABLE WITH THOSE PILES.   
(45-60) ENTER ANY DESCRIPTIVE REMARKS DESIRED.



| LINE LABEL | TORSION LABEL | HEAD LABEL | NUMBER OF SOIL STRATA | SOIL TABLE ID | SOIL DESCRIPTION OR OTHER REMARKS | LEAVE BLANK |
| --- | --- | --- | --- | --- | --- | --- |
| SOIL | TORSION | HEAD |  |  |  |  |
| 1--4 | 6--12 | 14--17 | 18--->20 | 41<-44 | 45------60 | 61--80 |



SOIL TORSIONAL ADHESION STRATA LINE

COLUMNS

COMMENTARY

LOCATION THIS LINE SET FOLLOWS TORSION HEADER LINE AND IS FOLLOWED BY THE USER INPUT TORSION DATA.

GENERAL THE TORSIONAL ADHESION STRATA LOCATIONS ARE DEFINED USING THIS LINE. THESE STRATA LOCATIONS ARE MEASURED FROM THE PILEHEAD. FIVE STRATA ARE INPUT PER LINE AND THIS LINE IS REPEATED UNTIL THE NUMBER OF STRATA DESIGNATED ON THE SOIL TORSION ADHESION HEADER LINE HAVE BEEN DESCRIBED.

( 1- 4) ENTER 'SOIL'.   
(14-17) ENTER 'SLOC'.   
(19-78) ENTER THE DISTANCES FROM THE PILEHEAD TO THE TOP AND BOTTOM OF EACH STRATUM. THE LOCATION OF THE BOTTOM OF THE LAST STRATUM ENTERED MUST BE AT LEAST TO THE BOTTOM OF THE DEEPEST PILE TO WHICH THIS TABLE APPLIES. THE LOCATION OF THE TOP OF A STRATUM MUST BE THE SAME AS THE BOTTOM OF THE PRECEDING STRATUM. THESE DISTANCES ARE VERTICALLY DOWN AND NOT ALONG THE AXIS OF THE PILE, WHICH MAY BE BATTERED.



| LINE LABEL | LINE TYPE | TORSIONAL ADHESION STRATA LOCATIONS | TORSIONAL ADHESION STRATA LOCATIONS | TORSIONAL ADHESION STRATA LOCATIONS | TORSIONAL ADHESION STRATA LOCATIONS | TORSIONAL ADHESION STRATA LOCATIONS | TORSIONAL ADHESION STRATA LOCATIONS | TORSIONAL ADHESION STRATA LOCATIONS | TORSIONAL ADHESION STRATA LOCATIONS | TORSIONAL ADHESION STRATA LOCATIONS | TORSIONAL ADHESION STRATA LOCATIONS |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | LINE TYPE | 1ST STRATUM | 1ST STRATUM | 2ND STRATUM | 2ND STRATUM | 3RD STRATUM | 3RD STRATUM | 4TH STRATUM | 4TH STRATUM | 5TH STRATUM | 5TH STRATUM |
| LINE LABEL | LINE TYPE | TOP | BOTTOM | TOP | BOTTOM | TOP | BOTTOM | TOP | BOTTOM | TOP | BOTTOM |
| SOIL | SLOC |  |  |  |  |  |  |  |  |  |  |
| 1-- 4 | 14--17 | 19<--24 | 25<--30 | 31<--36 | 37<--42 | 43<--48 | 49<--54 | 55<--60 | 61<--66 | 67<--72 | 73<--78 |
| DEFAULT |  |  |  |  |  |  |  |  |  |  |  |
| ENGLISH |  | FT | FT | FT | FT | FT | FT | FT | FT | FT | FT |
| METRIC |  | M | M | M | M | M | M | M | M | M | M |



SOIL TORSIONAL ADHESION CAPACITY LINE

COLUMNS

COMMENTARY

LOCATION THIS LINE SET FOLLOWS THE TORSION 'SLOC' LINE.

GENERAL THIS LINE SET IS USED TO ENTER THE TORSIONAL ADHESION CAPACITIES FOR THE TOP AND BOTTOM OF EACH STRATUM DEFINED BY THE TORSIONAL ADHESION STRATA LINES. THE ADHESION CAPACITY WITHIN A STRATUM IS CONSTANT AND EQUALS THE AVERAGE OF THE VALUES AT THE TOP AND BOTTOM OF THE STRATUM.

( 1- 4) ENTER 'SOIL'.

(19-78) ENTER THE ADHESION CAPACITIES AT THE TOP AND BOTTOM OF EACH STRATUM. IF MORE THAN FIVE STRATA ARE USED, REPEAT THIS LINE UNTIL ALL STRATA HAVE BEEN DEFINED.



| LINE LABEL | SOIL TORSIONAL ADHESION CAPACITIES | SOIL TORSIONAL ADHESION CAPACITIES | SOIL TORSIONAL ADHESION CAPACITIES | SOIL TORSIONAL ADHESION CAPACITIES | SOIL TORSIONAL ADHESION CAPACITIES | SOIL TORSIONAL ADHESION CAPACITIES | SOIL TORSIONAL ADHESION CAPACITIES | SOIL TORSIONAL ADHESION CAPACITIES | SOIL TORSIONAL ADHESION CAPACITIES | SOIL TORSIONAL ADHESION CAPACITIES |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | 1ST STRATUM | 1ST STRATUM | 2ND STRATUM | 2ND STRATUM | 3RD STRATUM | 3RD STRATUM | 4TH STRATUM | 4TH STRATUM | 5TH STRATUM | 5TH STRATUM |
| LINE LABEL | TOP | BOTTOM | TOP | BOTTOM | TOP | BOTTOM | TOP | BOTTOM | TOP | BOTTOM |
| SOIL |  |  |  |  |  |  |  |  |  |  |
| 1-- 4 | 19<--24 | 25<--30 | 31<--36 | 37<--42 | 43<--48 | 49<--54 | 55<--60 | 61<--66 | 67<--72 | 73<--78 |
| DEFAULT |  |  |  |  |  |  |  |  |  |  |
| ENGLISH | KIP/SQ.FT | KIP/SQ.FT | KIP/SQ.FT | KIP/SQ.FT | KIP/SQ.FT | KIP/SQ.FT | KIP/SQ.FT | KIP/SQ.FT | KIP/SQ.FT | KIP/SQ.FT |
| METRIC (KN) | KN/SQ.CM | KN/SQ.CM | KN/SQ.CM | KN/SQ.CM | KN/SQ.CM | KN/SQ.CM | KN/SQ.CM | KN/SQ.CM | KN/SQ.CM | KN/SQ.CM |
| METRIC (KG) | KG/SQ.CM | KG/SQ.CM | KG/SQ.CM | KG/SQ.CM | KG/SQ.CM | KG/SQ.CM | KG/SQ.CM | KG/SQ.CM | KG/SQ.CM | KG/SQ.CM |



SOIL TORSION ADHESION HEADER LINE

COLUMNS

COMMENTARY

COLUMNS

COMMENTARY

GENERAL EITHER THIS LINE FOLLOWED BY 'SLOC' AND CAPACITY LINE SETS,OR TORSION SPRING LINE SHOULD BE INCLUDED IN ANY PSI INPUTFILE.

THIS LINE IS USED TO MODEL THE TORSIONAL RESISTANCE OF THEPILE RESULTING FROM ADHESION OF THE SURROUNDING SOIL.

STARTING AT THE TOP STRATUM THE LENGTH OVER WHICH THE ADHESION MUST ACT TO TRANSFER THE PILE TORQUE TO THE SOIL IS COMPUTED. IF THIS LENGTH IS LESS THAN THE THICKNESS OF THE STRATUM, THE TORQUE IS COMPLETELY TRANSFERRED TO THE SOIL OVER THAT LENGTH. IF THE COMPUTED LENGTH IS GREATER THAN THE STRATUM THICKNESS THE TORQUE IS ONLY PARTIALLY TRANSFERRED IN THAT STRATUM. THE EXCESS PILE TORQUE IS TRANSFERRED IN THE NEXT DEEPER SOIL STRATUM. THE PROCEDURE IS REPEATED FOR EACH STRATUM IN TURN UNTIL THE ENTIRE PILE TORQUE IS TRANSFERRED OR UNTIL ALL SOIL STRATA HAVE REACHED THEIR CAPACITIES.

IF THE PILE TORQUE HAS NOT BEEN TRANSFERRED AFTER ALL STRATA HAVE REACHED THEIR CAPACITIES THE PILE FAILS IN TORSION AND A REPORT TO THAT EFFECT IS ISSUED.

THIS SOIL MODEL TAKES NO ACCOUNT OF SOIL DEFORMATIONS. THE TORSIONAL ROTATION AT THE PILEHEAD IS TAKEN TO BE EQUAL TO THE ELASTIC TWIST OF THE PILE.

( 1- 4) ENTER 'SOIL'.   
( 6-12) ENTER 'TORSION'.   
(14-17) ENTER 'HEAD'.   
(18-20) ENTER THE NUMBER OF SOIL STRATA TO BE DESCRIBED ON THE FOLLOWING LINES ('SOIL SLOC' AND 'SOIL' LINE SETS).   
(41-44) ENTER AN ALPHANUMERIC SOIL TABLE IDENTIFIER. THIS IDENTIFIER IS USED ON ONE OR MORE 'PILE' LINES TO ASSOCIATE THIS SOIL TABLE WITH THOSE PILES.   
(45-60) ENTER ANY DESCRIPTIVE REMARKS DESIRED.



| LINE LABEL | TORSION LABEL | HEAD LABEL | NUMBER OF SOIL STRATA | SOIL TABLE ID | SOIL DESCRIPTION OR OTHER REMARKS | LEAVE BLANK |
| --- | --- | --- | --- | --- | --- | --- |
| SOIL | TORSION | HEAD |  |  |  |  |
| 1--4 | 6--12 | 14--17 | 18--->20 | 41<-44 | 45------60 | 61--80 |



SOIL (CLAY) API AXIAL STRATUM LINE

COLUMNS

COMMENTARY

GENERAL THIS LINE SET IS USED TO SPECIFY THE SOIL PROPERTIES FOR EACHCLAY STRATUM. THE PROGRAM WILL USE THESE PROPERTIES TOCALCULATE AXIAL ADHESION AND BEARING CAPACITIES OR T-Z AXIALAND Q-Z END BEARING CURVES.

( 1- 4) ENTER 'SOIL'.   
( 6-12) ENTER 'API AXL'.   
( 13 ) IF THE API RP2A 10TH EDITION SOIL PROPERTIES ARE DESIRED ENTER A '1' HERE. OTHERWISE, LEAVE BLANK.   
(14-17) ENTER 'SLOC'.   
(19-24) ENTER THE DISTANCE FROM THE PILEHEAD TO THE TOP OF THIS SOIL STRATUM. THIS DISTANCE IS VERTICALLY DOWN AND NOT ALONG THE AXIS OF THE PILE, WHICH MAY BE BATTERED.   
(25-30) IF THIS DATA IS BEING USED FOR ADHESION, ENTER THE DISTANCE TO THE BOTTOM OF THIS STRATUM. IF THIS DATA IS BEING USED FOR T-Z AXIAL, ENTER THE DISTANCE FROM THE PILEHEAD TO BOTTOM OF THIS STRATUM IF THE T-Z DATA IS TO BE CONSTANT FOR THIS STRATUM. IF LEFT BLANK, THE T-Z DATA WILL VARY LINEARLY TO THE TOP OF THE NEXT STRATUM. NO GAPS SHOULD BE LEFT BETWEEN STRATA.   
(32-35) ENTER THE SOIL TYPE. SELECT FROM AMONG THE FOLLOWING:

'CLAY' - NORMAL.

'CLOC' - OVER-CONSOLIDATED GULF OF MEXICO CLAY (API 10TH ONLY).

'CLUC' - UNDER-CONSOLIDATED GULF OF MEXICO CLAY (API 10TH ONLY).

COLUMNS

COMMENTARY

(36-41) ENTER THE UNDRAINED SHEAR STRENGTH.   
(48-53) ENTER THE SUBMERGED UNIT WEIGHT.   
(66-71) ENTER THE OVERBURDEN PRESSURE IF THE INTERNALLY CALCULATED VALUE IS NOT ACCEPTABLE.   
(72-77) ENTER THE SOIL RESIDUAL FACTOR ( Tres / Tmax).  
(78-80) ENTER ZPEAK RATIO TO PILE DIAMETER (ONLY FOR API 22ND EDITION). ZPEAK IS THE DISPLACEMENT TO MAXIMUM SOIL PILE ADHESION OR UNIT SKIN FRICTION (ONLY FOR API RP 22ND EDITION) A DEFAULT VALUE FOR ZPEAK OF 1% OF THE PILE OUTER DIAMETER IS RECOMMENDED BY API 22ND EDITION. HOWEVER, THE VALUE MAY VARY FROM 0.25 TO



| LINE LABEL | AUTOMATIC AXIAL RESISTANCE GENERATION | API EDITION SELECTION | LINE TYPE | TOP OF STRATUM | BOTTOM OF STRATUM | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | ZPEAK RATIO TO PILE DIAMETER (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | AUTOMATIC AXIAL RESISTANCE GENERATION | API EDITION SELECTION | LINE TYPE | TOP OF STRATUM | BOTTOM OF STRATUM | SOIL TYPE | UNDRAINED SHEAR STRENGTH | SUBMERGED DENSITY | OVER- BURDEN PRESSURE | RESIDUAL FACTOR | ZPEAK RATIO TO PILE DIAMETER (%) |
| SOIL | API AXL |  | SLOC |  |  |  |  |  |  |  |  |
| 1--4 | 6--12 | 13 | 14--17 | 19<--24 | 25<--30 | 32--35 | 36<--41 | 48<--53 | 66<--71 | 72<--77 | 78<--80 |
| DEFAULT |  | 20TH |  |  |  |  |  |  |  | 0.7 | 1 |
| ENGLISH |  |  |  | FT | FT |  | KIP/SQ.FT | LB/CU.FT | KIP/SQ.FT |  |  |
| METRIC (KN) |  |  |  | M | M |  | KN/SQ.CM | TONNE/CU.M | KN/SQ.CM |  |  |
| METRIC (KG) |  |  |  | M | M |  | KG/SQ.CM | TONNE/CU.M | KG/SQ.CM |  |  |



SOIL (ROCK) API AXIAL STRATUM LINE

COLUMNS

COMMENTARY

GENERAL THIS LINE SET IS USED TO SPECIFY THE SOIL PROPERTIES FOR EACHROCK STRATUM. THE PROGRAM WILL USE THESE PROPERTIES TOCALCULATE AXIAL ADHESION AND BEARING CAPACITIES OR T-Z AXIALAND Q-Z END BEARING CURVES.

( 1- 4) ENTER 'SOIL'.   
( 6-12) ENTER 'API AXL'.   
( 13 ) IF THE API RP2A 10TH EDITION SOIL PROPERTIES ARE DESIRED ENTER A '1' HERE. OTHERWISE, LEAVE BLANK.   
(14-17) ENTER 'SLOC'.   
(19-24) ENTER THE DISTANCE FROM THE PILEHEAD TO THE TOP OF THIS SOIL STRATUM. THIS DISTANCE IS VERTICALLY DOWN AND NOT ALONG THE AXIS OF THE PILE, WHICH MAY BE BATTERED.   
(25-30) IF THIS DATA IS BEING USED FOR ADHESION, ENTER THE DISTANCE TO THE BOTTOM OF THIS STRATUM. IF THIS DATA IS BEING USED FOR T-Z AXIAL, ENTER THE DISTANCE FROM THE PILEHEAD TO BOTTOM OF THIS STRATUM IF THE T-Z DATA IS TO BE CONSTANT FOR THIS STRATUM. IF LEFT BLANK, THE T-Z DATA WILL VARY LINEARLY TO THE TOP OF THE NEXT STRATUM. NO GAPS SHOULD BE LEFT BETWEEN STRATA.   
(32-35) ENTER THE SOIL TYPE OF 'ROCK'.

COLUMNS

COMMENTARY

(36-41) ENTER THE UNIT SKIN FRICTION CAPACITY.   
(42-47) ENTER THE BEARING CAPACITY.   
(48-53) ENTER THE SUBMERGED UNIT WEIGHT.   
(78-80) ENTER ZPEAK RATIO TO PILE DIAMETER (ONLY FOR API 22ND EDITION). ZPEAK IS THE DISPLACEMENT TO MAXIMUM SOIL PILE ADHESION OR UNIT SKIN FRICTION (ONLY FOR API RP 22ND EDITION) A DEFAULT VALUE FOR ZPEAK OF 1% OF THE PILE OUTER DIAMETER IS RECOMMENDED BY API 22ND EDITION. HOWEVER, THE VALUE MAY VARY FROM 0.25 TO



| LINE LABEL | AUTOMATIC AXIAL RESISTANCE GENERATION | API EDITION SELECTION | LINE TYPE | TOP OF STRATUM | BOTTOM OF STRATUM | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | LEAVE BLANK | ZPEAK RATIO TO PILE DIAMETER (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | AUTOMATIC AXIAL RESISTANCE GENERATION | API EDITION SELECTION | LINE TYPE | TOP OF STRATUM | BOTTOM OF STRATUM | SOIL TYPE | UNIT SKIN FRICTION CAPACITY | BEARING CAPACITY | SUBMERGED DENSITY | LEAVE BLANK | ZPEAK RATIO TO PILE DIAMETER (%) |
| SOIL | API AXL |  | SLOC |  |  |  |  |  |  |  |  |
| 1--4 | 6--12 | 13 | 14--17 | 19<--24 | 25<--30 | 32--35 | 36<--41 | 42<--47 | 48<--53 | 54<--77 | 78--80 |
| DEFAULT |  | 20TH |  |  |  |  |  |  |  |  | 1 |
| ENGLISH |  |  |  | FT | FT |  | KIP/SQ.FT | KIP/SQ.FT | LB/CU.FT |  |  |
| METRIC (KN) |  |  |  | M | M |  | KN/SQ.CM | KN/SQ.CM | TONNE/CU.M |  |  |
| METRIC (KG) |  |  |  | M | M |  | KG/SQ.CM | KG/SQ.CM | TONNE/CU.M |  |  |



SOIL (SAND) API AXIAL STRATUM LINE

COLUMNS

COMMENTARY

GENERAL THIS LINE SET IS USED TO SPECIFY THE SOIL PROPERTIES FOR EACHSAND STRATUM. THE PROGRAM WILL USE THESE PROPERTIES TOCALCULATE AXIAL ADHESION AND BEARING CAPACITIES OR T-Z AXIALAND Q-Z END BEARING CURVES.

( 1- 4) ENTER 'SOIL'.   
( 6-12) ENTER 'API AXL'.   
( 13 ) IF THE API RP2A 10TH EDITION SOIL PROPERTIES ARE DESIRED ENTER A '1' HERE. OTHERWISE, LEAVE BLANK.   
(14-17) ENTER 'SLOC'.   
(19-24) ENTER THE DISTANCE FROM THE PILEHEAD TO THE TOP OF THIS SOIL STRATUM. THIS DISTANCE IS VERTICALLY DOWN AND NOT ALONG THE AXIS OF THE PILE, WHICH MAY BE BATTERED.   
(25-30) IF THIS DATA IS BEING USED FOR ADHESION, ENTER THE DISTANCE TO THE BOTTOM OF THIS STRATUM. IF THIS DATA IS BEING USED FOR T-Z AXIAL, ENTER THE DISTANCE FROM THE PILEHEAD TO BOTTOM OF THIS STRATUM IF THE T-Z DATA IS TO BE CONSTANT FOR THIS STRATUM. IF LEFT BLANK, THE T-Z DATA WILL VARY LINEARLY TO THE TOP OF THE NEXT STRATUM. NO GAPS SHOULD BE LEFT BETWEEN STRATA.   
(32-35) ENTER THE SOIL TYPE. SELECT FROM AMONG THE FOLLOWING:



| SOIL TYPE | API DESCRIPTION | FRICION ANGLE | LIMITING FRICION | BEARING FACTOR | LIMITING BEARING |
| --- | --- | --- | --- | --- | --- |
| 'GRAV' - | GRAVEL | 35.0 | 2.4 | 50.0 | 250.0 |
| 'SAND' - | DENSE SAND | 30.0 | 2.0 | 40.0 | 200.0 |
| 'SLN' - | DENSE SAND-SILT | 25.0 | 1.7 | 20.0 | 100.0 |
| 'SNSL' - | MEDIUM SAND-SILT | 20.0 | 1.4 | 12.0 | 60.0 |
| 'SILT' - | MEDIUM SILT | 15.0 | 1.0 | 8.0 | 40.0 |



COLUMNS

COMMENTARY

(36-41) ENTER THE COEFFICIENT OF LATERAL EARTH PRESSURE.   
(42-47) ENTER THE LIMITING END BEARING VALUE IF THE DEFAULT IS NOT ACCEPTABLE.   
(48-53) ENTER THE SUBMERGED UNIT WEIGHT.   
(54-59) ENTER THE FRICTION ANGLE IF THE DEFAULT IS NOT ACCEPTABLE.   
(60-65) ENTER THE BEARING CAPACITY FACTOR IF THE DEFAULT IS NOT ACCEPTABLE.   
(66-71) ENTER THE OVERBURDEN PRESSURE IF THE INTERNALLY CALCULATED VALUE IS NOT ACCEPTABLE.   
(72-77) ENTER THE LIMITING SKIN FRICTION VALUE IF THE DEFAULT IS NOT ACCEPTABLE.   
(78-80) ENTER ZPEAK RATIO TO PILE DIAMETER (ONLY FOR API 22ND EDITION). ZPEAK IS THE DISPLACEMENT TO MAXIMUM SOIL PILE ADHESION OR UNIT SKIN FRICTION (ONLY FOR API RP 22ND EDITION) A DEFAULT VALUE FOR ZPEAK OF 1% OF THE PILE OUTER DIAMETER IS RECOMMENDED BY API 22ND EDITION. HOWEVER, THE VALUE MAY VARY FROM 0.25 TO



| LINE LABEL | AUTOMATIC AXIAL RESISTANCE GENERATION | API EDITION SELECTION | LINE TYPE | TOP OF STRATUM | BOTTOM OF STRATUM | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | ZPEAK RATIO TO PILE DIAMETER (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | AUTOMATIC AXIAL RESISTANCE GENERATION | API EDITION SELECTION | LINE TYPE | TOP OF STRATUM | BOTTOM OF STRATUM | SOIL TYPE | COEFF. OF LATERAL EARTH PRESSURE | LIMITING END BEARING CAP. | SUBMERGED DENSITY | FRICTION ANGLE | BEARING CAPACITY FACTOR | OVER-BURDEN PRESSURE | LIMITING SKIN FRICTION | ZPEAK RATIO TO PILE DIAMETER (%) |
| SOIL | API AXL |  | SLOC |  |  |  |  |  |  |  |  |  |  |  |
| 1--4 | 6--12 | 13 | 14--17 | 19<--24 | 25<--30 | 32--35 | 36<--41 | 42<--47 | 48<--53 | 54<--59 | 60<--65 | 66<--71 | 72<--77 | 78<--80 |
| DEFAULT |  | 20TH |  |  |  |  | 1 | ABOVE |  | ABOVE | ABOVE |  | ABOVE | 1 |
| ENGLISH |  |  |  | FT | FT |  |  | KIP/SQ.FT | LB/CU.FT | DEG |  | KIP/SQ.FT | KIP/SQ.FT |  |
| METRIC (KN) |  |  |  | M | M |  |  | KN/SQ.CM | TONNE/CU.M | DEG |  | KN/SQ.CM | KN/SQ.CM |  |
| METRIC (KG) |  |  |  | M | M |  |  | KG/SQ.CM | TONNE/CU.M | DEG |  | KG/SQ.CM | KG/SQ.CM |  |



SOIL AXIAL ADHESION HEADER LINE

COLUMNS

COMMENTARY

COLUMNS

COMMENTARY

GENERAL

THIS LINE AND THE 'SLOC' LINE ARE USED TO MODEL THE AXIAL LOAD TRANSFER TO THE SOIL BY ADHESION. AN AXIAL ADHESION CAPACITY IS SPECIFIED AT THE TOP AND BOTTOM OF EACH SOIL STRATUM. IF THE VALUES ARE DIFFERENT AN AVERAGE IS USED. STARTING AT THE TOP STRATUM THE LENGTH OVER WHICH THE ADHESION MUST ACT IN ORDER TO TRANSFER THE PILE AXIAL LOAD IS COMPUTED. IF THIS LENGTH IS LESS THAN THE THICKNESS OF THAT STRATUM THE AXIAL LOAD IS COMPLETELY TRANSFERRED TO THE SOIL OVER THAT LENGTH. IF THE COMPUTED LENGTH IS GREATER THAN THE THICKNESS OF THE STRATUM THE AXIAL IS ONLY PARTIALLY TRANSFERRED IN THAT STRATUM. THE EXCESS PILE LOAD IS TRANSFERRED IN THE NEXT DEEPER SOIL STRATUM. THE PROCEDURE IS REPEATED FOR EACH SOIL STRATUM IN TURN UNTIL THE ENTIRE AXIAL LOAD IS TRANSFERRED OR UNTIL ALL SOIL STRATA HAVE REACHED THEIR CAPACITIES. ANY EXCESS AXIAL LOAD IS THEN TRANSFERRED BY END BEARING UNTIL THE BEARING CAPACITY IS REACHED. IF THE TOTAL PILE AXIAL LOAD HAS NOT THEN BEEN TRANSFERRED THE PILE LOAD EXCEEDS ITS CAPACITY AND IT FAILS, A REPORT TO THIS EFFECT IS ISSUED.

THIS SOIL MODEL TAKES NO ACCOUNT OF SOIL DEFORMATIONS IN THE AXIAL DIRECTION. THE AXIAL DISPLACEMENT AT THE PILEHEAD IS TAKEN TO BE EQUAL TO THE COMPRESSIVE (OR TENSILE) DEFORMATION OF THE PILE.

( 1- 4) ENTER 'SOIL'.   
( 6-10) ENTER 'AXIAL'.   
(14-17) ENTER 'HEAD'.   
(18-20) ENTER THE NUMBER OF SOIL STRATA TO BE DESCRIBED FOR ADHESION SOIL DATA.   
(21-30) ENTER THE END BEARING CAPACITY FOR THIS SOIL TABLE.   
(41-44) ENTER AN ALPHANUMERIC SOIL TABLE IDENTIFIER. THIS IDENTIFIER IS USED ON ONE OR MORE 'PILE' LINES TO ASSOCIATE THESE AXIAL SOIL PROPERTIES WITH THOSE PILES.   
(45-60) ENTER ANY DESCRIPTIVE REMARKS FOR THIS AXIAL SOIL DATA.   
(62-64) ENTER THE METHOD TO BE USED IN CONJUNCTION WITH CPT STRATA.

SELECT FROM THE FOLLOWING:

'ICP' - SIMPLIFIED ICP-05.   
'UWA' - OFFSHORE UWA-05.   
'FUG' - FUGRO-05.   
'NGI' - NGI-05.

(66-71) ENTER THE DIAMETER OF THE CONE PENETRATION TOOL FOR CPT STRATA.



| LINE LABEL | AXIAL LABEL | HEAD LABEL | NUMBER OF SOIL STRATA | END BEARING CAPACITY | SOIL TABLE ID | SOIL DESCRIPTION OR OTHER REMARKS | CPT METHOD | CPT TOOL DIAMETER | LEAVE BLANK |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOIL | AXIAL | HEAD |  |  |  |  |  |  |  |
| 1--4 | 6--10 | 14--17 | 18--->20 | 21<--30 | 41<--44 | 45----60 | 62--64 | 66--71 | 72--80 |
| DEFAULT |  |  |  |  |  |  | 'ICP' | 36mm |  |
| ENGLISH |  |  |  | KIP/SQ.FT |  |  |  | IN |  |
| METRIC (KN) |  |  |  | KN/SQ.CM |  |  |  | CM |  |
| METRIC (KG) |  |  |  | KG/SQ.CM |  |  |  | CM |  |



SOIL (CLAY) API AXIAL STRATUM LINE

COLUMNS

COMMENTARY

GENERAL THIS LINE SET IS USED TO SPECIFY THE SOIL PROPERTIES FOR EACHCLAY STRATUM. THE PROGRAM WILL USE THESE PROPERTIES TOCALCULATE AXIAL ADHESION AND BEARING CAPACITIES OR T-Z AXIALAND Q-Z END BEARING CURVES.

( 1- 4) ENTER 'SOIL'.   
( 6-12) ENTER 'API AXL'.   
( 13 ) IF THE API RP2A 10TH EDITION SOIL PROPERTIES ARE DESIRED ENTER A '1' HERE. OTHERWISE, LEAVE BLANK.   
(14-17) ENTER 'SLOC'.   
(19-24) ENTER THE DISTANCE FROM THE PILEHEAD TO THE TOP OF THIS SOIL STRATUM. THIS DISTANCE IS VERTICALLY DOWN AND NOT ALONG THE AXIS OF THE PILE, WHICH MAY BE BATTERED.   
(25-30) IF THIS DATA IS BEING USED FOR ADHESION, ENTER THE DISTANCE TO THE BOTTOM OF THIS STRATUM. IF THIS DATA IS BEING USED FOR T-Z AXIAL, ENTER THE DISTANCE FROM THE PILEHEAD TO BOTTOM OF THIS STRATUM IF THE T-Z DATA IS TO BE CONSTANT FOR THIS STRATUM. IF LEFT BLANK, THE T-Z DATA WILL VARY LINEARLY TO THE TOP OF THE NEXT STRATUM. NO GAPS SHOULD BE LEFT BETWEEN STRATA.   
(32-35) ENTER THE SOIL TYPE. SELECT FROM AMONG THE FOLLOWING:

'CLAY' - NORMAL.

'CLOC' - OVER-CONSOLIDATED GULF OF MEXICO CLAY (API 10TH ONLY).

'CLUC' - UNDER-CONSOLIDATED GULF OF MEXICO CLAY (API 10TH ONLY).

COLUMNS

COMMENTARY

(36-41) ENTER THE UNDRAINED SHEAR STRENGTH.   
(48-53) ENTER THE SUBMERGED UNIT WEIGHT.   
(66-71) ENTER THE OVERBURDEN PRESSURE IF THE INTERNALLY CALCULATED VALUE IS NOT ACCEPTABLE.   
(72-77) ENTER THE SOIL RESIDUAL FACTOR ( Tres / Tmax).  
(78-80) ENTER ZPEAK RATIO TO PILE DIAMETER (ONLY FOR API 22ND EDITION). ZPEAK IS THE DISPLACEMENT TO MAXIMUM SOIL PILE ADHESION OR UNIT SKIN FRICTION (ONLY FOR API RP 22ND EDITION) A DEFAULT VALUE FOR ZPEAK OF 1% OF THE PILE OUTER DIAMETER IS RECOMMENDED BY API 22ND EDITION. HOWEVER, THE VALUE MAY VARY FROM 0.25 TO



| LINE LABEL | AUTOMATIC AXIAL RESISTANCE GENERATION | API EDITION SELECTION | LINE TYPE | TOP OF STRATUM | BOTTOM OF STRATUM | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | ZPEAK RATIO TO PILE DIAMETER (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | AUTOMATIC AXIAL RESISTANCE GENERATION | API EDITION SELECTION | LINE TYPE | TOP OF STRATUM | BOTTOM OF STRATUM | SOIL TYPE | UNDRAINED SHEAR STRENGTH | SUBMERGED DENSITY | OVER- BURDEN PRESSURE | RESIDUAL FACTOR | ZPEAK RATIO TO PILE DIAMETER (%) |
| SOIL | API AXL |  | SLOC |  |  |  |  |  |  |  |  |
| 1--4 | 6--12 | 13 | 14--17 | 19<--24 | 25<--30 | 32--35 | 36<--41 | 48<--53 | 66<--71 | 72<--77 | 78<--80 |
| DEFAULT |  | 20TH |  |  |  |  |  |  |  | 0.7 | 1 |
| ENGLISH |  |  |  | FT | FT |  | KIP/SQ.FT | LB/CU.FT | KIP/SQ.FT |  |  |
| METRIC (KN) |  |  |  | M | M |  | KN/SQ.CM | TONNE/CU.M | KN/SQ.CM |  |  |
| METRIC (KG) |  |  |  | M | M |  | KG/SQ.CM | TONNE/CU.M | KG/SQ.CM |  |  |



SOIL (CPT) API AXIAL STRATUM LINE

COLUMNS

COMMENTARY

GENERAL THIS LINE SET IS USED TO SPECIFY THE SOIL PROPERTIES FOR EACHCPT STRATUM. THE PROGRAM WILL USE THESE PROPERTIES TOCALCULATE AXIAL ADHESION AND BEARING CAPACITIES OR T-Z AXIALAND Q-Z END BEARING CURVES.

( 1- 4) ENTER 'SOIL'.   
( 6-12) ENTER 'API AXL'.   
(14-17) ENTER 'SLOC'.   
(19-24) ENTER THE DISTANCE FROM THE PILEHEAD TO THE TOP OF THIS SOIL STRATUM. THIS DISTANCE IS VERTICALLY DOWN AND NOT ALONG THE AXIS OF THE PILE, WHICH MAY BE BATTERED.   
(25-30) IF THIS DATA IS BEING USED FOR ADHESION, ENTER THE DISTANCE TO THE BOTTOM OF THIS STRATUM. IF THIS DATA IS BEING USED FOR T-Z AXIAL, ENTER THE DISTANCE FROM THE PILEHEAD TO BOTTOM OF THIS STRATUM IF THE T-Z INPUT DATA ARE TO BE CONSTANT FOR THIS STRATUM. IF LEFT BLANK, THE T-Z INPUT DATA WILL VARY LINEARLY TO THE TOP OF THE NEXT STRATUM. NO GAPS SHOULD BE LEFT BETWEEN STRATA.   
(32-34) ENTER 'CPT'

COLUMNS

COMMENTARY

(36-41) ENTER THE COEFFICIENT OF LATERAL EARTH PRESSURE.   
(42-47) ENTER THE CONE TIP RESISTANCE FOR THE TOP OF THE STRATUM.   
(48-53) ENTER THE SUBMERGED DENSITY.   
(54-59) ENTER THE CONSTANT VOLUME INTERFACE FRICTION ANGLE FOR THE TOP OF THE STRATUM IF THE DEFAULT IS NOT ACCEPTABLE.   
(78-80) ENTER ZPEAK RATIO TO PILE DIAMETER (ONLY FOR API 22ND EDITION). ZPEAK IS THE DISPLACEMENT TO MAXIMUM SOIL PILE ADHESION OR UNIT SKIN FRICTION (ONLY FOR API RP 22ND EDITION) A DEFAULT VALUE FOR ZPEAK OF 1% OF THE PILE OUTER DIAMETER IS RECOMMENDED BY API 22ND EDITION. HOWEVER, THE VALUE MAY VARY FROM 0.25 TO



| LINE LABEL | AUTOMATIC AXIAL RESISTANCE GENERATION | API EDITION SELECTION | LINE TYPE | TOP OF STRATUM | BOTTOM OF STRATUM | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | ZPEAK RATIO TO PILE DIAMETER (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | AUTOMATIC AXIAL RESISTANCE GENERATION | API EDITION SELECTION | LINE TYPE | TOP OF STRATUM | BOTTOM OF STRATUM | SOIL TYPE | COEFF. OF LATERAL EARTH PRESSURE | CONE TIP RESISTANCE | SUBMERGED DENSITY | INTERFACE FRICTION ANGLE | LEAVE BLANK | ZPEAK RATIO TO PILE DIAMETER (%) |
| SOIL | API AXL |  | SLOC |  |  | CPT |  |  |  |  |  |  |
| 1--4 | 6--12 | 13 | 14--17 | 19<--24 | 25<--30 | 32--34 | 36<--41 | 42<--47 | 48<--53 | 54<--59 | 60--77 | 78<--80 |
| DEFAULT |  | 21ST |  |  |  |  | 1 |  |  | 28.8 |  | 1 |
| ENGLISH |  |  |  | FT | FT | CPT |  | KSI. | LB/CU.FT | DEG |  |  |
| METRIC (KN) |  |  |  | M | M | CPT |  | MPa | TONNE/CU.M | DEG |  |  |
| METRIC (KG) |  |  |  | M | M | CPT |  | KG/SQ.MM | TONNE/CU.M | DEG |  |  |



SOIL (ROCK) API AXIAL STRATUM LINE

COLUMNS

COMMENTARY

GENERAL THIS LINE SET IS USED TO SPECIFY THE SOIL PROPERTIES FOR EACHROCK STRATUM. THE PROGRAM WILL USE THESE PROPERTIES TOCALCULATE AXIAL ADHESION AND BEARING CAPACITIES OR T-Z AXIALAND Q-Z END BEARING CURVES.

( 1- 4) ENTER 'SOIL'.   
( 6-12) ENTER 'API AXL'.   
( 13 ) IF THE API RP2A 10TH EDITION SOIL PROPERTIES ARE DESIRED ENTER A '1' HERE. OTHERWISE, LEAVE BLANK.   
(14-17) ENTER 'SLOC'.   
(19-24) ENTER THE DISTANCE FROM THE PILEHEAD TO THE TOP OF THIS SOIL STRATUM. THIS DISTANCE IS VERTICALLY DOWN AND NOT ALONG THE AXIS OF THE PILE, WHICH MAY BE BATTERED.   
(25-30) IF THIS DATA IS BEING USED FOR ADHESION, ENTER THE DISTANCE TO THE BOTTOM OF THIS STRATUM. IF THIS DATA IS BEING USED FOR T-Z AXIAL, ENTER THE DISTANCE FROM THE PILEHEAD TO BOTTOM OF THIS STRATUM IF THE T-Z DATA IS TO BE CONSTANT FOR THIS STRATUM. IF LEFT BLANK, THE T-Z DATA WILL VARY LINEARLY TO THE TOP OF THE NEXT STRATUM. NO GAPS SHOULD BE LEFT BETWEEN STRATA.   
(32-35) ENTER THE SOIL TYPE OF 'ROCK'.

COLUMNS

COMMENTARY

(36-41) ENTER THE UNIT SKIN FRICTION CAPACITY.   
(42-47) ENTER THE BEARING CAPACITY.   
(48-53) ENTER THE SUBMERGED UNIT WEIGHT.   
(78-80) ENTER ZPEAK RATIO TO PILE DIAMETER (ONLY FOR API 22ND EDITION). ZPEAK IS THE DISPLACEMENT TO MAXIMUM SOIL PILE ADHESION OR UNIT SKIN FRICTION (ONLY FOR API RP 22ND EDITION) A DEFAULT VALUE FOR ZPEAK OF 1% OF THE PILE OUTER DIAMETER IS RECOMMENDED BY API 22ND EDITION. HOWEVER, THE VALUE MAY VARY FROM 0.25 TO



| LINE LABEL | AUTOMATIC AXIAL RESISTANCE GENERATION | API EDITION SELECTION | LINE TYPE | TOP OF STRATUM | BOTTOM OF STRATUM | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | LEAVE BLANK | ZPEAK RATIO TO PILE DIAMETER (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | AUTOMATIC AXIAL RESISTANCE GENERATION | API EDITION SELECTION | LINE TYPE | TOP OF STRATUM | BOTTOM OF STRATUM | SOIL TYPE | UNIT SKIN FRICTION CAPACITY | BEARING CAPACITY | SUBMERGED DENSITY | LEAVE BLANK | ZPEAK RATIO TO PILE DIAMETER (%) |
| SOIL | API AXL |  | SLOC |  |  |  |  |  |  |  |  |
| 1--4 | 6--12 | 13 | 14--17 | 19<--24 | 25<--30 | 32--35 | 36<--41 | 42<--47 | 48<--53 | 54<--77 | 78--80 |
| DEFAULT |  | 20TH |  |  |  |  |  |  |  |  | 1 |
| ENGLISH |  |  |  | FT | FT |  | KIP/SQ.FT | KIP/SQ.FT | LB/CU.FT |  |  |
| METRIC (KN) |  |  |  | M | M |  | KN/SQ.CM | KN/SQ.CM | TONNE/CU.M |  |  |
| METRIC (KG) |  |  |  | M | M |  | KG/SQ.CM | KG/SQ.CM | TONNE/CU.M |  |  |



SOIL (SAND) API AXIAL STRATUM LINE

COLUMNS

COMMENTARY

GENERAL THIS LINE SET IS USED TO SPECIFY THE SOIL PROPERTIES FOR EACHSAND STRATUM. THE PROGRAM WILL USE THESE PROPERTIES TOCALCULATE AXIAL ADHESION AND BEARING CAPACITIES OR T-Z AXIALAND Q-Z END BEARING CURVES.

( 1- 4) ENTER 'SOIL'.   
( 6-12) ENTER 'API AXL'.   
( 13 ) IF THE API RP2A 10TH EDITION SOIL PROPERTIES ARE DESIRED ENTER A '1' HERE. OTHERWISE, LEAVE BLANK.   
(14-17) ENTER 'SLOC'.   
(19-24) ENTER THE DISTANCE FROM THE PILEHEAD TO THE TOP OF THIS SOIL STRATUM. THIS DISTANCE IS VERTICALLY DOWN AND NOT ALONG THE AXIS OF THE PILE, WHICH MAY BE BATTERED.   
(25-30) IF THIS DATA IS BEING USED FOR ADHESION, ENTER THE DISTANCE TO THE BOTTOM OF THIS STRATUM. IF THIS DATA IS BEING USED FOR T-Z AXIAL, ENTER THE DISTANCE FROM THE PILEHEAD TO BOTTOM OF THIS STRATUM IF THE T-Z DATA IS TO BE CONSTANT FOR THIS STRATUM. IF LEFT BLANK, THE T-Z DATA WILL VARY LINEARLY TO THE TOP OF THE NEXT STRATUM. NO GAPS SHOULD BE LEFT BETWEEN STRATA.   
(32-35) ENTER THE SOIL TYPE. SELECT FROM AMONG THE FOLLOWING:



| SOIL TYPE | API DESCRIPTION | FRICION ANGLE | LIMITING FRICION | BEARING FACTOR | LIMITING BEARING |
| --- | --- | --- | --- | --- | --- |
| 'GRAV' - | GRAVEL | 35.0 | 2.4 | 50.0 | 250.0 |
| 'SAND' - | DENSE SAND | 30.0 | 2.0 | 40.0 | 200.0 |
| 'SLN' - | DENSE SAND-SILT | 25.0 | 1.7 | 20.0 | 100.0 |
| 'SNSL' - | MEDIUM SAND-SILT | 20.0 | 1.4 | 12.0 | 60.0 |
| 'SILT' - | MEDIUM SILT | 15.0 | 1.0 | 8.0 | 40.0 |



COLUMNS

COMMENTARY

(36-41) ENTER THE COEFFICIENT OF LATERAL EARTH PRESSURE.   
(42-47) ENTER THE LIMITING END BEARING VALUE IF THE DEFAULT IS NOT ACCEPTABLE.   
(48-53) ENTER THE SUBMERGED UNIT WEIGHT.   
(54-59) ENTER THE FRICTION ANGLE IF THE DEFAULT IS NOT ACCEPTABLE.   
(60-65) ENTER THE BEARING CAPACITY FACTOR IF THE DEFAULT IS NOT ACCEPTABLE.   
(66-71) ENTER THE OVERBURDEN PRESSURE IF THE INTERNALLY CALCULATED VALUE IS NOT ACCEPTABLE.   
(72-77) ENTER THE LIMITING SKIN FRICTION VALUE IF THE DEFAULT IS NOT ACCEPTABLE.   
(78-80) ENTER ZPEAK RATIO TO PILE DIAMETER (ONLY FOR API 22ND EDITION). ZPEAK IS THE DISPLACEMENT TO MAXIMUM SOIL PILE ADHESION OR UNIT SKIN FRICTION (ONLY FOR API RP 22ND EDITION) A DEFAULT VALUE FOR ZPEAK OF 1% OF THE PILE OUTER DIAMETER IS RECOMMENDED BY API 22ND EDITION. HOWEVER, THE VALUE MAY VARY FROM 0.25 TO



| LINE LABEL | AUTOMATIC AXIAL RESISTANCE GENERATION | API EDITION SELECTION | LINE TYPE | TOP OF STRATUM | BOTTOM OF STRATUM | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | ZPEAK RATIO TO PILE DIAMETER (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | AUTOMATIC AXIAL RESISTANCE GENERATION | API EDITION SELECTION | LINE TYPE | TOP OF STRATUM | BOTTOM OF STRATUM | SOIL TYPE | COEFF. OF LATERAL EARTH PRESSURE | LIMITING END BEARING CAP. | SUBMERGED DENSITY | FRICTION ANGLE | BEARING CAPACITY FACTOR | OVER-BURDEN PRESSURE | LIMITING SKIN FRICTION | ZPEAK RATIO TO PILE DIAMETER (%) |
| SOIL | API AXL |  | SLOC |  |  |  |  |  |  |  |  |  |  |  |
| 1--4 | 6--12 | 13 | 14--17 | 19<--24 | 25<--30 | 32--35 | 36<--41 | 42<--47 | 48<--53 | 54<--59 | 60<--65 | 66<--71 | 72<--77 | 78<--80 |
| DEFAULT |  | 20TH |  |  |  |  | 1 | ABOVE |  | ABOVE | ABOVE |  | ABOVE | 1 |
| ENGLISH |  |  |  | FT | FT |  |  | KIP/SQ.FT | LB/CU.FT | DEG |  | KIP/SQ.FT | KIP/SQ.FT |  |
| METRIC (KN) |  |  |  | M | M |  |  | KN/SQ.CM | TONNE/CU.M | DEG |  | KN/SQ.CM | KN/SQ.CM |  |
| METRIC (KG) |  |  |  | M | M |  |  | KG/SQ.CM | TONNE/CU.M | DEG |  | KG/SQ.CM | KG/SQ.CM |  |



SOIL T-Z API AXIAL HEADER LINE

COLUMNS

COMMENTARY

GENERAL

THIS LINE IS USED TO SPECIFY THE NUMBER OF SOIL STRATA AND THE SOIL IDENTIFIER FOR A T-Z AXIAL SOIL DESCRIPTION. IT IS FOLLOWED BY SOIL STRATUM LINES.

A T-Z API AXIAL SOIL DESCRIPTION ACCOUNTS FOR SOIL DEFORMATION RESULTING FROM THE TRANSFER OF PILE AXIAL LOAD TO THE SOIL THROUGH THE ACTION OF SHEAR FORCES BETWEEN THE PILE LATERAL SURFACE AND THE SURROUNDING SOIL. THIS DATA SET WILL AUTOMATICALLY GENERATE THE T-Z DATA AND THE END BEARING Q-Z DATA ACCORDING TO THE API RP2A 20TH AND 21ST EDITIONS.

THE SEQUENCE OF LINES REQUIRED FOR A T-Z SOIL DESCRIPTION ISAS FOLLOWS:

1. THIS SOIL T-Z API AXIAL HEADER LINE.   
2. SOIL API AXL RECORD FOR EACH STRATUM.

COLUMNS

COMMENTARY

( 1- 4) ENTER 'SOIL'.   
( 6-10) ENTER 'TZAPI'.   
(14-17) ENTER 'HEAD'.   
(18-20) ENTER THE NUMBER OF SOIL STRATA FOR THIS T-Z DESCRIPTION.   
(21-27) ENTER THE EFFECTIVE PILE LENGTH. ONLY NEEDED FOR THE KOLK AND VAN DER VELDE OVERRIDE FOR CLAY STRATA.   
(28-33) ENTER A FACTOR THAT WILL SCALE THE API-GENERATED T-VALUES.   
(34-40) ENTER A FACTOR THAT WILL SCALE THE API-GENERATED Z-VALUES.   
(41-44) ENTER A SOIL TABLE IDENTIFIER. THIS IDENTIFIER IS USED ON ONE OR MORE 'PILE' LINES TO ASSOCIATE THIS SOIL TABLE WITH THOSE PILES.   
(45-60) ENTER ANY DESCRIPTIVE COMMENTS DESIRED.   
(62-64) ENTER THE METHOD TO BE USED IN CONJUNCTION WITH CPT STRATA. SELECT FROM THE FOLLOWING:

'ICP' - SIMPLIFIED ICP-05.   
'UWA' - OFFSHORE UWA-05.   
'FUG' - FUGRO-05.   
'NGI' - NGI-05.

(66-71) ENTER THE DIAMETER OF THE CONE PENETRATION TOOL FOR CPT STRATA.   
(73-73) ENTER 'K' IN ORDER TO OVERRIDE THE SKIN FRICTION CALCULATION FOR CLAY BY USING THE KOLK AND VAN DER VELDE METHOD.   
(75-80) ENTER AN EFFECTIVE PILE OD. ONLY NEEDED FOR THE KOLK AND VAN DER VELDE OVERRIDE FOR CLAY STRATA.



| LINE LABEL | T-Z AXIAL LABEL | HEAD LABEL | NUMBER OF SOIL STRATA | EFFECTIVE PILE LENGTH | T FACTOR | Z FACTOR | SOIL TABLE ID | SOIL DESCRIPTION OR OTHER REMARKS | CPT METHOD | CPT TOOL DIAMETER | KOLK VD VELDE OVERRIDE | KOLK VD VELDE PILE OD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOIL | TZAPI | HEAD |  |  |  |  |  |  |  |  |  |  |
| 1--4 | 6--10 | 14--17 | 18-->20 | 21--27 | 28--33 | 34--40 | 41--44 | 45--60 | 62--64 | 66--71 | 73 | 75--80 |
| DEFAULT |  |  |  |  |  |  |  |  |  |  |  |  |
| ENGLISH |  |  |  | FT |  |  |  |  |  | IN |  | IN |
| METRIC |  |  |  | M |  |  |  |  |  | CM |  | CM |



PILEHEAD AXIAL SPRING LINE

COLUMNS

COMMENTARY

GENERAL

THIS LINE IS USED IF THE PILE AXIAL BEHAVIOR IS TO BE MODELED AS A LINEAR SPRING AT THE PILEHEAD. FOR THE SUBSEQUENT LATERAL SOLUTION, THE INTERNAL AXIAL FORCE IN THE PILE IS ASSUMED TO VARY LINEARLY FROM THE PILEHEAD AXIAL LOAD TO ZERO AT THE BOTTOM OF THE PILE. IF THIS LINE IS USED, THEN NO OTHER SOIL AXIAL OR BEARING LINES ARE USED.

( 1- 4) ENTER 'SOIL'.   
( 6-10) ENTER 'AXIAL'.   
(14-17) ENTER 'HEAD'.   
(31-40) ENTER THE LINEAR STIFFNESS VALUE FOR THE PILEHEAD SPRING.   
(41-44) ENTER AN ALPHANUMERIC SOIL TABLE IDENTIFIER. THIS IDENTIFIER IS USED ON ONE OR MORE 'PILE' LINES TO ASSOCIATE THIS SPRING WITH PARTICULAR PILES.   
(45-60) ENTER ANY DESCRIPTIVE REMARKS.



| LINE LABEL | AXIAL LABEL | HEAD LABEL | LINEAR STIFFNESS VALUE | SOIL TABLE ID | REMARKS | LEAVE BLANK |
| --- | --- | --- | --- | --- | --- | --- |
| SOIL | AXIAL | HEAD |  |  |  |  |
| 1--4 | 6--10 | 14--17 | 31<--40 | 41<--44 | 45----60 | 61--80 |
| DEFAULT |  |  |  |  |  |  |
| ENGLISH |  |  | KIP/IN |  |  |  |
| METRIC (KN) |  |  | KN/M |  |  |  |
| METRIC (KG) |  |  | KG/CM |  |  |  |



SOIL AXIAL ADHESION STRATA LINE

COLUMNS

COMMENTARY

LOCATION THIS LINE SET FOLLOWS THE ADHESION HEADER LINE AND ISFOLLOWED BY SOIL ADHESION CAPACITY LINE.

GENERAL THE ADHESION SOIL STRATA LOCATIONS ARE DEFINED USING THIS LINE. THESE STRATA LOCATIONS ARE MEASURED FROM THE PILEHEAD. FIVE STRATA ARE INPUT PER LINE AND THIS LINE TYPE IS REPEATED UNTIL THE NUMBER OF STRATA DESIGNATED ON THE SOIL AXIAL HEAD LINE HAVE BEEN DESCRIBED.

( 1- 4) ENTER 'SOIL'.   
( 6- 9) ENTER 'ADHA'.   
(14-17) ENTER 'SLOC'.   
(19-78) ENTER THE DISTANCES FROM THE PILEHEAD TO THE TOP AND BOTTOM OF EACH STRATUM. THE LOCATION OF THE BOTTOM OF THE LAST STRATUM ENTERED MUST BE AT LEAST TO THE BOTTOM OF THE DEEPEST PILE TO WHICH THIS TABLE APPLIES. THE LOCATION OF THE TOP OF A STRATUM MUST BE THE SAME AS THE BOTTOM OF THE PRECEDING STRATUM. THESE DISTANCES ARE VERTICALLY DOWN AND NOT ALONG THE AXIS OF THE PILE, WHICH MAY BE BATTERED.



| LINE LABEL | AXIAL ADHESION | LINE TYPE | AXIAL ADHESION STRATA LOCATIONS | AXIAL ADHESION STRATA LOCATIONS | AXIAL ADHESION STRATA LOCATIONS | AXIAL ADHESION STRATA LOCATIONS | AXIAL ADHESION STRATA LOCATIONS | AXIAL ADHESION STRATA LOCATIONS | AXIAL ADHESION STRATA LOCATIONS | AXIAL ADHESION STRATA LOCATIONS | AXIAL ADHESION STRATA LOCATIONS | AXIAL ADHESION STRATA LOCATIONS |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | AXIAL ADHESION | LINE TYPE | 1ST STRATUM | 1ST STRATUM | 2ND STRATUM | 2ND STRATUM | 3RD STRATUM | 3RD STRATUM | 4TH STRATUM | 4TH STRATUM | 5TH STRATUM | 5TH STRATUM |
| LINE LABEL | AXIAL ADHESION | LINE TYPE | TOP | BOTTOM | TOP | BOTTOM | TOP | BOTTOM | TOP | BOTTOM | TOP | BOTTOM |
| SOIL | ADHA | SLOC |  |  |  |  |  |  |  |  |  |  |
| 1-- 4 | 6-- 9 | 14--17 | 19<--24 | 25<--30 | 31<--36 | 37<--42 | 43<--48 | 49<--54 | 55<--60 | 61<--66 | 67<--72 | 73<--78 |
| DEFAULT |  |  |  |  |  |  |  |  |  |  |  |  |
| ENGLISH |  |  | FT | FT | FT | FT | FT | FT | FT | FT | FT | FT |
| METRIC |  |  | M | M | M | M | M | M | M | M | M | M |



SOIL AXIAL ADHESION CAPACITY LINE

COLUMNS

COMMENTARY

LOCATION THIS LINE FOLLOWS THE SOIL LOCATION LINES FOR ADHESION DATA.

GENERAL THIS LINE SET IS USED TO ENTER THE AXIAL ADHESION CAPACITIES FOR THE TOP AND BOTTOM OF EACH STRATUM DEFINED BY THE SOIL ADHESION STRATA LINES. THE ADHESION CAPACITY IS CONSTANT WITHIN A STRATUM AND EQUALS THE AVERAGE OF THE VALUES INPUT AT ITS TOP AND BOTTOM.

( 1- 4) ENTER 'SOIL'.   
( 6- 9) ENTER 'ADHA'.   
(14-16) ENTER 'EXT' IF THE VALUES ENTERED ON THIS LINE ARE FOR ADHESION ON THE EXTERIOR SURFACE OF THE PILE. ENTER 'INT' IF THE VALUES ENTERED ARE FOR ADHESION ON THE INTERIOR SURFACE OF THE PILE. IF LEFT BLANK THE VALUES WILL BE FOR BOTH THE EXTERIOR AND INTERIOR SURFACES. IF DATA IS INPUT FOR EXTERIOR ADHESION AND NOT FOR INTERIOR ADHESION THEN THERE WILL BE NO INTERIOR ADHESION AND VICE VERSA.   
( 17 ) ENTER 'C' IF THE VALUES ENTERED ON THIS LINE ARE FOR RESISTING COMPRESSION IN THE PILE AND 'T' IF FOR RESISTING PILE TENSION. IF LEFT BLANK THEN THESE VALUES WILL APPLY TO EITHER PILE TENSION OR COMPRESSION.   
(19-78) ENTER THE ADHESION CAPACITIES AT THE TOP AND BOTTOM OF EACH STRATUM. IF MORE THAN FIVE STRATA ARE USED, REPEAT THIS LINE UNTIL ALL STRATA ARE DEFINED.



| LINE LABEL | AXIAL ADHESION | EXTERNAL OR INTERNAL ADHESION | TENSION OR COMPRESSION RESISTANCE | SOIL AXIAL ADHESION CAPACITIES | SOIL AXIAL ADHESION CAPACITIES | SOIL AXIAL ADHESION CAPACITIES | SOIL AXIAL ADHESION CAPACITIES | SOIL AXIAL ADHESION CAPACITIES | SOIL AXIAL ADHESION CAPACITIES | SOIL AXIAL ADHESION CAPACITIES | SOIL AXIAL ADHESION CAPACITIES | SOIL AXIAL ADHESION CAPACITIES | SOIL AXIAL ADHESION CAPACITIES |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | AXIAL ADHESION | EXTERNAL OR INTERNAL ADHESION | TENSION OR COMPRESSION RESISTANCE | 1ST STRATUM | 1ST STRATUM | 2ND STRATUM | 2ND STRATUM | 3RD STRATUM | 3RD STRATUM | 4TH STRATUM | 4TH STRATUM | 5TH STRATUM | 5TH STRATUM |
| LINE LABEL | AXIAL ADHESION | EXTERNAL OR INTERNAL ADHESION | TENSION OR COMPRESSION RESISTANCE | TOP | BOTTOM | TOP | BOTTOM | TOP | BOTTOM | TOP | BOTTOM | TOP | BOTTOM |
| SOIL | ADHA |  |  |  |  |  |  |  |  |  |  |  |  |
| 1-- 4 | 6-- 9 | 14--16 | 17 | 19<--24 | 25<--30 | 31<--36 | 37<--42 | 43<--48 | 49<--54 | 55<--60 | 61<--66 | 67<--72 | 73<--78 |
| DEFAULT |  | BOTH | BOTH |  |  |  |  |  |  |  |  |  |  |
| ENGLISH |  |  |  | KIP/SQ.FT | KIP/SQ.FT | KIP/SQ.FT | KIP/SQ.FT | KIP/SQ.FT | KIP/SQ.FT | KIP/SQ.FT | KIP/SQ.FT | KIP/SQ.FT | KIP/SQ.FT |
| METRIC (KN) |  |  |  | KN/SQ.CM | KN/SQ.CM | KN/SQ.CM | KN/SQ.CM | KN/SQ.CM | KN/SQ.CM | KN/SQ.CM | KN/SQ.CM | KN/SQ.CM | KN/SQ.CM |
| METRIC (KG) |  |  |  | KG/SQ.CM | KG/SQ.CM | KG/SQ.CM | KG/SQ.CM | KG/SQ.CM | KG/SQ.CM | KG/SQ.CM | KG/SQ.CM | KG/SQ.CM | KG/SQ.CM |



SOIL AXIAL ADHESION HEADER LINE

COLUMNS

COMMENTARY

COLUMNS

COMMENTARY

GENERAL

THIS LINE AND THE 'SLOC' LINE ARE USED TO MODEL THE AXIAL LOAD TRANSFER TO THE SOIL BY ADHESION. AN AXIAL ADHESION CAPACITY IS SPECIFIED AT THE TOP AND BOTTOM OF EACH SOIL STRATUM. IF THE VALUES ARE DIFFERENT AN AVERAGE IS USED. STARTING AT THE TOP STRATUM THE LENGTH OVER WHICH THE ADHESION MUST ACT IN ORDER TO TRANSFER THE PILE AXIAL LOAD IS COMPUTED. IF THIS LENGTH IS LESS THAN THE THICKNESS OF THAT STRATUM THE AXIAL LOAD IS COMPLETELY TRANSFERRED TO THE SOIL OVER THAT LENGTH. IF THE COMPUTED LENGTH IS GREATER THAN THE THICKNESS OF THE STRATUM THE AXIAL IS ONLY PARTIALLY TRANSFERRED IN THAT STRATUM. THE EXCESS PILE LOAD IS TRANSFERRED IN THE NEXT DEEPER SOIL STRATUM. THE PROCEDURE IS REPEATED FOR EACH SOIL STRATUM IN TURN UNTIL THE ENTIRE AXIAL LOAD IS TRANSFERRED OR UNTIL ALL SOIL STRATA HAVE REACHED THEIR CAPACITIES. ANY EXCESS AXIAL LOAD IS THEN TRANSFERRED BY END BEARING UNTIL THE BEARING CAPACITY IS REACHED. IF THE TOTAL PILE AXIAL LOAD HAS NOT THEN BEEN TRANSFERRED THE PILE LOAD EXCEEDS ITS CAPACITY AND IT FAILS, A REPORT TO THIS EFFECT IS ISSUED.

THIS SOIL MODEL TAKES NO ACCOUNT OF SOIL DEFORMATIONS IN THE AXIAL DIRECTION. THE AXIAL DISPLACEMENT AT THE PILEHEAD IS TAKEN TO BE EQUAL TO THE COMPRESSIVE (OR TENSILE) DEFORMATION OF THE PILE.

( 1- 4) ENTER 'SOIL'.   
( 6-10) ENTER 'AXIAL'.   
(14-17) ENTER 'HEAD'.   
(18-20) ENTER THE NUMBER OF SOIL STRATA TO BE DESCRIBED FOR ADHESION SOIL DATA.   
(21-30) ENTER THE END BEARING CAPACITY FOR THIS SOIL TABLE.   
(41-44) ENTER AN ALPHANUMERIC SOIL TABLE IDENTIFIER. THIS IDENTIFIER IS USED ON ONE OR MORE 'PILE' LINES TO ASSOCIATE THESE AXIAL SOIL PROPERTIES WITH THOSE PILES.   
(45-60) ENTER ANY DESCRIPTIVE REMARKS FOR THIS AXIAL SOIL DATA.   
(62-64) ENTER THE METHOD TO BE USED IN CONJUNCTION WITH CPT STRATA.

SELECT FROM THE FOLLOWING:

'ICP' - SIMPLIFIED ICP-05.   
'UWA' - OFFSHORE UWA-05.   
'FUG' - FUGRO-05.   
'NGI' - NGI-05.

(66-71) ENTER THE DIAMETER OF THE CONE PENETRATION TOOL FOR CPT STRATA.



| LINE LABEL | AXIAL LABEL | HEAD LABEL | NUMBER OF SOIL STRATA | END BEARING CAPACITY | SOIL TABLE ID | SOIL DESCRIPTION OR OTHER REMARKS | CPT METHOD | CPT TOOL DIAMETER | LEAVE BLANK |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOIL | AXIAL | HEAD |  |  |  |  |  |  |  |
| 1--4 | 6--10 | 14--17 | 18--->20 | 21<--30 | 41<--44 | 45----60 | 62--64 | 66--71 | 72--80 |
| DEFAULT |  |  |  |  |  |  | 'ICP' | 36mm |  |
| ENGLISH |  |  |  | KIP/SQ.FT |  |  |  | IN |  |
| METRIC (KN) |  |  |  | KN/SQ.CM |  |  |  | CM |  |
| METRIC (KG) |  |  |  | KG/SQ.CM |  |  |  | CM |  |



SOIL T-Z AXIAL STRATUM LOCATION LINE

COLUMNS

COMMENTARY

GENERAL

THIS LINE IS USED FOR EACH STRATUM TO SPECIFY WHETHER THE T-Z CURVE IS SYMMETRICAL, THE NUMBER OF POINTS DEFINING IT, THE LOCATIONS OF THE TOP AND BOTTOM OF THE STRATUM AND TO ENTER A T FACTOR FOR MULTIPLYING THE T VALUES ENTERED ON THE FOLLOWING T-Z LINE.

THE T-Z STRATA LOCATIONS NEED NOT COINCIDE WITH THE P-Y STRATA LOCATIONS.

( 1- 4) ENTER 'SOIL'.   
(14-17) ENTER 'SLOC'.   
(18-19) ENTER 'SM' IF THE T-Z CURVE FOR THIS STRATUM HAS THE SAME SHAPE WHETHER THE PILE IS IN TENSION OR COMPRESSION. IF 'SM' IS ENTERED THEN THE FOLLOWING T-Z LINES FOR THIS STRATUM MUST HAVE ENTRIES ONLY FOR POSITIVE T AND Z VALUES. THE ORIGIN, T=0, Z=0, MUST BE THE FIRST POINT ENTERED IN THIS CASE.   
(22-23) ENTER THE NUMBER OF POINTS ON THE FOLLOWING T-Z CURVE. ONE POINT CONSISTS OF A T VALUE AND A Z VALUE. THE NUMBER ENTERED HERE MAY NOT BE GREATER THAN THE VALUE ENTERED IN COLUMNS 22-23 OF THE T-Z AXIAL HEADER LINE ('SOIL TZAXIAL HEAD' LINE SET) OR 30 IF THOSE COLUMNS ARE BLANK.   
(25-30) ENTER THE DISTANCE FROM THE PILEHEAD TO THE TOP OF THIS STRATUM. THE STRATUM AND T-Z LINES ARE ENTERED IN ORDER OF INCREASING DEPTH. THESE DISTANCES ARE VERTICALLY DOWN AND NOT ALONG THE AXIS OF THE PILE, WHICH MAY BE BATTERED. THE FIRST POINT NEED NOT BE AT THE PILEHEAD.   
(31-36) IF THE FOLLOWING T-Z DATA IS CONSTANT FOR THIS STRATUM, ENTER THE DISTANCE FROM THE PILEHEAD TO THE BOTTOM OF THIS STRATUM. IF LEFT BLANK, THE T-Z DATA WILL VARY LINEARLY TO THE TOP OF THE NEXT STRATUM. NO GAPS SHOULD BE LEFT BETWEEN STRATA.   
(39-44) T ON THE T-Z LINES FOR THIS STRATUM WILL BE MULTIPLIED BY THIS VALUE. THIS ENTRY CAN BE USED TO CHANGE INPUT INTO MORE CONVENIENT UNITS IF DESIRED.   
(45-60) ENTER ANY DESCRIPTIVE REMARKS DESIRED.



| LINE LABEL | LINE TYPE | SYMMETRICAL T-Z CURVE | NUMBER OF POINTS PER CURVE | STRATUM LOCATION | STRATUM LOCATION | T FACTOR | SOIL STRATUM DESCRIPTION | LEAVE BLANK |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | LINE TYPE | SYMMETRICAL T-Z CURVE | NUMBER OF POINTS PER CURVE | TOP | BOTTOM | T FACTOR | SOIL STRATUM DESCRIPTION | LEAVE BLANK |
| SOIL | SLOC |  |  |  |  |  |  |  |
| 1-- 4 | 14--17 | 18--19 | 22--->23 | 25<--30 | 31<--36 | 39<--44 | 45<----60 | 61--80 |
| DEFAULT |  |  |  |  |  | 1 |  |  |
| ENGLISH |  |  |  | FT | FT |  |  |  |
| METRIC |  |  |  | M | M |  |  |  |



SOIL T-Z LINE

COLUMNS

COMMENTARY

GENERAL THIS LINE IS USED TO ENTER THE T-Z DATA FOR THE SOIL STRATUM DEFINED ON THE IMMEDIATELY PRECEDING STRATUM LOCATION LINE. THE NUMBER OF POINTS ENTERED MUST BE THE SAME AS SPECIFIED IN COLUMNS 22-23 OF THAT LINE. FOR A SYMMETRICAL T-Z CURVE ('SM' IN COLUMNS 18-19 OF THE STRATUM LOCATION LINE) ONLY POINTS HAVING POSITIVE T AND Z VALUES SHOULD BE ENTERED AND THE FIRST POINT MUST BE T=0, Z=0. UP TO 5 POINTS PER LINE MAY BE ENTERED AND AS MANY LINES AS NECESSARY MAY BE ENTERED. FOR VALUES OF Z GREATER THAN THE LAST ENTERED VALUE THE PROGRAM USES THE LAST ENTERED T VALUE, THAT IS, THE CURVE IS FLAT.

( 1- 4) ENTER 'SOIL'.   
(14-16) ENTER 'T-Z'.   
(18-77) ENTER THE T-Z DATA FOR THIS STRATUM.



| LINE LABEL | LINE TYPE | T-Z CURVE DATA POINTS | T-Z CURVE DATA POINTS | T-Z CURVE DATA POINTS | T-Z CURVE DATA POINTS | T-Z CURVE DATA POINTS | T-Z CURVE DATA POINTS | T-Z CURVE DATA POINTS | T-Z CURVE DATA POINTS | T-Z CURVE DATA POINTS | T-Z CURVE DATA POINTS | LEAVE BLANK |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | LINE TYPE | 1ST POINT | 1ST POINT | 2ND POINT | 2ND POINT | 3RD POINT | 3RD POINT | 4TH POINT | 4TH POINT | 5TH POINT | 5TH POINT | LEAVE BLANK |
| LINE LABEL | LINE TYPE | T | Z | T | Z | T | Z | T | Z | T | Z | LEAVE BLANK |
| SOIL | T-Z |  |  |  |  |  |  |  |  |  |  |  |
| 1-- 4 | 14--16 | 18<--23 | 24<--29 | 30<--35 | 36<--41 | 42<--47 | 48<--53 | 54<--59 | 60<--65 | 66<--71 | 72<--77 | 78--80 |
| DEFAULT |  |  |  |  |  |  |  |  |  |  |  |  |
| ENGLISH |  | KSI | IN | KSI | IN | KSI | IN | KSI | IN | KSI | IN |  |
| METRIC (KN) |  | KN/SQ.CM | CM | KN/SQ.CM | CM | KN/SQ.CM | CM | KN/SQ.CM | CM | KN/SQ.CM | CM |  |
| METRIC (KG) |  | KG/SQ.CM | CM | KG/SQ.CM | CM | KG/SQ.CM | CM | KG/SQ.CM | CM | KG/SQ.CM | CM |  |



SOIL T-Z AXIAL HEADER LINE

COLUMNS

COMMENTARY

GENERAL

THIS LINE IS USED TO SPECIFY THE NUMBER OF SOIL STRATA, THE MAXIMUM NUMBER OF POINTS DEFINING THE T-Z CURVES AND THE SOIL IDENTIFIER FOR A T-Z AXIAL SOIL DESCRIPTION.

A T-Z AXIAL SOIL DESCRIPTION ACCOUNTS FOR SOIL DEFORMATION RESULTING FROM THE TRANSFER OF PILE AXIAL LOAD TO THE SOIL THROUGH THE ACTION OF SHEAR FORCES BETWEEN THE PILE LATERAL SURFACE AND THE SURROUNDING SOIL.

THE SEQUENCE OF LINES REQUIRED FOR A T-Z SOIL DESCRIPTION ISAS FOLLOWS:

1. THIS SOIL T-Z AXIAL HEADER LINE.   
2. AN AXIAL STRATUM LOCATION LINE FOR THE UPPERMOST STRATUM.   
3. ONE OR MORE T-Z LINES FOR THE UPPERMOST STRATUM.   
4. AN AXIAL STRATUM LOCATION LINE FOR THE SECOND STRATUM.   
5. T-Z LINES FOR THE SECOND STRATUM.

ETC.

COLUMNS

COMMENTARY

( 1- 4 ) ENTER 'SOIL'.   
( 6-12) ENTER 'TZAXIAL'.   
(14-17) ENTER 'HEAD'.   
(18-20) ENTER THE NUMBER OF SOIL STRATA FOR THIS T-Z DESCRIPTION.   
(22-23) IF ANY T-Z CURVE ENTERED IS DEFINED AT MORE THAN 30 POINTS ENTER THAT NUMBER HERE. OTHERWISE, LEAVE BLANK.   
(28-33) ENTER THE FACTOR TO BE APPLIED TO ALL T INPUT VALUES.   
(34-40) ENTER THE FACTOR TO BE APPLIED TO ALL Z INPUT VALUES.   
(41-44) ENTER A SOIL TABLE IDENTIFIER. THIS IDENTIFIER IS USED ON ONE OR MORE 'PILE' LINES TO ASSOCIATE THIS SOIL TABLE WITH THOSE PILES.   
(45-60) ENTER ANY DESCRIPTIVE COMMENTS DESIRED.

( 61 ) CONSIDER BASE SHEAR IN ANALYSIS



| LINE LABEL | T-Z AXIAL LABEL | HEAD LABEL | NUMBER OF SOIL STRATA | MORE THAN 30 DATA POINTS FOR T-Z CURVE | T FACTOR | Z FACTOR | SOIL TABLE ID | SOIL DESCRIPTION OR OTHER REMARKS | CONSIDER BASE SHEAR IN ANALYSIS? | LEAVE BLANK |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOIL | TZAXIAL | HEAD |  |  |  |  |  |  |  |  |
| 1--4 | 6--12 | 14--17 | 18--->20 | 22--->23 | 28<--33 | 34<--40 | 41--44 | 45-----60 | 61 | 62--80 |
| DEFAULT |  |  |  |  | 1 | 1 |  |  |  |  |



SOIL T-Z END BEARING STRATUM LINE

COLUMNS

COMMENTARY

GENERAL THIS LINE IS USED FOR EACH SOIL STRATUM TO SPECIFY THE NUMBER OF POINTS ON THE T-Z END BEARING CURVE, THE LOCATIONS OF THE TOP AND BOTTOM OF THE STRATUM, AND TO ENTER A T FACTOR FOR MULTIPLYING THE T VALUES ENTERED ON THE FOLLOWING T-Z LINE ('SOIL T-Z' END BEARING LINE SET).

( 1- 4) ENTER 'SOIL'.   
(14-17) ENTER 'SLOC'.   
(22-23) ENTER THE NUMBER OF POINTS ON THE FOLLOWING T-Z CURVE. ONE POINT CONSISTS OF A T VALUE AND A Z VALUE. THE NUMBER ENTERED HERE MAY NOT BE GREATER THAN THE VALUE ENTERED IN COLUMNS 22-23 OF THE BEARING HEADER LINE ('SOIL BEARING HEAD' LINE SET) OR 30 IF THOSE COLUMNS ARE BLANK.   
(25-30) ENTER THE DISTANCE FROM THE PILEHEAD TO THE TOP OF THIS SOIL STRATUM. THIS DISTANCE IS VERTICALLY DOWN AND NOT ALONG THE AXIS OF THE PILE, WHICH MAY BE BATTERED.   
(31-36) ENTER THE DISTANCE FROM THE PILEHEAD TO THE BOTTOM OF THESOIL STRATUM IF THE T-Z DATA IS CONSTANT THROUGHOUT THISSTRATUM. IF LEFT BLANK, THE T-Z DATA WILL VARY LINEARLY TOTHE TOP OF THE NEXT STRATUM. FOR THE LAST STRATUM THE BOTTOMDISTANCE SHOULD BE ENTERED AS SOME VALUE DEEPER THAN THE PILETIP (TAKING PILE BATTER INTO ACCOUNT).  
(39-44) ENTER THE T FACTOR FOR THIS T-Z CURVE. THIS FACTOR IS USED TO MODIFY THE T VALUES INPUT FOR THIS SOIL STRATUM. IT IS INDEPENDENT OF THE T FACTOR ENTERED ON THE 'PLGRUP' LINES. THIS FACTOR MAY BE USED IN CONJUNCTION WITH NORMALIZED T-Z CURVES TO OBTAIN THE CORRECT T MAGNITUDES OR IT MAY BE USED FOR UNIT CONVERSIONS.   
(45-60) ENTER ANY DESCRIPTIVE REMARKS ABOUT THIS SOIL STRATUM.



| LINE LABEL | LINE TYPE | NUMBER OF POINTS PER CURVE | STRATUM LOCATION | STRATUM LOCATION | T FACTOR | SOIL STRATUM DESCRIPTION | LEAVE BLANK |
| --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | LINE TYPE | NUMBER OF POINTS PER CURVE | TOP | BOTTOM | T FACTOR | SOIL STRATUM DESCRIPTION | LEAVE BLANK |
| SOIL | SLOC |  |  |  |  |  |  |
| 1--4 | 14--17 | 22--->23 | 25<--30 | 31<--36 | 39<--44 | 45----60 | 61--80 |
| DEFAULT |  |  |  |  | 1 |  |  |
| ENGLISH |  |  | FT | FT |  |  |  |
| METRIC |  |  | M | M |  |  |  |



SOIL T-Z END BEARING HEADER LINE

COLUMNS

COMMENTARY

GENERAL

THIS LINE FOLLOWED BY 'SLOC' LINES IS USED TO MODEL PILE END BEARING ACCOUNTING FOR THE RESILIENCE OF THE SOIL. THE T-Z BEARING DATA MAY BE ENTERED FOR BOTH POSITIVE (BEARING) AND NEGATIVE (SUCTION) VALUES OF FORCE AND DISPLACEMENT. IF ONLY POSITIVE VALUES ARE ENTERED, THEN THE SUCTION RESISTANCE IS ZERO FOR ALL NEGATIVE DISPLACEMENTS. FOR VALUES OF Z GREATER THAN THE LAST VALUE ENTERED, THE VALUE OF T IS TAKEN TO BE THE LAST ENTERED VALUE AND SIMILARLY FOR THE FIRST, I.E. THE CURVE IS EXTRAPOLATED FLAT AT BOTH ENDS. IN ORDER TO USE THESE LINES THE SOIL AXIAL BEHAVIOR MUST BE MODELED WITH T-Z DATA ('SOIL BEARING HEAD', 'SOIL SLOC', AND 'SOIL T-Z' LINES). THIS LINE WILL THEN FOLLOW THOSE T-Z AXIAL LINES. THIS LINE SETS UP THE GENERAL PARAMETERS AND TABLE IDENTIFICATION FOR THE END BEARING T-Z DATA. THE END BEARING LINE ORDER IS AS FOLLOWS:

THIS SOIL BEARING HEADER LINE.

SOIL END BEARING STRATUM LINE FOR 1ST STRATUM.

SOIL END BEARING T-Z LINES FOR 1ST STRATUM.

SOIL END BEARING STRATUM LINE FOR 2ND STRATUM.

SOIL END BEARING T-Z LINES FOR 2ND STRATUM.

ETC.

COLUMNS

COMMENTARY

( 1- 4) ENTER 'SOIL'.   
( 6-12) ENTER 'BEARING'.   
(14-17) ENTER 'HEAD'.   
(18-20) ENTER THE NUMBER OF SOIL STRATA FOR THIS END BEARING T-Z DESCRIPTION. DO NOT LEAVE THIS FIELD BLANK. THE PROGRAM PERMITS END BEARING TO BE SPECIFIED AT SEVERAL POINTS ALONG THE PILE SO THAT STEPPED PILES CAN BE MODELED. IN THE USUAL CASE, END BEARING WILL ONLY EXIST AT THE PILE TIP. IN THIS CASE IT IS ONLY NECESSARY TO ENTER ONE STRATUM WHICH WILL INCLUDE THE PILE TIP.   
(22-23) IF ANY T-Z CURVE ENTERED ('SOIL T-Z' LINE) IS DEFINED AT MORE THAN 30 POINTS, ENTER THAT NUMBER HERE. OTHERWISE, LEAVE BLANK.   
(34-40) ENTER THE FACTOR TO BE APPLIED TO ALL "Z" INPUT VALUES.   
(41-44) ENTER THE UNIQUE ALPHANUMERIC SOIL TABLE IDENTIFIER. THIS IDENTIFIER IS USED ON ONE OR MORE 'PILE' LINES TO ASSOCIATE THIS TABLE WITH THOSE PILES.   
(45-60) ENTER ANY DESCRIPTIVE COMMENTS DESIRED.



| LINE LABEL | BEARING LABEL | HEAD LABEL | NUMBER OF SOIL STRATA | MORE THAN 30 DATA POINTS FOR T-Z CURVE | Z FACTOR | SOIL TABLE ID | SOIL TABLE DESCRIPTION | LEAVE BLANK |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOIL | BEARING | HEAD |  |  |  |  |  |  |
| 1--4 | 6--12 | 14--17 | 18--->20 | 22--->23 | 34<--40 | 41<--44 | 45-----60 | 61--80 |
| DEFAULT |  |  |  |  | 1 |  |  |  |



SOIL T-Z END BEARING DATA LINE

COLUMNS

COMMENTARY

GENERAL THIS LINE SET IS USED TO INPUT THE END BEARING T-Z DATA FOREACH SOIL STRATUM DEFINED ON THE IMMEDIATELY PRECEDINGSTRATUM LOCATION LINE. THE NUMBER OF POINTS ENTERED MUST BETHE SAME AS SPECIFIED IN COLUMNS 22-23 OF THAT LINE. THISLINE MAY BE REPEATED AS REQUIRED UNTIL ALL STRATA ARE DEFINED.

( 1- 4) ENTER 'SOIL'.   
(14-16) ENTER 'T-Z'.   
(18-77) ENTER THE POINTS ON THE BEARING PRESSURE (T) VERSUS DISPLACEMENT (Z) CURVE FOR THIS STRATUM.



| LINE LABEL | LINE TYPE | T-Z CURVE DATA POINTS | T-Z CURVE DATA POINTS | T-Z CURVE DATA POINTS | T-Z CURVE DATA POINTS | T-Z CURVE DATA POINTS | T-Z CURVE DATA POINTS | T-Z CURVE DATA POINTS | T-Z CURVE DATA POINTS | T-Z CURVE DATA POINTS | T-Z CURVE DATA POINTS |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | LINE TYPE | 1ST ENTRY | 1ST ENTRY | 2ND ENTRY | 2ND ENTRY | 3RD ENTRY | 3RD ENTRY | 4TH ENTRY | 4TH ENTRY | 5TH ENTRY | 5TH ENTRY |
| LINE LABEL | LINE TYPE | T | Z | T | Z | T | Z | T | Z | T | Z |
| SOIL | T-Z |  |  |  |  |  |  |  |  |  |  |
| 1-- 4 | 14--16 | 18<--23 | 24<--29 | 30<--35 | 36<--41 | 42<--47 | 48<--53 | 54<--59 | 60<--65 | 66<--71 | 72<--77 |
| DEFAULT |  |  |  |  |  |  |  |  |  |  |  |
| ENGLISH |  | KSI | IN | KSI | IN | KSI | IN | KSI | IN | KSI | IN |
| METRIC (KN) |  | KN/SQ.CM | CM | KN/SQ.CM | CM | KN/SQ.CM | CM | KN/SQ.CM | CM | KN/SQ.CM | CM |
| METRIC (KG) |  | KG/SQ.CM | CM | KG/SQ.CM | CM | KG/SQ.CM | CM | KG/SQ.CM | CM | KG/SQ.CM | CM |



PSI LOAD CASE SELECTION

COLUMNS

COMMENTARY

GENERAL THIS LINE MAY BE USED TO SPECIFY THE LOAD CASES IN THE SACSIV INPUT FILE THAT ARE TO BE USED FOR A PILE CAPACITY ANDCODE CHECK. THIS LINE CAN BE REPEATED AS OFTEN AS NECESSARYTO SELECT ANY OR ALL OF THE LOAD CASES.

( 7- 8) ENTER THE FUNCTION FOR THE LOAD CASE SELECTION: 'IN' - INCLUDE THESE LOAD CASES FOR PILE CHECK AND CAPACITY. 'EX' - EXCLUDE THESE LOAD CASES FOR PILE CHECK AND CAPACITY.   
(17-75) ENTER THE LOAD CASE IDENTIFIERS FOR ALL LOAD CASES TO BE SELECTED. THE LOAD CASES CAN BE IN ANY ORDER.



| LINE LABEL | FUNCTION | LOAD CASE SELECTION | LOAD CASE SELECTION | LOAD CASE SELECTION | LOAD CASE SELECTION | LOAD CASE SELECTION | LOAD CASE SELECTION | LOAD CASE SELECTION | LOAD CASE SELECTION | LOAD CASE SELECTION | LOAD CASE SELECTION | LOAD CASE SELECTION | LOAD CASE SELECTION |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | FUNCTION | 1ST | 2ND | 3RD | 4TH | 5TH | 6TH | 7TH | 8TH | 9TH | 10TH | 11TH | 12TH |
| LCSEL |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 1-- 5 | 7-- 8 | 17-->20 | 22-->25 | 27-->30 | 32-->35 | 37-->40 | 42-->45 | 47-->50 | 52-->55 | 57-->60 | 62-->65 | 67-->70 | 72-->75 |
| DEFAULT | 'IN' |  |  |  |  |  |  |  |  |  |  |  |  |



PILE DESCRIPTION LINE

COLUMNS

COMMENTARY

GENERAL

THIS LINE IS REQUIRED FOR EACH PILE THAT IS TO BE INCLUDED IN THE ANALYSIS. IT IS USED TO SPECIFY EACH PILE'S GEOMETRY AND TO DESIGNATE THE SOIL TABLES THAT ARE TO BE USED FOR ITS ANALYSIS.

( 1- 4) ENTER 'PILE'. THE FIRST LINE IS A HEADER WITH ONLY THIS ENTRY.   
( 7-10) ENTER THE JOINT NAME IN THE STRUCTURAL MODEL THAT CONNECTS TO THIS PILE. THIS JOINT MUST BE ONE OF THOSE DESIGNATED BY 'PILEHD' OR '222222' IN COLUMNS 55-60 ON THE SACS IV 'JOINT' LINES.   
(11-14) EITHER THIS FIELD OR COLUMNS 21-50 ARE USED TO SPECIFY THE PILE'S BATTER, BUT NOT BOTH. IF THE BATTER IS SPECIFIED BY A SECOND JOINT IN THE STRUCTURE ENTER THE NAME OF THAT JOINT HERE. THIS JOINT MUST BE ABOVE THE PILEHEAD JOINT. THE AXIS OF THE PILE WILL BE ON THE LINE THROUGH THIS JOINT AND THE PILEHEAD JOINT.   
(16-18) ENTER THE PILE GROUP LABEL THAT IDENTIFIES THE 'PLGRUP' WHERETHE PROPERTIES FOR THIS PILE ARE SPECIFIED.  
(21-50) IF A BATTER DEFINITION JOINT WAS ENTERED IN COLUMNS 11-14 THEN LEAVE THESE FIELDS BLANK. OTHERWISE, ENTER THE X, Y, AND Z DISTANCES (GLOBAL DIRECTIONS) FROM THE PILEHEAD TO A POINT ABOVE IT. THE AXIS OF THE PILE WILL BE ON THE LINE FROM THE PILEHEAD TO THIS POINT. FOR EXAMPLE X=1.0, Y=0.0, Z=8.0 WOULD DEFINE A BATTER OF 1:8 WITH POSITIVE SLOPE IN THE X-Z PLANE.

COLUMNS

COMMENTARY

(51-56) THE DEFAULT INITIAL LOCAL COORDINATES FOR PILES ARE DEFINEDTHE SAME AS FOR MEMBERS IN SACS IV WITH THE LOCAL X AXISPOINTING UPWARD FROM THE PILEHEAD ALONG THE AXIS OF THE PILE(SEE THE ACCOMPANYING FIGURE). THE LOCAL Y AND Z AXES MAY BEROTATED FROM THESE DIRECTIONS BY THE AMOUNT ENTERED HERE.IF AN ANGLE IS ENTERED HERE, PILE ANALYSES WILL BE DONE INTHE PLANES DEFINED BY THESE ROTATED COORDINATE AXES. THEAUTOMATIC ALIGNMENT OF THE PILE ANALYSIS PLANE TO COINCIDEWITH THE PLANE OF MAXIMUM PILEHEAD DEFLECTION WILL NOT BEDONE (SEE THE 'PLTLC' LINE FOR A DISCUSSION OF THE AUTOMATICALIGNMENT FEATURE).  
(69-72) ENTER THE SOIL TABLE IDENTIFIER TO DEFINE THE SOIL PROPERTIES ASSOCIATED WITH THIS PILE IN THE LOCAL X-Z PLANE. THE ENTRY MUST MATCH AN ENTRY IN THE SOIL TABLE INPUT.   
(74-77) ENTER THE SOIL TABLE IDENTIFIER FOR THE LOCAL X-Y PLANE ONLY IF DIFFERENT FROM THE X-Z PLANE. NORMALLY THIS ENTRY IS LEFT BLANK EXCEPT WHEN SOIL PROPERTIES ARE DIRECTIONAL AS IN THE CASE OF MUDSLIDES. IF THE X-Z AND X-Y SOIL TABLES ARE DIFFERENT, THE AUTOMATIC ALIGNMENT OF THE PILE TO COINCIDE WITH THE PLANE OF MAXIMUM PILEHEAD DEFLECTION WILL NOT BE DONE.



| LINE LABEL | PILEHEAD JOINT NAME | BATTER DEFINITION JOINT NAME | PILE GROUP LABEL | BATTER DEFINITION COORDINATES | BATTER DEFINITION COORDINATES | BATTER DEFINITION COORDINATES | PILE CHORD ANGLE | SOIL TABLE ID X-Z PLANE | SOIL TABLE ID X-Y PLANE |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | PILEHEAD JOINT NAME | BATTER DEFINITION JOINT NAME | PILE GROUP LABEL | X | Y | Z | PILE CHORD ANGLE | SOIL TABLE ID X-Z PLANE | SOIL TABLE ID X-Y PLANE |
| PILE |  |  |  |  |  |  |  |  |  |
| 1--4 | 7-->10 | 11-->14 | 16<!--18 | 21<!--30 | 31<!--40 | 41<!--50 | 51<!--56 | 69<!--72 | 74<!--77 |
| DEFAULT |  |  |  |  |  |  | 0 |  |  |
| ENGLISH |  |  |  | IN | IN | IN | DEG |  |  |
| METRIC |  |  |  | CM | CM | CM | DEG |  |  |



PILE SUPERELEMENT CREATION

COLUMNS

COMMENTARY

GENERAL THIS LINE IS OPTIONAL FOR ANY PSI RUN. IT IS USED TO SPECIFYTHAT A SUPERELEMENT IS TO BE CREATED AND WHICH PSI LOAD CASESARE TO BE USED. THIS LINE SHOULD IMMEDIATELY FOLLOW THE'PSIOPT' LINE. A SECOND SEPARATE SUPERELEMENT FILE MAY BEGENERATED BY SPECIFYING A SECOND 'PILSUP' LINE.

( 8-10) SELECT THE METHOD THAT THE PILEHEAD STIFFNESSES ARE TO BE CALCULATED (THIS IS PRIMARILY USED FOR SUBSEQUENT DYNAMIC ANALYSES): 'AVG' - PILEHEAD LOADS AND DEFLECTIONS SELECTED FROM PSI LOAD CASES AND THE PILEHEAD STIFFNESSES ARE AVERAGED FOR ALL SIMILAR PILE AND ALL SELECTED LOAD CASES. 'MAX' - USE THE MAXIMUM DEFLECTION ON ANY PILE IN THE SELECTED LOAD CASE FOR EACH PILE GROUP.   
( 12 ) ENTER AN 'X' TO INDICATE THAT LOAD CASES SPECIFIED HERE ARE TO BE EXCLUDED FROM SUPERELEMENT CREATION. LEAVING THIS BLANK MEANS LOAD CASES SPECIFIED ARE TO BE USED.   
(21-24) ENTER THE PSI LOAD CASE TO BE USED IN CREATING THE SUPERELEMENT OF THE PILEHEAD STIFFNESSES FOR LOADS IN THE GLOBAL X-DIRECTION.   
(25-28) ENTER THE PSI LOAD CASE TO BE USED IN CREATING THE SUPERELEMENT OF THE PILEHEAD STIFFNESSES FOR LOADS IN THE GLOBAL Y-DIRECTION. IF LEFT BLANK, THE PILE LOADS AND DEFLECTIONS FROM THE X-DIRECTION WILL BE USED FOR THE Y-DIRECTION ALSO.   
(29-36) IF SECOND LOAD CASES ARE TO BE USED, ENTER THESE LOAD CASES.   
(37-44) IF THIRD LOAD CASES ARE TO BE USED, ENTER THESE LOAD CASES.   
(45-52) IF FOURTH LOAD CASES ARE TO BE USED, ENTER THESE LOAD CASES.



| LINE LABEL | PILE SUPER- ELEMENT OPTION | LOAD CASE EXCLUSION | SUPER-element LOAD CASE SELECTION | SUPER-element LOAD CASE SELECTION | SUPER-element LOAD CASE SELECTION | SUPER-element LOAD CASE SELECTION | SUPER-element LOAD CASE SELECTION | SUPER-element LOAD CASE SELECTION | SUPER-element LOAD CASE SELECTION | SUPER-element LOAD CASE SELECTION | LEAVE BLANK |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | PILE SUPER- ELEMENT OPTION | LOAD CASE EXCLUSION | 1ST X LOAD CASE | 1ST Y LOAD CASE | 2ND X LOAD CASE | 2ND Y LOAD CASE | 3RD X LOAD CASE | 3RD Y LOAD CASE | 4TH X LOAD CASE | 4TH Y LOAD CASE | LEAVE BLANK |
| PILSUP |  |  |  |  |  |  |  |  |  |  |  |
| 1--6 | 8--10 | 12 | 21-->24 | 25-->28 | 29-->32 | 33-->36 | 37-->40 | 41-->44 | 45-->48 | 49-->52 | 53--80 |
| DEFAULT | 'AVG' |  |  |  |  |  |  |  |  |  |  |



PILE GROUP DESCRIPTION LINE

COLUMNS

COMMENTARY

GENERAL THIS LINE IS USED TO SPECIFY PROPERTIES OF A PILE OR GROUP OFPILES. A PILE WITH PROPERTIES THAT VARY ALONG ITS LENGTH ISDESCRIBED WITH SEVERAL 'PLGRUP' LINES HAVING THE SAME GROUPLABEL. EACH 'PLGRUP' LINE SPECIFIES THE PROPERTIES FOR ASEGMENT OF THE PILE. THE 'PLGRUP' LINES IN THIS CASE AREINPUT IN ORDER FROM THE PILEHEAD DOWN.

( 1- 6) ENTER 'PLGRUP'. THE FIRST LINE IS A HEADER LINE HAVING ONLY THIS ENTRY.   
( 8-10) ENTER THE UNIQUE GROUP LABEL FOR THIS PILE TYPE. THIS GROUP LABEL WILL BE REFERENCED BY SUBSEQUENT 'PILE' LINES.   
(12-18) IF THIS PILE HAS CROSS SECTION PROPERTIES SPECIFIED ON A'PLSECT' LINE, ENTER THE CROSS SECTION LABEL.  
(19-19) ENTER A 'U' IF A PILE FROM THIS PILE GROUP IS TO BE CONSIDERED 'DRIVEN UNPLUGGED' FOR THE PURPOSE OF CALCULATING AXIAL SOIL RESISTANCE USING API GUIDELINES. ONLY APPLIES TO THE END SEGMENT.   
(20-31) IF THE CROSS SECTION PROPERTIES HAVE NOT BEEN DESCRIBED ON A'PLSECT' LINE, ENTER THE OUTSIDE DIAMETER AND WALL THICKNESSHERE. THE PROGRAM WILL COMPUTE THE STIFFNESS PROPERTIES.  
(32-49) ENTER THE MATERIAL PROPERTIES OF THE PILE.   
(50-57) ENTER THE LENGTH OF THIS SEGMENT OF THE PILE. THE SUM OF THE LENGTHS OF ALL SEGMENTS WITH THE SAME GROUP LABEL EQUALS THE TOTAL PILE LENGTH.   
(58-69) THE PILE DIMENSIONS FOR SOIL RESISTANCE CALCULATIONS MAY BE OVERRIDDEN BY THESE ENTRIES. IF LEFT BLANK THE TRUE DIMENSIONS ARE USED. FOR TUBES ENTER THE EFFECTIVE OUTER DIAMETER AND WALL THICKNESS. FOR 'H' PILES ENTER THE EFFECTIVE WIDTH AND DEPTH (SEE THE ACCOMPANYING FIGURES).   
(70-74) THIS FACTOR IS USED TO MODIFY THE T-Z DATA FOR THIS PILE SEGMENT. THE AXIAL SOIL FORCE PER UNIT LENGTH IS CALCULATED BY MULTIPLYING THE PILE PERIMETER BY THE SOIL RESISTANCE "T" AND THIS FACTOR.   
(75-80) ENTER THE EFFECTIVE END BEARING AREA FOR THIS PILE SEGMENT. THE USER MAY SPECIFY END BEARING AREAS FOR THE BOTTOM OF EACH PILE SEGMENT TO MODEL A STEPPED PILE. HOWEVER, IN THE USUAL CASE, ONLY THE LAST SEGMENT WILL HAVE AN END BEARING AREA.



| LINE LABEL | GROUP LABEL | CROSS SECTION LABEL | DRIVEN UNPLG. | TUBULAR DIMENSIONS | TUBULAR DIMENSIONS | MATERIAL PROPERTIES | MATERIAL PROPERTIES | MATERIAL PROPERTIES | PILE SEGMENT LENGTH | PILE SURFACE DIMENSIONSB | PILE SURFACE DIMENSIONSB | T FACTOR | AVAILABLE END BEARING AREA |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | GROUP LABEL | CROSS SECTION LABEL | DRIVEN UNPLG. | OUTSIDE DIAMETER | WALL THICKNESS | E X 1000 | G X 1000 | SY | PILE SEGMENT LENGTH | A | WALL THK. | T FACTOR | AVAILABLE END BEARING AREA |
| LINE LABEL | GROUP LABEL | CROSS SECTION LABEL | DRIVEN UNPLG. | OUTSIDE DIAMETER | WALL THICKNESS | E X 1000 | G X 1000 | SY | PILE SEGMENT LENGTH | O.D. | DEPTH | T FACTOR | AVAILABLE END BEARING AREA |
| LINE LABEL | GROUP LABEL | CROSS SECTION LABEL | DRIVEN UNPLG. | OUTSIDE DIAMETER | WALL THICKNESS | E X 1000 | G X 1000 | SY | PILE SEGMENT LENGTH | FL. WIDTH |  | T FACTOR | AVAILABLE END BEARING AREA |
| PLGRP |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 1--6 | 8<--10 | 12<--18 | 19 | 20<--25 | 26<--31 | 32<--37 | 38<--43 | 44<--49 | 50<--57 | 58<--63 | 64<--69 | 70<--74 | 75<--80 |
| DEFAULT |  |  |  |  |  | 29.0 ENGL | 11.6 ENGL | 36.0 ENGL |  |  | IN | 1 |  |
| ENGLISH |  |  |  | IN | IN | KSI | KSI | KSI | FT | IN | CM |  | SQ.FT |
| METRIC (KN) |  |  |  | CM | CM | KN/SQ.CM | KN/SQ.CM | KN/SQ.CM | M | CM | CM |  | SQ.M |
| METRIC (KG) |  |  |  | CM | CM | KG/SQ.CM | KG/SQ.CM | KG/SQ.CM | M | CM |  |  | SQ.M |



PILE CROSS SECTION PROPERTY LINE

COLUMNS

COMMENTARY

GENERAL THIS LINE IS USED TO SPECIFY CROSS SECTION PROPERTIES FOR 'H'PILES OR TUBULAR PILES WITH PROPERTIES DIFFERENT FROM THOSEOF STANDARD TUBES, FOR EXAMPLE, A TUBE GROUTED INSIDE OFANOTHER TUBE.

( 1- 6) ENTER 'PLSECT' ON EACH LINE OF THIS SET. THE FIRST LINE IS A HEADER LINE HAVING ONLY THIS ENTRY.   
( 8-14) ENTER THE UNIQUE CROSS SECTION LABEL FOR THIS PARTICULAR CROSS SECTION. THIS LABEL WILL BE USED ON SUBSEQUENT 'PLGRUP' LINES. ANY COMBINATION OF ALPHANUMERIC CHARACTERS MAY BE USED.   
(16-18) ENTER 'TUB' OR 'H ' FOR TUBULAR OR 'H' TYPE CROSS SECTIONS. FOR A GROUTED DOUBLE TUBULAR, ENTER 'TUB' AND THEN ADD THE APPROPRIATE DIMENSIONS UNDER PROPERTY LABELS C AND D.   
(19-48) ENTER THE CROSS SECTION PROPERTIES FOR STIFFNESS CALCULATIONS (AREA, TORSIONAL CONSTANT, AND MOMENTS OF INERTIA ABOUT THE LOCAL Y AND Z AXES).   
(51-74) ENTER THE CROSS SECTIONAL PROPERTIES FOR STRESS CALCULATIONS ACCORDING TO THE FOLLOWING SCHEDULE (SEE THE ACCOMPANYING FIGURES):

PROPERTY

TUBULAR

'H'

LABEL

PILE

PILE

(51-56) A OUTER DIAMETER FLANGE WIDTH   
(57-62) B WALL THICKNESS DEPTH   
(63-68) C INNER TUBE OD SHEAR AREA IN Y DIRECTION   
(69-74) D INNER TUBE WT SHEAR AREA IN Z DIRECTION *

* THIS IS THE AREA USED FOR CALCULATING SHEAR STRESS. FOR TUBES IT IS TAKEN AS ONE HALF OF THE AREA OF THE CROSS SECTION.

(75-80) THE USER MAY ENTER THE WEIGHT PER UNIT LENGTH OF THE PILE. IF SO ENTERED, THE VALUE ENTERED HERE WILL OVERRIDE THE MATERIAL DENSITY ENTERED ON THE 'PSIOPT' LINE.



| LINE LABEL | CROSS SECTION LABEL | CROSS SECTION TYPE | CROSS SECTION STIFFNESS PROPERTIES | CROSS SECTION STIFFNESS PROPERTIES | CROSS SECTION STIFFNESS PROPERTIES | CROSS SECTION STIFFNESS PROPERTIES | CROSS SECTION DETAILS FOR STRESS CALCULATIONSBCD | CROSS SECTION DETAILS FOR STRESS CALCULATIONSBCD | CROSS SECTION DETAILS FOR STRESS CALCULATIONSBCD | CROSS SECTION DETAILS FOR STRESS CALCULATIONSBCD | WEIGHT PER UNIT LENGTH |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | CROSS SECTION LABEL | CROSS SECTION TYPE | AREA | J | IY | IZ | O.D. | WALL THK. | INNER O.D. | INNER W.T. | WEIGHT PER UNIT LENGTH |
| LINE LABEL | CROSS SECTION LABEL | CROSS SECTION TYPE | AREA | J | IY | IZ | FL. WIDTH | DEPTH | Y SHEAR AREA | Z SHEAR AREA | WEIGHT PER UNIT LENGTH |
| PLSECT |  |  |  |  |  |  |  |  |  |  |  |
| 1--6 | 8<--14 | 16<--18 | 19<--24 | 25<--32 | 33<--40 | 41<--48 | 51<--56 | 57<--62 | 63<--68 | 69<--74 | 75<--80 |
| DEFAULT |  |  |  |  |  |  |  | IN | SQ.IN | SQ.IN |  |
| ENGLISH |  |  | SQ.IN | IN**4 | IN**4 | IN**4 | IN | CM | SQ.CM | SQ.CM | KIP/FT |
| METRIC |  |  | SQ.CM | CM**4 | CM**4 | CM**4 | CM |  |  |  | TONNE/M |



LOAD CASE PLOT SELECTION LINE

COLUMNS

COMMENTARY

GENERAL THIS LINE IS USED TO SPECIFY THE LOAD CASES TO BE INCLUDEDFOR PLOTTING. IF OMITTED, ALL LOAD CASES WILL BEAUTOMATICALLY INCLUDED.

( 7-80) ENTER THE LOAD CASE NAMES FOR ALL LOAD CASES TO BE PLOTTED. THE LOAD CASES CAN BE IN ANY ORDER.



| LINE LABEL | LOAD CASE SELECTIONS FOR PLOTTING | LOAD CASE SELECTIONS FOR PLOTTING | LOAD CASE SELECTIONS FOR PLOTTING | LOAD CASE SELECTIONS FOR PLOTTING | LOAD CASE SELECTIONS FOR PLOTTING | LOAD CASE SELECTIONS FOR PLOTTING | LOAD CASE SELECTIONS FOR PLOTTING | LOAD CASE SELECTIONS FOR PLOTTING | LOAD CASE SELECTIONS FOR PLOTTING | LOAD CASE SELECTIONS FOR PLOTTING | LOAD CASE SELECTIONS FOR PLOTTING | LOAD CASE SELECTIONS FOR PLOTTING | LOAD CASE SELECTIONS FOR PLOTTING | LOAD CASE SELECTIONS FOR PLOTTING | LOAD CASE SELECTIONS FOR PLOTTING |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | 1ST | 2ND | 3RD | 4TH | 5TH | 6TH | 7TH | 8TH | 9TH | 10TH | 11TH | 12TH | 13TH | 14TH | 15TH |
| PLTLC |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 1-- 5 | 7-->10 | 12-->15 | 17-->20 | 22-->25 | 27-->30 | 32-->35 | 37-->40 | 42-->45 | 47-->50 | 52-->55 | 57-->60 | 62-->65 | 67-->70 | 72-->75 | 77-->80 |



PILE PLOT SELECTION LINE

COLUMNS

COMMENTARY

GENERAL THIS LINE IS USED TO SPECIFY THE PILES TO BE INCLUDED FOR PLOTTING. IF OMITTED, ALL PILES WILL BE AUTOMATICALLY INCLUDED.

( 7-80) ENTER THE PILEHEAD JOINT NAMES OF THE PILES TO BE PLOTTED. THE PILES CAN BE IN ANY ORDER.



| LINE LABEL | PILE SELECTIONS FOR PLOTTING | PILE SELECTIONS FOR PLOTTING | PILE SELECTIONS FOR PLOTTING | PILE SELECTIONS FOR PLOTTING | PILE SELECTIONS FOR PLOTTING | PILE SELECTIONS FOR PLOTTING | PILE SELECTIONS FOR PLOTTING | PILE SELECTIONS FOR PLOTTING | PILE SELECTIONS FOR PLOTTING | PILE SELECTIONS FOR PLOTTING | PILE SELECTIONS FOR PLOTTING | PILE SELECTIONS FOR PLOTTING | PILE SELECTIONS FOR PLOTTING | PILE SELECTIONS FOR PLOTTING | PILE SELECTIONS FOR PLOTTING |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | 1ST | 2ND | 3RD | 4TH | 5TH | 6TH | 7TH | 8TH | 9TH | 10TH | 11TH | 12TH | 13TH | 14TH | 15TH |
| PLTPL |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 1--5 | 7-->10 | 12-->15 | 17-->20 | 22-->25 | 27-->30 | 32-->35 | 37-->40 | 42-->45 | 47-->50 | 52-->55 | 57-->60 | 62-->65 | 67-->70 | 72-->75 | 77-->80 |



PLOT REQUEST LINE

COLUMNS

COMMENTARY

GENERAL

THIS LINE IS USED TO SPECIFY THE PLOTS AND PLOT OPTIONS DESIRED. IF OMITTED, NO PLOT INFORMATION WILL BE WRITTEN TO THE NEUTRAL PICTURE FILE. THE NEUTRAL PICTURE FILE CAN SUBSEQUENTLY BE PROCESSED TO OBTAIN HARDCOPY PLOTS OR TO VIEW THE PLOTS INTERACTIVELY.

( 7-74)

```txt
ENTER THE DESIRED SELECTIONS IN ANY ORDER FROM THE FOLLOWING LIST:  
'SD' - SOIL DATA (P-Y, T-Z, ADHESION, ETC.).  
'DA' - AXIAL DEFLECTIONS.  
'DL' - LATERAL DEFLECTIONS (Y AND Z SHOWN SEPARATELY).  
'DT' - LATERAL DEFLECTIONS (VECTOR SUM OF Y AND Z).  
'RL' - LATERAL ROTATIONS (Y AND Z SHOWN SEPARATELY).  
'RT' - LATERAL ROTATIONS (VECTOR SUM OF Y AND Z).  
'ML' - BENDING MOMENTS (Y AND Z SHOWN SEPARATELY).  
'MT' - BENDING MOMENTS (VECTOR SUM OF Y AND Z).  
'AL' - AXIAL LOADS.  
'SL' - SHEAR LOADS (Y AND Z SHOWN SEPARATELY).  
'ST' - SHEAR LOADS (VECTOR SUM OF Y AND Z).  
'AS' - AXIAL SOIL REACHMENTS.  
'LS' - LATERAL SOIL REACHMENTS (Y AND Z SHOWN SEPARATELY).  
'TS' - LATERAL SOIL REACHMENTS (VECTOR SUM OF Y AND Z).  
'UC' - UNITY CHECK RATIO.  
'PR' - PILE REDESIGN (PILE THICKNESS REQUIRED VERSUS DEPTH)  
'LG' - LIGHT GRID (MAJOR AXIS DIVISIONS).  
'DG' - DENSE GRID (ALL AXIS DIVISIONS).  
'XH' - CROSS Hatching. 
```

FOR THE SELECTIONS DA, DL, DT, RL, RT, ML, MT, AL, SL, ST, AS, LS, TS, AND UC, THE ENVELOPE FOR ALL LOAD CASES MAY BE REQUESTED BY APPENDING AN 'E' TO THE REQUEST, SUCH AS 'DAE' FOR THE AXIAL DEFLECTION ENVELOPE.



| LINE LABEL | PLOT SELECTIONS | PLOT SELECTIONS | PLOT SELECTIONS | PLOT SELECTIONS | PLOT SELECTIONS | PLOT SELECTIONS | PLOT SELECTIONS | PLOT SELECTIONS | PLOT SELECTIONS | PLOT SELECTIONS | PLOT SELECTIONS | PLOT SELECTIONS | PLOT SELECTIONS | PLOT SELECTIONS |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | 1ST | 2ND | 3RD | 4TH | 5TH | 6TH | 7TH | 8TH | 9TH | 10TH | 11TH | 12TH | 13TH | 14TH |
| PLTRQ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 1-- 5 | 7<-- 9 | 12<--14 | 17<--19 | 22<--24 | 27<--29 | 32<--34 | 37<--39 | 42<--44 | 47<--49 | 52<--54 | 57<--59 | 62<--64 | 67<--69 | 72<--74 |



PLOT SIZE SELECTION LINE

COLUMNS

COMMENTARY

GENERAL THIS LINE IS USED TO SPECIFY THE SIZE PARAMETERS FOR PLOTTING. IF OMITTED, THE DEFAULT VALUES WILL BE USED.

( 6-11) ENTER THE SIZE OF THE OVERALL PLOT IN THE X-DIRECTION.   
(12-17) ENTER THE SIZE OF THE OVERALL PLOT IN THE Y-DIRECTION.   
(18-23) ENTER THE SIZE OF THE CHARACTERS USED.   
(24-29) ENTER THE SPACING BETWEEN LINES USED FOR CROSS HATCHING. CROSS HATCHING IS USED FOR AREA FILLING.   
(30-32) IF YOU HAVE A MULTI-PEN PLOTTER, THE DIFFERENT VARIABLES PLOTTED ON THE SAME GRAPH CAN BE SHOWN IN DIFFERENT COLORS. ENTER THE NUMBER OF DIFFERENT PENS TO BE USED FOR YOUR SPECIFIC PLOTTER.



| LINE LABEL | X SIZE | Y SIZE | CHAR. SIZE | CROSS HATCH SPACING | NUMBER OF PENS |
| --- | --- | --- | --- | --- | --- |
| PLTSZ |  |  |  |  |  |
| 1--5 | 6<--11 | 12<--17 | 18<--23 | 24<--29 | 30--->32 |
| DEFAULT | 8.5 ENGL | 11.0 ENGL | 0.10 ENGL | 0.1 ENGL | 1 |
| ENGLISH | IN | IN | IN | IN |  |
| METRIC | CM | CM | CM | CM |  |



PSI OPTIONS LINE

COLUMNS

COMMENTARY

GENERAL

THIS LINE IS REQUIRED IN ANY PSI RUN. IT IS USED TO SPECIFY THE OVERALL ANALYSIS PARAMETERS, THE TYPE OF ANALYSIS, AND THE OUTPUT REPORTS DESIRED.

( 8- 9)

ENTER THE COORDINATE USED IN THE SACS IV ANALYSIS TO INDICATE THE UPWARD VERTICAL DIRECTION. OPTIONS ARE + OR - X, Y, OR Z.

(10-12)

NTER THE INPUT UNITS. OPTIONS ARE:

'ENG' - ENGLISH UNITS.

'MN ' - METRIC UNITS WITH KILONEWTONS AS THE FORCE UNIT.

'MET' - METRIC UNITS WITH KILOGRAMS AS THE FORCE UNIT.

(15-15)

ENTER 'N' IF EQUILIBRIUM RELAXATION IS NOT TO BE USED.

'Y' CAN IMPROVE THE CHANCES OF CONVERGENCE.

(17-18)

ENTER 'CE' IF THE PROGRAM IS TO CONTINUE TO PROCESS ALL LOAD CASES REGARDLESS OF ERRORS ENCOUNTERED DURING THE ITERATION PROCEDURE.

(19-20)

ENTER 'SK' IF THE PILE/STRUCTURE COUPLED INTERACTION ANALYSIS IS TO BE SKIPPED.

(21-22)

ENTER 'NA' IF FINE TUNING IS NOT TO BE PERFORMED.

(23-24)

NTER THE FINAL PILE ANALYSIS OPTION:

'SK' - SKIP FINAL PILE ANALYSIS.

'EX' - EXECUTE FINAL PILE ANALYSIS AND REPORT RESULTS IN WO PLANES.

'CB' - EXECUTE FINAL PILE ANALYSIS AND REPORT RESULTS AS THE VECTOR RESULTANT AT EACH PILE STATION.

'C1' - SAME AS 'CB' EXCEPT ONLY EVERY OTHER LINE IN THE OUTPUT IS PRINTED.

'C2' - SAME AS 'C1' EXCEPT ONLY EVERY THIRD LINE IS PRINTED.

'SM' - EXECUTE FINAL PILE ANALYSIS WITH SUMMARY PRINT ONLY.

COLUMNS

COMMENTARY

(25-43) ENTER THE DISPLACEMENT AND ROTATION CONVERGENCE TOLERANCES AND THE MAXIMUM NUMBER OF ITERATIONS PERMITTED. ITERATION CONTINUES UNTIL EVERY PILEHEAD DEGREE OF FREEDOM HAS CONVERGED TO WITHIN THESE TOLERANCES OR UNTIL THE MAXIMUM ALLOWED NUMBER OF ITERATIONS HAS BEEN EXCEEDED.

(44-45) ENTER 'PT' IF THE PILEHEAD STIFFNESS TABLES ARE TO BE PRINTED.   
(46-47) ENTER 'PT' IF THE REDUCED STRUCTURAL STIFFNESS IS TO BE PRINTED.   
(48-49) ENTER 'PT' IF THE REDUCED STRUCTURAL FORCES ARE TO BE PRINTED.   
(50-51) ENTER 'PT' IF INTERMEDIATE ITERATION RESULTS ARE TO BE PRINTED.   
(52-53) ENTER 'PT' IF THE INPUT DATA TO PSI IS TO BE PRINTED.

(54-55) PILE FILE OUTPUT OPTION: 'PF' - IF THE AUXILIARY PILE DETAIL FILE IS TO BE CREATED. 'PP' - IF A PILE POSTFILE IS TO BE CREATED FOR FATIGUE.   
(56-58) ENTER 'FTG' IF THE SCF OPTION FOR PILE IS SELECTED IN FATIGUE ANALYSIS. NOTE: THE PILE FATIGUE SCF FACTOR CAN BE PRE-SELECTED BY ENTERING 'AWS' FOR AMERICAN WELDING SOCIETY, 'DNV' FOR DET NORSKE VERITAS, 'DE ' FOR DEPARTMENT OF ENERGY OR 'BS ' FOR BRITISH STANDARDS SCF'S.   
(59-60) ENTER 'S2' TO USE API-RP2A WSD 21ST Supplement 2. THE DEFAULT VERSION IS Supplement 3.   
(61-61) ENTER 'F' IF THE PILE DISPLACEMENT RATIO THAT IS USED FOR THE DETERMINATION OF SKIN FRICTION IN CPT-BASED SOILS SHOULD MAKE USE OF THE U.W.A. FINAL FILLING RATIO (FFR).   
(62-64) ENTER THE NUMBER OF INCREMENTAL PILE LENGTHS FOR THE FINITE DIFFERENCE SOLUTION.   
(67-72) ENTER THE FORCE CONVERGENCE TOLERANCE IN PERCENT. THIS IS THE ALLOWABLE FORCE DIFFERENCE BETWEEN THE PILEHEAD AND THE STRUCTURE.   
(73-80) ENTER THE WEIGHT DENSITY OF THE PILE MATERIAL IF THE PILE SELF-WEIGHT IS TO BE INCLUDED IN THE ANALYSIS.



| LINE LABEL | UPWARD VERTICAL | UNITS OPTION | RELAX EQUILI-BRIUM | CONTINUE WITH ERRORS OPTION | ANALYSIS OPTIONS | ANALYSIS OPTIONS | ANALYSIS OPTIONS | CONVERGENCE CRITERIA | CONVERGENCE CRITERIA | CONVERGENCE CRITERIA | OUTPUT OPTIONS | OUTPUT OPTIONS | OUTPUT OPTIONS | OUTPUT OPTIONS | OUTPUT OPTIONS | OUTPUT OPTIONS | OUTPUT OPTIONS | OUTPUT OPTIONS | API 21ST SPT.2 OPT. | UWA FFR OPT. | NUMBER OF PILE INCRE-MENTS | FORCE CONV. TOL. | MATERIAL WEIGHT DENSITY |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | UPWARD VERTICAL | UNITS OPTION | RELAX EQUILI-BRIUM | CONTINUE WITH ERRORS OPTION | SKIP INTER-ACTION ANALYSIS | NO FINE TUNE | FINAL TILE ANALYSIS | DISPLACE-MENT | ROTA-TION | MAX. ITERATIONS | PILE STIFF. TABLES | REDUCED STRUCT. STIFFNESS | REDUCED FORCE VECTOR | INTER-MEDIATE RESULTS | INPUT ECHO | PILE FILE OPT. | PILE SCF OPT. |  | API 21ST SPT.2 OPT. | UWA FFR OPT. | NUMBER OF PILE INCRE-MENTS | FORCE CONV. TOL. |  |
| PSIOPT |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 1--6 | 8--9 | 10<--12 | 15 | 17--18 | 19--20 | 21--22 | 23--24 | 25<--32 | 33<--40 | 41-->43 | 44--45 | 46--47 | 48--49 | 50--51 | 52--53 | 54--55 | 56--58 | 59--60 | 61 | 62-->64 | 67<--72 | 73<--80 |  |
| DEFAULT | ' +Z' | 'ENG' | 'Y' |  |  |  |  | 0.001 ENGL | 0.0001 | 20 |  |  |  |  |  |  |  |  |  | 100 | 0.5 | 0 |  |
| ENGLISH |  |  |  |  |  |  |  | IN | RAD |  |  |  |  |  |  |  |  |  |  |  | % | LB/CU.FT |  |
| METRIC |  |  |  |  |  |  |  | CM | RAD |  |  |  |  |  |  |  |  |  |  |  | % | TONNE/CU.M |  |



SCOUR

COLUMNS

COMMENTARY

GENERAL

THIS LINE SPECIFIES THE OVERALL SEABED EROSION DEPTH THAT IS TO BE ACCOUNTED FOR WHEN HAVING PSI OR PILE3D AUTOMATICALLY GENERATE LOAD TRANSFER CURVES USING METHODS PRESENTED IN API-RP2A WSD 21ST EDITION SUPPLEMENT 3. NOTE THAT SOILS WITH USER-GENERATED T-Z AND P-Y INPUT ARE UNAFFECTED BY THIS LINE. SPECIFICATION OF A SCOUR DEPTH WILL ENSURE THAT A SCOUR REDUCTION FACTOR IS APPLIED TO THE CONE TIP RESISTANCE FOR STRATA WHOSE AXIAL RESISTANCE IS TO BE DETERMINED FROM CPT DATA. FURTHERMORE, FOR STRATA WHOSE LATERAL RESISTANCE IS CALCULATED IN ACCORDANCE WITH RP2A RECOMMENDATIONS, THE VERTICAL EFFECTIVE STRESS AND SUBGRADE MODULUS REACTION VALUES ARE LOWERED IN ACCORDANCE WIH THE SUGGESTIONS OF THE COMMENTARY ON SOIL REACTION FOR LATERALLY LOADED PILES (C6.8).

(7- 7)

SPECIFY THE CALCULATION METHOD FOR THE SCOUR REDUCTION FACTOR.LEAVE BLANK TO USE THE RATIO OF VERTICAL EFFECTIVE STRESS THATHAS BEEN PROPOSED BY NNI.'F' => USE THE FUGRO FORMULA FOR HIGH GENERAL SCOUR DEPTHS(SEE API-RP2A WSD 21ST EDITION SUPPLEMENT 3, C6.4.3e)

(9-14)

ENTER THE "GENERAL SCOUR DEPTH" OR "OVERALL SEABED EROSION DEPTH"



| LINE LABEL | SCOUR REDUCTION METHOD | GENERAL SCOUR DEPTH | LEAVE BLANK |
| --- | --- | --- | --- |
| SCOUR |  |  |  |
| 1--5 | 7 | 9<-14 | 15--------80 |
| DEFAULT | NNI | 0 |  |
| ENGLISH |  | FT |  |
| METRIC |  | M |  |



SOIL (CLAY) API LATERAL STRATUM LINE

COLUMNS

COMMENTARY

GENERAL THIS LINE SET IS USED TO SPECIFY THE SOIL PROPERTIES FOR EACHCLAY STRATUM. THE PROGRAM WILL USE THESE PROPERTIES TOCALCULATE P-Y DATA FOR THE SOIL ACCORDING TO APIRECOMMENDATIONS.

( 1- 4) ENTER 'SOIL'.   
( 6-12) ENTER 'API LAT'.   
(14-17) ENTER 'SLOC'.   
(19-22) ENTER THE SOIL TYPE 'CLAY'.   
( 23 ) ENTER 'C' IF THE P-Y CURVE GENERATED IS FOR CYCLIC LOAD CONDITIONS, OR 'S' IF FOR STATIC LOAD CONDITIONS.   
(25-36) ENTER THE DISTANCES FROM THE PILEHEAD TO THE TOP AND BOTTOM OF THIS SOIL STRATUM. THESE DISTANCES ARE VERTICALLY DOWN AND NOT ALONG THE AXIS OF THE PILE, WHICH MAY BE BATTERED.

COLUMNS

COMMENTARY

(37-40) ENTER THE "P" FACTOR FOR THIS P-Y CURVE. THIS FACTOR IS USED TO MODIFY THE GENERATED "P" VALUES FOR THIS SOIL STRATUM.   
(41-44) ENTER THE AMOUNT TO BE ADDED TO THE GENERATED "Y" VALUES. THIS IN EFFECT SHIFTS THE P-Y CURVE ALONG THE Y-AXIS. THIS SHIFT CAN BE USED WITH BOTH SYMMETRICAL AND NONSYMMETRICAL P-Y CURVES AND IS USEFUL FOR MODELING MUDSLIDES.   
(45-50) ENTER THE UNDRAINED SHEAR STRENGTH.   
(51-56) ENTER THE EFFECTIVE UNIT WEIGHT OF THE SOIL.   
(57-62) ENTER THE API RP2A EMPIRICAL PARAMETER "J".   
(63-68) ENTER THE API RP2A REFERENCE STRAIN.   
(70-76) ENTER A HIGH PRECISION "P" FACTOR FOR THIS P-Y CURVE. THIS FACTOR MAY BE USED TO SCALE THE "P" VALUES FOR THIS STRATUM. IF A "P" FACTOR HAS BEEN SPECIFIED IN COLUMNS 37-40 , THE HIGH PRECISION "P" FACTOR BECOMES A MULTIPLIER FOR THE ORIGINAL "P" FACTOR.



| LINE LABEL | AUTOMATIC LATERAL RESISTANCE GENERATION | LINE TYPE | SOIL TYPE | STATIC OR CYCLIC | TOP OF STRATUM | BOTTOM OF STRATUM | P FACTOR | Y SHIFT | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | HIGH PRECISION P FACTOR |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | AUTOMATIC LATERAL RESISTANCE GENERATION | LINE TYPE | SOIL TYPE | STATIC OR CYCLIC | TOP OF STRATUM | BOTTOM OF STRATUM | P FACTOR | Y SHIFT | UNDRAINED SHEAR STRENGTH | EFFECTIVE UNIT WEIGHT OF SOIL | API RP2A EMPIRICAL PARAMETER "J" | API RP2A REFERENCE STRAIN | HIGH PRECISION P FACTOR |
| SOIL | API LAT | SLOC |  |  |  |  |  |  |  |  |  |  |  |
| 1--4 | 6--12 | 14--17 | 19--22 | 23 | 25<--30 | 31<--36 | 37<--40 | 41<--44 | 45<--50 | 51<--56 | 57<--62 | 63<--68 | 70--76 |
| DEFAULT |  |  |  | 'S' |  |  | 1 | 0 |  |  | 0.5 |  | 1 |
| ENGLISH |  |  |  |  | FT | FT |  | IN | KIP/SQ.FT | LB/CU.FT |  |  |  |
| METRIC (KN) |  |  |  |  | M | M |  | CM | KN/SQ.CM | TONNE/CU.M |  |  |  |
| METRIC (KG) |  |  |  |  | M | M |  | CM | KG/SQ.CM | TONNE/CU.M |  |  |  |



SOIL (SAND) API LATERAL STRATUM LINE

COLUMNS

COMMENTARY

GENERAL THIS LINE SET IS USED TO SPECIFY THE SOIL PROPERTIES FOR EACHSAND STRATUM. THE PROGRAM WILL USE THESE PROPERTIES TOCALCULATE P-Y DATA FOR THE SOIL ACCORDING TO APIRECOMMENDATIONS.

( 1- 4) ENTER 'SOIL'.   
( 6-12) ENTER 'API LAT'.   
(14-17) ENTER 'SLOC'.   
(19-22) ENTER THE SOIL TYPE. THE PROGRAM WILL USE THE LISTED VALUES FOR THE ANGLE OF INTERNAL FRICTION UNLESS OVERRIDDEN IN COLUMNS 63-68.



| INPUT | SOIL CLASS | FRCTION ANGLE |
| --- | --- | --- |
| 'GRAV' | GRAVEL | 40.0 |
| 'SAND' | CLEAN SAND | 35.0 |
| 'SILSN' | SILTY SAND | 30.0 |
| 'SNSL' | SANDY SILT | 25.0 |
| 'SILT' | SILT | 20.0 |



( 23 ) ENTER 'C' IF THE P-Y CURVE GENERATED IS FOR CYCLIC LOAD CONDITIONS, OR 'S' IF FOR STATIC LOAD CONDITIONS.   
( 24 ) ENTER SOIL LOCATION RELATIVE TO THE WATER TABLE. 'A' - ABOVE WATER TABLE 'B' - BELOW WATER TABLE   
(25-36) ENTER THE DISTANCES FROM THE PILEHEAD TO THE TOP AND BOTTOM OF THIS SOIL STRATUM. THESE DISTANCES ARE VERTICALLY DOWN AND NOT ALONG THE AXIS OF THE PILE, WHICH MAY BE BATTERED.

COLUMNS

COMMENTARY

(37-40) ENTER THE "P" FACTOR FOR THIS P-Y CURVE. THIS FACTOR IS USED TO MODIFY THE GENERATED "P" VALUES FOR THIS SOIL STRATUM.   
(41-44) ENTER THE AMOUNT TO BE ADDED TO THE GENERATED "Y" VALUES. THIS IN EFFECT SHIFTS THE P-Y CURVE ALONG THE Y-AXIS. THIS SHIFT CAN BE USED WITH BOTH SYMMETRICAL AND NONSYMMETRICAL P-Y CURVES AND IS USEFUL FOR MODELING MUDSLIDES.   
(51-56) ENTER THE EFFECTIVE UNIT WEIGHT OF THE SOIL.   
(57-62) ENTER THE INITIAL MODULUS OF SUBGRADE REACTION. IF LEFT BLANK, THE PROGRAM WILL CALCULATE A VALUE BASED ON FIGURE 6.8.7-1 OF API RP2A 20TH EDITION.   
(63-68) ENTER THE FRICTION ANGLE IF YOU WISH TO OVERRIDE THE RP2A DEFAULT VALUES LISTED IN THE TABLE IN THE ADJACENT COLUMN OF THIS COMMENTARY.   
(70-76) ENTER A HIGH PRECISION "P" FACTOR FOR THIS P-Y CURVE. THIS FACTOR MAY BE USED TO SCALE THE "P" VALUES FOR THIS STRATUM. IF A "P" FACTOR HAS BEEN SPECIFIED IN COLUMNS 37-40 , THE HIGH PRECISION "P" FACTOR BECOMES A MULTIPLIER FOR THE ORIGINAL "P" FACTOR.



| LINE LABEL | AUTOMATIC LATERAL RESISTANCE GENERATION | LINE TYPE | SOIL TYPE | STATIC OR CYCLIC | SAND STRATUM LOCATION | TOP OF STRATUM | BOTTOM OF STRATUM | P FACTOR | Y SHIFT | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | HIGH PRECISION P FACTOR |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | AUTOMATIC LATERAL RESISTANCE GENERATION | LINE TYPE | SOIL TYPE | STATIC OR CYCLIC | SAND STRATUM LOCATION | TOP OF STRATUM | BOTTOM OF STRATUM | P FACTOR | Y SHIFT | EFF. UNIT WT OF SOIL | INIT. MOD SUBGRADE REACT. | INTERNAL FRICTION ANGLE | HIGH PRECISION P FACTOR |
| SOIL | API LAT | SLOC |  |  |  |  |  |  |  |  |  |  |  |
| 1--4 | 6--12 | 14--17 | 19--22 | 23 | 24 | 25<--30 | 31<--36 | 37<--40 | 41<--44 | 51<--56 | 57<--62 | 63<--68 | 70--76 |
| DEFAULT |  |  |  | 'S' | 'A' |  |  | 1 | 0 |  |  |  | 1 |
| ENGLISH |  |  |  |  |  | FT | FT |  | IN | LB/CU.FT | LB/CU.IN | DEG |  |
| METRIC (KN) |  |  |  |  |  | M | M |  | CM | TONNE/CU.M | KN/CU.CM | DEG |  |
| METRIC (KG) |  |  |  |  |  | M | M |  | CM | TONNE/CU.M | KG/CU.CM | DEG |  |



SOIL API LATERAL HEADER LINE

COLUMNS

COMMENTARY

GENERAL

THIS LINE FOLLOWED BY THE 'API 10TH EDITION LATERAL STRATUM'LINE SET IS USED TO ENTER THE SOIL PROPERTIES REQUIRED FORTHE PROGRAM TO GENERATE P-Y CURVES ACCORDING TORECOMMENDATIONS IN RP2A. THESE LINE SETS ARE USED IN PLACE OFLINES 'SOIL LATERAL HEAD', 'SOIL SLOC' AND 'SOIL P-Y'.

P-Y CURVES ARE GENERATED FOR A PILE OF SPECIFIED DIAMETER(COLUMNS 28-33). WORKING P-Y CURVES FOR PILES OF DIFFERENTDIAMETER ARE GENERATED BY ONE OF TWO TECHNIQUES AT THE USER'SOPTION:

1. IF 'YEXP' IS ENTERED IN COLUMNS 24-27 THEN BOTH THE

INPUT P AND Y DATA ARE SCALED BY THE RATIO OF PILE

DIAMETER TO THE REFERENCE DIAMETER.

2. IF COLUMNS 24-27 ARE BLANK THEN ONLY THE P VALUES ARE SCALED.

( 1- 4) ENTER 'SOIL'.   
( 6-12) ENTER 'LATERAL'.   
(14-17) ENTER 'HEAD'.   
(18-20) ENTER THE NUMBER OF SOIL STRATA FOR THIS P-Y DESCRIPTION. DO NOT LEAVE THIS FIELD BLANK.

COLUMNS

COMMENTARY

(24-27) ENTER 'YEXP' TO CAUSE BOTH THE INPUT P AND Y VALUES TO BE MULTIPLIED BY THE RATIO OF THE PILE DIAMETER TO THE REFERENCE DIAMETER TO PRODUCE THE WORKING P-Y CURVE FOR THE PILE. IF LEFT BLANK ONLY THE P VALUES WILL BE MULTIPLIED BY THE DIAMETER RATIO.   
(28-33) ENTER THE DIAMETER FOR WHICH THIS P-Y DATA IS GENERATED. THE INPUT P VALUES WILL BE MULTIPLIED BY THE RATIO OF THE PILE DIAMETER TO THIS REFERENCE DIAMETER. IN ADDITION IF 'YEXP' IS ENTERED IN COLUMNS 24-27 THEN THE Y VALUES WILL ALSO BE MULTIPLIED BY THIS RATIO.   
(41-44) ENTER THE UNIQUE ALPHANUMERIC SOIL TABLE IDENTIFIER. THIS IDENTIFIER IS USED ON ONE OR MORE 'PILE' LINES TO ASSOCIATE THIS SOIL TABLE WITH THOSE PILES.   
(45-60) ENTER ANY DESCRIPTIVE REMARKS DESIRED.



| LINE LABEL | LATERAL LABEL | HEAD LABEL | NUMBER OF SOIL STRATA | P-Y CURVE SCALING | REFERENCE DIAMETER | SOIL TABLE ID | SOIL DESCRIPTION OR OTHER REMARKS | LEAVE BLANK |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOIL | LATERAL | HEAD |  |  |  |  |  |  |
| 1--4 | 6--12 | 14--17 | 18-->20 | 24--27 | 28<--33 | 41<--44 | 45----60 | 61--80 |
| DEFAULT |  |  |  |  |  |  |  |  |
| ENGLISH |  |  |  |  | IN |  |  |  |
| METRIC |  |  |  |  | CM |  |  |  |



API 10TH EDITION LATERAL STRATUM

COLUMNS

COMMENTARY

GENERAL THIS LINE SET IS USED TO SPECIFY THE SOIL PROPERTIES FOR EACHSTRATUM. THE PROGRAM WILL USE THESE PROPERTIES TO CALCULATEP-Y DATA FOR THE SOIL ACCORDING TO API RECOMMENDATIONS.

( 1- 4) ENTER 'SOIL'.   
( 6-12) ENTER 'API LAT'.   
( 13 ) ENTER '1'.   
(14-17) ENTER 'SLOC'.   
(19-22) ENTER THE SOIL TYPE. FOR ALL EXCEPT CLAY THE PROGRAM WILL USE THE LISTED VALUES FOR THE ANGLE OF INTERNAL FRICTION.

INPUT SOIL CLASS FRICTIONANGLE

'CLAY' CLAY NOT APPLICABLE   
'SAND' CLEAN SAND 35.0   
'SLSN' SILTY SAND 30.0   
'SNSL' SANDY SILT 25.0   
'SILT' SILT 20.0

( 23 ) IF THE SOIL TYPE IS CLAY LEAVE THIS FIELD BLANK. OTHERWISE, ENTER 'C' IF THE P-Y CURVE GENERATED IS FOR CYCLIC LOAD CONDITIONS, OR 'S' IF FOR STATIC LOAD CONDITIONS.   
( 24 ) ENTER 'A' OR LEAVE BLANK FOR SAND ABOVE THE WATER TABLE. ENTER 'B' FOR SAND BELOW THE WATER TABLE.   
(25-36) ENTER THE DISTANCES FROM THE PILEHEAD TO THE TOP AND BOTTOM OF THIS SOIL STRATUM. THESE DISTANCES ARE VERTICALLY DOWN AND NOT ALONG THE AXIS OF THE PILE, WHICH MAY BE BATTERED.

COLUMNS

COMMENTARY

(37-40) ENTER THE P FACTOR FOR THIS P-Y CURVE. THIS FACTOR IS USED TO MODIFY THE GENERATED P VALUES FOR THIS SOIL STRATUM.   
(41-44) ENTER THE AMOUNT TO BE ADDED TO THE GENERATED Y VALUES. THIS IN EFFECT SHIFTS THE P-Y CURVE ALONG THE Y-AXIS. THIS SHIFT CAN BE USED WITH BOTH SYMMETRICAL AND NONSYMMETRICAL P-Y CURVES AND IS USEFUL FOR MODELING MUDSLIDES.   
(45-50) IF THE SOIL TYPE IS CLAY, ENTER THE UNDRAINED SHEAR STRENGTH. OTHERWISE, LEAVE THIS FIELD BLANK.   
(51-56) ENTER THE EFFECTIVE UNIT WEIGHT OF THE SOIL.   
(57-62) IF THE SOIL TYPE IS CLAY ENTER THE RP2A EMPIRICAL PARAMETER, "J". APPROPRIATE VALUES ARE FROM 0.25 TO 0.50, WITH 0.50 THE USUAL VALUE FOR GULF OF MEXICO CLAYS. FOR ALL OTHER SOIL TYPES ENTER THE INITIAL SLOPE, K1. VALUES SUGGESTED BY RP2A ARE:

LOOSE SOILS 20.0 (LB/SQ.IN)/IN MEDIUM SOILS 60.0 (LB/SQ.IN)/IN DENSE SOILS 125.0 (LB/SQ.IN)/IN

(63-68) IF THE SOIL TYPE IS CLAY, ENTER THE RP2A REFERENCE STRAIN. THIS IS DEFINED IN RP2A AS THE "STRAIN WHICH OCCURS AT ONE-HALF THE MAXIMUM STRESS ON LABORATORY UNDRAINED COMPRESSION TESTS OF UNDISTURBED SOIL SAMPLES."

FOR ALL OTHER SOIL TYPES ENTER THE FRICTION ANGLE IF YOU WISH TO OVERRIDE THE RP2A DEFAULT VALUES LISTED IN THE TABLE IN THE ADJACENT COLUMN OF THIS COMMENTARY.



| LINE LABEL | AUTOMATIC LATERAL RESISTANCE GENERATION | API 10TH EDITION FLAG | LINE TYPE | SOIL TYPE | STATIC OR CYCLIC | WATER TABLE LEVEL | TOP OF STRatum | BOTTOM OF STRatum | P FACTOR | Y SHIFT | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS | SOIL CHARACTERISTICS |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | AUTOMATIC LATERAL RESISTANCE GENERATION | API 10TH EDITION FLAG | LINE TYPE | SOIL TYPE | STATIC OR CYCLIC | WATER TABLE LEVEL | TOP OF STRatum | BOTTOM OF STRatum | P FACTOR | Y SHIFT | UNDRAINED SHEAR STRENGTH (FOR CLAY) | EFFECTIVE UNIT WEIGHT OF SOIL | SOIL PARAMETER (SEE ABOVE) | SOIL PARAMETER (SEE ABOVE) |
| SOIL | API LAT | 1 | SLOC |  |  |  |  |  |  |  |  |  |  |  |
| 1--4 | 6--12 | 13 | 14--17 | 19--22 | 23 | 24 | 25<--30 | 31<--36 | 37<--40 | 41<--44 | 45<--50 | 51<--56 | 57<--62 | 63<--68 |
| DEFAULT |  |  |  |  | 'S' |  |  |  | 1 | 0 |  |  |  |  |
| ENGLISH |  |  |  |  |  |  | FT | FT |  | IN | KIP/SQ.FT | LB/CU.FT | NONE, LB/CU.IN | NONE, DEG |
| METRIC (KN) |  |  |  |  |  |  | M | M |  | CM | KN/SQ.CM | TONNE/CU.M | NONE, KN/CU.CM | NONE, DEG |
| METRIC (KG) |  |  |  |  |  |  | M | M |  | CM | KG/SQ.CM | TONNE/CU.M | NONE, KG/CU.CM | NONE, DEG |



SOIL LATERAL HEADER LINE

COLUMNS

COMMENTARY

GENERAL

THIS LINE AND THE SOIL LOCATION AND P-Y LINES ARE USED TO MODEL RESILIENT BEHAVIOR OF THE SOIL SUBJECT TO PRESSURE EXERTED BY THE LATERAL SURFACE OF THE PILE.

LATERAL PRESSURE DATA IS INPUT AS FORCE PER UNIT LENGTH ALONG A PILE OF SPECIFIED REFERENCE DIAMETER (COLUMNS 28-33). WORKING "P-Y" CURVES FOR PILES OF DIFFERENT DIAMETER ARE PRODUCED BY ONE OF TWO TECHNIQUES AT THE USER'S OPTION:

1. IF 'YEXP' IS ENTERED IN COLUMNS 24-27 THEN BOTH THE INPUT "P" AND "Y" DATA ARE SCALED BY THE RATIO OF PILE DIAMETER TO THE REFERENCE DIAMETER.   
2. IF COLUMNS 24-27 ARE BLANK THEN ONLY THE "P" VALUES ARE SCALED.

THIS LINE IS USED TO SPECIFY PARAMETERS DEFINING THE SOILLATERAL STIFFNESS. THE ORDER OF LINES FOR P-Y DATA INPUT IS:

1. THIS LATERAL HEADER LINE.   
2. A LATERAL STRATUM LINE ('SOIL SLOC' LINE SET) FOR THE FIRST STRATUM.   
3. ONE OR MORE LATERAL P-Y LINES ('SOIL P-Y' LINE SET) AS NEEDED FOR THE FIRST STRATUM.   
4. A LATERAL STRATUM LINE FOR THE SECOND STRATUM.   
5. LATERAL P-Y LINES FOR THE SECOND STRATUM.

ETC.

( 1- 4) ENTER 'SOIL'.   
( 6-12) ENTER 'LATERAL'.   
(14-17) ENTER 'HEAD'.

COLUMNS

COMMENTARY

(18-20) ENTER THE NUMBER OF SOIL STRATA FOR THIS P-Y DESCRIPTION. DO NOT LEAVE THIS FIELD BLANK.   
(22-23) IF ANY P-Y CURVE ENTERED ('SOIL T-Z' LINE SET) IS DEFINED AT MORE THAN 30 POINTS, ENTER THAT NUMBER HERE. OTHERWISE, LEAVE BLANK.   
(24-27) ENTER 'YEXP' TO CAUSE BOTH THE INPUT "P" AND "Y" VALUES TO BE MULTIPLIED BY THE RATIO OF THE PILE DIAMETER TO THE REFERENCE DIAMETER TO PRODUCE THE WORKING "P-Y" CURVE FOR THE PILE. IF LEFT BLANK, ONLY THE "P" VALUES WILL BE MULTIPLIED BY THE DIAMETER RATIO.   
(28-33) ENTER THE DIAMETER FOR WHICH THIS P-Y DATA IS GENERATED. THE INPUT "P" VALUES WILL BE MULTIPLIED BY THE RATIO OF THE PILE DIAMETER TO THIS REFERENCE DIAMETER. IN ADDITION, IF 'YEXP' IS ENTERED IN COLUMNS 24-27, THEN THE "Y" VALUES WILL ALSO BE MULTIPLIED BY THIS RATIO.   
(34-40) ENTER THE FACTOR FOR THE "Y" VALUES. THIS FACTOR WILL BE USED TO MULTIPLY THE INPUT "Y" VALUES.   
(41-44) ENTER THE SOIL TABLE IDENTIFYING LABEL. THIS IDENTIFIER IS USED ON ONE OR MORE 'PILE' LINES TO ASSOCIATE THIS SOIL TABLE WITH THOSE PILES.   
(45-60) ENTER ANY DESCRIPTIVE REMARKS DESIRED.



| LINE LABEL | LATERAL LABEL | HEAD LABEL | NUMBER OF SOIL STRATA | MORE THAN 30 DATA POINTS FOR P-Y CURVE | P-Y CURVE SCALING | REFERENCE DIAMETER | Y FACTOR | SOIL TABLE ID | SOIL DESCRIPTION OR OTHER REMARKS | LEAVE BLANK |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOIL | LATERAL | HEAD |  |  |  |  |  |  |  |  |
| 1-- 4 | 6--12 | 14--17 | 18-->20 | 22-->23 | 24--27 | 28<-->33 | 34<-->40 | 41<-->44 | 45-->60 | 61-->80 |
| DEFAULT |  |  |  |  |  |  | 1 |  |  |  |
| ENGLISH |  |  |  |  |  | IN |  |  |  |  |
| METRIC |  |  |  |  |  | CM |  |  |  |  |



SOIL LATERAL HEADER LINE

COLUMNS

COMMENTARY

GENERAL

THIS LINE AND THE SOIL LOCATION AND P-Y LINES ARE USED TO MODEL RESILIENT BEHAVIOR OF THE SOIL SUBJECT TO PRESSURE EXERTED BY THE LATERAL SURFACE OF THE PILE.

LATERAL PRESSURE DATA IS INPUT AS FORCE PER UNIT LENGTH ALONG A PILE OF SPECIFIED REFERENCE DIAMETER (COLUMNS 28-33). WORKING "P-Y" CURVES FOR PILES OF DIFFERENT DIAMETER ARE PRODUCED BY ONE OF TWO TECHNIQUES AT THE USER'S OPTION:

1. IF 'YEXP' IS ENTERED IN COLUMNS 24-27 THEN BOTH THE INPUT "P" AND "Y" DATA ARE SCALED BY THE RATIO OF PI METER TO THE REFERENCE DIAMETER.   
2. IF COLUMNS 24-27 ARE BLANK THEN ONLY THE "P" VALUES ARE SCALED.

THIS LINE IS USED TO SPECIFY PARAMETERS DEFINING THE SOILLATERAL STIFFNESS. THE ORDER OF LINES FOR P-Y DATA INPUT IS:

1. THIS LATERAL HEADER LINE.   
2. A LATERAL STRATUM LINE ('SOIL SLOC' LINE SET) FOR THE FIRST STRATUM.   
3. ONE OR MORE LATERAL P-Y LINES ('SOIL P-Y' LINE SET) AS NEEDED FOR THE FIRST STRATUM.

4. A LATERAL STRATUM LINE FOR THE SECOND STRATUM.   
5. LATERAL P-Y LINES FOR THE SECOND STRATUM.ETC.

( 1- 4) ENTER 'SOIL'.   
( 6-12) ENTER 'LATERAL'.   
(14-17) ENTER 'HEAD'.

COLUMNS

COMMENTARY

(18-20) ENTER THE NUMBER OF SOIL STRATA FOR THIS P-Y DESCRIPTION. DO NOT LEAVE THIS FIELD BLANK.   
(22-23) IF ANY P-Y CURVE ENTERED ('SOIL T-Z' LINE SET) IS DEFINED AT MORE THAN 30 POINTS, ENTER THAT NUMBER HERE. OTHERWISE, LEAVE BLANK.   
(24-27) ENTER 'YEXP' TO CAUSE BOTH THE INPUT "P" AND "Y" VALUES TO BE MULTIPLIED BY THE RATIO OF THE PILE DIAMETER TO THE REFERENCE DIAMETER TO PRODUCE THE WORKING "P-Y" CURVE FOR THE PILE. IF LEFT BLANK, ONLY THE "P" VALUES WILL BE MULTIPLIED BY THE DIAMETER RATIO.   
(28-33) ENTER THE DIAMETER FOR WHICH THIS P-Y DATA IS GENERATED. THE INPUT "P" VALUES WILL BE MULTIPLIED BY THE RATIO OF THE PILE DIAMETER TO THIS REFERENCE DIAMETER. IN ADDITION, IF 'YEXP' IS ENTERED IN COLUMNS 24-27, THEN THE "Y" VALUES WILL ALSO BE MULTIPLIED BY THIS RATIO.   
(34-40) ENTER THE FACTOR FOR THE "Y" VALUES. THIS FACTOR WILL BE USED TO MULTIPLY THE INPUT "Y" VALUES.   
(41-44) ENTER THE SOIL TABLE IDENTIFYING LABEL. THIS IDENTIFIER IS USED ON ONE OR MORE 'PILE' LINES TO ASSOCIATE THIS SOIL TABLE WITH THOSE PILES.   
(45-60) ENTER ANY DESCRIPTIVE REMARKS DESIRED.   
( 61 ) CONSIDER BASE MOMENT IN ANALYSIS   
(63-64) NUMBER OF PARTS TO CALCULATE BASE MOMENT



| LINE LABEL | LATERAL LABEL | HEAD LABEL | NUMBER OF SOIL STRATA | MORE THAN 30 DATA POINTS FOR P-Y CURVE | P-Y CURVE SCALING | REFERENCE DIAMETER | Y FACTOR | SOIL TABLE ID | SOIL DESCRIPTION REMARKS | CONSIDER BASE MOMENT IN ANALYSIS? | NUMBER OF PARTS FOR BASE MOMENT | LEAVE BLANK |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOIL | LATERAL | HEAD |  |  |  |  |  |  |  |  |  |  |
| 1--4 | 6--12 | 14--17 | 18--->20 | 22--->23 | 24--27 | 28<--33 | 34<--40 | 41<--44 | 45--60 | 61 | 63--64 | 65--80 |
| DEFAULT |  |  |  |  |  |  | 1 |  |  |  |  |  |
| ENGLISH |  |  |  |  |  | IN |  |  |  |  |  |  |
| METRIC |  |  |  |  |  | CM |  |  |  |  |  |  |



SOIL P-Y STRATUM LINE

COLUMNS

COMMENTARY

GENERAL THE LOCATION OF EACH SOIL STRATUM IS DEFINED USING THIS LINE.THE P-Y DATA FOR THIS STRATUM FOLLOWS THIS LINE.

( 1- 4) ENTER 'SOIL'.   
(14-17) ENTER 'SLOC'.   
(18-19) ENTER 'SM' IF THE SOIL P-Y CURVE IS THE SAME IN THE POSITIVE AND NEGATIVE DISPLACEMENT DIRECTIONS. IN THIS CASE ONLY POSITIVE VALUES OF P AND Y WILL BE ENTERED ON THE FOLLOWING P-Y LINE ('SOIL P-Y' LINE SET). THE ORIGIN (P=0.0, Y=0.0) MUST BE THE FIRST POINT ENTERED ON THAT LINE.   
(22-23) ENTER THE NUMBER OF POINTS ON THE FOLLOWING P-Y CURVE. ONE POINT CONSISTS OF A "P" VALUE AND A "Y" VALUE. THE NUMBER ENTERED HERE MAY NOT BE GREATER THAN THE VALUE ENTERED IN COLUMNS 22-23 OF THE P-Y LATERAL HEADER LINE ('SOIL LATERAL HEAD' LINE) OR 30 IF THOSE COLUMNS ARE BLANK.   
(25-30) ENTER THE DISTANCE FROM THE PILEHEAD TO THE TOP OF THIS SOIL STRATUM. THIS DISTANCE IS VERTICALLY DOWN AND NOT ALONG THE AXIS OF THE PILE, WHICH MAY BE BATTERED.   
(31-36) ENTER THE DISTANCE FROM THE PILEHEAD TO THE BOTTOM OF THIS SOIL STRATUM IF THE P-Y DATA IS CONSTANT THROUGHOUT THIS STRATUM. IF LEFT BLANK, THE P-Y DATA WILL VARY LINEARLY TO THE TOP OF THE NEXT STRATUM.   
(37-40) ENTER THE "P" FACTOR FOR THIS P-Y CURVE. THIS FACTOR IS USED TO MODIFY THE INPUT "P" VALUES FOR THIS SOIL STRATUM.   
(41-44) ENTER THE AMOUNT TO BE ADDED TO THE INPUT "Y" VALUES. THIS IN EFFECT SHIFTS THE P-Y CURVE ALONG THE Y-AXIS. THIS SHIFT CAN BE USED WITH BOTH SYMMETRICAL AND NONSYMMETRICAL INPUT CURVES AND IS USEFUL FOR MODELING MUDSLIDES.   
(45-60) ENTER ANY DESCRIPTIVE REMARKS ABOUT THIS SOIL STRATUM.   
(70-76) ENTER A HIGH PRECISION "P" FACTOR FOR THIS P-Y CURVE. THIS



| LINE LABEL | LINE TYPE | SYMMETRY INDICATOR | NUMBER OF POINTS PER CURVE | STRATUM LOCATION | STRATUM LOCATION | P FACTOR | Y SHIFT | SOIL DESCRIPTION OR OTHER REMARKS | HIGH PRECISION P FACTOR | LEAVE BLANK |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | LINE TYPE | SYMMETRY INDICATOR | NUMBER OF POINTS PER CURVE | TOP | BOTTOM | P FACTOR | Y SHIFT | SOIL DESCRIPTION OR OTHER REMARKS | HIGH PRECISION P FACTOR | LEAVE BLANK |
| SOIL | SLOC |  |  |  |  |  |  |  |  |  |
| 1--4 | 14--17 | 18--19 | 22--->23 | 25<--30 | 31<--36 | 37<--40 | 41<--44 | 45--60 | 70--76 | 77--80 |
| DEFAULT |  |  |  |  |  | 1 | 0 |  | 1 |  |
| ENGLISH |  |  |  | FT | FT |  | IN |  |  |  |
| METRIC |  |  |  | M | M |  | CM |  |  |  |



SOIL P-Y DATA LINE

COLUMNS

COMMENTARY

GENERAL THIS LINE IS USED TO INPUT THE LATERAL FORCE-DISPLACEMENT (P-Y) DATA FOR EACH SOIL STRATUM. IF A SYMMETRICAL P-Y CURVE IS ENTERED ('SM' IN COLUMNS 18-19 OF THE PRECEDING P-Y STRATUM LINE) ONLY THE POSITIVE HALF OF THE P-Y CURVE SHOULD BE ENTERED, THE FIRST POINT IN THIS CASE MUST BE THE ORIGIN (P=0.0, Y=0.0). THE DATA MUST BE ENTERED IN ORDER OF INCREASING VALUES OF THE DISPLACEMENT, Y.

FOR VALUES OF Y GREATER THAN THE LARGEST SPECIFIED VALUE OR SMALLER THAN THE SMALLEST SPECIFIED VALUE THE VALUE OF P IS ASSUMED TO BE CONSTANT AND EQUAL TO THE VALUE CORRESPONDING TO THOSE Y VALUES.

( 1- 4) ENTER 'SOIL'.   
(14-16) ENTER 'P-Y'.   
(18-77) ENTER THE "P" AND "Y" VALUES TO DESCRIBE THE P-Y CURVE. THIS LINE MAY BE REPEATED AS NECESSARY TO ENTER THE NUMBER OF POINTS SPECIFIED ON THE PRECEDING P-Y STRATUM LINE ('SOIL SLOC' LINE SET).



| LINE LABEL | LINE TYPE | P-Y CURVE DATA POINTS | P-Y CURVE DATA POINTS | P-Y CURVE DATA POINTS | P-Y CURVE DATA POINTS | P-Y CURVE DATA POINTS | P-Y CURVE DATA POINTS | P-Y CURVE DATA POINTS | P-Y CURVE DATA POINTS | P-Y CURVE DATA POINTS | P-Y CURVE DATA POINTS |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | LINE TYPE | 1ST POINT | 1ST POINT | 2ND POINT | 2ND POINT | 3RD POINT | 3RD POINT | 4TH POINT | 4TH POINT | 5TH POINT | 5TH POINT |
| LINE LABEL | LINE TYPE | P | Y | P | Y | P | Y | P | Y | P | Y |
| SOIL | P-Y |  |  |  |  |  |  |  |  |  |  |
| 1-- 4 | 14--16 | 18<--23 | 24<--29 | 30<--35 | 36<--41 | 42<--47 | 48<--53 | 54<--59 | 60<--65 | 66<--71 | 72<--77 |
| DEFAULT |  |  |  |  |  |  |  |  |  |  |  |
| ENGLISH |  | KIP/IN | IN | KIP/IN | IN | KIP/IN | IN | KIP/IN | IN | KIP/IN | IN |
| METRIC (KN) |  | KN/CM | CM | KN/CM | CM | KN/CM | CM | KN/CM | CM | KN/CM | CM |
| METRIC (KG) |  | KG/CM | CM | KG/CM | CM | KG/CM | CM | KG/CM | CM | KG/CM | CM |



SOIL LIQUEFACTION HEADER LINE

COLUMNS

COMMENTARY

GENERAL

THIS LINE IS USED TO SPECIFY THE NUMBER OF SOIL STRATA ANDTHE SOIL IDENTIFIER FOR LIQUEFACTION DESCRIPTION. IT ISFOLLOWED BY SOIL LIQUEFACTION STRATUM LINES.LIQUEFACTION OF SOIL ACCOUNTS FOR REDUCTION IN SOIL SHEARSTRENGTH RESULTING FROM THE BUILDING UP OF PORE PRESSURE INSATURATED SANDY SOILS DUE TO SEVERE EARTHQUAKE SHAKING.THIS DATA SET WILL AUTOMATICALLY CALCULATE THE POTENTIAL FOLIQUEFACTION IN A SOIL STARTUM AND CHNAGE THE SOIL SKINFRICTION AND LATERAL LOAD RESISTANCE PROPERTIES ACCORDINGLY.

THE SEQUENCE OF LINES REQUIRED FOR A LIQUEFACTION DESCRIPTION IS AS FOLLOWS:

1. SOIL LIQUEFACTION HEADER LINE.   
2. SOIL LIQUEFACTION DETAILS FOR EACH STRATUM.

COLUMNS

COMMENTARY

( 1- 4) ENTER 'SOIL'.   
( 6-12) ENTER 'LIQUEFY'.   
(14-17) ENTER 'HEAD'.   
(18-20) ENTER THE NUMBER OF SOIL STRATA FOR THIS DESCRIPTION.   
(21-26) ENTER THE VALUE OF HORIZONTAL SHIFT (%) IN CYCLIC RESISTANCE RATIO (CRR) CURVE. DEFAULT VALUE IS ZERO. ENTER A +VE VALUE FOR AN UNCONSERVATIVE AND A -VE VALUE FOR A CONSERVATIVE ESTIMATE OF THE LIQUEFACTION FACTOR OF SAFETY.   
(27-32) ENTER THE VALUE OF VERTICAL SHIFT (%) IN CYCLIC RESISTANCE RATIO (CRR) CURVE. DEFAULT VALUE IS ZERO. ENTER A +VE VALUE FOR AN UNCONSERVATIVE AND A -VE VALUE FOR A CONSERVATIVE ESTIMATE OF THE LIQUEFACTION FACTOR OF SAFETY.   
(34-36) ENTER THE VALUE OF EARTHQUAKE MAGNITUDE. THE VALUE SHOULD BE BETWEEN 5.5 AND 8.5. DEFAULT IS 7.5.   
(37-40) ENTER THE VALUE OF PEAK GROUND ACCELEATION AS A FRACTION OF GRA VITY. THE VALUE SHOULD BE BETWEEN 0.0 AND 1.0. DEFAULT IS 0.5.   
(41-44) ENTER A SOIL TABLE IDENTIFIER. THIS IDENTIFIER IS USED ON ONE OR MORE 'PILE' LINES TO ASSOCIATE THIS SOIL TABLE WITH THOSE PILES.   
(45-50) ENTER A FACTOR THAT WILL SCALE THE CALCULATED LIQUEFACTION MULTIPLIER. THE VALUE SHOULD BE GREATER THAN ZERO. DEFAULT VALUE IS 1.0.   
(51-60) ENTER ANY DESCRIPTIVE COMMENTS DESIRED.



| LINE LABEL | LIQUEFACTION LABEL | HEAD LABEL | NUMBER OF SOIL STRATA | PERCENT HORIZONTAL SHIFT IN CRR CURVE | PERCENT VERTICAL SHIFT IN CRR CURVE | (Mw) EARTHQUAKE MAGNITUDE | (amax) PEAK GROUND ACCELERATION | SOIL TABLE ID | LIQUEFACTION MULTIPLIER FACTOR | SOIL DESCRIPTION OR OTHER REMARKS |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOIL | LIQUEFY | HEAD |  |  |  |  |  |  |  |  |
| 1--4 | 6--12 | 14--17 | 18--->20 | 21--26 | 27--32 | 34--36 | 37--40 | 41--44 | 45--50 | 51--60 |
| DEFAULT |  |  |  | 0 | 0 | 7.5 | 0.5 |  | 1 |  |
| ENGLISH |  |  |  |  |  |  |  |  |  |  |
| METRIC |  |  |  |  |  |  |  |  |  |  |



SOIL LIQUEFACTION STRATUM LINE

COLUMNS

COMMENTARY

GENERAL THIS LINE SET IS USED TO SPECIFY THE SOIL AND EARQUAKE PROPERTIES. THE PROGRAM WILL USE THESE PROPERTIES TO CALCULATE LIQUEFACTION POTENTIAL OF EACH STRATUM AND MODIFY THE SOIL T-Z AND P-Y CURVES ACCORDINGLY.

( 1- 4) ENTER 'SOIL'.   
( 6-12) ENTER 'LIQUEFY'.   
(14-17) ENTER 'SLOC'.   
( 18 ) ENTER 'A' FOR STRATUM ABOVE THE WATER TABLE. ENTER 'B' OR LEAVE BLANK FOR STRATUM BELOW THE WATER TABLE.   
(19-30) ENTER THE DISTANCES FROM THE PILEHEAD TO THE TOP AND BOTTOM OF THIS SOIL STRATUM. THESE DISTANCES ARE VERTICALLY DOWN AND NOT ALONG THE AXIS OF THE PILE, WHICH MAY BE BATTERED.

COLUMNS

COMMENTARY

(31-33) ENTER 'CPT' TO USE CPT BASED METHOD. ENTER 'N ' IF LIQUEFACTION IS NOT TO BE CONSIDERED FOR THIS STRATUM.   
(34-37) ENTER 'SAND', 'CLAY', OR 'SILT'. LEAVE BLANK IF SOIL TYPE IS NOT KNOWN. SOIL TYPE 'CLAY' WOULD MEAN NO LIQUEFACTION IN THIS STRATUM.   
(45-50) ENTER THE CONE TIP RESISTANCE FOR THE STRATUM.   
(51-56) ENTER THE SLEEVE FRICTION FOR THE STRATUM.   
(57-62) ENTER THE SEBMERGED UNIT WEIGHT.



| LINE LABEL | LIQUEFACTION LABEL | LINE TYPE | WATER TABLE | TOP OF STRATUM | BOTTOM OF STRATUM | CALCULATION METHOD | SOIL TYPE | CONE TIP RESISTANCE | SLEEVE FRICTION | SEBMERGED UNIT WEIGHT |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOIL | LIQUEFY | SLOC |  |  |  |  |  |  |  |  |
| 1--4 | 6--12 | 14--17 | 18 | 19<--24 | 25<--30 | 31--33 | 34--37 | 45<--50 | 51<--56 | 57<--62 |
| DEFAULT |  |  | 'B' |  |  | 'CPT' |  |  |  |  |
| ENGLISH |  |  |  | FT | FT |  |  | KSI | KSI | LB/CU.FT |
| METRIC (KN) |  |  |  | M | M |  |  | MPa | MPa | TONNE/CU.M |
| METRIC (KG) |  |  |  | M | M |  |  | KG/SQ.MM | KG/SQ.MM | TONNE/CU.M |



AXIAL TABLE ENTRY LINES

COLUMNS

COMMENTARY

GENERAL

THE 'TABR' ENTRIES ARE OPTIONAL. THE PSI PROGRAM AUTOMATICALLY DEVELOPS 'TABR' VALUES AND USES A FINE TUNING PROCEDURE TO CONVERGE TO THE SOLUTION. NORMAL CONVERGENCE FOR PILEHEAD LOADS ARE 0.5 PERCENT. USE THE 'TABR' INPUTS ONLY IF THE AUTOMATIC PROCEDURE FAILS TO ADEQUATELY CONVERGE.

THIS LINE SET IS USED TO DEFINE THOSE AXIAL LOADS OR DISPLACEMENTS FOR WHICH PILE SOLUTIONS WILL BE GENERATED.

( 1- 4) ENTER 'TABR'.

( 6-10) ENTER 'AXIAL'.

(12-13) ENTER 'LD' IF THE TABLE IS IN TERMS OF AXIAL LOAD, ENTER 'DF' IF IT IS IN TERMS OF AXIAL DISPLACEMENTS. IF THE SOIL AXIAL DESCRIPTION IS IN TERMS OF ADHESION INSTEAD OF T-Z CURVES THEN AXIAL LOADS MUST BE ENTERED ON THIS LINE.

IF THE T-Z CURVE IS NOT A MONOTONICALLY INCREASING FUNCTION OF DISPLACEMENT THEN AXIAL DISPLACEMENTS MUST BE ENTERED ON THIS LINE. IF THE PILE IS EXPECTED TO BE LOADED NEARLY TO ITS AXIAL CAPACITY THEN AXIAL DISPLACEMENTS SHOULD BE ENTERED ON THIS LINE (T-Z AXIAL DESCRIPTION ONLY). FOR T-Z DATA, IF A VERY LARGE VALUE OF AXIAL DISPLACEMENT IS ENTERED, THEN THE RESULTING PILEHEAD LOAD WILL BE THE PILE CAPACITY.

COLUMNS

COMMENTARY

(16-69) ENTER THE AXIAL LOADS OR DISPLACEMENTS AT WHICH PILE SOLUTIONS WILL BE GENERATED. VALUES MUST BE ENTERED IN INCREASING ORDER FROM THE MOST NEGATIVE TO THE MOST POSITIVE. TENSION AND ELONGATION ARE POSITIVE; COMPRESSION AND CONTRACTION ARE NEGATIVE. O.O SHOULD BE ONE OF THE ENTRIES. IF MORE THAN 9 VALUES ARE TO BE INPUT ENTER A 'C' IN COLUMN 80 AND THEN ENTER ANOTHER LINE OF THIS TYPE WITH THE REMAINING TABLE ENTRY VALUES.   
(70-72) ENTER THE IDENTIFIER OF THE 'PLGRUP' TO WHICH THIS SET OF TABLE ENTRY POINTS APPLIES. IF THIS FIELD IS LEFT BLANK THEN THESE TABLE ENTRY POINTS WILL APPLY TO ALL PILE GROUPS EXCEPT THOSE WHICH ARE REFERRED TO ON OTHER AXIAL 'TABR' LINES.   
(74-77) ENTER THE IDENTIFIER FOR THE 'SOIL' TO WHICH THIS SET OF TABLE ENTRY POINTS APPLIES. IF THIS FIELD IS LEFT BLANK THEN THESE TABLE ENTRY POINTS WILL APPLY TO ALL SOILS EXCEPT THOSE WHICH ARE REFERRED TO ON OTHER AXIAL 'TABR' LINES.   
( 80 ) ENTER 'C' IF MORE AXIAL TABLE ENTRY POINTS ARE ENTERED ON THE NEXT LINE.



| LINE LABEL | AXIAL LABEL | LOAD OR DEFLEC- TION | *2TABLE ENTRY POINTS | *2TABLE ENTRY POINTS | *2TABLE ENTRY POINTS | *2TABLE ENTRY POINTS | *2TABLE ENTRY POINTS | *2TABLE ENTRY POINTS | *2TABLE ENTRY POINTS | *2TABLE ENTRY POINTS | *2TABLE ENTRY POINTS | *2TABLE ENTRY POINTS | PLGRP ID | SOIL ID | CONTINU- ATION |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | AXIAL LABEL | LOAD OR DEFLEC- TION | 1ST ENTRY | 2ND ENTRY | 3RD ENTRY | 4TH ENTRY | 5TH ENTRY | 6TH ENTRY | 7TH ENTRY | 8TH ENTRY | 9TH ENTRY |  | PLGRP ID | SOIL ID | CONTINU- ATION |
| TABR | AXIAL |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 1-- 4 | 6--10 | 12--13 | 16<--21 | 22<--27 | 28<--33 | 34<--39 | 40<--45 | 46<--51 | 52<--57 | 58<--63 | 64<--69 | 70<--72 | 74<--77 | 80 |  |
| DEFAULT |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ENGLISH |  |  | KIP OR IN | KIP OR IN | KIP OR IN | KIP OR IN | KIP OR IN | KIP OR IN | KIP OR IN | KIP OR IN | KIP OR IN |  |  |  |  |
| METRIC (KN) |  |  | KN OR CM | KN OR CM | KN OR CM | KN OR CM | KN OR CM | KN OR CM | KN OR CM | KN OR CM | KN OR CM |  |  |  |  |
| METRIC (KG) |  |  | KG OR CM | KG OR CM | KG OR CM | KG OR CM | KG OR CM | KG OR CM | KG OR CM | KG OR CM | KG OR CM |  |  |  |  |



PILEHEAD LATERAL DEFLECTION TABLE ENTRY LINES

COLUMNS

COMMENTARY

GENERAL

THE 'TABR' ENTRIES ARE OPTIONAL. THE PSI PROGRAM AUTOMATICALLY DEVELOPS 'TABR' VALUES AND USES A FINE TUNING PROCEDURE TO CONVERGE TO THE SOLUTION. NORMAL CONVERGENCE FOR PILEHEAD LOADS ARE 0.5 PERCENT. USE THE 'TABR' INPUTS ONLY IF THE AUTOMATIC PROCEDURE FAILS TO ADEQUATELY CONVERGE.

THIS LINE SET IS USED TO DEFINE THOSE PILEHEAD LATERAL DISPLACEMENTS FOR WHICH PILE SOLUTIONS WILL BE GENERATED.

( 1- 4) ENTER 'TABR'.   
( 6-13) ENTER 'DEFLECTN'.   
(16-69) ENTER THE LATERAL DISPLACEMENTS AT WHICH PILE SOLUTIONS WILL BE GENERATED. VALUES MUST BE ENTERED IN INCREASING ORDER OF MAGNITUDE. IF MORE THAN 9 VALUES ARE TO BE INPUT ENTER A 'C' IN COLUMN 80 AND THEN ENTER ANOTHER LINE OF THIS TYPE WITH THE TABLE ENTRY VALUES DESIRED.

COLUMNS

COMMENTARY

NORMALLY THE P-Y DATA IS SYMMETRICAL AND ONLY POSITIVE VALUES NEED BE ENTERED HERE. IF THE P-Y DATA IS NOT SYMMETRICAL AND IF SOME PILES MOVE IN A NEGATIVE DIRECTION (EITHER IN THE PILEHEAD Y OR Z DIRECTION) THEN THE DATA SHOULD START WITH NEGATIVE DISPLACEMENTS.

(70-72)

ENTER THE IDENTIFIER OF THE 'PLGRUP' TO WHICH THIS SET OF TABLE ENTRY POINTS APPLIES. IF THIS FIELD IS LEFT BLANK THEN THESE TABLE ENTRY POINTS WILL APPLY TO ALL PILE GROUPS EXCEPT THOSE WHICH ARE REFERRED TO ON OTHER LATERAL DEFLECTION 'TABR' LINES.

(74-77)

ENTER THE IDENTIFIER FOR THE 'SOIL' TO WHICH THIS SET OF TABLE ENTRY POINTS APPLIES. IF THIS FIELD IS LEFT BLANK THEN THESE TABLE ENTRY POINTS WILL APPLY TO ALL SOILS EXCEPT THOSE WHICH ARE REFERRED TO ON OTHER LATERAL DEFLECTION 'TABR' LINES.

( 80 )

ENTER 'C' IF MORE DEFLECTION TABLE ENTRY POINTS ARE ENTERED ON THE NEXT LINE.



| LINE LABEL | LATERAL DEFLECTION LABEL | *2TABLE ENTRY POINTS | *2TABLE ENTRY POINTS | *2TABLE ENTRY POINTS | *2TABLE ENTRY POINTS | *2TABLE ENTRY POINTS | *2TABLE ENTRY POINTS | *2TABLE ENTRY POINTS | *2TABLE ENTRY POINTS | *2TABLE ENTRY POINTS | *2TABLE ENTRY POINTS | PLGRUP ID | SOIL ID | CONTINU- ATION |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | LATERAL DEFLECTION LABEL | 1ST ENTRY | 2ND ENTRY | 3RD ENTRY | 4TH ENTRY | 5TH ENTRY | 6TH ENTRY | 7TH ENTRY | 8TH ENTRY | 9TH ENTRY |  | PLGRUP ID | SOIL ID | CONTINU- ATION |
| TABR | DEFLECTN |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 1-- 4 | 6--13 | 16<--21 | 22<--27 | 28<--33 | 34<--39 | 40<--45 | 46<--51 | 52<--57 | 58<--63 | 64<--69 | 70<--72 | 74<--77 | 80 |  |
| DEFAULT |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ENGLISH |  | IN | IN | IN | IN | IN | IN | IN | IN | IN |  |  |  |  |
| METRIC |  | CM | CM | CM | CM | CM | CM | CM | CM | CM |  |  |  |  |



PILEHEAD ROTATION TABLE ENTRY LINES

COLUMNS

COMMENTARY

GENERAL

THE 'TABR' ENTRIES ARE OPTIONAL. THE PSI PROGRAM AUTOMATICALLY DEVELOPS 'TABR' VALUES AND USES A FINE TUNING PROCEDURE TO CONVERGE TO THE SOLUTION. NORMAL CONVERGENCE FOR PILEHEAD LOADS ARE 0.5 PERCENT. USE THE 'TABR' INPUTS ONLY IF THE AUTOMATIC PROCEDURE FAILS TO ADEQUATELY CONVERGE.

THIS LINE SET IS USED TO DEFINE THOSE PILEHEAD ROTATIONS FOR WHICH PILE SOLUTIONS WILL BE GENERATED.

( 1- 4)

ENTER 'TABR'.

( 6-13)

ENTER 'ROTATION'.

(16-69)

ENTER THE PILEHEAD ROTATIONS AT WHICH PILE SOLUTIONS WILL BE GENERATED. VALUES MUST BE ENTERED IN ORDER OF INCREASING MAGNITUDE STARTING WITH THE MOST NEGATIVE THROUGH 0.0 TO THE MOST POSITIVE VALUE. IF MORE THAN 9 VALUES ARE TO BE INPUT, ENTER A 'C' IN COLUMN 80 AND THEN ENTER ANOTHER LINE OF THIS TYPE WITH THE TABLE ENTRY VALUES DESIRED.

COLUMNS

COMMENTARY

BOTH POSITIVE AND NEGATIVE VALUES OF PILEHEAD ROTATION MUST BE ENTERED, REGARDLESS OF THE CHARACTER OF THE P-Y CURVES (SYMMETRICAL OR NOT). THE SIGNIFICANCE OF THE SIGN OF THE ROTATION IS THAT A POSITIVE ROTATION TENDS TO INCREASE PILEHEAD DISPLACEMENTS CAUSED BY A POSITIVE PILEHEAD SHEAR WHILE A NEGATIVE VALUE TENDS TO DECREASE THOSE DISPLACEMENTS.

(70-72)

ENTER THE IDENTIFIER OF THE 'PLGRUP' TO WHICH THIS SET OF TABLE ENTRY POINTS APPLIES. IF THIS FIELD IS LEFT BLANK THEN THESE TABLE ENTRY POINTS WILL APPLY TO ALL PILE GROUPS EXCEPT THOSE WHICH ARE REFERRED TO ON OTHER PILEHEAD ROTATION 'TABR' LINES.

(74-77)

ENTER THE IDENTIFIER FOR THE 'SOIL' TO WHICH THIS SET OF TABLE ENTRY POINTS APPLIES. IF THIS FIELD IS LEFT BLANK THEN THESE TABLE ENTRY POINTS WILL APPLY TO ALL SOILS EXCEPT THOSE WHICH ARE REFERRED TO ON OTHER PILEHEAD ROTATION 'TABR' LINES.

( 80 )

ENTER 'C' IF MORE ROTATION TABLE ENTRY POINTS ARE ENTERED ON THE NEXT LINE.



| LINE LABEL | PILEHEAD ROTATION LABEL | *2TABLE ENTRY POINTS | *2TABLE ENTRY POINTS | *2TABLE ENTRY POINTS | *2TABLE ENTRY POINTS | *2TABLE ENTRY POINTS | *2TABLE ENTRY POINTS | *2TABLE ENTRY POINTS | *2TABLE ENTRY POINTS | *2TABLE ENTRY POINTS | PLGRUP ID | SOIL ID | CONTINU- ATION |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | PILEHEAD ROTATION LABEL | 1ST ENTRY | 2ND ENTRY | 3RD ENTRY | 4TH ENTRY | 5TH ENTRY | 6TH ENTRY | 7TH ENTRY | 8TH ENTRY | 9TH ENTRY | PLGRUP ID | SOIL ID | CONTINU- ATION |
| TABR | ROTATION |  |  |  |  |  |  |  |  |  |  |  |  |
| 1-- 4 | 6--13 | 16<--21 | 22<--27 | 28<--33 | 34<--39 | 40<--45 | 46<--51 | 52<--57 | 58<--63 | 64<--69 | 70<--72 | 74<--77 | 80 |
| DEFAULT |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ENGLISH |  | RAD | RAD | RAD | RAD | RAD | RAD | RAD | RAD | RAD |  |  |  |
| METRIC |  | RAD | RAD | RAD | RAD | RAD | RAD | RAD | RAD | RAD |  |  |  |



PILEHEAD TORSION TABLE ENTRY LINES

COLUMNS

COMMENTARY

GENERAL

THE 'TABR' ENTRIES ARE OPTIONAL. THE PSI PROGRAM AUTOMATICALLY DEVELOPS 'TABR' VALUES AND USES A FINE TUNING PROCEDURE TO CONVERGE TO THE SOLUTION. NORMAL CONVERGENCE FOR PILEHEAD LOADS ARE 0.5 PERCENT. USE THE 'TABR' INPUTS ONLY IF THE AUTOMATIC PROCEDURE FAILS TO ADEQUATELY CONVERGE.

THIS LINE SET IS USED TO SPECIFY PILEHEAD TORQUES FOR WHICH PILE SOLUTIONS WILL BE GENERATED. THE TORQUE SOLUTIONS ARE INDEPENDENT OF THE AXIAL AND LATERAL SOLUTIONS.

IF SOIL TORSIONAL ADHESION DATA OR SPRING DATA IS INPUT THEN TORQUES SHOULD BE ENTERED ON THIS LINE, NORMALLY TWO VALUES ARE SUFFICIENT, E.G. 0.0 AND 100.0. IF NO TORSION ADHESION DATA IS INPUT AND THE SOIL AXIAL DESCRIPTION IS IN TERMS OF ADHESION THAN THE TORSION DATA DEFAULTS TO THE AXIAL ADHESION DESCRIPTION. ENTER THIS LINE WITH NO TORQUE VALUES IF TORSION DATA IS OMITTED AND THE AXIAL DESCRIPTION IS T-Z OR SPRING DATA.

COLUMNS

COMMENTARY

( 1- 4) ENTER 'TABR'.   
( 6-12) ENTER 'TORSION'.   
(16-69) ENTER THE TABLE ENTRY POINTS.   
(70-72) ENTER THE IDENTIFIER OF THE 'PLGRUP' TO WHICH THIS SET OF TABLE ENTRY POINTS APPLIES. IF THIS FIELD IS LEFT BLANK THEN THESE TABLE ENTRY POINTS WILL APPLY TO ALL 'PLGRUPS' EXCEPT THOSE WHICH ARE REFERRED TO ON OTHER TORSION TABR LINES.   
(74-77) ENTER THE IDENTIFIER FOR THE 'SOIL' TO WHICH THIS SET OF TABLE ENTRY POINTS APPLIES. IF THIS FIELD IS LEFT BLANK THEN THESE TABLE ENTRY POINTS WILL APPLY TO ALL 'SOILS' EXCEPT THOSE WHICH ARE REFERRED TO ON OTHER TORSION TABR LINES.   
( 80 ) ENTER 'C' IF MORE TORSION TABLE ENTRY POINTS ARE ENTERED ON THE NEXT LINE.



| LINE LABEL | PILEHEAD TORSION LABEL | *2TABLE ENTRY POINTS | *2TABLE ENTRY POINTS | *2TABLE ENTRY POINTS | *2TABLE ENTRY POINTS | *2TABLE ENTRY POINTS | *2TABLE ENTRY POINTS | *2TABLE ENTRY POINTS | *2TABLE ENTRY POINTS | *2TABLE ENTRY POINTS | *2TABLE ENTRY POINTS | PLGRP ID | SOIL ID | CONTINU- ATION |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | PILEHEAD TORSION LABEL | 1ST ENTRY | 2ND ENTRY | 3RD ENTRY | 4TH ENTRY | 5TH ENTRY | 6TH ENTRY | 7TH ENTRY | 8TH ENTRY | 9TH ENTRY |  | PLGRP ID | SOIL ID | CONTINU- ATION |
| TABR | TORSION |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 1-- 4 | 6--12 | 16<--21 | 22<--27 | 28<--33 | 34<--39 | 40<--45 | 46<--51 | 52<--57 | 58<--63 | 64<--69 | 70<--72 | 74<--77 | 80 |  |
| DEFAULT |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ENGLISH |  | KIP-FT | KIP-FT | KIP-FT | KIP-FT | KIP-FT | KIP-FT | KIP-FT | KIP-FT | KIP-FT |  |  |  |  |
| METRIC (KN) |  | KN-M | KN-M | KN-M | KN-M | KN-M | KN-M | KN-M | KN-M | KN-M |  |  |  |  |
| METRIC (KG) |  | KG-M | KG-M | KG-M | KG-M | KG-M | KG-M | KG-M | KG-M | KG-M |  |  |  |  |



SOIL TORSION ADHESION HEADER LINE

COLUMNS

COMMENTARY

COLUMNS

COMMENTARY

GENERAL EITHER THIS LINE FOLLOWED BY 'SLOC' AND CAPACITY LINE SETS,OR TORSION SPRING LINE SHOULD BE INCLUDED IN ANY PSI INPUTFILE.

THIS LINE IS USED TO MODEL THE TORSIONAL RESISTANCE OF THEPILE RESULTING FROM ADHESION OF THE SURROUNDING SOIL.

STARTING AT THE TOP STRATUM THE LENGTH OVER WHICH THE ADHESION MUST ACT TO TRANSFER THE PILE TORQUE TO THE SOIL IS COMPUTED. IF THIS LENGTH IS LESS THAN THE THICKNESS OF THE STRATUM, THE TORQUE IS COMPLETELY TRANSFERRED TO THE SOIL OVER THAT LENGTH. IF THE COMPUTED LENGTH IS GREATER THAN THE STRATUM THICKNESS THE TORQUE IS ONLY PARTIALLY TRANSFERRED IN THAT STRATUM. THE EXCESS PILE TORQUE IS TRANSFERRED IN THE NEXT DEEPER SOIL STRATUM. THE PROCEDURE IS REPEATED FOR EACH STRATUM IN TURN UNTIL THE ENTIRE PILE TORQUE IS TRANSFERRED OR UNTIL ALL SOIL STRATA HAVE REACHED THEIR CAPACITIES.

IF THE PILE TORQUE HAS NOT BEEN TRANSFERRED AFTER ALL STRATA HAVE REACHED THEIR CAPACITIES THE PILE FAILS IN TORSION AND A REPORT TO THAT EFFECT IS ISSUED.

THIS SOIL MODEL TAKES NO ACCOUNT OF SOIL DEFORMATIONS. THE TORSIONAL ROTATION AT THE PILEHEAD IS TAKEN TO BE EQUAL TO THE ELASTIC TWIST OF THE PILE.

( 1- 4) ENTER 'SOIL'.   
( 6-12) ENTER 'TORSION'.   
(14-17) ENTER 'HEAD'.   
(18-20) ENTER THE NUMBER OF SOIL STRATA TO BE DESCRIBED ON THE FOLLOWING LINES ('SOIL SLOC' AND 'SOIL' LINE SETS).   
(41-44) ENTER AN ALPHANUMERIC SOIL TABLE IDENTIFIER. THIS IDENTIFIER IS USED ON ONE OR MORE 'PILE' LINES TO ASSOCIATE THIS SOIL TABLE WITH THOSE PILES.   
(45-60) ENTER ANY DESCRIPTIVE REMARKS DESIRED.



| LINE LABEL | TORSION LABEL | HEAD LABEL | NUMBER OF SOIL STRATA | SOIL TABLE ID | SOIL DESCRIPTION OR OTHER REMARKS | LEAVE BLANK |
| --- | --- | --- | --- | --- | --- | --- |
| SOIL | TORSION | HEAD |  |  |  |  |
| 1--4 | 6--12 | 14--17 | 18--->20 | 41<-44 | 45------60 | 61--80 |



SOIL TORSIONAL ADHESION STRATA LINE

COLUMNS

COMMENTARY

LOCATION THIS LINE SET FOLLOWS TORSION HEADER LINE AND IS FOLLOWED BY THE USER INPUT TORSION DATA.

GENERAL THE TORSIONAL ADHESION STRATA LOCATIONS ARE DEFINED USING THIS LINE. THESE STRATA LOCATIONS ARE MEASURED FROM THE PILEHEAD. FIVE STRATA ARE INPUT PER LINE AND THIS LINE IS REPEATED UNTIL THE NUMBER OF STRATA DESIGNATED ON THE SOIL TORSION ADHESION HEADER LINE HAVE BEEN DESCRIBED.

( 1- 4) ENTER 'SOIL'.   
(14-17) ENTER 'SLOC'.   
(19-78) ENTER THE DISTANCES FROM THE PILEHEAD TO THE TOP AND BOTTOM OF EACH STRATUM. THE LOCATION OF THE BOTTOM OF THE LAST STRATUM ENTERED MUST BE AT LEAST TO THE BOTTOM OF THE DEEPEST PILE TO WHICH THIS TABLE APPLIES. THE LOCATION OF THE TOP OF A STRATUM MUST BE THE SAME AS THE BOTTOM OF THE PRECEDING STRATUM. THESE DISTANCES ARE VERTICALLY DOWN AND NOT ALONG THE AXIS OF THE PILE, WHICH MAY BE BATTERED.



| LINE LABEL | LINE TYPE | TORSIONAL ADHESION STRATA LOCATIONS | TORSIONAL ADHESION STRATA LOCATIONS | TORSIONAL ADHESION STRATA LOCATIONS | TORSIONAL ADHESION STRATA LOCATIONS | TORSIONAL ADHESION STRATA LOCATIONS | TORSIONAL ADHESION STRATA LOCATIONS | TORSIONAL ADHESION STRATA LOCATIONS | TORSIONAL ADHESION STRATA LOCATIONS | TORSIONAL ADHESION STRATA LOCATIONS | TORSIONAL ADHESION STRATA LOCATIONS |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | LINE TYPE | 1ST STRATUM | 1ST STRATUM | 2ND STRATUM | 2ND STRATUM | 3RD STRATUM | 3RD STRATUM | 4TH STRATUM | 4TH STRATUM | 5TH STRATUM | 5TH STRATUM |
| LINE LABEL | LINE TYPE | TOP | BOTTOM | TOP | BOTTOM | TOP | BOTTOM | TOP | BOTTOM | TOP | BOTTOM |
| SOIL | SLOC |  |  |  |  |  |  |  |  |  |  |
| 1-- 4 | 14--17 | 19<--24 | 25<--30 | 31<--36 | 37<--42 | 43<--48 | 49<--54 | 55<--60 | 61<--66 | 67<--72 | 73<--78 |
| DEFAULT |  |  |  |  |  |  |  |  |  |  |  |
| ENGLISH |  | FT | FT | FT | FT | FT | FT | FT | FT | FT | FT |
| METRIC |  | M | M | M | M | M | M | M | M | M | M |



SOIL TORSIONAL ADHESION CAPACITY LINE

COLUMNS

COMMENTARY

LOCATION THIS LINE SET FOLLOWS THE TORSION 'SLOC' LINE.

GENERAL THIS LINE SET IS USED TO ENTER THE TORSIONAL ADHESION CAPACITIES FOR THE TOP AND BOTTOM OF EACH STRATUM DEFINED BY THE TORSIONAL ADHESION STRATA LINES. THE ADHESION CAPACITY WITHIN A STRATUM IS CONSTANT AND EQUALS THE AVERAGE OF THE VALUES AT THE TOP AND BOTTOM OF THE STRATUM.

( 1- 4) ENTER 'SOIL'.

(19-78) ENTER THE ADHESION CAPACITIES AT THE TOP AND BOTTOM OF EACH STRATUM. IF MORE THAN FIVE STRATA ARE USED, REPEAT THIS LINE UNTIL ALL STRATA HAVE BEEN DEFINED.



| LINE LABEL | SOIL TORSIONAL ADHESION CAPACITIES | SOIL TORSIONAL ADHESION CAPACITIES | SOIL TORSIONAL ADHESION CAPACITIES | SOIL TORSIONAL ADHESION CAPACITIES | SOIL TORSIONAL ADHESION CAPACITIES | SOIL TORSIONAL ADHESION CAPACITIES | SOIL TORSIONAL ADHESION CAPACITIES | SOIL TORSIONAL ADHESION CAPACITIES | SOIL TORSIONAL ADHESION CAPACITIES | SOIL TORSIONAL ADHESION CAPACITIES |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINE LABEL | 1ST STRATUM | 1ST STRATUM | 2ND STRATUM | 2ND STRATUM | 3RD STRATUM | 3RD STRATUM | 4TH STRATUM | 4TH STRATUM | 5TH STRATUM | 5TH STRATUM |
| LINE LABEL | TOP | BOTTOM | TOP | BOTTOM | TOP | BOTTOM | TOP | BOTTOM | TOP | BOTTOM |
| SOIL |  |  |  |  |  |  |  |  |  |  |
| 1-- 4 | 19<--24 | 25<--30 | 31<--36 | 37<--42 | 43<--48 | 49<--54 | 55<--60 | 61<--66 | 67<--72 | 73<--78 |
| DEFAULT |  |  |  |  |  |  |  |  |  |  |
| ENGLISH | KIP/SQ.FT | KIP/SQ.FT | KIP/SQ.FT | KIP/SQ.FT | KIP/SQ.FT | KIP/SQ.FT | KIP/SQ.FT | KIP/SQ.FT | KIP/SQ.FT | KIP/SQ.FT |
| METRIC (KN) | KN/SQ.CM | KN/SQ.CM | KN/SQ.CM | KN/SQ.CM | KN/SQ.CM | KN/SQ.CM | KN/SQ.CM | KN/SQ.CM | KN/SQ.CM | KN/SQ.CM |
| METRIC (KG) | KG/SQ.CM | KG/SQ.CM | KG/SQ.CM | KG/SQ.CM | KG/SQ.CM | KG/SQ.CM | KG/SQ.CM | KG/SQ.CM | KG/SQ.CM | KG/SQ.CM |



SOIL TORSION ADHESION HEADER LINE

COLUMNS

COMMENTARY

COLUMNS

COMMENTARY

GENERAL EITHER THIS LINE FOLLOWED BY 'SLOC' AND CAPACITY LINE SETS,OR TORSION SPRING LINE SHOULD BE INCLUDED IN ANY PSI INPUTFILE.

THIS LINE IS USED TO MODEL THE TORSIONAL RESISTANCE OF THEPILE RESULTING FROM ADHESION OF THE SURROUNDING SOIL.

STARTING AT THE TOP STRATUM THE LENGTH OVER WHICH THE ADHESION MUST ACT TO TRANSFER THE PILE TORQUE TO THE SOIL IS COMPUTED. IF THIS LENGTH IS LESS THAN THE THICKNESS OF THE STRATUM, THE TORQUE IS COMPLETELY TRANSFERRED TO THE SOIL OVER THAT LENGTH. IF THE COMPUTED LENGTH IS GREATER THAN THE STRATUM THICKNESS THE TORQUE IS ONLY PARTIALLY TRANSFERRED IN THAT STRATUM. THE EXCESS PILE TORQUE IS TRANSFERRED IN THE NEXT DEEPER SOIL STRATUM. THE PROCEDURE IS REPEATED FOR EACH STRATUM IN TURN UNTIL THE ENTIRE PILE TORQUE IS TRANSFERRED OR UNTIL ALL SOIL STRATA HAVE REACHED THEIR CAPACITIES.

IF THE PILE TORQUE HAS NOT BEEN TRANSFERRED AFTER ALL STRATA HAVE REACHED THEIR CAPACITIES THE PILE FAILS IN TORSION AND A REPORT TO THAT EFFECT IS ISSUED.

THIS SOIL MODEL TAKES NO ACCOUNT OF SOIL DEFORMATIONS. THE TORSIONAL ROTATION AT THE PILEHEAD IS TAKEN TO BE EQUAL TO THE ELASTIC TWIST OF THE PILE.

( 1- 4) ENTER 'SOIL'.   
( 6-12) ENTER 'TORSION'.   
(14-17) ENTER 'HEAD'.   
(18-20) ENTER THE NUMBER OF SOIL STRATA TO BE DESCRIBED ON THE FOLLOWING LINES ('SOIL SLOC' AND 'SOIL' LINE SETS).   
(41-44) ENTER AN ALPHANUMERIC SOIL TABLE IDENTIFIER. THIS IDENTIFIER IS USED ON ONE OR MORE 'PILE' LINES TO ASSOCIATE THIS SOIL TABLE WITH THOSE PILES.   
(45-60) ENTER ANY DESCRIPTIVE REMARKS DESIRED.



| LINE LABEL | TORSION LABEL | HEAD LABEL | NUMBER OF SOIL STRATA | SOIL TABLE ID | SOIL DESCRIPTION OR OTHER REMARKS | LEAVE BLANK |
| --- | --- | --- | --- | --- | --- | --- |
| SOIL | TORSION | HEAD |  |  |  |  |
| 1--4 | 6--12 | 14--17 | 18--->20 | 41<-44 | 45------60 | 61--80 |

