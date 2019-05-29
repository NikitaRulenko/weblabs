var RecoveryPassword = {
    code: 0,
    valid: false,
    recovery(recWay, value) {
        if (recWay == "sms") {
            this.code = smsSend.send(value);
        } else if (recWay == "email") {
            this.code = emailSend.send(value);
        } else return false;
    },
    validate() {
        return codeValidator.verify();
    }
}

var codeValidator = {
    valid: false,
    verify(userCode, code) {
        if (userCode === code) {
            valid = true;
            return valid;
        } else return false;
    }
}

var emailSend = {
    send(value) {
        var check = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;
        if (check.test(value) == false) return false;
        else {
            return codeGen.generate();
        }
    }
}

var smsSend = {
    send(value) {
        if (typeof (value) != "string" || value.length != 11 || isNaN(value) || isNaN(Number.parseInt(value))) return false;
        else {
            return codeGen.generate();
        }
    }
}

var codeGen = {
    code: 0,
    generate() {
        this.code = Math.floor(Math.random() * (99999 - 10000 + 1)) + 10000;
        return this.code;
    },
    checkCode(value) {
        if (value == this.code) return true;
        else return false;
    }
}