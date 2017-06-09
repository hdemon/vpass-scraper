const Nightmare = require('nightmare')
const exec = require('child_process').exec
const cheerio = require('cheerio')

const nightmare = Nightmare({
  show: false,
  executionTimeout: 60000
})

nightmare
  .goto('https://www.smbc-card.com/mem/index.jsp')
  .wait('#contWrap > div.ktop_infoAreaWrap > div > ul.ktop_infoBox.line.valignTop > li > div.loginInfoBox > form > ul > li:nth-child(1) > input[type="text"]')
  .insert('#contWrap > div.ktop_infoAreaWrap > div > ul.ktop_infoBox.line.valignTop > li > div.loginInfoBox > form > ul > li:nth-child(1) > input[type="text"]', process.env['VPASS_USER_ID'])
  .insert('#contWrap > div.ktop_infoAreaWrap > div > ul.ktop_infoBox.line.valignTop > li > div.loginInfoBox > form > ul > li:nth-child(2) > input[type="password"]', process.env['VPASS_PASSWORD'])
  .click('#contWrap > div.ktop_infoAreaWrap > div > ul.ktop_infoBox.line.valignTop > li > div.loginInfoBox > form > p > input')
  .wait('#side > div:nth-child(4) > ul > li:nth-child(2) > a')
  .click('#side > div:nth-child(4) > ul > li:nth-child(2) > a')
  .wait('#vp-view-VC8403-001_RS0001_month')
  .insert('#vp-view-VC8403-001_RS0001_month', process.env['VPASS_CARD_EXPIRE_MONTH'])
  .insert('#vp-view-VC8403-001_RS0001_year', process.env['VPASS_CARD_EXPIRE_YEAR'])
  .insert('#vp-view-VC8403-001_RS0001_cvv2', process.env['VPASS_SECURITY_CODE'])
  .wait(1000)
  .click('#vp-view-VC8403-001_RS0001_GMVC8403001C300001-btn01')
  .wait('#vp_alcor_view_Logic_122 > div > table')
  .evaluate(function() {
    return document.querySelector('html').innerHTML;
  })
  .end()
  .then(function(html) {
    const $ = cheerio.load(html)
    const balance = Number($('#vp_alcor_view_Label_179').html()) * 10000
    console.log(balance) 
    const data = { date: new Date(), balance }
  })
  .catch((error) => error && console.error(error))
