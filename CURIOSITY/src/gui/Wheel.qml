import QtQuick 1.1

Item {
    id: root
    property real value : 0

    width: 250; height: 250

    Image {
        id: wheel
        x: 0; y: 46
        smooth: true
        source: "img/wheel.png"
        transform: Rotation {
            id: wheelRotation
            origin.x: 125; origin.y: 79
            angle: root.value
            Behavior on angle {
                SpringAnimation {
                    spring: 1.4
                    damping: .15
                }
            }
        }
    }
}
