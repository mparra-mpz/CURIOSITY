import QtQuick 2.2
import QtQuick.Controls 1.2

Rectangle {
    width: 450
    height: 250
    color: "#222"

    Connection {
        x: 0
        y: 0
        c_color: "#222"
        c_text: "Joystick"
        c_list: ["Genius® Joystick Metal Strike 3D", "Genius® Gamepad PS3 / PC Max Fire Blaze 3", "Joystick Nintendo", "Joystick Atari"]
    }

    Connection {
        x: 0
        y: 90
        c_color: "#222"
        c_text: "Bluetooth"
        c_list: ["CURIOSITY", "DISCOVERY", "MARS POLAR LANDER", "VOYAGER"]
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
        value: 50
    }

    ButtonAdapt {
        x: 10
        y: 190
        ba_text: "Connect"
    }

    ButtonAdapt {
        x: 135
        y: 190
        ba_text: "Disconnect"
    }
}
