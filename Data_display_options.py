import time
import matplotlib
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from  Sensor_Data_absorber import  Get_Sensor_values_degital
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,FigureCanvasAgg
import PySimpleGUI as sg



def colorblind(size,color):
    if 6 <= size <= 7:
        c = color
    elif 5 <= size < 6:
        c = 'darkgreen'
    elif 4 <= size < 5:
        c = 'olive'
    elif 3 <= size < 4:
        c = 'gold'
    elif 2 <= size < 3:
        c = 'orange'
    elif 1 <= size < 2:
        c = 'orangered'
    elif 0 <= size < 1:
        c = 'tomato'
    elif  size < 0:
        c = 'red'
    else:
        c = color
    return (c)


def draw_figure(canvas, figure, loc=(0, 0)):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

def figure_draw_1(fig2,ax2,mean,fig_agg2,j,xax):
    ax2.cla()
    ax2.grid()
    ax2.plot(xax, mean, color='blue', label="average")
    ax2.set_xlabel("time")
    ax2.set_ylabel("sensor average")
    ax2.set_xlim(left=max(0, j - 50), right=j + 50)
    ax2.set_ylim(ymin=0, ymax=300)
    ax2.legend(loc="upper left")
    return (fig_agg2)


def square_maker(ax,fig_agg,center,size,color):
    rep,i,rep1,rep2,rep3,k,rep4,j=[],0,[0,0,0],[],[],0,[0,0,0],0
    while i < len(center) :
        rep.append(np.linspace(center[i] - size[i] / 2, center[i] + size[i] / 2, num=10))
        i+=1
    rep1[0], rep4[0] = np.meshgrid(rep[1], rep[2])
    rep1[1], rep4[1] = np.meshgrid(rep[0], rep[2])
    rep1[2], rep4[2] = np.meshgrid(rep[0], rep[1])
    while k < len(rep1):
        rep2.append(np.ones_like(rep1[k]) * (center[k] - size[k] / 2))
        rep3.append(np.ones_like(rep1[k]) * (center[k] + size[k] / 2))
        k+=1
    p = colorblind(size[0],color)
    ax.plot_wireframe(rep3[0], rep1[0], rep4[0], color=p, rstride=1, cstride=1, alpha=0.6)
    ax.plot_wireframe( rep1[1], rep2[1], rep4[1], color='gray', rstride=1, cstride=1, alpha=0.6)
    ax.plot_wireframe( rep1[1], rep3[1], rep4[1], color='gray', rstride=1, cstride=1, alpha=0.6)
    return (ax, fig_agg)




def make_cube_ulti_new_oof(ax,data, fig_agg):
    ses = 7
    list1 = [[(((7 - (data[4])) / 2) - (14 - ses)), 0, 0],
             [(((7 - (data[0])) / 2) - (14 - ses)), 7.5, 0],
             [(((7 - (data[5])) / 2) - (14 - ses)), 0, 7.5],
             [(((7 - (data[1])) / 2) - (14 - ses)), 7.5, 7.5],
             [(((7 - data[6]) / 2) - (14 - ses)), 0, 15],
             [(((7 - data[2]) / 2) - (14 - ses)), 7.5, 15],
             [(((7 - (data[7])) / 2) - (14 - ses)), 0, 22.5],
             [(((7 - (data[3])) / 2) - (14 - ses)), 7.5, 22.5]]
    list2 = [(7 - ((data[4])), 7.5, 7.5), (7 - (data[0]), 7.5, 7.5),
             (7 - (data[5]), 7.5, 7.5),(7 - (data[1]), 7.5, 7.5),
             (7 - (data[6]), 7.5, 7.5),(7 - (data[6]), 7.5, 7.5),
             (7 - (data[7]), 7.5, 7.5), (7 - (data[3]), 7.5, 7.5)]
    list3 = ['b', 'b', 'g', 'g', 'g', 'g', 'b', 'b']
    i = 0
    ax.cla()

    while i< len(list3):
         ax, fig_agg = square_maker(ax,fig_agg,list1[i],list2[i],list3[i])
         i+= 1
    ax.set_xlim(-15, 15)
    ax.set_zlim(000, 18)
    return(fig_agg)





def Liniar_display(PORT):
    layout = [[sg.Canvas(key='-CANVAS-2')]]
    gui = sg.Window(title="Live Feed figure", layout=layout, size=(1500, 900), finalize=True,
                    resizable=True, element_justification='c')
    gui.Maximize()
    canvas_elem2 = gui['-CANVAS-2']
    canvas2 = canvas_elem2.TKCanvas
    fig2, ax2 = plt.subplots(1, 1)
    fig2.set_size_inches(15, 6)
    ax2.grid()
    fig_agg2 = draw_figure(canvas2, fig2)
    mean, xax, j = [], [], 0
    while True:
        (event, values) = gui.read(timeout=0)
        mean.append(Get_Sensor_values_degital(PORT))
        j = j + 1
        xax.append(j)
        fig_agg2 = figure_draw_1(fig2, ax2, mean, fig_agg2, j, xax)
        fig_agg2.draw()
        if event == sg.WIN_CLOSED:
            gui.close()
            break
            sys.exit()
    return ()


def three_D_display(PORT):
    data1 = [0, 0, 0, 0, 0, 0, 0, 0]
    data = [0, 0, 0, 0, 0, 0, 0, 0]
    layout = [[sg.Canvas(key='-CANVAS-')]]
    gui = sg.Window(title="Live Feed figure", layout=layout, size=(800, 1000), finalize=True,
                    resizable=True, element_justification='c')
    gui.Maximize()
    canvas_elem = gui['-CANVAS-']
    canvas = canvas_elem.TKCanvas
    fig = plt.figure()
    fig.set_size_inches(8, 8)
    ax = fig.add_subplot(projection='3d')
    fig_agg = draw_figure(canvas, fig)
    while True:
                (event, values) = gui.read(timeout=0)
                puredata = Get_Sensor_values_degital(PORT)
                for i in range(0, len(puredata)):
                    data[i] = puredata[i] * 7 / 250
                fig_agg = make_cube_ulti_new_oof(ax, data, fig_agg,)
                fig_agg.draw()

                if event == sg.WIN_CLOSED:
                    gui.close()
                    break
                    sys.exit()

    return ()

