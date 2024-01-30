import QtQuick
import QtQuick.Controls.Basic
ApplicationWindow {
    visible: true
    width: 400
    height: 600
    title: "Sick_Fishes"
    flags: Qt.FramelessWindowHint
    
    property string currTime: "00:00:00"
    property QtObject backend
    Rectangle {
        anchors.fill: parent
        Image {
            sourceSize.width: parent.width
            sourceSize.height: parent.height
            source: "./images/fish2.png"
            fillMode: Image.PreserveAspectCrop
        }
        Connections {
         target: backend
        function onUpdated(msg) {
        currTime = msg;
        }
        }
        Rectangle {
            anchors.fill: parent
            color: "transparent"
            Text {
                anchors {
                    bottom: parent.bottom
                    bottomMargin: 12
                    left: parent.left
                    leftMargin: 12
                }
                text: currTime
                font.pixelSize: 48
                color: "white"
            }
        }
    }
        Item {
        width: 640
        height: 480
        Button {
            text: "Import PNG"
            anchors.bottom: parent.bottom
            anchors.bottomMargin: 10
            anchors.horizontalCenter: parent.horizontalCenter
            onClicked: backend.importPNG()
        }
    }
    Item {
        width: 640
        height: 480
        Button {
            text: "Exit"
            anchors.bottom: parent.bottom
            anchors.bottomMargin: 10
            anchors.left: parent.left
            anchors.leftMargin: 30
            onClicked: Qt.quit()
        }
    }

}