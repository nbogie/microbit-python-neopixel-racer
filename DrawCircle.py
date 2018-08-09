import arcade
arcade.open_window(800,600,"Drawing Example")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()
arcade.draw_circle_filled(420, 285, 18, arcade.color.GREEN)
arcade.finish_render()
arcade.run()
