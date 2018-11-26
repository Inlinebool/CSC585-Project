const height = 600;
const width = 600;

const projection_view = d3.selectAll("#projection_view");
const sentence_view = d3.selectAll("#sentence_view");

let minX = 100;
let maxX = 0;
let minY = 100;
let maxY = 0;

for (let i = 0; i < projection.length; i++) {
    if (projection[i][0] < minX) {
        minX = projection[i][0];
    }
    if (projection[i][0] > maxX) {
        maxX = projection[i][0];
    }
    if (projection[i][1] < minY) {
        minY = projection[i][1];
    }
    if (projection[i][1] > maxY) {
        maxY = projection[i][1];
    }
}

projectionMap = {};
for (let i = 0; i < projection.length; i++) {
    projectionMap[projection[i]] = i;
}
relationMap = {
    "per:spouse": 0,
    "per:city_of_birth": 1,
    "org:city_of_headquarters": 2,
    "no_relation": 3
};
relations = ["per:spouse", "per:city_of_birth", "org:city_of_headquarters", "no_relation"];

d3.select("#btn_relation_1").text(relations[0]);
d3.select("#btn_relation_2").text(relations[1]);
d3.select("#btn_relation_3").text(relations[2]);
d3.select("#btn_relation_4").text(relations[3]);

console.log([minX, maxX]);
console.log([minY, maxY]);

const xScale = d3.scaleLinear().domain([minX, maxX]).range([5, width - 5]);
const yScale = d3.scaleLinear().domain([minY, maxY]).range([5, height - 5]);
const scaleAccent = d3.scaleOrdinal(d3.schemeAccent);

function clearSelected() {
    d3.selectAll("circle").classed("selected", false);
    selectedSentences = [];
    d3.selectAll(".sentence").remove();
}

let selectedSentences = [];

function writeSentences() {
    for (let i = 0; i < selectedSentences.length; i++) {
        let sentence = data[selectedSentences[i]]["sentence"];
        console.log(sentence);
        const entity = data[selectedSentences[i]]["entity"];
        const slotValue = data[selectedSentences[i]]["slotValue"];
        sentence = sentence.replace(entity, "<span class=\"entity\">" + entity + "</span>");
        sentence = sentence.replace(slotValue, "<span class=\"slotValue\">" + slotValue + "</span>");
        // var view = document.getElementById("sentence_view");
        // var div = document.createElement("div");
        // var p = document.createElement("p");
        // p.innerHTML = sentence;
        // var text = document.createTextNode(sentence);
        // p.appendChild(text);
        // div.appendChild(p);
        // view.appendChild(div);
        sentence_view.append("div")
            .classed("sentence", true)
            .append("p")
            .html(sentence);
    }
}

const brush = d3.brush();

projection_view.call(
    brush
        .on("brush", function () {
            var e = d3.event.selection;
            var xMin = xScale.invert(e[0][0]);
            var xMax = xScale.invert(e[1][0]);
            var yMin = yScale.invert(e[0][1]);
            var yMax = yScale.invert(e[1][1]);

            // console.log([xMin, xMax, yMin, yMax]);

            d3.selectAll("circle").classed("selected", function (d) {
                if (d[0] >= xMin && d[0] <= xMax && d[1] >= yMin && d[1] <= yMax) {
                    if (!selectedSentences.includes(projectionMap[d])) {
                        selectedSentences.push(projectionMap[d]);
                    }
                    return true;
                } else {
                    return false;
                }
            });
        })
        .on("start", function () {
            clearSelected();
        })
        .on("end", function () {
            writeSentences();
        }));

projection_view.selectAll("circle").data(projection).enter()
    .append("circle")
    .attr("cx", function (d) {
        return xScale(d[0])
    })
    .attr("cy", function (d) {
        return yScale(d[1])
    })
    .attr("r", 2)
    .attr("fill", function (d) {
        const relation = data[projectionMap[d]]["relation"];
        // if (relation === "no_relation") {
        //     return "white";
        // }
        return scaleAccent(relationMap[relation]);
    })
    .on("click", function (d) {
        clearSelected();
        // console.log(d);
        var point = d3.select(this);
        point.classed("selected", true);
        selectedSentences.push(projectionMap[d]);
        writeSentences();
    });
