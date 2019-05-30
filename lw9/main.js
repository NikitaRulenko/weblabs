var RecoveryPassword = {
    code: 0,
    valid: false,
    recovery(recWay, userData) {
        if (recWay == "sms" && Sms.send(userData) == true) {
            this.code = codeGenerator();
        } else if (recWay == "email" && Email.send(userData) == true) {
            this.code = codeGenerator();
        } else return false;
    },
    validate(userCode) {
        if (userCode === this.code) {
            this.valid = true;
            return this.valid;
        } else return false;
    }
}

function codeGenerator(){
    return Math.floor(Math.random() * (99999 - 10000 + 1)) + 10000;
} 

var Email = {
    send(email) {
        var check = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;
        if (check.test(email) == false) return false;
        else {
            return true;
        }
    }
}

var Sms = {
    send(number) {
        if (typeof (number) != "string" || number.length != 11 || isNaN(number) || isNaN(Number.parseInt(number))) return false;
        else {
            return true;
        }
    }
}

