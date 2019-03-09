/** Returnes value and type of input param
 * 
 * @param {*} value 
 * 
 */
function varDump(value){
  var value, typeCheck;

  typeCheck = typeof(value);
  console.log("type = ", typeCheck, " value = ", value);
}
