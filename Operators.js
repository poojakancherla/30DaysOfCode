var meal_cost = 10.0;
var tip_percent = 1;
var tax_percent = 1;

var tip = meal_cost * (tip_percent / 100); 
var tax = meal_cost * (tax_percent / 100); 
var total_cost = meal_cost + tip + tax;

console.log(Math.round(total_cost));
