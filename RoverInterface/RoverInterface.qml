import QtQuick 1.0

Rectangle {
    width: 700
    height: 350
    Text {
        x: 30
        y: 10
        width: 50
        height: 20
        text: "Joystick"
        font.bold: true
        font.pointSize: 13
    }
    ListView {
        id: list_joystick
        x: 30
        y: 40
        width: 300
        height: 120
        delegate: Component {
            Rectangle {
                width: 300
                height: 40
                color: ((index % 2 == 0)?"#222":"#111")
                Text {
                    id: title
                    elide: Text.ElideRight
                    text: name
                    color: "white"
                    font.bold: true
                    font.pointSize: 9
                    anchors.leftMargin: 10
                    anchors.fill: parent
                    verticalAlignment: Text.AlignVCenter
                }
                MouseArea {
                    anchors.fill: parent
                    onClicked: console.log(name)
                }
            }
        }
        model: ListModel {
            ListElement {
                name: "Genius® Joystick Metal Strike 3D"
            }

            ListElement {
                name: "Genius® Gamepad PS3 / PC Max Fire Blaze 3"
            }

            ListElement {
                name: "Joystick Nintendo"
            }

            ListElement {
                name: "Joystick Atari"
            }
        }
    }
    Text {
        x: 30
        y: 190
        width: 70
        height: 20
        text: "Bluetooth"
        font.bold: true
        font.pointSize: 13
    }
    ListView {
        id: list_bluetooth
        x: 30
        y: 220
        width: 300
        height: 120
        delegate: Component {
            Rectangle {
                width: 300
                height: 40
                color: ((index % 2 == 0)?"#222":"#111")
                Text {
                    id: title
                    elide: Text.ElideRight
                    text: name
                    color: "white"
                    font.bold: true
                    font.pointSize: 9
                    anchors.leftMargin: 10
                    anchors.fill: parent
                    verticalAlignment: Text.AlignVCenter
                }
                MouseArea {
                    anchors.fill: parent
                    onClicked: console.log(name)
                }
            }
        }
        model: ListModel {
            ListElement {
                name: "CURIOSITY"
            }

            ListElement {
                name: "DISCOVERY"
            }

            ListElement {
                name: "MARS POLAR LANDER"
            }

            ListElement {
                name: "VOYAGER"
            }
        }
    }
    Text {
        x: 475
        y: 10
        width: 50
        height: 20
        text: "Speed"
        font.bold: true
        font.pointSize: 13
    }
    Dial {
        id: dial
        x: 400
        y: 75
        //anchors.centerIn: parent
        value: slider.x * 100 / (container.width - 34)
    }
}
