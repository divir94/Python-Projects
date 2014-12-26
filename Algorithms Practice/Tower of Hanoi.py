def move_tower(n, From, to, using):
    # base case
    if n==1:
        print "%s -> %s" % (From, to)
        return
    # recursive step
    move_tower(n-1, From, using, to)
    move_tower(1, From, to, using)
    move_tower(n-1, using, to, From)

move_tower(5, 'A', 'B', 'C')