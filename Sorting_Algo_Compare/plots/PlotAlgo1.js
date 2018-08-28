// You can reproduce this figure in plotly.js with the following code!

// Learn more about plotly.js here: https://plot.ly/javascript/getting-started

/* Here's an example minimal HTML template
 *
 * <!DOCTYPE html>
 *   <head>
 *     <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
 *   </head>
 *   <body>
 *   <!-- Plotly chart will be drawn inside this div -->
 *   <div id="plotly-div"></div>
 *     <script>
 *     // JAVASCRIPT CODE GOES HERE
 *     </script>
 *   </body>
 * </html>
 */

trace1 = {
  x: ['13295', '5038', '29961', '13654', '7059', '4028', '13174', '4858', '8652', '13140', '6831', '11550'], 
  y: ['Insertion sort', 'Selection sort', 'Bubble sort', 'Merge sort', 'Quick sort', 'Counting sort', 'Radix sort', 'Shell sort', 'Odd-Even sort', 'Cocktail sort', 'Heap sort', 'Comb sort'], 
  hoverinfo: 'x+y', 
  marker: {
    size: 10, 
    symbol: 'circle'
  }, 
  mode: 'markers', 
  name: 'Column 0', 
  text: ['13295', '5038', '29961', '13654', '7059', '4028', '13174', '4858', '8652', '13140', '6831', '11550'], 
  textsrc: 'samhassan20:24:ffbdee', 
  type: 'scatter', 
  uid: 'f0b5f9', 
  xsrc: 'samhassan20:24:ffbdee', 
  ysrc: 'samhassan20:24:5ccd21'
};
data = [trace1];
layout = {
  autosize: true, 
  font: {family: '"Open Sans", verdana, arial, sans-serif'}, 
  hovermode: 'closest', 
  margin: {
    r: 50, 
    b: 100, 
    l: 150, 
    pad: 5
  }, 
  paper_bgcolor: 'rgb(255, 254, 254)', 
  plot_bgcolor: 'rgb(255, 254, 254)', 
  showlegend: false, 
  title: 'Sorting time for 8 bit unsigned integer with arraysize 100 (10 iterations)', 
  titlefont: {color: 'rgb(11, 128, 241)'}, 
  width: 1269.67, 
  xaxis: {
    autorange: false, 
    range: [2477.9996966, 31511.0003034], 
    title: 'Time in microseconds', 
    titlefont: {color: 'rgb(31, 119, 180)'}, 
    type: 'linear'
  }, 
  yaxis: {
    autorange: true, 
    range: [-0.781507918804, 11.7815079188], 
    title: 'Sorting Algorithms', 
    titlefont: {color: 'rgb(31, 119, 180)'}, 
    type: 'category'
  }
};
Plotly.plot('plotly-div', {
  data: data,
  layout: layout
});