import queue as q

customqueue=q.Queue(maxSize=3)


customqueue.put(1)
customqueue.put(2)
customqueue.put(3)

customqueue.get()