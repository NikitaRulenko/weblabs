function pulloutArray(arr){
  var mass = '';
  var output = [];

  mass = arr.toString();
  mass.split('');

  for(var i = 0; i<=mass.length; i++){
    if(mass[i] == '0' ||
       mass[i] == '1' ||
       mass[i] == '2' ||
       mass[i] == '3' ||
       mass[i] == '4' ||
       mass[i] == '5' ||
       mass[i] == '6' ||
       mass[i] == '7' ||
       mass[i] == '8' ||
       mass[i] == '9'){
      output.push(parseInt(mass[i]));
    }
  }

  console.log(output);
}
