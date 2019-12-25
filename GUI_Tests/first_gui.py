import math
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


def merge_sort(graph, boxes, xs):
    # This is an interative, in place merge sort. Using an im-place merge
    # sort allows me to easily manage drawing the rectangles. I DID NOT
    # WRITE THIS. Credit to:
    # https://gist.github.com/m00nlight/a076d3995406ca92acd6
    # In the future, I may write a new helper method to avoid using an
    # in-place merge, but for now, this works.

    # The likely best solution is using the "generated" array as the "extra"
    # array space, but the biggest difficulty is graphing all of the blocks
    # easily
    unit = 1
    while unit <= len(xs):
        h = 0
        for h in range(0, len(xs), unit * 2):
            l, r = h, min(len(xs), h + 2 * unit)
            mid = h + unit
            # merge xs[h:h + 2 * unit]
            p, q = l, mid
            while p < mid and q < r:
                # use <= for stable merge merge
                if xs[p] <= xs[q]:
                    p += 1
                else:
                    tmp = xs[q]
                    xs[p + 1: q + 1] = xs[p:q]
                    xs[p] = tmp
                    p, mid, q = p + 1, mid + 1, q + 1
            draw_boxes(graph, boxes, xs)
            window.read(30)

        unit *= 2


def quick_sort(graph, boxes, arr, left, right):
    if left >= right:
        return

    p = partition(arr, left, right)
    draw_boxes(graph, boxes, arr)
    window.read(100)
    quick_sort(graph, boxes, arr, left, p - 1)
    quick_sort(graph, boxes, arr, p + 1, right)


def partition(arr, left, right):
    pivot = arr[left]
    i, j = left + 1, right
    while True:  # consider even or odd length lists
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i <= j:
            arr[j], arr[i] = arr[i], arr[j]
        else:
            break
    arr[left], arr[j] = arr[j], arr[left]  # swap pivot in
    return j


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
        'Generate'), sg.Button('Clear'), sg.Button('Bubble Sort'),
     sg.Button('Insertion Sort'), sg.Button('Selection Sort'), sg.Button(
        'Quick Sort'), sg.Button('Merge Sort'), sg.Button('Radix Sort')]
]

window = sg.Window('Sorting Visualization', layout)
window.Finalize()

graph = window['graph']
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
    elif event == 'Clear':
        COUNTER = 0
        clear_graph(graph, boxes)
    elif event == 'Insertion Sort':
        for i in range(len(generated)):
            insert = generated[i]
            j = i - 1
            while j >= 0 and insert < generated[j]:  # right to left, stable
                generated[j + 1] = generated[j]
                j -= 1
            generated[j + 1] = insert
            draw_boxes(graph, boxes, generated)
            window.read(30)
    elif event == 'Selection Sort':
        for i in range(len(generated)):
            min_index = i
            for j in range(i + 1, len(generated)):
                if generated[min_index] > generated[j]:
                    min_index = j
            generated[min_index], generated[i] = generated[i], \
                                                 generated[min_index]
            draw_boxes(graph, boxes, generated)
            window.read(30)
    elif event == 'Merge Sort':
        merge_sort(graph, boxes, generated)
    elif event == 'Radix Sort':
        num_digits = math.ceil(math.log(CANVAS_HEIGHT, 10))
        count_sort = [[] for i in range(10)]
        for digit in range(num_digits):
            for i in range(NUM_ELEMENTS):
                remainder = int((generated[i] // math.pow(10, digit))) % 10
                count_sort[remainder].append(generated[i])
                flat = [leaves for tree in count_sort for leaves in tree]
                draw_boxes(graph, boxes, flat + generated[i:])
                window.read(30)
            generated[:] = [leaves for tree in count_sort for leaves in tree]
            for digit_sublist in count_sort:
                digit_sublist.clear()
            draw_boxes(graph, boxes, generated)
            window.read(100)

    elif event == 'Quick Sort':
        quick_sort(graph, boxes, generated, 0, NUM_ELEMENTS - 1)
    elif event == 'Generate':
        COUNTER = 0  # reset counter
        generated = new_dataset()
        draw_boxes(graph, boxes, generated)
    # elif event == 'Iterate':
    #     COUNTER += 1
    #     # graph.MoveFigure(boxes[0], 10,10)
    #     graph.TKCanvas.itemconfig(boxes[COUNTER], fill="red")
    #     if (COUNTER >= 1):
    #         graph.TKCanvas.itemconfig(boxes[COUNTER - 1], fill="black")
