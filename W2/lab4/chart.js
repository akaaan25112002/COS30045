window.onload = function () {
    const w = 500;
    const h = 300;
    const padding = 10;

    d3.csv("Task_2.4_data.csv").then(function (data) {
        const dataset = data.map(d => +d.wombats);

        const barWidth = w / dataset.length;

        const yScale = d3.scaleLinear()
            .domain([0, d3.max(dataset)])
            .range([h - padding * 2, 0]);

        const svg = d3.select("#chart")
            .append("svg")
            .attr("width", w)
            .attr("height", h);

        svg.selectAll("rect")
            .data(dataset)
            .enter()
            .append("rect")
            .attr("x", (d, i) => i * barWidth)
            .attr("y", d => yScale(d))
            .attr("width", barWidth - padding)
            .attr("height", d => h - yScale(d) - padding * 2)
            .attr("fill", d => d > 20 ? "tomato" : d > 10 ? "orange" : "green");

        svg.selectAll("text")
            .data(dataset)
            .enter()
            .append("text")
            .text(d => d)
            .attr("x", (d, i) => i * barWidth + (barWidth - padding) / 2)
            .attr("y", d => yScale(d) - 5)
            .attr("text-anchor", "middle")
            .attr("font-size", "12px")
            .attr("fill", "black");
    });
};
