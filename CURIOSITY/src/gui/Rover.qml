import QtQuick 1.1

Rectangle {
    signal connection
    signal disconnection

    width: 450
    height: 250
    color: "#222"

    Connection {
        x: 0
        y: 0
        c_color: "#222"
        c_text: "Joystick"
        i_color: "#111"
        c_title_text: joystick
    }

    Connection {
        x: 0
        y: 90
        c_color: "#222"
        c_text: "Bluetooth"
        i_color: "#111"
        c_title_text: bluetooth
    }

    Text {
        x: 320
        y: 10
        width: 50
        height: 20
        text: "Speed"
        font.bold: true
        font.pointSize: 13
        color: "#fff"
    }

    Dial {
        id: dial
        x: 240
        y: 40
        value: speed
    }

    Rectangle {
        x: 10
        y: 190
        width: 85
        height: 50
        color: "#111"
        radius: 9
        Text {
            text: "Connect"
            color: "#fff"
            font.bold: true
            anchors.centerIn: parent
        }
        MouseArea {
            anchors.fill: parent
            onClicked: connection()
        }
    }

    Rectangle {
        x: 135
        y: 190
        width: 85
        height: 50
        color: "#111"
        radius: 9
        Text {
            text: "DiConnect"
            color: "#fff"
            font.bold: true
            anchors.centerIn: parent
        }
        MouseArea {
            anchors.fill: parent
            onClicked: disconnection()
        }
    }

}
