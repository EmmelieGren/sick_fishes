import QtQuick
import QtQuick.Controls.Basic
import QtQuick.Controls

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
            id: exitButton
            text: "Exit"
            background: Rectangle {
                implicitWidth: 100
                implicitHeight: 40
                border.color: "#26282a"
                border.width: 1
                radius: 8
                color: exitButton.down ? "#d6d6d6" : "#f6f6f6"
            }            
            anchors.bottom: parent.bottom
            anchors.bottomMargin: 10
            anchors.left: parent.left
            anchors.leftMargin: 230

            onClicked: Qt.quit()
        }
    }
    Item {
        width: 640
        height: 480
        Button {
            id: importButton
            text: "Import image"
            background: Rectangle {
                implicitWidth: 100
                implicitHeight: 40
                border.color: "#26282a"
                border.width: 1
                radius: 8
                color: importButton.down ? "#d6d6d6" : "#f6f6f6"
            }
            anchors.bottom: parent.bottom
            anchors.bottomMargin: 10
            anchors.left: parent.left
            anchors.leftMargin: 70
            
            onClicked: backend.importPNG()
        }
    }
    
}