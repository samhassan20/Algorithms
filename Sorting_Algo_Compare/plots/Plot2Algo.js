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
  x: ['934771', '586778', '267779', '518970', '7544', '762415', '422405', '768415', '732834', '829585', '422405'], 
  y: ['Insertion sort', 'Selection sort', 'Bubble sort', 'Odd-Even sort', 'Cocktail sort', 'Merge sort', 'Quick sort', 'Shell sort', 'Heap sort', 'Comb sort', 'Radix sort'], 
  hoverinfo: 'x+y', 
  marker: {size: 10}, 
  mode: 'markers', 
  name: 'Column 0', 
  text: ['999999', '999999', '999999', '999999', '999999', '283552', '752913', '369422', '297081', '927527', '304628'], 
  textsrc: 'samhassan20:26:ec2512', 
  type: 'scatter', 
  uid: '1aaa6f', 
  xsrc: 'samhassan20:26:10350a', 
  ysrc: 'samhassan20:26:d63e2f'
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
  title: 'Sorting time for 64 bit unsigned integer with arraysize 10<sup>4</sup> (10 iterations)', 
  titlefont: {color: 'rgb(31, 119, 180)'}, 
  xaxis: {
    autorange: true, 
    range: [-50762.3190547, 993077.319055], 
    title: 'Time in microseconds', 
    titlefont: {color: 'rgb(31, 119, 180)'}, 
    type: 'linear'
  }, 
  yaxis: {
    autorange: true, 
    range: [-0.710461744368, 10.7104617444], 
    title: 'Sorting Algorithms', 
    titlefont: {color: 'rgb(31, 119, 180)'}, 
    type: 'category'
  }
};
Plotly.plot('plotly-div', {
  data: data,
  layout: layout
});