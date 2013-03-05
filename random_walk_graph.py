import sys, os, random
import PyQt4.QtCore 
import PyQt4.QtGui 
import matplotlib
from matplotlib import pyplot 
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar
from matplotlib.figure import Figure
from matplotlib.ticker import FormatStrFormatter
from conf_info import ConfInfo
from copy import deepcopy
import numpy as np

class StatisticGraph(PyQt4.QtGui.QWidget):
    def __init__(self, parent=None):
        self.parent = parent
        PyQt4.QtGui.QWidget.__init__(self, self.parent)
        self.create_main_frame()
        self.text_font = matplotlib.font_manager.FontProperties(size=8)
        # 0 means the only one dimension calculation
        # 1 means two dimensional calculation
        self.dimension = 0

        self.answer_set =  []
        self.answer_map =  {}
    def set_dimension(self, value):
        self.dimension = value

    def plot_graph(self, conf_info):
        self.conf_info = conf_info
        if(self.dimension == 0):
            if(conf_info.check_valid()):
                self.one_d_draw()
                return self.answer_map
        elif(self.dimension == 1):
            if(conf_info.check_valid()):
                self.two_d_draw()
                return self.answer_map
        
    def clear_graph(self):
        self.axes.clear()  
        self.clear_data()
        self.canvas.draw()
        
    def clear_data(self):
        self.answer_set = []
        self.answer_map =  {}
    def two_d_draw(self):
        self.clear_data()
        self.axes.clear()     
        
        #self.axes.grid(self.grid_cb.isChecked())
 #       self.axes.xaxis.set_major_formatter(FormatStrFormatter('%0.0f'))
 #       self.axes.set_axes([0, 100, 0, 100])
#        self.axes.set_ylim((0, 100))
        repeat_time = self.conf_info.repeat_time
        initial_state = self.conf_info.initial_state
        number_of_walkers = self.conf_info.random_walk_number
        upper_range = self.conf_info.upper_range
        lower_range = self.conf_info.lower_range
        range_of_walk = range(repeat_time+1)
        self.axes.plot(self.one_d_walk("x", repeat_time, initial_state, upper_range , lower_range ), self.one_d_walk("y", repeat_time, initial_state, upper_range , lower_range ))
        for i in range(int(number_of_walkers)-1):
            self.axes.plot(self.one_d_walk("x", repeat_time, initial_state, upper_range , lower_range ), self.one_d_walk("y", repeat_time, initial_state, upper_range , lower_range ))
        self.canvas.draw()
    def one_d_walk(self,name,  T=10, initial_state=1, upper_range = 1, lower_range = 1):
        """random one_d_walk with a fair coin"""
        x=initial_state;     answer= [x]
        for t in xrange(T):
            u = random.uniform(lower_range, upper_range)
            x+= u
            if (t%1 == 0 ) :
                answer.append(x )
        self.answer_set.append(answer)
        self.answer_map[name] = deepcopy(self.answer_set)
        return answer
    def one_d_draw(self):
        
        self.axes.clear()     
        self.answer_set = []   
        #self.axes.grid(self.grid_cb.isChecked())
 #       self.axes.xaxis.set_major_formatter(FormatStrFormatter('%0.0f'))
 #       self.axes.set_axes([0, 100, 0, 100])
