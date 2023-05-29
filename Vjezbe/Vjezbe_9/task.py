import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from lib import Body, BodySystem


dt, observed_time, video_frames = 100, 3600 * 24 * 366, 400

earth = Body(5.9742 * 10**24,
             np.array([1.486 * 10**11, 0, 0]), np.array([0, 29783, 0], dtype=np.float64))
sun = Body(1.989 * 10**30, np.array([0, 0, 0], dtype=np.float64),
           np.array([0, 0, 0], dtype=np.float64))

body_system = BodySystem([earth, sun])
timestamps, positions = body_system.get_graph(dt, observed_time)
p_e, p_s = positions[0], positions[1]

x_e, y_e, z_e = [p[0] for p in p_e], [p[1]
                                      for p in p_e], [p[2] for p in p_e]
x_s, y_s, z_s = [p[0] for p in p_s], [p[1] for p in p_s], [p[2] for p in p_s]


def animate(frame):
    multiplier = observed_time/dt / video_frames
    current_snapshot = int(multiplier * frame)
    day = observed_time * (frame/video_frames) / (3600*24)

    plt.cla()
    plt.xlim(-2*10**11, 2*10**11)
    plt.ylim(-2*10**11, 2*10**11)
    plt.axis('off')

    plt.plot(x_e[:current_snapshot], y_e[:current_snapshot],
             '-', label='Earth')
    plt.plot(x_s[:current_snapshot], y_s[:current_snapshot],
             '-', label='Sun')
    plt.title(f"Day {day:.2f}", loc='left')


anim = animation.FuncAnimation(plt.gcf(), animate, frames=video_frames)
anim.save('anim_earth-sun.mp4', writer='ffmpeg', fps=60)
