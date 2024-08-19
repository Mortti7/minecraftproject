def on_forever():
    agent.move(UP, 1)
    agent.place(DOWN)
    agent.set_item(DIRT, 1, 1)
loops.forever(on_forever)
