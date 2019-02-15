var odd = function(number) {
  return number % 2 === 1;
}

var even = function(number) {
  return number % 2 === 0;
}

// TODO: filter for elimination 0 value
var eliminateZero = function(number) {
  return 
  // your code
}

// TODO: get every second element in sequence
var everySecond = function(number) {
  // your code
}

function filterArray(arr, filter) {
  var resultArray = [];
  for (i = 0; i < arr.length; i++) {
    if (filter(arr[i])) {
      // TODO: add filtered element in resultArray
      // your code
    }
  }
  return resultArray;
}

var arr = [0, 1, 2, 3, 4, 0, 5];

console.log(filterArray(arr, odd)); // [1, 3, 5]
console.log(filterArray(arr, even)); // [2, 4]
console.log(filterArray(arr, eliminateZero)); // [1, 2, 3, 4, 5]
