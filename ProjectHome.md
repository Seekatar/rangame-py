# Rangame's Latest Iteration #
Showing how order can come from chaos, this game shows what happens when plotting points 1/2 way to a randomly picked corner of a triangle.  Try it with other shapes or divisors to get interesting images.

This requires [PyGame](http://www.pygame.org/) to be installed on the target computer.  It has been tested on Windows and Raspberry Pi with Raspian.

<p align='center'>
<img src='https://rangame-py.googlecode.com/git/doc/random3.gif' />
</p>

# Running Rangame #
To run, simply execute Rangame.py in your installed version of Python.  The keys are as follows:

| **Key** | **Action** |
|:--------|:-----------|
| ESC | Quit the app |
| c | show the config dialog |
| p or space | plot another set of points |
| r | re-initialize the points |
| h | toggle the histogram |
| w | wipe the window |
| F1 | Help (is coming) |

The configuration dialog allows you to change how things work.  By default, you get a regular triangle.

<p align='center'>
<img src='https://rangame-py.googlecode.com/git/doc/rangame_options.png' />
</p>

| **Option** | **Action** |
|:-----------|:-----------|
| Sides | The number of sides for the shape.  From 2-20 (yes, 2) |
| Points to Plot | Number of points to draw each time |
| Divisor | This is the interesting value.  As the sides change, change this to get interesting images.  See the examples below |
| Radius | If using a Regular shape, the radius of the shape |
| Create Regular shape | Creates a regular (even sided) shape.  If off you use the mouse to set the points. |
| Show Histogram after plot | Show a transparent histogram after the plot.  Use h to toggle it |
| Foreground | Color of the points to plot.  You can change the color between plots |
| Background | Color to set after wiping the window (w) |

Here's a screenshot of the Python version with translucent histogram<br />
<img width='300' height='300' src='https://rangame-py.googlecode.com/git/doc/rangame_5.png' />

## Examples ##
<table cellpadding='0' border='0' cellspacing='0'>
<blockquote><tr>
<blockquote><td>
<blockquote><p align='center'><img src='https://rangame-py.googlecode.com/git/doc/random3.gif' border='0' width='300' height='300' /></p></td>
</blockquote><td>  <p align='left'>

<B>

Settings:<br>
<br>
</B><br>
<br>
<br>
<blockquote>Radius: 200<br />
Divisor: 2<br />
Plotted three times, each 1000 points with blue, cyan, and magenta.</p>
<p align='left'>This is the default settings made a bit more interesting with the colors.</p>
</blockquote></td>
</blockquote></tr>
<blockquote><tr>
</blockquote><blockquote><td>
<blockquote><p align='center'><img src='https://rangame-py.googlecode.com/git/doc/random5.gif' border='0' width='200' height='200' /></p></td>
</blockquote><td>  <p align='left'>

<B>

Settings:<br>
<br>
</B><br>
<br>
<br>
<blockquote>Radius: 50<br />
Divisor: 0.666667<br />
Plotted three times, each 1000 points with blue, cyan, and magenta.</p>
<p align='left'>This is rather interesting since instead of going 1/2 the distance to the point it goes 1/.666667 or 1.5 the distance to the point. In other words it goes past each point.</p>
</blockquote></td>
</blockquote></tr>
<blockquote><tr>
<blockquote><td>
<blockquote><p align='center'><img src='https://rangame-py.googlecode.com/git/doc/random6.gif' border='0' width='200' height='200' /></p></td>
</blockquote><td>  <p align='left'>

<B>

Settings:<br>
<br>
</B><br>
<br>
<br>
<blockquote>Points: 5<br />
Radius: 100<br />
Divisor: 1.6<br />
When I first tried other than three points, I was disappointed to see that it didn't work. Then, by adjusting the divisor, I found that for all figures you could get similar results.</p>
</blockquote></td>
</blockquote></blockquote></tr>
<blockquote><tr>
<blockquote><td>
<blockquote><p align='center'><img src='https://rangame-py.googlecode.com/git/doc/random7.gif' border='0' width='200' height='200' /></p></td>
</blockquote><td>  <p align='left'>

<B>

Settings:<br>
<br>
</B><br>
<br>
<br>
<blockquote>Points: 4<br />
Radius: 100<br />
Divisor: 1.9</p>
</blockquote></td>
</blockquote></blockquote></tr>
</blockquote><blockquote><tr>
<blockquote><td>
<blockquote><p align='center'><img src='https://rangame-py.googlecode.com/git/doc/random8.gif' height='332' width='476' /></p>
<p align='left'>Is this art or what?<br /> This is several plots on the same screen, using the manually set points option.</p></td>
</blockquote></blockquote></tr>
</table>