[
    {
        "id": "9f188f9e.d5b82",
        "type": "tab",
        "label": "Flow 1"
    },
    {
        "id": "b884c6dc.cf2a18",
        "type": "rpi-gpio in",
        "z": "9f188f9e.d5b82",
        "name": "Button",
        "pin": "7",
        "intype": "up",
        "debounce": "25",
        "read": true,
        "x": 90,
        "y": 180,
        "wires": [
            [
                "856f630d.50815",
                "d69f7f06.4fc1a"
            ]
        ]
    },
    {
        "id": "856f630d.50815",
        "type": "debug",
        "z": "9f188f9e.d5b82",
        "name": "",
        "active": true,
        "console": "false",
        "complete": "false",
        "x": 430,
        "y": 160,
        "wires": []
    },
    {
        "id": "5619b6ca.9c21c8",
        "type": "rpi-gpio out",
        "z": "9f188f9e.d5b82",
        "name": "LED",
        "pin": "11",
        "set": true,
        "level": "0",
        "freq": "",
        "out": "out",
        "x": 450,
        "y": 240,
        "wires": []
    },
    {
        "id": "d69f7f06.4fc1a",
        "type": "switch",
        "z": "9f188f9e.d5b82",
        "name": "if input is 1",
        "property": "payload",
        "propertyType": "msg",
        "rules": [
            {
                "t": "eq",
                "v": "1",
                "vt": "str"
            },
            {
                "t": "else"
            }
        ],
        "checkall": "true",
        "outputs": 2,
        "x": 150,
        "y": 260,
        "wires": [
            [
                "2edf8f00.a5e302"
            ],
            [
                "99176b72.b2dff8"
            ]
        ]
    },
    {
        "id": "2edf8f00.a5e302",
        "type": "change",
        "z": "9f188f9e.d5b82",
        "name": "Change to 0",
        "rules": [
            {
                "t": "set",
                "p": "payload",
                "pt": "msg",
                "to": "0",
                "tot": "str"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 310,
        "y": 320,
        "wires": [
            [
                "5619b6ca.9c21c8"
            ]
        ]
    },
    {
        "id": "99176b72.b2dff8",
        "type": "change",
        "z": "9f188f9e.d5b82",
        "name": "Change to 1",
        "rules": [
            {
                "t": "set",
                "p": "payload",
                "pt": "msg",
                "to": "1",
                "tot": "str"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 310,
        "y": 220,
        "wires": [
            [
                "5619b6ca.9c21c8"
            ]
        ]
    }
]
