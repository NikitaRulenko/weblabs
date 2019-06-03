describe("RecoveryPassword", function () {

  it("SMS recovery method", function () {
    assert.equal(resultSMS, true);
  });

  it("Email recovery method", function () {
    assert.equal(resultEmail, true);
  });

  it("Validate code method", function () {
    assert.equal(resultValidate, false);
  });
});