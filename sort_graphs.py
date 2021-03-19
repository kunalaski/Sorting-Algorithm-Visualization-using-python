import tkinter as tk
import tkinter.font as tkFont
from tkinter.ttk import *
import random

#Bar swap methods
def swap(pos_0, pos_1):
    bar11, _, bar12, _ = canvas.coords(pos_0)
    bar21, _, bar22, _ = canvas.coords(pos_1)
    canvas.move(pos_0, bar21-bar11, 0)
    canvas.move(pos_1, bar12-bar22, 0)

worker = None 

#Insertion Sort
def _insertion_sort():
    global barList
    global lengthList

    for i in range(len(lengthList)):
        cursor = lengthList[i]
        cursorBar = barList[i]
        pos = i

        while pos > 0 and lengthList[pos - 1] > cursor:
            lengthList[pos] = lengthList[pos - 1]
            canvas.itemconfig(barList[pos], fill='red')
            canvas.itemconfig(barList[pos-1], fill='red')
            barList[pos], barList[pos - 1] = barList[pos - 1], barList[pos]
            swap(barList[pos],barList[pos-1])   
            yield    
            canvas.itemconfig(barList[pos], fill='white')
            canvas.itemconfig(barList[pos-1], fill='white')                                  
            pos -= 1                                   

        lengthList[pos] = cursor
        barList[pos] = cursorBar
        canvas.itemconfig(barList[pos], fill='red')
        canvas.itemconfig(cursorBar, fill='red')
        swap(barList[pos],cursorBar)
        canvas.itemconfig(barList[pos], fill='white')
        canvas.itemconfig(cursorBar, fill='white')


#Bubble Sort
def _bubble_sort():
    global barList
    global lengthList
    
    for i in range(len(lengthList) - 1):
        for j in range(len(lengthList) - i - 1):
            if(lengthList[j] > lengthList[j + 1]):
                canvas.itemconfig(barList[j], fill='red')
                canvas.itemconfig(barList[j+1], fill='red')
                lengthList[j] , lengthList[j + 1] = lengthList[j + 1] , lengthList[j]
                barList[j], barList[j + 1] = barList[j + 1] , barList[j]
                swap(barList[j + 1] , barList[j])
                yield    
                canvas.itemconfig(barList[j], fill='white')
                canvas.itemconfig(barList[j+1], fill='white')    
           

#Selection Sort            
def _selection_sort():
    global barList    
    global lengthList
    global b
    global s
    for i in range(len(lengthList)):
        min = i
        for j in range(i + 1 ,len(lengthList)):
            if(lengthList[j] < lengthList[min]):
                min = j
        canvas.itemconfig(barList[i], fill='red')
        canvas.itemconfig(barList[min], fill='red')
        lengthList[min], lengthList[i] = lengthList[i] ,lengthList[min]
        barList[min] , barList[i] = barList[i] , barList[min]
        swap(barList[min] , barList[i])        
        yield
        canvas.itemconfig(barList[i], fill='white')
        canvas.itemconfig(barList[min], fill='white')

#Quick Sort
def _quick_sort(lengthList1, barList1, start, end):
    if(start >= end):
        return
    else:   
        pivot = lengthList1[end]
        #canvas.itemconfig(barList[end], fill='red')
        pivid = start
        for i in range(start, end):
            if(lengthList1[i] < pivot):
                canvas.itemconfig(barList1[i], fill='red')
                canvas.itemconfig(barList1[pivid], fill='red')
                lengthList1[i], lengthList1[pivid] = lengthList1[pivid], lengthList1[i]
                barList[i], barList[pivid] = barList[pivid], barList[i]
                swap(barList[i], barList[pivid])
                yield
                canvas.itemconfig(barList1[i], fill='white')
                canvas.itemconfig(barList1[pivid], fill='white')
                pivid += 1
            yield
        canvas.itemconfig(barList1[end], fill='red')
        canvas.itemconfig(barList1[pivid], fill='red')
        lengthList1[end], lengthList1[pivid] = lengthList1[pivid], lengthList1[end]
        barList[end], barList[pivid] = barList[pivid], barList[end]
        swap(barList[end], barList[pivid])
        yield
        canvas.itemconfig(barList1[end], fill='white')
        canvas.itemconfig(barList1[pivid], fill='white')
        yield from _quick_sort(lengthList1, barList, start, pivid-1)    
        yield from _quick_sort(lengthList1, barList, pivid+1, end)

#Merge Sort
def merge_(mergelist, lengthList1, barList1, low, mid, high):
    merged = []
    start1 = low
    h=low
    i=low
    j=mid+1
    #left = start
    #right = mid+1

    while h <= mid and j <= high:
        if lengthList1[h] < lengthList1[j]:
            merged.append(lengthList1[h])
            h += 1
        else:
            merged.append(lengthList1[j])
            j +=1
    while h <= mid:
        merged.append(lengthList1[h])
        h += 1

    while j <= high:
        merged.append(lengthList1[j])
        j += 1

    for i, k in enumerate(merged):
        d = mergelist.index(k)
        lengthList1[low + i] = k
        canvas.itemconfig(barList[d], fill='red')
        canvas.itemconfig(barList[low + i], fill='red')
        mergelist[d], mergelist[low + i] = mergelist[low + i], mergelist[d]
        barList1[d], barList1[low+i] = barList1[low+i], barList1[d]
        swap(barList1[d], barList1[low+i])
        yield
        canvas.itemconfig(barList[d], fill='white')
        canvas.itemconfig(barList[low + i], fill='white')
        

