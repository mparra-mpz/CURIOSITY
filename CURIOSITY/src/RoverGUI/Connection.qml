import QtQuick 2.2
import QtQuick.Controls 1.2

Item {
    id: connection
    property alias c_color: c_rectangle.color
    property alias c_text: c_title.text
    property alias c_list: c_list.model

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

        ComboBox {
            id: c_list
            x: 10
            y: 40
            width: 210
            height: 30
            onCurrentIndexChanged: console.log(c_list.currentText)
        }
    }
}
