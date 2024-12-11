let URL = "https://jsonplaceholder.typicode.com/users";

function sendRequest(method, url, body = null) {
  //   return new Promise((resolve, reject) => {
  //     let xhr = new XMLHttpRequest();
  //     xhr.open(method, url);
  //     xhr.responseType = "json";
  //     xhr.setRequestHeader("Content-Type", "application/json");
  //     xhr.onload = () => {
  //       if (xhr.status >= 400) {
  //         reject("chunga changa");
  //       } else {
  //         resolve(xhr.response);
  //       }
  //     };
  //     xhr.onerror = () => {
  //       reject("Eroria");
  //     };
  //     xhr.send(JSON.stringify(body));
  //   });
  let headers = {
    "Content-Type": "application/json",
  };
  return fetch(url, {
    method: method,
    body: JSON.stringify(body),
    headers: headers,
  }).then((response) => {
    if (response.ok) {
      return response.json();
    } else {
      return response.json().then((error) => {
        let err = new Error("What's that?");
        err.data = error;
        throw err;
      });
    }
  });
}

// sendRequest("GET", URL)
//   .then((data) => console.log(data))
//   .catch((err) => console.log(err));

let body = { name: "Akop", age: 27 };

sendRequest("POST", URL, body)
  .then((data) => console.log(data))
  .catch((err) => console.log(err));
