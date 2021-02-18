designFile = "D:/github/KeetV2HW/PDNAnalyzer_Output/PowerSupplyV2/odb.tgz"

powerNets = ["+12", "V12V", "V5V", "NetD3_2", "OBDV5V", "V4V", "V3V3", "V5-SHIFT"]

groundNets = ["GND"]

excitation = [
{
"id": "0",
"type": "load",
"power_pins": [ ("R3", "2") ],
"ground_pins": [ ("R5", "1") ],
"current": 0.0001,
"Rpin": 1000,
}
,
{
"id": "1",
"type": "source",
"power_pins": [ ("Conn1", "16") ],
"ground_pins": [ ("Conn1", "4") ],
"voltage": 12,
"Rpin": 0,
}
,
{
"id": "2",
"type": "load",
"power_pins": [ ("R2", "2") ],
"ground_pins": [ ("R6", "1") ],
"resistance": 1E-09,
"Rpin": 55400,
}
,
{
"id": "3",
"type": "load",
"power_pins": [ ("IC3", "1"), ("IC3", "2") ],
"ground_pins": [ ("IC3", "6") ],
"current": 0.0015,
"Rpin": 88.8888888888889,
}
,
{
"id": "4",
"type": "load",
"power_pins": [ ("IC7", "3") ],
"ground_pins": [ ("IC7", "2") ],
"current": 0.07,
"Rpin": 1.42857142857143,
}
,
{
"id": "5",
"type": "load",
"power_pins": [ ("U1", "3") ],
"ground_pins": [ ("U1", "5") ],
"current": 0.0003,
"Rpin": 333.333333333333,
}
,
{
"id": "6",
"type": "load",
"power_pins": [ ("R26", "2") ],
"ground_pins": [ ("Q6", "2") ],
"resistance": 1E-09,
"Rpin": 1650,
}
,
{
"id": "7",
"type": "load",
"power_pins": [ ("IC5", "38"), ("IC5", "29"), ("IC5", "27"), ("IC5", "17"), ("IC5", "5") ],
"ground_pins": [ ("IC5", "39"), ("IC5", "28"), ("IC5", "18"), ("IC5", "6") ],
"current": 0.012,
"Rpin": 37.037037037037,
}
,
{
"id": "8",
"type": "load",
"power_pins": [ ("IC6", "42"), ("IC6", "39"), ("IC6", "27"), ("IC6", "16"), ("IC6", "14"), ("IC6", "10") ],
"ground_pins": [ ("IC6", "41"), ("IC6", "40"), ("IC6", "20"), ("IC6", "17"), ("IC6", "11") ],
"current": 0.6,
"Rpin": 0.909090909090909,
}
,
{
"id": "9",
"type": "load",
"power_pins": [ ("IC10", "8") ],
"ground_pins": [ ("IC10", "4") ],
"current": 0.002,
"Rpin": 50,
}
,
{
"id": "10",
"type": "load",
"power_pins": [ ("IC4", "6") ],
"ground_pins": [ ("IC4", "3") ],
"current": 0.0001,
"Rpin": 1000,
}
,
{
"id": "11",
"type": "load",
"power_pins": [ ("IC8", "3") ],
"ground_pins": [ ("IC8", "1") ],
"current": 0.0001,
"Rpin": 1000,
}
,
{
"id": "12",
"type": "load",
"power_pins": [ ("IC9", "2") ],
"ground_pins": [ ("R37", "1") ],
"current": 0.0001,
"Rpin": 1000,
}
,
{
"id": "13",
"type": "source",
"power_pins": [ ("L1", "2") ],
"ground_pins": [ ("IC1", "7"), ("IC1", "12") ],
"voltage": 5,
"Rpin": 0,
}
,
{
"id": "14",
"type": "load",
"power_pins": [ ("IC1", "9"), ("IC1", "10") ],
"ground_pins": [ ("IC1", "7"), ("IC1", "12") ],
"current": 0.336114560126305,
"Rpin": 0.595035216340655,
}
]


voltage_regulators = [
{
"id": "15",
"type": "linear",

"in": [ ("IC4", "6") ],
"out": [ ("IC4", "1") ],
"ref": [ ("IC4", "3") ],

"v2": -1.6935299898,
"i1": 4E-05,
"Ro": 0,
"Rpin": 0,
}
,
{
"id": "16",
"type": "linear",

"in": [ ("IC8", "3") ],
"out": [ ("IC8", "2") ],
"ref": [ ("IC8", "1") ],

"v2": -1.3552958774,
"i1": 6.5E-05,
"Ro": 0,
"Rpin": 0,
}
,
{
"id": "17",
"type": "linear",

"in": [ ("IC9", "2") ],
"out": [ ("IC9", "1") ],
"ref": [ ("R37", "1") ],

"v2": -8.697605215,
"i1": 0,
"Ro": 0,
"Rpin": 0,
}
,
{
"id": "18",
"type": "linear",

"in": [ ("M1", "3") ],
"out": [ ("M1", "2") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 5E-07,
}
,
{
"id": "19",
"type": "linear",

"in": [ ("M3", "2") ],
"out": [ ("M3", "3") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 5E-07,
}
,
{
"id": "20",
"type": "linear",

"in": [ ("D3", "2") ],
"out": [ ("R42", "2") ],
"ref": [],

"v2": -0.3,
"i1": 0,
"Ro": 1E-06,
"Rpin": 5E-07,
}
]


# Resistors / Inductors

passives = []


# Material Properties:

tech = [

        {'name': 'TOP_SOLDER', 'DielectricConstant': 3.5, 'Thickness': 1.016E-05},
        {'name': 'TOP_LAYER', 'Conductivity': 47000000, 'Thickness': 3.556E-05},
        {'name': 'SUBSTRATE-1', 'DielectricConstant': 4.8, 'Thickness': 0.0009},
        {'name': 'BOTTOM_LAYER', 'Conductivity': 47000000, 'Thickness': 3.556E-05},
        {'name': 'BOTTOM_SOLDER', 'DielectricConstant': 3.5, 'Thickness': 1.016E-05}

       ]

special_settings = {'removecutoutsize' : 7.8 }


plating_thickness = 0.7
finished_hole_diameters = False
