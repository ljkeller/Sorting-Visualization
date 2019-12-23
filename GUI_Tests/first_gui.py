import random
import PySimpleGUI as sg

CANVAS_HEIGHT = 820
CANVAS_WIDTH = 1400
NUM_ELEMENTS = 175
BLOCK_WIDTH = int(CANVAS_WIDTH / NUM_ELEMENTS)
COUNTER = 0


def new_dataset():
    return [random.randint(0, CANVAS_HEIGHT) for i in range(NUM_ELEMENTS)]


def clear_graph(graph, graph_elements):
    for i in range(len(graph_elements)):
        graph.DeleteFigure(graph_elements[i])
    graph_elements.clear()


def draw_boxes(graph, rectangles, elements):
    clear_graph(graph, rectangles)  # clear graph elements & clear their IDs
    for i in range(len(elements)):  # When appending to list, allows us to
        # save
        # all figures
        rectangles.append(graph.DrawRectangle((i * BLOCK_WIDTH, elements[i]),
                                              (i * BLOCK_WIDTH + BLOCK_WIDTH,
                                               0),
                                              fill_color='black',
                                              line_color='white'))

sg.ChangeLookAndFeel('DarkAmber')
layout = [
    [sg.Graph(canvas_size=(CANVAS_WIDTH, CANVAS_HEIGHT),
              graph_bottom_left=(0, 0),
              graph_top_right=(CANVAS_WIDTH, CANVAS_HEIGHT),
              background_color='grey',
              key='graph')],
    [sg.T('Generate, and select sorting method:'), sg.Button(
        'Generate'),
     sg.Button('Iterate'), sg.Button('Clear'), sg.Button('Bubble Sort'),
     sg.Button('Insertion Sort'), sg.Button('Selection Sort'), sg.Button(
        'Quick Sort'), sg.Button('Merge Sort')]
]

window = sg.Window('Sorting Visualization', layout)
window.Finalize()

graph = window['graph']
generated = new_dataset()
boxes = []

while True:
    event, values = window.read()
    if event == None:
        break
    if event == 'Bubble Sort':
        swap = True
        for i in range(len(generated)):
            swap = False
            for j in range(len(generated) - i - 1):
                if generated[j] > generated[j + 1]:
                    generated[j], generated[j + 1] = generated[j + 1], \
                                                     generated[j]
                    swap = True
            if not swap:
                break
            draw_boxes(graph, boxes, generated)
            window.read(30)  # updates the window
        generated = new_dataset()
    elif event == 'Clear':
        COUNTER = 0
        clear_graph(graph, boxes)
    elif event == 'Insertion Sort':
        for i in range(len(generated)):
            insert = generated[i]
            j = i - 1
            while j >= 0 and insert < generated[j]: #right to left, stable
                generated[j+1] = generated[j]
                j-=1
            generated[j+1] = insert
            draw_boxes(graph, boxes, generated)
            window.read(30)
        generated = new_dataset()
    elif event == 'Selection Sort':
        for i in range(len(generated)):
            min_index = i
            for j in range(i+1, len(generated)):
                if generated[min_index] > generated[j]:
                    min_index = j
            generated[min_index], generated[i] = generated[i], \
                                                 generated[min_index]
            draw_boxes(graph, boxes, generated)
            window.read(30)

    elif event == 'Generate':
        COUNTER = 0  # reset counter
        draw_boxes(graph, boxes, generated)
        generated = new_dataset()
    elif event == 'Iterate':
        COUNTER += 1
        # graph.MoveFigure(boxes[0], 10,10)
        graph.TKCanvas.itemconfig(boxes[COUNTER], fill="red")
        if (COUNTER >= 1):
            graph.TKCanvas.itemconfig(boxes[COUNTER - 1], fill="black")
