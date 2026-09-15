SACS

Quality Control

Version 24.00

Trademark Notice

Bentley and the "B" Bentley logo are either registered or unregistered trademarks or service marks of Bentley Systems, Incorporated. All other marks are the property of their respective owners.

Copyright Notice

Copyright © 2024, Bentley Systems, Incorporated. All Rights Reserved.

TABLE OF CONTENTS

1 INTRODUCTION .. 4   
2 SOFTWARE CONTROL PROCEDURES ..

## 2.1 Module Version Identification ..... 5
## 2.2 Implementation Of Updates ... 5
## 2.3 Modules Release Protocol .. 5

3 SOFTWARE TESTING PROCEDURES .

## 3.1 Static Tests .... 7
## 3.2 System Integration Tests...
## 3.3 Dynamic Tests ....
## 3.4 Third-Party Tests ...

4 SOFTWARE SUPPORT SERVICES ... . 8   
5 FUNCTIONAL ORGANIZATION DESCRIPTION . 9

## 5.1 Program Development.. 9
## 5.2 System Integration.... 9
## 5.3 Beta Testing ..... 9
## 5.4 Final Testing and Release.... 9
## 5.5 Documentation ..... 9

6 APPENDIX A... .. 10

## 6.1 Quality Assurance Release Information..... .10

1 INTRODUCTION

This document is issued for the information of users and the potential users of the Bentley SACS Software System programs. The program quality control topics covered in this document are Software Control Procedures, Testing Procedures, Software Support Services, Functional Organization Description and Documentation. The development of the quality control procedure has occurred over many years and is intended to meet the specifications of NATO Standards Document AQAP-13.

2 SOFTWARE CONTROL PROCEDURES

Bentley Systems Inc. develops and maintains the Bentley SACS Software suite at its office in Metairie, Louisiana. The program system, comprising over twenty-five (25) interrelated program modules, resides at Bentley SACS’s on-site data processing facility which houses personal computers running Windows 10 & Windows 11 operating system.

Early on, in the development of the Bentley SACS System of programs Bentley Systems Inc. established management guidelines for the control of a continuously developing software product line. The central procedure for maintaining large-scale, multifaceted software that exists in an environment that requires continual innovations was to maintain all versions of the software in one set of source code. Bentley SACS has developed an internal program maintenance system that allows this to be accomplished in a highly automated procedure. Control procedures are described in the following sections.

## 2.1 Module Version Identification

Each program module in the Bentley SACS System is tracked throughout its life by a unique module version identification number. This ID number shows three principal module qualities. For example, in the ID #MM.UU.PP.BB

MM is the major release number

UU is the update number

PP is the patch number

BB is the build number.

Module version identifications are reported in the output listing files or, where applicable, under the help about features.

## 2.2 Implementation of Updates

All updates and modifications to Bentley SACS System modules are performed by Bentley SACS engineers and programmers at Bentley SACS’s in-house data processing facility headquartered in Metairie, Louisiana.

## 2.3 Modules Release Protocol

Distribution of all Bentley SACS modules and major system releases are processed through the Module Release Group at Bentley SACS’s Metairie office. Each Software release is monitored by this office which verifies testing group clearance, machine type and operating system compatibility, export and shipping requirements and any particular special client requirements.

The delivery of the program system is made through Bentley’s software download center. Such distributions consist of a software installer containing all SACS modules all data files required by the program modules and the necessary support software. Also included will be a series of inputs and corresponding outputs for selected analysis models which are described in Appendix A. These analysis models have been designed to demonstrate the various functions of the program modules being

delivered. Successful installation of the program system is achieved when identical results are produced for these analysis models on the receiving computer system.

3 SOFTWARE TESTING PROCEDURES

Bentley SACS maintains a comprehensive in-house testing program. The testing program processes each newly developed or updated program module through four levels of test verification:

Level 1 Static tests

Level 2 System integration tests

Level 3 Dynamic tests

Level 4 Third-party tests

## 3.1 Static Tests

Static tests are carried out during the software module design and/or update phase by the engineer/programmer in charge. These tests verify the basic functioning of the software and its compatibility with the various language translators and computer operating systems. Program modules which are hardware and/or firmware dependent are checked for proper function at this time.

## 3.2 System Integration Tests

The Bentley SACS Suite of program modules have been designed to draw upon one common input database and one common output database. All newly generated or updated program modules are tested for compatibility with these two databases. Additionally, all program modules are verified for compatibility of input and output format with the Bentley SACS System as a whole.

## 3.3 Dynamic Tests

