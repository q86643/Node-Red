[
     {
         "id": "9f188f9e.d5b82",
         "type": "tab",
         "label": "Flow 1"
     },
     {
         "id": "4403c19b.523d8",
         "type": "tab",
         "label": "Flow 2"
     },
     {
         "id": "79627a2c.5c8d74",
         "type": "tab",
         "label": "Flow 3"
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
     },
     {
         "id": "57a0c7c4.696038",
         "type": "inject",
         "z": "4403c19b.523d8",
         "name": "",
         "topic": "",
         "payload": "",
         "payloadType": "date",
         "repeat": "5",
         "crontab": "",
         "once": true,
         "x": 110,
         "y": 100,
         "wires": [
             [
                 "90a730f4.5ea99",
                 "a44e1a5a.fb3178"
             ]
         ]
     },
     {
         "id": "90a730f4.5ea99",
         "type": "function",
         "z": "4403c19b.523d8",
         "name": "Payload",
         "func": "msg.headers={\n    deviceKey: \"bFjTuQaVO6LYaGil\"\n    };\n\nreturn msg;",
         "outputs": 1,
         "noerr": 0,
         "x": 280,
         "y": 100,
         "wires": [
             [
                 "84f03d85.dc86c"
             ]
         ]
     },
     {
         "id": "84f03d85.dc86c",
         "type": "http request",
         "z": "4403c19b.523d8",
         "name": "",
         "method": "GET",
         "ret": "txt",
         "url": "http://api.mediatek.com/mcs/v2/devices/DpcaDo6Z/datachannels/Temperature/datapoints.csv",
         "tls": "",
         "x": 450,
         "y": 100,
         "wires": [
             [
                 "8363290f.8f6b58",
                 "9a5ed89.e2e7628"
             ]
         ]
     },
     {
         "id": "8363290f.8f6b58",
         "type": "http response",
         "z": "4403c19b.523d8",
         "name": "",
         "statusCode": "",
         "headers": {},
         "x": 650,
         "y": 100,
         "wires": []
     },
     {
         "id": "9a5ed89.e2e7628",
         "type": "debug",
         "z": "4403c19b.523d8",
         "name": "",
         "active": true,
         "console": "false",
         "complete": "payload",
         "x": 710,
         "y": 200,
         "wires": []
     },
     {
         "id": "a44e1a5a.fb3178",
         "type": "function",
         "z": "4403c19b.523d8",
         "name": "Payload",
         "func": "msg.headers={\n    deviceKey: \"bFjTuQaVO6LYaGil\"\n    };\n\nreturn msg;",
         "outputs": 1,
         "noerr": 0,
         "x": 280,
         "y": 180,
         "wires": [
             [
                 "95f95a25.8f3b08"
             ]
         ]
     },
     {
         "id": "95f95a25.8f3b08",
         "type": "http request",
         "z": "4403c19b.523d8",
         "name": "",
         "method": "GET",
         "ret": "txt",
         "url": "http://api.mediatek.com/mcs/v2/devices/DpcaDo6Z/datachannels/Humidity/datapoints.csv",
         "tls": "",
         "x": 450,
         "y": 180,
         "wires": [
             [
                 "8363290f.8f6b58",
                 "9a5ed89.e2e7628"
             ]
         ]
     }
 ]