#        self.axes.set_ylim((0, 100))
        repeat_time = self.conf_info.repeat_time
        initial_state = self.conf_info.initial_state
        number_of_walkers = self.conf_info.random_walk_number
        upper_range = self.conf_info.upper_range
        lower_range = self.conf_info.lower_range
        range_of_walk = range(repeat_time+1)
        self.axes.plot(range_of_walk, self.one_d_walk("y", repeat_time, initial_state, upper_range , lower_range ))
        for i in range(int(number_of_walkers)-1):
            self.axes.plot(range_of_walk, self.one_d_walk("y", repeat_time, initial_state, upper_range , lower_range ))
        print "enter one_d_draw"
        self.canvas.draw()
       
    def auto_label_lost_value(self, bars):
        # attach some text labels
        for i, bar in enumerate(bars):
            height = self.new_lost_height[i]
            self.axes.text(bar.get_x()-bar.get_width()/4.0, 0.9*height, '%d'%int(self.lost_frame[i]),
                    ha='center', va='bottom')
                    
    def auto_label_value(self, bars):
        # attach some text labels
        for i, bar in enumerate(bars):
            height = self.new_height[i]
            self.axes.text(bar.get_x()-bar.get_width()/4.0, 0.9*height, '%d'%int(self.total_frame[i]),
                    ha='center', va='bottom')
                    
    def label_percentage(self, bars):
        # attach some text labels
        for i, bar in enumerate(bars):
            height = self.new_height[i]
#            print self.percentage
#            print i, len(bars)
            # to ignore the disoder first serial times of reading 
            try:
                self.axes.text(bar.get_x()+bar.get_width()/2., 1.02*height, '%d'%height+'%',  #%self.percentage[i]
                    ha='center', va='bottom').set_fontproperties(self.text_font)   
            except:
                pass
                
    def create_main_frame(self):
        self.main_frame = PyQt4.QtGui.QWidget(self.parent)
        
        # Create the mpl Figure and FigCanvas objects. 
        # 5x4 inches, 100 dots-per-inch
        #dpi = dots per inch
        self.dpi = 100
        self.fig = Figure((6.7, 3.5), dpi=self.dpi)
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(self.main_frame)
        
        # Since we have only one plot, we can use add_axes 
        # instead of add_subplot, but then the subplot
        # configuration tool in the navigation toolbar wouldn't
        # work.
        #
        self.axes = self.fig.add_subplot(111)
        
        # Bind the 'pick' event for clicking on one of the bars
        #
#        self.canvas.mpl_connect('pick_event', self.on_pick)
        
        # Create the navigation toolbar, tied to the canvas
        #
        self.mpl_toolbar = NavigationToolbar(self.canvas, self.main_frame)
        
        # Other GUI controls
        # 
#        self.textbox = PyQt4.QtGui.QLineEdit()
#        self.textbox.setMinimumWidth(200)
#        #self.connect(self.textbox, PyQt4.QtCore.SIGNAL('editingFinished ()'), self.one_d_draw)
#        #self.connect(self.draw_button, PyQt4.QtCore.SIGNAL('clicked()'), self.one_d_draw)
#        
#        self.grid_cb = PyQt4.QtGui.QCheckBox("Show &Grid")
#        self.grid_cb.setChecked(False)
#        #self.connect(self.grid_cb, PyQt4.QtCore.SIGNAL('stateChanged(int)'), self.one_d_draw)
#        
#        slider_label = PyQt4.QtGui.QLabel('Bar width (%):')
#        self.slider = PyQt4.QtGui.QSlider(PyQt4.QtCore.Qt.Horizontal)
#        self.slider.setRange(1, 100)
#        self.slider.setValue(20)
#        self.slider.setTracking(True)
#        self.slider.setTickPosition(PyQt4.QtGui.QSlider.TicksBothSides)
#        #self.connect(self.slider, PyQt4.QtCore.SIGNAL('valueChanged(int)'), self.one_d_draw)
#        
#        #
#        # Layout with box sizers
#        # 
        hbox = PyQt4.QtGui.QHBoxLayout()
#        
#        for w in [ self.textbox, self.draw_button, self.grid_cb,
#                    slider_label, self.slider]:
#            hbox.addWidget(w)
#            hbox.setAlignment(w, PyQt4.QtCore.Qt.AlignVCenter)
#        
        vbox = PyQt4.QtGui.QVBoxLayout()
        vbox.addWidget(self.canvas)
        vbox.addWidget(self.mpl_toolbar)
        vbox.addLayout(hbox)
#        
        self.main_frame.setLayout(vbox)
#

