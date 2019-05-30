var autoTest = {
    passedTestCount: 0,
    code: 0,
    codeGen: false,
    RecoveryPassword_sms: false,
    RecoveryPassword_email: false,
    RecoveryPassword_validate: false,
    emailSend: false,
    smsSend: false,

    test_codeGen_generate() {
        this.code = codeGenerator();
        if (typeof (this.code) == "number" ||
            toString(this.code).length == 5) {
            this.codeGen = true;
            this.passedTestCount++;
            console.log("codeGen_test => PASSED");
        }
    },

    test_smsSend() {
        Sms.send(this.code);
        if (typeof (this.code) == "number" ||
            toString(this.code).length == 5) {
            this.smsSend = true;
            this.passedTestCount++;
            console.log("smsSend_test => PASSED");
        }
    },

    test_emailSend() {
        Email.send(this.code);
        if (typeof (this.code) == "number" ||
            toString(this.code).length == 5) {
            this.emailSend = true;
            this.passedTestCount++;
            console.log("emailSend_test => PASSED");
        }
    },

    test_RecoveryPassword_sms() {
        code = RecoveryPassword.recovery("sms", "89877183558");
        if (typeof (this.code) == "number" ||
            toString(this.code).length == 5) {
            this.RecoveryPassword_sms = true;
            this.passedTestCount++;
            console.log("RecoveryPassword_sms_test => PASSED");
        }
    },

    test_RecoveryPassword_email() {
        code = RecoveryPassword.recovery("email", "test@test.ru");
        if (typeof (this.code) == "number" ||
            toString(this.code).length == 5) {
            this.RecoveryPassword_email = true;
            this.passedTestCount++;
            console.log("RecoveryPassword_sms_email => PASSED");
        }
    },

    test_RecoveryPassword_validate() {
        var check = RecoveryPassword.validate(this.code);
        if (check == true) {
            this.RecoveryPassword_validate = true;
            this.passedTestCount++;
            console.log("RecoveryPassword_email_Validate => PASSED");
        } else console.log("validate_state: ", check);
    },

    test_all() {
        this.test_codeGen_generate();
        this.test_smsSend();
        this.test_emailSend();
        this.test_RecoveryPassword_sms();
        this.test_RecoveryPassword_email();
        this.test_RecoveryPassword_validate();

        if (this.passedTestCount != 6) {
            if (this.RecoveryPassword_sms == false)
                console.log("RecoveryPassword_sms got a problem");
            if (this.RecoveryPassword_email == false)
                console.log("RecoveryPassword_email got a problem");
            if (this.RecoveryPassword_validate == false)
                console.log("RecoveryPassword_validate got a problem");
            if (this.emailSend == false)
                console.log("emailSend got a problem");
            if (this.smsSend == false)
                console.log("smsSend got a problem");
            if (this.codeGen_generate == false)
                console.log("codeGen_generate got a problem");

            return console.log("passed tests count = ", this.passedTestCount);
        }
    }
}