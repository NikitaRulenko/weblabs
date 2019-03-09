/** Foo gets usr data from object
 * 
 * @param {object} obj 
 * @returns {object} as filtered result
 */
function getUserProfileFromObj(obj) {
  if (typeof(obj) !== 'object' || Object.keys(obj).length === 0) {
    return false;
  } else {
    return {
      'username': obj.name,
      'email': obj.email
    };
  }
}

//test data: var user = { 'name': 'Вася', 'age': 35, 'isAdmin': false, 'email': 'pedik@yoba.com' };

/** Refactored foo do the same shit as previous just only looks pretty =)
 * @param {object} obj
 * @returns {object}
 */
function getUserProfileFromObj(obj) {
  if (typeof(obj) === 'object' && Object.keys(obj).length !== 0) {
    return {
      'username': obj.name,
      'email': obj.email
    };
  }
  return false;
}
