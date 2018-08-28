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
  x: ['18003', '853581', '967266', '740523', '481898', '73742', '113736', '73742'], 
  y: ['Insertion sort', 'Selection sort', 'Bubble sort', 'Merge sort', 'Quick sort', 'Shell sort', 'Heap sort', 'Comb sort'], 
  hoverinfo: 'x+y', 
  marker: {size: 10}, 
  mode: 'markers', 
  name: 'Column 0', 
  text: ['18003', '853581', '967266', '740523', '481898', '73742', '113736', '73742'], 
  textsrc: 'samhassan20:30:62a82e', 
  type: 'scatter', 
  uid: '99510b', 
  xsrc: 'samhassan20:30:62a82e', 
  ysrc: 'samhassan20:30:f9d318'
};
data = [trace1];
layout = {
  autosize: true, 
  hovermode: 'closest', 
  margin: {
    r: 50, 
    b: 100, 
    l: 150, 
    pad: 5
  }, 
  title: 'Sorting time for words (string data)', 
  titlefont: {color: 'rgb(31, 119, 180)'}, 
  xaxis: {
    autorange: true, 
    range: [-41688.9970458, 1026957.99705], 
    title: 'Time in microseconds', 
    titlefont: {color: 'rgb(31, 119, 180)'}, 
    type: 'linear'
  }, 
  yaxis: {
    autorange: true, 
    range: [-0.497323221057, 7.49732322106], 
    title: 'Sorting Algorithms', 
    titlefont: {color: 'rgb(31, 119, 180)'}, 
    type: 'category'
  }
};
Plotly.plot('plotly-div', {
  data: data,
  layout: layout
});