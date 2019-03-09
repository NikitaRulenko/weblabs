

/** Foo does a check of array and use actual filter to return params as need. 
 * 
 * @callback filterCallback
 * @param {number} [number] 
 * @param {number} [index] 
 * @returns {boolean}
 */

 /** Looks for odd values and returns true if it is.
 *  
 * @type {filterCallback}
 */
var odd = function(number, i) {
    return number % 2 === 1;
  }
  
  /** Looks for even values and returns true if it is.
   * 
   * @type {filterCallback}
   */
  var even = function(number, i) {
    return (number % 2 === 0 && number !== 0);
  }
  
  /** Looks for zeroes in array and ignore them in pullout.
   * 
   * @type {filterCallback}
   */
  var eliminateZero = function(number, i) {
    return (number !== 0);
  }
  
  /** Checks array and returns only every second value of it.
   * 
   * @type {filterCallback}
   */
  var everySecond = function(number, index) {
    return index % 2 === 1;
  }
  
  /** Foo does a check of array and use actual filter to return params as need. 
   * 
   * @param {array} arr 
   * @param {filterCallback} filter 
   * @returns {array} resultArray is a filtered array
   */
  function filterArray(arr, filter) {
    var resultArray = [];
    var i;
    console.log(filter);
    for (i = 0; i < arr.length; i++) {
      if (filter(arr[i], i)) {
        resultArray.push(arr[i]);
      }
    }
    return resultArray;
  }
  
  var arr = [0, 1, 2, 3, 4, 0, 5];
  
  console.log(filterArray(arr, odd)); // [1, 3, 5]
  console.log(filterArray(arr, even)); // [2, 4]
  console.log(filterArray(arr, eliminateZero)); // [1, 2, 3, 4, 5]
  console.log(filterArray(arr, everySecond)); // [1, 3, 0]
  