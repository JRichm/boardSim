from window import Window

screen_width = 500
screen_height = 500
fps = 60

window = Window(screen_width, screen_height, fps)

while window.running:
    window.Update()

window.Quit()