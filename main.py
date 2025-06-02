from time_series_visualizer import draw_line_plot, draw_bar_plot, draw_box_plot

# Save figures to check results
line_fig = draw_line_plot()
line_fig.savefig('line_plot.png')

bar_fig = draw_bar_plot()
bar_fig.savefig('bar_plot.png')

box_fig = draw_box_plot()
box_fig.savefig('box_plot.png')
