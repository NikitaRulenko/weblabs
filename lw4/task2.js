/** Reads an array and left just numbers except any other values
 * 
 * @param {array} arr 
 * @return {array} output array
 *  
 */
function pulloutArray(arr) {
  var output = [];

  for (var i = 0; i <= arr.length; i++) {
    var type;
    type = typeof(arr[i]);
    if (type === "number") {
      output.push(arr[i]);
    } else if (type === "object") {
      for (var j = 0; j <= arr[i].length; j++) {
        type = typeof(arr[i][j]);
        if (type === "number") {
          output.push(arr[i][j]);
        }
      }
    }
  }
  return output;
}

//test data var into = [1, 222, 3, [4,5,666], 7, ,"bogobogo",8, 9];
