window.onload = function () {
    var width = 960,
        height = 500;

    var y = d3.scale.linear()
        //.domain([0, d3.max(data.data.map(function (d) { return d.mg}))])
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
    //.attr('height', function(d) {return (d.mg) + 'px'; })
    //.attr("width", "9px");

    g.append("rect")
        .attr("height", function(d){ return height - y(d.mg)})
        .attr("width", barWidth - 1);

    g.append("text")
        .text(function(d) { return d.format })
        .attr("y", function(d) { return  y(d.mg) + 3})
        .attr("x", barWidth / 2)
        .attr("dy", ".75em")

}