Program modules which have cleared the Static and System Integration tests are then made available to Bentley SACS’s Engineering Consultancy group in Metairie. This group performs program module tests, in which test results are verified against results of completed design projects.

## 3.4 Third-Party Tests

In parallel with Dynamic testing, Bentley SACS issues pre-releases of the Bentley SACS System to a number of third-party test sites in Brazil, Norway, France and the United States for testing of new features and/or special requests needed on short notice.

4 SOFTWARE SUPPORT SERVICES

Bentley SACS provides an extensive software support network to supplement the Bentley SACS software quality control measures. Clients worldwide may communicate with Bentley SACS software representatives via telephone, telefax or e-mail seven days a week. The client will speak or communicate directly with one of Bentley SACS’s engineers who maintains and/or uses the Bentley SACS System on a daily basis.

The interaction which results from this support system provides a continuous feedback of ideas, enhancements and improvements to the Bentley SACS system and thus maintains the state-of-the-art nature and high quality in the software product line.

5 FUNCTIONAL ORGANIZATION DESCRIPTION

Bentley SACS software development and maintenance are performed in five different phases. All phases require at least vice-presidential approval to initiate and complete. The five phases are listed in the following sections.

## 5.1 Program Development

This includes conceptual development as well as incorporating corrections, enhancements and modifications. This staff includes engineer/programmers and applied research engineers.

## 5.2 System Integration

All modifications and newly developed software are tested for conformity in internal architecture and compatibility with existing software. All new software is given initial testing to verify that the programs are performing according to the Program Development guidelines. Also, any documentation changes are noted and submitted to the Documentation Group. The programs are then submitted for Beta testing.

## 5.3 Beta Testing

Testing is continued by in-house engineers. This testing is performed on existing project data and compared to previous results from those projects. Also, outside third-party companies participate in Beta testing by accepting pre-releases of the program to be used on actual projects. All reports are submitted to the System Integration Group for final evaluation.

## 5.4 Final Testing and Release

Final testing is performed on all programs on each computer type currently supported by Bentley SACS. Standard Master Test Data is created on Bentley SACS’s quality assurance server for all programs. These Master Tests are then performed on all other hardware releases and the program outputs are compared to the Master Outputs from the quality assurance server. All program releases are done in machine readable form (binary or absolute) and each release contains a complete set of installation data and output prints, described in Appendix A, to be used at each installation for quality assurance. Since it is impossible to test the programs on all hardware operating systems and compiler libraries, the final testing procedure is to be performed by the client by comparing the supplied quality test data with the test data created by the client.

## 5.5 Documentation

Documentation changes are normally made to coincide with new releases of the software reflecting the input from the System Integration. Documents are related to the current release of each program. Each document is identified by the date of its release as shown on the title page of each document. Documents are not updated on a page basis but are released as complete documents.

# 6 APPENDIX A

## 6.1 Quality Assurance Release Information

The following is a list of installation data and output prints provided for quality assurance testing. The final quality assurance testing is to be performed by the client by comparing the supplied quality test data with the test data created by the client.



| Demo 1. Static Topside | Demo 1. Static Topside |
| --- | --- |
| sacinpdemo01 | SACS IV data |
| saclstdemo01.std | Output listing of SACS IV |
| rundemo01.runx | SACS run file |





