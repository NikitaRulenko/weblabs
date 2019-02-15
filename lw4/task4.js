function getUserProfileFromObj(obj){
  if(typeof(obj)!='object' || Object.keys(obj).length == 0){
    console.log('Input data must be an object and it cant be empty!');
  }
  else{
    obj = JSON.stringify(obj);
    obj = JSON.parse(obj);
    console.log('Username: ', user.name,', email: ', user.email);
  }
}

//test data: var user = { "name": "Вася", "age": 35, "isAdmin": false, "email": "pedik@yoba.com" };
