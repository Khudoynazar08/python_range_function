def oraliq(min,max,qadam=1):
    """range(stop) -> range object
    range(start, stop[, step]) -> range object

    Return an object that produces a sequence of integers from start (inclusive)
    to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.
    start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.
    These are exactly the valid indices for a list of 4 elements.
    When step is given, it specifies the increment (or decrement)."""
    sonlar=[]
    while min<max:
        sonlar.append(min)
        if qadam!=1:
            min+=qadam
        else:
            min+=1
    return sonlar
print(oraliq(1,22,4))