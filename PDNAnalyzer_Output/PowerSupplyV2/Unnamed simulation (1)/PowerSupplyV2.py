designFile = "D:/github/KeetV2HW/PDNAnalyzer_Output/PowerSupplyV2/odb.tgz"

powerNets = ["+12"]

groundNets = ["GND"]

excitation = [
{
"id": "0",
"type": "source",
"power_pins": [ ("Conn1", "16") ],
"ground_pins": [ ("Conn1", "4") ],
"voltage": 12,
"Rpin": 5,
}
,
{
"id": "1",
"type": "load",
"power_pins": [ ("M1", "3") ],
"ground_pins": [ ("Conn1", "4") ],
"current": 0.0001,
"Rpin": 1000,
}
]


voltage_regulators = []


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
