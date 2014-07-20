import QtQuick 1.1

Item {
    id: connection
    property alias c_color: c_rectangle.color
    property alias c_text: c_title.text
    property alias c_list_model: c_list.model

    Rectangle {
        id: c_rectangle
        width: 210
        height: 70

        Text {
            id: c_title
            x: 10
            y: 10
            width: 50
            height: 20
            font.bold: true
            font.pointSize: 13
            color: "#fff"
        }
        ListView {
            id: c_list
            x: 10
            y: 40
            width: 210
            height: 30
            delegate: Component {
                Rectangle {
                    width: 210
                    height: 30
                    color: "#111"
                    clip: true
                    Text {
                        id: title
                        text: c_list_model[0]
                        elide: Text.ElideRight
                        color: "white"
                        font.bold: true
                        font.pointSize: 9
                        anchors.leftMargin: 10
                        anchors.fill: parent
                        verticalAlignment: Text.AlignVCenter
                    }
                    MouseArea {
                        anchors.fill: parent
                        onClicked: console.log(c_list_model[0])
                    }
                }
            }
        }
    }
}
