function checkEmail(str){
  var result = str.match(/^[0-9a-z-\.]+\@[0-9a-z-]{1,}\.[a-z]{2,}$/i);
  if (!result){
    alert('Введите валидный e-mail.');
    return false;
  }return true;
}

function checkPassword(pass, confrim) {
  if (pass.length < 6) {
    alert('Длина пароля должна быть не менее 6-ти символов.');
    return false;
  }
  if (pass != confrim) {
    alert('Введенные пароли не совпадают.');
    return false;
  }
  return true;
}

function checkAgreementRules() {
  var result = document.getElementsByClassName("registration__check-confirmation")[0].checked;
  if (!result) {
    alert("Примите условия соглашения!");
    return false;
  }
  return true;
}

function registration()
{
  var email = document.getElementsByClassName("registration__login")[0].value;
  var pass = document.getElementsByClassName("password-block__password")[0].value;
  var confirm = document.getElementsByClassName("password-block__password-repeat")[0].value;
  if (checkEmail(email) && checkPassword(pass, confirm)
      && checkAgreementRules()) {
    alert("Регистрация прошла успешно!");
  }
}

document.getElementsByClassName("registration")[0].onsubmit = function() {
  registration();
};
