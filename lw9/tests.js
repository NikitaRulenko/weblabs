var autoTest = {
    passedTestCount: 0,
    valid_code: 0,
    RecoveryPassword_sms: false,
    RecoveryPassword_email: false,
    RecoveryPassword_validate: false,
    emailSend: false,
    smsSend: false,
    codeGen_generate: false,
    codeGen_checkCode: false,
    codeValidator: false,

    test_codeGen_generate() {
        valid_code = codeGen.generate();
        if (typeof (valid_code) == "number") {
            codeGen_generate = true;
            this.passedTestCount++;
        }
    },

    test_codeGen_checkCode() {
        if (codeGen.checkCode(valid_code) == true) {
            codeGen_checkCode = true;
            this.passedTestCount++;
        }
    },

    test_smsSend() {
        valid_code = smsSend.send("89877183558");
        if (typeof (valid_code) == "number") {
            smsSend = true;
            this.passedTestCount++;
        }
    },

    test_emailSend() {
        valid_code = emailSend.send("test@test.ru");
        if (typeof (valid_code) == "number") {
            emailSend = true;
            this.passedTestCount++;
        }
    },

    test_RecoveryPassword_sms() {
        valid_code = RecoveryPassword.recovery("sms", "89877183558");
        if (typeof (valid_code) == "number") {
            RecoveryPassword_sms = true;
            this.passedTestCount++;
        }
    },

    test_RecoveryPassword_email() {
        valid_code = RecoveryPassword.recovery("email", "test@test.ru");
        if (typeof (valid_code) == "number") {
            RecoveryPassword_email = true;
            this.passedTestCount++;
        }
    },

    test_RecoveryPassword_validate() {
        var check = RecoveryPassword.validate();
        if (check == true) {
            RecoveryPassword_validate = true;
            this.passedTestCount++;
        }
    },

    test_codeValidator() {
        var userCode = RecoveryPassword.code;
        var genedCode = codeGen.code;
        codeValidator.verify(userCode, genedCode);
        if (codeValidator.verify = true) {
            codeValidator = true;
            this.passedTestCount++;
        }
    },

    test_all() {
        this.test_codeGen_generate();
        this.test_codeGen_checkCode();
        this.test_smsSend();
        this.test_emailSend();
        this.test_RecoveryPassword_sms();
        this.test_RecoveryPassword_email();
        this.test_RecoveryPassword_validate();
        this.test_codeValidator();

        if (this.passedTestCount == 8) return true;
        else {
            if (this.RecoveryPassword_sms = false) console.log("RecoveryPassword_sms got a problem");
            if (this.RecoveryPassword_email = false) console.log("RecoveryPassword_email got a problem");
            if (this.RecoveryPassword_validate = false) console.log("RecoveryPassword_validate got a problem");
            if (this.emailSend = false) console.log("emailSend got a problem");
            if (this.smsSend = false) console.log("smsSend got a problem");
            if (this.codeGen_generate = false) console.log("codeGen_generate got a problem");
            if (this.codeGen_checkCode = false) console.log("codeGen_checkCode got a problem");
            if (this.codeValidator = false) console.log("codeValidator got a problem");
        }
    }

}