designFile = "D:/github/KeetV2HW/PDNAnalyzer_Output/PowerSupplyV2/odb.tgz"

powerNets = ["+12", "V12V", "V5V", "NetD3_2", "OBDV5V", "V4V"]

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
"power_pins": [ ("IC5", "38"), ("IC5", "29"), ("IC5", "27"), ("IC5", "17"), ("IC5", "5") ],
"ground_pins": [ ("IC5", "39"), ("IC5", "28"), ("IC5", "18"), ("IC5", "6") ],
"current": 0.012,
"Rpin": 37.037037037037,
}
,
{
"id": "5",
"type": "load",
"power_pins": [ ("IC4", "6") ],
"ground_pins": [ ("IC4", "3") ],
"current": 0.0001,
"Rpin": 1000,
}
,
{
"id": "6",
"type": "source",
"power_pins": [ ("L1", "2") ],
"ground_pins": [ ("IC1", "7"), ("IC1", "12") ],
"voltage": 5,
"Rpin": 0,
}
,
{
"id": "7",
"type": "load",
"power_pins": [ ("IC1", "9"), ("IC1", "10") ],
"ground_pins": [ ("IC1", "7"), ("IC1", "12") ],
"current": 0.00669216646123586,
"Rpin": 29.8856881636901,
}
]


voltage_regulators = [
{
"id": "8",
"type": "linear",

"in": [ ("IC4", "6") ],
"out": [ ("IC4", "1") ],
"ref": [ ("IC4", "3") ],

"v2": -1.700780147,
"i1": 4E-05,
"Ro": 0,
"Rpin": 0,
}
,
{
"id": "9",
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
"id": "10",
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
"id": "11",
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
