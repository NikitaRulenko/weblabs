//dont understand the difference between undef and null
function isArrayEqual(a, b){
  if (Array.isArray(a) && Array.isArray(b) && JSON.stringify(a) == JSON.stringify(b)) {
    return true;
  }
  return false;
}

//understand everything and doing blowjob =)
function isArrayEqual(a, b){
  if (Array.isArray(a) && Array.isArray(b) && a.length === b.length){

    for (var i = 0; i < a.length; i++){
      if ((typeof(a[i]) !== typeof(b[i]) || a[i] !== b[i]) &&
        !(Array.isArray(a[i]) && Array.isArray(b[i]) && isArrayEqual(a[i],b[i])))
          return false;
    }

  } else {
    return false;
  }
  return true;
}
