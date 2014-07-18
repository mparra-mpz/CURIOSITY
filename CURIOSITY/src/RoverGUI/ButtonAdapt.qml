import QtQuick 2.2
import QtQuick.Controls 1.2

Item {
    id: button
    property alias ba_text: b_text.text

    Rectangle {
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
            onClicked: console.log(b_text.text + " clicked")
        }
    }
}