def _merge_sort_(mergelist, lengthList1, barList1, start, end):
    if(end <= start):
        return
    mid = int((start + end)/2)
    yield from _merge_sort_(mergelist, lengthList1, barList1, start, mid)
    yield from _merge_sort_(mergelist, lengthList1, barList1, mid+1, end)
    yield from merge_(mergelist, lengthList1, barList1, start, mid, end)
    yield


#Triggering Methods

def insertion_sort():     
    global worker
    global label
    label.destroy()
    label = Label(window, text='Visualization of Insertion sort', font=fontStyle1)
    label.grid(column=1, row=0, pady=10)
    worker = _insertion_sort()
    animate()

def selection_sort():     
    global worker
    global label
    label.destroy()
    label = Label(window, text='Visualization of Selection sort', font=fontStyle1)
    label.grid(column=1, row=0, pady=10)
    worker = _selection_sort()
    animate()

def bubble_sort(): 
    global worker
    global label
    label.destroy()
    label = Label(window, text='Visualization of Bubble sort', font=fontStyle1)
    label.grid(column=1, row=0, pady=10)
    worker = _bubble_sort()
    animate()    


def merge_sort():     
    global worker
    global label
    label.destroy()
    label = Label(window, text='Visualization of Merge sort', font=fontStyle1)
    label.grid(column=1, row=0, pady=10)
    mergelist = []
    for i in lengthList:
        mergelist.append(i)
    worker = _merge_sort_(mergelist, lengthList, barList, 0, len(lengthList)-1)
    animate()


def quick_sort():     
    global worker
    global label
    label.destroy()
    label = Label(window, text='Visualization of Quick sort', font=fontStyle1)
    label.grid(column=1, row=0, pady=10)
    worker = _quick_sort(lengthList, barList, 0, len(lengthList)-1)
    animate()



#Animation Methodds
def animate():      
    global worker
    if worker is not None:
        try:
            next(worker)
            window.after(50, animate)    
        except StopIteration:            
            worker = None
        finally:
            window.after_cancel(animate) 


def generate():
    global barList
    global lengthList
    global label
    label.destroy()
    label = Label(window, text='Choose an Sorting algorithm', font=fontStyle1)
    label.grid(column=1, row=0, pady=10)
    canvas.delete('all')
    barstart = 5
    barend = 15
    barList = []
    lengthList = []

    randomY = random.sample(range(1, 360), 60)
    for Y in randomY:
        bar = canvas.create_rectangle(barstart, Y, barend, 365, fill='white')
        barList.append(bar)
        barstart += 10
        barend += 10


    #Getting length of the bar and appending into length list
    for bar in barList:
        bar = canvas.coords(bar)
        length = bar[3] - bar[1]
        lengthList.append(length)
'''
    for i in range(len(lengthList)-1):
        if lengthList[i] == min(lengthList):
            canvas.itemconfig(barList[i], fill='#8CFF19')
        elif lengthList[i] == max(lengthList):
            canvas.itemconfig(barList[i], fill='#00FFFF')
'''


window = tk.Tk()
window.title('Sorting Representation using graphss')
#window.configure(bg="black")
#window.geometry('610x450')

canvas = tk.Canvas(window, width='610', height='400', bg="black")
canvas.grid(column=0,row=1, columnspan = 50)
fontStyle = tkFont.Font(family="Times New Roman")
fontStyle1 = tkFont.Font(family="Times New Roman", size=15)
#Buttons
insert = tk.Button(window, text='Insertion Sort', padx=20, pady=20, relief="raised", borderwidth=4, font=fontStyle, command=insertion_sort)
select = tk.Button(window, text='Selection Sort', padx=20, pady=20, relief="raised", borderwidth=4, font=fontStyle, command=selection_sort)
bubble = tk.Button(window, text='Bubble Sort', padx=20, pady=20, relief="raised", borderwidth=4, font=fontStyle, command=bubble_sort)
merge = tk.Button(window, text='Merge Sort', padx=20, pady=20, relief="raised", borderwidth=4, font=fontStyle, command=merge_sort)
quick = tk.Button(window, text='Quick Sort', padx=20, pady=20, relief="raised", borderwidth=4, font=fontStyle, command=quick_sort)
shuf = tk.Button(window, text='Shuffle', padx=150, pady=20, relief="raised", borderwidth=4, font=fontStyle, command=generate)
insert.grid(column=0,row=2, padx=20, pady=10)
select.grid(column=1,row=2, padx=20, pady=10)
bubble.grid(column=2,row=2, padx=30, pady=10)
merge.grid(column=3,row=2, padx=30, pady=10)
quick.grid(column=4,row=2, padx=30, pady=10)
shuf.grid(column=1, row=4, padx=30, pady=10, columnspan=3)
label = Label(window, text='Choose an Sorting algorithm', font=fontStyle1)
label.grid(column=1, row=0, pady=10)
generate()
window.mainloop()



                                                                                             
