import QtQuick 1.1

Item {
    id: connection
    property alias c_color: c_rectangle.color
    property alias c_text: c_title.text
    property alias i_color: i_rectangle.color
    property alias c_title_text: title.text

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

        Rectangle {
            id: i_rectangle
            x: 10
            y: 40
            width: 210
            height: 30
            color: c_color
            radius: 5
            Text {
                id: title
                elide: Text.ElideRight
                color: "white"
                font.bold: true
                font.pointSize: 9
                anchors.fill: parent
                anchors.leftMargin: 10
                verticalAlignment: Text.AlignVCenter
            }
        }
    }
}
