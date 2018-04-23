process.stdin.resume();
process.stdin.setEncoding('ascii');

var input_stdin = "";
var input_stdin_array = "";
var input_currentline = 0;

process.stdin.on('data', function (data) {
    input_stdin += data;
});

process.stdin.on('end', function () {
    input_stdin_array = input_stdin.split("\n");
    main();    
});

// Reads complete line from STDIN
function readLine() {
    return input_stdin_array[input_currentline++];
}

function main() {
    var i = 4
    var d = 4.0
    var s = "HackerRank "
    var i1; 
    var d1; 
    var s1; // Declare second integer, double, and String variables.

    i1 = Number(readLine()); 
    d1 = Number(readLine()); 
    s1 = readLine(); // Read and save an integer, double, and String to your variables.


    console.log(i + i1);// Print the sum of both integer variables on a new line.

    console.log((d + d1).toFixed(1));// Print the sum of the double variables on a new line.

    console.log(s + s1);

}