window.onload = function () {
    //console.log("start")
    var width = 960,
        height = 500;

    var y = d3.scale.linear()
        .range([data.data.length * height, 0]);

    var chart = d3.select(".chart")
            .attr("width", width)
            .attr("height", height);

    var barWidth = width / data.data.length;

    var g = chart.selectAll("g")
    .data(data.data)
    .enter()
    .append('g')
    .attr("transform", function(d,i) { return "translate("+ (20 + (i* 20)) +", 0)";})

    g.append("rect")
        .attr("height", function(d){ return height - y(d.mg)})
        .attr("width", barWidth - 10);

    g.append("text")
        .text(function(d) { return d.format })
        .attr("y", function(d) { return  y(d.mg) + 3})
        .attr("x", barWidth / 2)
        .attr("dy", ".75em")

        //console.log(getCurrentBloodMg(data.data))
}

// Get current mg of caffeine in the blood
// Assuming half life is 6 hours, we calculate
// A' = A * 2^(-t/h)
// where A' = amount remaining, A = initial amount
// t = time elapsed and h = half life
var getRemainingMg = function(mg, startTime) {
  nowSeconds = (new Date).getTime() / 1000.0;
  timeElapsed = nowSeconds - startTime;
  sixHours = 6 * 60 * 60;
  remainingMg = mg * Math.pow(2, (-1 * timeElapsed/sixHours));
  //console.log("Caffeing remaining from " + mg  +"mg after " + timeElapsed  +"s :", remainingMg)
  return remainingMg;
}

var getCurrentBloodMg = function(data) {
  return data.reduce(function(prev, datum) {
    return prev + getRemainingMg(datum.mg, datum.date);
  }, 0)
}
