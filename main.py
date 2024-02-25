from window import Window

screen_width = 800
screen_height = 800
fps = 60

window = Window(screen_width, screen_height, fps)

while window.running:
    window.update()

window.quit()