| Demo 2. Static Offshore | Demo 2. Static Offshore |
| --- | --- |
| seainp(staticdemo02 | Seastate static load data |
| sacinpdemo02 | SACS IV static data |
| jcninpdemo02 | Joint Can data for static analysis |
| seainp.ldfdemo02 | Seastate large deflection load data |
| pilinpdemo02 | Pile input data |
| saclstdemo02.std | Output listing of Seastate, SACS IV and Joint Can run |
| ldflstdemo02.std | Output listing of large deflection analysis run |
| pillstdemo02.std | Output listing of single pile analysis |
| demo02.runx | SACS multi-file run file (runs entire demo) |
| staticdemo02.runx | Run file for static analysis |
| ldfdemo02.runx | Run file for large deflection analysis |
| piledemo02.runx | Run file for single-pile analysis |
| Demo 3. Basic Non-Linear Add-On | Demo 3. Basic Non-Linear Add-On |
| sacinp.gapdemo03 | SACS IV input data for Gap analysis |
| gapinpdemo03 | Gap input data |
| sacinp.psidemo03 | SACS IV input data for PSI analysis |
| psiinpdemo03 | Pile/Soil Interaction input data |
| gaplstdemo03.std | Output listing of nonlinear Gap analysis |
| psilstdemo03.std | Output listing of PSI analysis |
| demo03.runx | SACS multi-file run file (runs entire demo 3) |
| gapdemo03.runx | Run file for Gap analysis |
| psidemo03.runx | Run file for PSI analysis |





| Demo 4a. Basic Dynamic Add-On (w/Dynamic Response) | Demo 4a. Basic Dynamic Add-On (w/Dynamic Response) |
| --- | --- |
| sacinpdemo04a | Seastate and SACS IV data |
| dyninpdemo04a | Dynpac modal analysis data |
| dyrinpdemo04a | Dynamic response (earthquake) data |
| saclstdemo04a.std | Output listing for static analysis run |
| dynlstdemo04a.std | Output listing for modal analysis run |
| eqklstdemo04a.std | Output listing for earthquake analysis |
| demo04a.runx | SACS multi-file run file (runs entire demo 4a) |
| staticdemo04a.runx | Static analysis run file |
| dynpacdemo04a.runx | Modal analysis run file |
| earthquakedemo04a.runx | Earthquake analysis run file |
| Demo 4b. Basic Dynamic Add-On (w/Wave Response) | Demo 4b. Basic Dynamic Add-On (w/Wave Response) |
| sacinpdemo04b | SACS IV data |
| seainp_modedemo04b | Seastate modal analysis load data |
| seainp.wavedemo04b | Seastate wave response load data |
| dyninpdemo04b | Modal analysis input data |
| wvrinpdemo04b | Wave response input data |
| dynlstdemo04b.std | Output listing for modal analysis run |
| wvrlstdemo04b.std | Output listing for wave response run |
| demo04b.runx | SACS multi-file run file (runs entire demo 4b) |
| dynpacdemo04b.runx | Modal analysis run file |
| wave responsedemo04b.runx | Wave response run file |





| Demo 5a. Basic Dynamic Fatigue (w/Dynamic Response) | Demo 5a. Basic Dynamic Fatigue (w/Dynamic Response) |
| --- | --- |
| sacinpdemo05a | SACS IV data |
| dyninpdemo05a | Dynpac modal analysis data |
| dyrinpdemo05a | Dynamic response (earthquake) data |
| ftginpdemo05a | Fatigue data |
| saclstdemo05a.std | Output listing for static analysis run |
| dynlstdemo05a.std | Output listing for modal analysis run |
| eqklstdemo05a.std | Output listing for earthquake analysis |
| ftglstdemo05a.std | Output listing for fatigue analysis |
| demo05a.run | SACS multi-file run file (runs entire demo 5a) |
| staticdemo05a.runx | Static analysis run file |
| dynpacdemo05a.runx | Modal analysis run file |
| earthquakedemo05a.runx | Earthquake analysis run file |
| fatiguedemo05a.runx | Fatigue analysis run file |
| Demo 5b. Basic Dynamic Fatigue (w/Wave Response) | Demo 5b. Basic Dynamic Fatigue (w/Wave Response) |
| sacinpdemo05b | SACS IV data |
| seainp_modedemo05b | Seastate modal analysis load data |
| seainp.wavedemo05b | Seastate wave response load data |
| dyninpdemo05b | Modal analysis input data |
| wvrinpdemo05b | Wave response input data |
| dynlstdemo05b.std | Output listing for modal analysis run |
| wvrlstdemo05b.std | Output listing for wave response run |
| ftglstdemo05b.std | Output listing for fatigue analysis run |
| demo05b.runx | SACS multi-file run file (runs entire demo) |
| dynpacdemo05b.runx | Modal analysis run file |
| wave responsedemo05b.runx | Wave response run file |
| fatiguedemo05b.runx | Fatigue analysis run file |





| Demo 6. Advanced Dynamic Fatigue | Demo 6. Advanced Dynamic Fatigue |
| --- | --- |
| sacinpdemo06 | SACS IV data |
| seainp_modedemo06 | Seastate modal analysis load data |
| seainp.fatiguedemo06 | Seastate fatigue analysis load data |
| dyninpdemo06 | Modal analysis input data |
| dyrinpdemo06 | Earthquake analysis input data |
| wvrinpdemo06 | Wave response input data |
| ftginpdemo06 | Fatigue analysis input data |
| saclstdemo06.std | Output listing for static analysis run |
| dynlstdemo06.std | Output listing for modal analysis run |
| eqklstdemo06.std | Output listing for earthquake analysis |
| wvrlstdemo06.std | Output listing for wave response run |
| ftglstdemo06.std | Output listing for fatigue analysis run |
| demo06.runx | SACS multi-file run file (runs entire demo 6) |
| dynpacdemo06.runx | Modal analysis run file |
| earthquakedemo06.runx | Earthquake analysis run file |
| wave responsedemo06.runx | Wave response run file |
| fatiguedemo06.runx | Fatigue analysis run file |





| Demo 7. Plastic Non-Linear Add-On | Demo 7. Plastic Non-Linear Add-On |
| --- | --- |
| sacinpdemo07 | SACS IV data |
| sacinp.gapdemo07 | SACS IV data for nonlinear gap analysis |
| gapinpdemo07 | Gap analysis input data |
| psiinpdemo07 | Pile/Soil Interaction input data |
| clpinpdemo07 | Nonlinear collapse analysis input data |
| saclstdemo07.std | Output listing of static analysis run |
| gaplstdemo07.std | Output listing of Gap analysis run |
| psilstdemo07.std | Output listing of PSI analysis |
| clplstdemo07.std | Output listing of nonlinear collapse analysis |
| demo07.runx | SACS multi-file run file (runs entire demo 7) |
| gapdemo07.runx | Gap analysis run file |
| psidemo07.runx | Run file for PSI analysis |
| collapsedemo07.runx | Nonlinear collapse analysis run file |
| Demo 8. Advanced Dynamic Add-On | Demo 8. Advanced Dynamic Add-On |
| sacinpdemo08 | SACS IV data |
| seainpdemo08 | Seastate input data |
| dyninpdemo08 | Modal analysis input data |
| dyrinpdemo08 | Earthquake analysis input data |
| wvrinpdemo08 | Wave response input data |
| saclstdemo08.std | Output listing for static analysis run |
| dynlstdemo08.std | Output listing for modal analysis run |
| eqklstdemo08.std | Output listing for earthquake analysis |
| wvrlstdemo08.std | Output listing for wave response run |
| demo08.runx | SACS multi-file run file (runs entire demo8) |
| staticdemo08.runx | Static analysis run file |
| dynpacdemo08.runx | Modal analysis run file |
| earthquakedemo08.runx | Earthquake analysis run file |
| wave responsedemo08.runx | Wave response run file |





| Demo 9. Basic Marine Add-On | Demo 9. Basic Marine Add-On |
| --- | --- |
| sacinpdemo09 | SACS IV data |
| gapinpdemo09 | Gap analysis input data |
| towinpdemo09 | Tow analysis input data |
| gaplstdemo09.std | Output listing for Gap analysis run |
| towlstdemo09.std | Output listing for Tow analysis run |
| demo09.runx | SACS multi-file run file (runs entire demo 9) |
| gapdemo09.runx | Gap analysis run file |
| towdemo09.runx | Tow analysis run file |
| Demo 10. Marine Installation Add-On | Demo 10. Marine Installation Add-On |
| sacinpdemo10 | SACS IV data |
| fltinpdemo10 | Flotation/upending input data |
| Inhinpdemo10 | Launch analysis input data |
| fltlstdemo10.std | Output listing for flotation/upending run |
| Inhlstdemo10.std | Output listing for Launch analysis run |
| demo10.runx | SACS multi-file run file (runs entire demo 10) |
| flotationdemo10.runx | Flotation/upending run file |
| launchdemo10.runx | Launch analysis run file |





| Demo 11. Advanced Marine Transport Add-On | Demo 11. Advanced Marine Transport Add-On |
| --- | --- |
| sacinpdemo11 | SACS IV data |
| fltinpdemo11 | Flotation/upending input data |
| Inhinpdemo11 | Launch analysis input data |
| gapinpdemo11 | Gap analysis input data |
| towinpdemo11 | Tow analysis input data |
| fltlstdemo11.std | Output listing for flotation upending run |
| Inhlstdemo11.std | Output listing for Launch analysis run |
| gaplstdemo11.std | Output listing for Gap analysis run |
| towlstdemo11.std | Output listing for Tow analysis run |
| demo11.runx | SACS multi-file run file (runs entire demo 11) |
| flotationdemo11.runx | Flotation/upending run file |
| launchdemo11.runx | Launch analysis run file |
| gapdemo11.runx | Gap analysis run file |
| towdemo11.runx | Tow analysis run file |
| Demo 12. Miscellaneous | Demo 12. Miscellaneous |
| sacinp.mtodemo12 | SACS IV data for Material Take-Off analysis |
| mtoinpdemo12 | Material Take-Off data |
| mtolstdemo12.std | Output listing for material take-off |
| demo12.runx | SACS multi-file run file (runs entire demo 12) |
| mtodemo12.runx | Material Take-Off run file |

