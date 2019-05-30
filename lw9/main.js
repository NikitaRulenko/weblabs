var RecoveryPassword = {
    code: 0,
    valid: false,
    recovery(recWay, userData) {
        if (recWay == "sms") {
            if (typeof (userData) == "string" &&
                userData.length == 11 &&
                isNaN(userData) == false &&
                isNaN(Number.parseInt(userData)) == false) {
                this.code = codeGenerator();
            } else return false;

            Sms.send(this.code);

        } else if (recWay == "email") {
            var check = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;
            if (check.test(userData) == true) this.code = codeGenerator();
            else return false;

            Email.send(this.code);

        } else return false;
    },
    validate(userCode) {
        if (userCode === this.code) {
            this.valid = true;
            return this.valid;
        } else return false;
    }
}

function codeGenerator() {
    return Math.floor(Math.random() * (99999 - 10000 + 1)) + 10000;
}

var Email = {
    send(code) {
        console.log(code);
    }
}

var Sms = {
    send(code) {
        console.log(code);
    }
}