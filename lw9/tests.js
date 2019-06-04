describe("RecoveryPassword making request for recovery and validate recovery code", function () {

  describe("Recovery methods shall get recovery code by SMS or Email", function () {
    
    it("puts invalid data to recovery method field", function () {
      assert.equal(RecoveryPassword.recovery("smss", "11111111111"), false);
    });

    it("use valid method parameter (SMS) to recovery", function () {
      assert.equal(RecoveryPassword.recovery("sms", "11111111111"), true);
    });

    it("use valid method parameter (Email) to recovery", function () {
      assert.equal(RecoveryPassword.recovery("email", "test@test.ru"), true);
    });

    it("puts invalid type of data as recovery parameter", function () {
      assert.equal(RecoveryPassword.recovery("sms", 123), false);
      assert.equal(RecoveryPassword.recovery(123, 123), false);
      assert.equal(RecoveryPassword.recovery("email", 123), false);
      assert.equal(RecoveryPassword.recovery(), false);
    });
    
    it("puts valid data to SMS recovery method", function () {
      assert.equal(RecoveryPassword.recovery("sms", "11111111111"), true);
    });

    it("puts invalid data to SMS recovery method", function () {
      assert.equal(RecoveryPassword.recovery("sms", "1111111111w"), false);
    });

    it("puts valid data to Email recovery method", function () {
      assert.equal(RecoveryPassword.recovery("email", "test@test.ru"), true);
    });

    it("Email recovery method wrong adress", function () {
      assert.equal(RecoveryPassword.recovery("email", "123"), false);
      assert.equal(RecoveryPassword.recovery("email", "test@r"), false);
      assert.equal(RecoveryPassword.recovery("email", "testt.ru"), false);
      //assert.equal(RecoveryPassword.recovery("email", "test@r.ru"), false);
      assert.equal(RecoveryPassword.recovery("email", "@r.ru"), false);
    });

  });

  describe("Validate method checks a recovery code", function () {
    it("puts valid data to email method to get a correct code", function () {
      assert.equal(RecoveryPassword.recovery("email", "test@test.ru"), true);
      assert.equal(RecoveryPassword.validate(RecoveryPassword.code), true);
      assert.equal(RecoveryPassword.valid, true);
    });

    it("puts invalid data to email method so false must be returned", function () {
      assert.equal(RecoveryPassword.recovery("email", "testt.ru"), false);
      assert.equal(RecoveryPassword.valid, false);
    });

    it("puts valid data to SMS method to get a correct code", function () {
      assert.equal(RecoveryPassword.recovery("sms", "89877183999"), true);
      assert.equal(RecoveryPassword.validate(RecoveryPassword.code), true);
      assert.equal(RecoveryPassword.valid, true);
    });

    it("puts invalid data to SMS method so false must be returned", function () {
      assert.equal(RecoveryPassword.recovery("sms", "qwe1"), false);
      assert.equal(RecoveryPassword.valid, false);
    });

  });

});

describe("Code generator creates recovery code", function () {
  it("generates code", function () {
    assert.equal(toString(codeGenerator()).length, 18);
  });
});


mocha.run();