import QtQuick 1.1

Item {
    id: button
    property alias ba_text: b_text.text

    Rectangle {
        signal action_command

        width: 85
        height: 50
        color: "#111"
        radius: 9
        Text {
            id: b_text
            anchors.centerIn: parent
            color: "#fff"
            font.bold: true
        }
        MouseArea {
            anchors.fill: parent
            onClicked: {action_command();}
        }
    }
}
