'''
stopwatch.py
12/19/2017
GUI to allow researcher to edit eye tracker footage while overseeing
participant
Emerson Wenzel


usage: call this program in the command line via python
       (i.e. type "python stopwatch.py") while in the same folder
       or if the file can be located with file explorer / is on the
       desktop, "open" it with python.
'''


from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
        QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
        QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
                             QVBoxLayout, QWidget, QFileDialog)
import sys
import time
import os.path
from msvcrt import getch
import moviepy.editor as mpy



CONST_ADDITION_TO_NAME = "edited"

class Stopwatch(QDialog):

    def __init__(self):
        super().__init__()
        self.title = 'Clean Eye Tracker Data'
        self.left = 100
        self.top = 100
        self.width = 400
        self.height = 300
        self.initUI()


    def start_time_sec(self):
        print('start_time_sec called.')
        self.start_time_sec_button.setEnabled(False)
        self.end_time_sec_button.setEnabled(True)
        
        #Get the new time stamp
        new_start_time = time.clock()
        self.timeArray.append(new_start_time)

        #Write the new time stamp to the UI
        text = self.time_stamp_label.text()      
        text = text + str(new_start_time)[0:5] + '\t\t   '
        self.time_stamp_label.setText(text)
        
    def end_time_sec(self):
        print('end_time_sec called.')
        self.start_time_sec_button.setEnabled(True)
        self.end_time_sec_button.setEnabled(False)

        #Get the new time stamp
        new_end_time = time.clock()
        self.timeArray.append(new_end_time)

        #Write the new time stamp to the UI
        text = self.time_stamp_label.text()
        text = text + str(new_end_time)[0:5] + '\n\t   '
        self.time_stamp_label.setText(text)

        
    def start_timer(self):
        print('start_timer called.')
        #Begin the timer
        self.timeStart = time.clock()


        #If this is the first time the button is hit
        #(i.e. starting timer), change it to red
        if (self.start_timer_button.text() == 'Start Timer'):
            self.start_timer_button.setText('Stop Timing')
            self.start_timer_button.setStyleSheet('QPushButton '\
                                                  '{background-color: red;}')
            self.start_time_sec_button.setEnabled(True)
            
        #if this is the second time it is being hit
        #(i.e. end of timer, grey out all buttons)
        else:
            print('second hit')
            
            #If they forgot to end the last time section, add one more)
            if (len(self.timeArray) % 2 == 1):
                #self.timeArray.append(time.clock())
                self.end_time_sec()
                
            print(self.timeArray)
            self.start_time_sec_button.setEnabled(False)
            self.end_time_sec_button.setEnabled(False)
            self.start_timer_button.setEnabled(False)
            self.select_file_button.setEnabled(True)


    def select_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,'QFileDialog.getOpenFileName()')
        if fileName:
            print(fileName)

            for i in list(range(len(fileName))):
                b_index = (len(fileName) - 1) - i
                if (fileName[b_index] == '/' or fileName[b_index] == '\\'):
                    self.AVI_file_dir = fileName[0:b_index+1]
                    self.AVI_file_name = fileName[b_index+1:len(fileName)]
                    break
            
            text = self.file_location_label.text()[0:11]
            self.file_location_label.setText(text + fileName)
            self.make_new_avi_button.setEnabled(True)


    def make_new_avi(self):
        if (self.make_new_avi_button.text() == 'Make New AVI'):
            videoClips = []
            for startIndex in list(range(int(len(self.timeArray)/2))):
                try:
                    videoClips.append(mpy.VideoFileClip(self.AVI_file_dir + self.AVI_file_name)\
                                      .subclip(self.timeArray[startIndex*2],self.timeArray[startIndex*2 + 1]))
                    print('concatenating files')
                except:
                    error_msg = 'time sections selected did not fit chosen video'
                    self.info_label.setText(error_msg)
                    print(error_msg)
                    break

            try:
                self.info_label.setText('Please wait while your video is being created')
                finalClip = mpy.concatenate_videoclips(videoClips, method='compose')
                finalClip.write_videofile(self.AVI_file_dir + CONST_ADDITION_TO_NAME + self.AVI_file_name, codec = 'libx264')
                self.info_label.setText('video completed!')
            except:
                error_msg = 'error trying to create new file'
                self.info_label.setText(error_msg)
                print(error_msg)

            self.make_new_avi_button.setText('Close Program')

        else:
            exit()
            '''
            self.time_stamp_label.setText('\tStart of Section:\tEnd of Section:\n\n\t   ')
            self.make_new_avi_button.setText('Make New AVI')
            self.info_label.setText('')
            self.timeArray = []
            self.AVI_file_dir = ''
            self.AVI_file_name = ''
            self.file_location_label.setText(	self.file_location_label.text()[0:11])
            self.start_timer_button.setText('Start Timer')
            self.start_timer_button.setStyleSheet('')
            self.start_time_sec_button.setEnabled(False)
            self.end_time_sec_button.setEnabled(False)
            self.start_timer_button.setEnabled(True)
            self.select_file_button.setEnabled(False)
            self.make_new_avi_button.setEnabled(False)
            '''
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        
        self.timeArray = []
        self.timeStart = 0

        self.create_layout()
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.main_box)
        self.setLayout(windowLayout)


        

    def create_layout(self):
        self.main_box = QGroupBox("")
        layout = QHBoxLayout()
        column_one = QVBoxLayout()
        column_two = QVBoxLayout()

        self.start_timer_button=QPushButton("Start Timer", self)
        self.start_timer_button.clicked.connect(self.start_timer)
        self.start_timer_button.resize(175,80)

        self.start_time_sec_button=QPushButton("Start Cut", self)
        self.start_time_sec_button.clicked.connect(self.start_time_sec)
        self.start_time_sec_button.setEnabled(False)
            
        self.end_time_sec_button=QPushButton("End Cut", self)
        self.end_time_sec_button.clicked.connect(self.end_time_sec)
        self.end_time_sec_button.setEnabled(False)
             
        self.time_stamp_label = QLabel('\tStart of Section:\tEnd of Section:\n\n\t   ', self)
        self.time_stamp_label.resize(200,200)


        self.file_location_label = QLabel('AVI FILE : ')

        self.select_file_button = QPushButton('Select file', self)
        self.select_file_button.clicked.connect(self.select_file)
        self.select_file_button.setEnabled(False)
        

        self.make_new_avi_button = QPushButton('Make New AVI', self)
        self.make_new_avi_button.clicked.connect(self.make_new_avi)
        self.make_new_avi_button.setEnabled(False)

        self.info_label = QLabel('')
        
        column_one.addWidget(self.file_location_label)
        column_one.addWidget(self.select_file_button)

        column_one.addStretch()

        column_one.addWidget(self.info_label)
        column_one.addStretch()
        
        start_stop_box = QHBoxLayout()        
        start_stop_box.addWidget(self.start_time_sec_button)
        start_stop_box.addWidget(self.end_time_sec_button)

        
        column_one.addLayout(start_stop_box)
        column_one.addWidget(self.start_timer_button)
        column_one.addWidget(self.make_new_avi_button)

        
        column_two.addWidget(self.time_stamp_label)
        column_two.addStretch()
        
        layout.addLayout(column_one)
        layout.addLayout(column_two)
        self.main_box.setLayout(layout)



 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    stopwatch = Stopwatch()
sys.exit(stopwatch.exec_())


